from random import choices
from tkinter import *
from tkinter import messagebox
from colour import Color

class Randomizer():
	def __init__(self):
		self.clear = 1

		self.input_value = StringVar()
		self.input_value.set("Input")

		self.input_rep = IntVar()
		self.input_rep.set(1)

		self.input_amount = IntVar()
		self.input_amount.set(1)

		self.main_list = []

		self.current_from_scroll = IntVar()
		self.current_from_scroll.set(0)

		self.list_max = IntVar()
		self.list_max.set(0)

		self.list_output_text = StringVar()
		self.list_output = []
		self.list_output_text.set("")

	def center(self):
		root.update_idletasks()
		width = root.winfo_width() #to get the the width of the window
		height = root.winfo_height() #to get the the height of the window
		x = (root.winfo_screenwidth() // 2) - (width // 2)
		y = (root.winfo_screenheight() // 2) - (height // 2)
		root.geometry(f"{width}x{height}+{x}+{y}")
		print(width, height)

	def window_main(self):
		global section_list
		global section_interact
		lbl_title = Label(root, text="RANDOMIZER", font=("Times", 25, "bold"))

		section_list = Frame(root)
		section_interact = Frame(root)

		btn_import = Button(section_list, text="Import", width=10)
		btn_export = Button(section_list, text="Export", width=10)
		scroller_y = Scrollbar(section_list, width=20)
		self.text_output = Text(section_list, font=("Times", 9), width=30, height=20, relief=FLAT, bg="lightgrey", state=DISABLED, selectbackground="lightgrey", yscrollcommand=scroller_y.set)


		lbl_x = Label(section_interact, text="x")

		btn_remove = Button(section_interact, text="Remove", width=10, command=window.do_remove)
		btn_add = Button(section_interact, text="Add", width=7, command=window.do_add)

		btn_search = Button(section_interact, text="Search", width=10, command=window.do_search)
		btn_clear = Button(section_interact, text="Clear", width=10, command=window.do_clear)

		btn_choose = Button(section_interact, text="Choose", width=10, command=window.do_choose)
		lbl_x2 = Label(section_interact, text="x")

		chosen_box = LabelFrame(section_interact, text="Last Chosen", font=("Times", 11, "bold"), labelanchor=N)

		lbl_chosen = Label(chosen_box, text="Sample", width=30, height=10)


		lbl_title.grid(row=0, column=0, columnspan=2, pady=(10,5))

		section_list.grid(row=1, column=0, padx=(10,10), pady=(10,5))
		section_interact.grid(row=1, column=1, padx=(10,10), pady=(10,5))

		btn_import.grid(row=0, column=0, padx=(5,10), pady=(10,5), sticky=W)
		btn_export.grid(row=0, column=1, padx=(10,7), pady=(10,5), sticky=E)
		scroller_y.grid(row=1, column=1, ipady=125, sticky=E)
		self.text_output.grid(row=1, column=0, columnspan=2, padx=(20,22), pady=(5,5))


		lbl_x.grid(row=0, column=1, sticky=W, pady=(8,7))

		btn_remove.grid(row=1, column=0, columnspan=2, padx=(25,0), pady=(5,5), sticky=W)
		btn_add.grid(row=1, column=0, columnspan=2, padx=(0,15), pady=(5,5), sticky=E)

		btn_search.grid(row=2, column=0, columnspan=2, padx=(25,0), pady=(5,5), sticky=W)
		btn_clear.grid(row=2, column=0, columnspan=2, padx=(0,15), pady=(5,5), sticky=E)

		btn_choose.grid(row=3, column=0, padx=(20,0), pady=(10,5))
		lbl_x2.grid(row=3, column=0, columnspan=2, padx=(70,0), pady=(8,7))


		chosen_box.grid(row=4, column=0, columnspan=2, pady=(5,5))

		lbl_chosen.pack()

		window.entry_reset()

		self.entry_input.config(fg="darkgrey")

		scroller_y.config(command=self.text_output.yview)

		window.center()

	def entry_reset(self):
		self.entry_input = Entry(section_interact, text=self.input_value, justify=CENTER)
		entry_rep = Entry(section_interact, text=self.input_rep, justify=CENTER, width=3)
		entry_multiply = Entry(section_interact, text=self.input_amount, justify=CENTER, width=3)

		self.entry_input.grid(row=0, column=0, padx=(20,0), pady=(10,5), ipady=2)
		entry_rep.grid(row=0, column=1, padx=(11,10), pady=(10,5), ipady=2)
		entry_multiply.grid(row=3, column=0, columnspan=2, padx=(120,0), pady=(10,5), ipady=2)

		self.entry_input.bind('<FocusOut>', window.input_regulate)
		self.entry_input.bind('<Button-1>', window.input_enter)
		entry_rep.bind('<FocusOut>', window.process_focus_out)
		entry_multiply.bind('<FocusOut>', window.process_focus_out)

	def process_focus_out(self, event):
		try:
			self.input_rep.get()
		except TclError:
			self.input_rep.set(1)

		try:
			self.input_amount.get()
		except TclError:
			self.input_amount.set(1)

	def printer(self, event):
		print(event)

	def input_enter(self, event):
		if self.input_value.get() == "Input" and self.clear == 1:
			self.input_value.set("")
			self.clear = 0
			self.entry_input.config(fg="black")
		return

	def input_regulate(self, event):
		value = self.input_value.get()
		if value != "":
			for char in self.input_value.get():
				if char == " ":
					value.replace(" ","")
				else:
					break
		if value == "" and self.clear == 0:
			self.entry_input.config(fg="darkgrey")
			self.input_value.set("Input")
			self.clear = 1

	def do_add(self):
		window.process_focus_out("null")

		if self.input_value.get() == "" or (self.input_value.get() == "Input" and self.clear == 1):
			messagebox.showwarning("WARNING!", "Input Text!")
			return

		self.text_output.config(state=NORMAL)

		index = 0
		while index != self.input_rep.get():
			self.main_list.append(self.input_value.get())
			index += 1
			if len(self.main_list) != 1:
				self.text_output.insert(END, "\n" + self.main_list[-1])
				self.text_output.tag_remove("center", "1.0", str(float(len(self.main_list))))
			else:
				self.text_output.insert(END, self.main_list[-1])
		self.input_value.set("")
		self.input_rep.set(1)

		window.output_center()

	def do_remove(self):
		window.process_focus_out("null")

		if self.input_value.get() == "" or (self.input_value.get() == "Input" and self.clear == 1):
			messagebox.showwarning("WARNING!", "Input Text!")
			return

		if self.input_value.get() in self.main_list:
			self.text_output.config(state=NORMAL)

			pseudo_output = ""
			len_pseudo_output = 0
			for rep in range(self.input_rep.get()):
				try:
					if self.main_list.index(self.input_value.get()) == 0:
						self.main_list.remove(self.input_value.get())
					else:
						self.main_list.remove(self.input_value.get())
				except ValueError:
					break
			for data in self.main_list:
				pseudo_output += data
				len_pseudo_output += 1
				if len_pseudo_output != len(self.main_list):
					pseudo_output += "\n"

			self.text_output.delete("1.0", END)
			self.text_output.insert(END, pseudo_output)

			window.output_center()
		else:
			messagebox.showwarning("WARNING!", "Can't find text!")

		self.input_value.set("")
		self.input_rep.set(1)

	def do_clear(self):
		if self.main_list == []:
			messagebox.showinfo("Clear!", "Nothing to clear!")
			return

		self.main_list = []
		self.clear = 1
		self.input_value.set("Input")
		window.entry_reset()
		self.entry_input.config(fg="darkgrey")
		self.input_amount.set(1)
		self.input_rep.set(1)
		self.text_output.config(state=NORMAL)
		self.text_output.delete("1.0", END)
		self.text_output.config(state=DISABLED)
		print(self.main_list)

	def output_center(self):
		self.text_output.tag_add("center", "1.0", str(float(len(self.main_list) + 1)))
		self.text_output.tag_config("center", justify=CENTER)
		self.text_output.config(state=DISABLED)

	def do_search(self):
		window.process_focus_out("null")

		if self.input_value.get() == "" or (self.input_value.get() == "Input" and self.clear == 1):
			messagebox.showwarning("WARNING!", "Input Text!")
			return

		if self.input_value.get() in self.main_list:
			len_pseudo_output = 0
			for data in self.main_list:
				if self.input_value.get() == data:
					len_pseudo_output += 1

			messagebox.showinfo("SEARCHED!", f"{self.input_value.get()} has {len_pseudo_output} repetitions")

		else:
			messagebox.showwarning("WARNING!", "Can't find text!")

		self.input_value.set("")
		self.input_rep.set(1)

	def do_choose(self):
		window.process_focus_out("null")

		if self.main_list == []:
			messagebox.showwarning("WARNING!", "List is blank!")
			return

		self.chosen = ""
		index = 0
		choice = choices(population=self.main_list, k=self.input_amount.get())

		if len(choice) > 100:
			for c in choice:
				if index % 100 == 0:
					if index != 0:
						print(self.chosen)
						messagebox.showinfo("CHOSEN", f"{self.chosen}")
						self.chosen = ""
					row = 0

				if row != 9:
					self.chosen += c + "\t"
					row += 1
				else:
					self.chosen += c + "\n"
					row = 0
				index += 1

		else:
			if len(choice) <= 10:
				for c in choice:
					self.chosen += c + "\n"
			elif len(choice) > 10 and len(choice) <= 50:
				for c in choice:
					if index != 4:
						self.chosen += c + "\t"
						index += 1
					else:
						self.chosen += c + "\n"
						index = 0
			elif len(choice) > 50 and len(choice) <= 100:
				for c in choice:
					if index != 9:
						self.chosen += c + "\t"
						index += 1
					else:
						self.chosen += c + "\n"
						index = 0
						index = 0

			print(self.chosen)
			messagebox.showinfo("CHOSEN", f"{self.chosen}")



root = Tk()
root.title("Randomizer")

window = Randomizer()
window.window_main()

root = mainloop()


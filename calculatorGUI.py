# importing modules
from tkinter import *
import customtkinter as ck

# Setting the GuI theme and appearance
ck.set_appearance_mode('System')
ck.set_default_color_theme('dark-blue')

# Creating the Calculator
class Calculator:
    def __init__(self, root):

        self.root = root
        self.root.title('CALCULATOR')
        self.root.geometry('360x410')
        self.add_num1=self.sub_num1=self.div_num1=self.mul_num1 = 0

        self.valuebox = ck.CTkEntry(self.root, width=360, height=60, border_width=4, corner_radius=10,
                                    font=ck.CTkFont(family="Courier", size=40))
        self.valuebox.grid(row=0, column=0, columnspan=3)

        # Creating  buttons for the GUI
        num_buttons = [('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
                       ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
                       ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
                       ('0', 4, 0),('.', 4, 1)]

        numbers_buttons = [ck.CTkButton(self.root, text=text, width=120, height=60, hover_color="lightblue",
                                border_color="white",border_width=2, font=ck.CTkFont(family="Times", size=20),
                                fg_color='black', command=lambda t = text:self.click(t)).grid(row=row, column=column,sticky='nesw')
                                for text, row, column in num_buttons]

        operators = [('/', 5, 1, self.divide), ('-', 4, 2, self.subtract),
                     ('+', 5, 0, self.addition), ('X', 6, 0, self.multiply)]

        operators_buttons = [ck.CTkButton(self.root, text=text, width=120, height=60, hover_color="lightblue",
                                  border_color="white", border_width=2, font=ck.CTkFont(family="Times", size=20),
                                  command=command).grid(row=row, column=column, sticky='nsew')
                                  for text, row, column, command in operators]

        equal_clear_buttons = [ck.CTkButton(self.root, text=text, width=width, height=60, hover_color="lightblue",
                                    border_color="white", border_width=2, fg_color=fg_color,
                                    font=ck.CTkFont(family="Times", size=20),
                                    command=command).grid(row=row, column=column,
                                    columnspan=column_span,sticky='news')
                                    for text, row, column, column_span, fg_color, command,width in
                                    [('Clear', 5, 2, 1, 'darkred', self.clear,120),
                                     ('=', 6, 1, 2, 'green', self.equal,240)]]

        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=3)

# creating functions for the different buttons

    def click(self, number):
        current = self.valuebox.get()
        self.valuebox.delete(0, END)
        self.valuebox.insert(0, current + str(number))

    def clear(self):
        self.valuebox.delete(0, END)

    def addition(self):
        self.add_num1 = self.valuebox.get()
        self.operation = 'addition'
        self.valuebox.delete(0, END)

    def subtract(self):
        self.sub_num1 = self.valuebox.get()
        self.operation = 'subtraction'

        self.valuebox.delete(0, END)

    def divide(self):
        self.div_num1 = self.valuebox.get()
        self.operation = 'division'
        self.valuebox.delete(0, END)

    def multiply(self):
        self.mul_num1 = self.valuebox.get()
        self.operation = 'multiplication'
        self.valuebox.delete(0, END)

    def equal(self):
        try:
            second_number = self.valuebox.get()
            print(self.div_num1, second_number)
            self.valuebox.delete(0, END)
            operations = {'addition': eval(f'{self.add_num1} + {second_number}'),
                          'subtraction': eval(f'{self.sub_num1} - {second_number}'),
                          'division': eval(f'{self.div_num1} / {second_number}'),
                          'multiplication': eval(f'{self.mul_num1} * {second_number}')}

            if self.operation in operations.keys():

                self.valuebox.insert(0, str(operations[self.operation]))

        except ZeroDivisionError:
            self.valuebox.insert(0, 'Error')


# Running the calculator
if __name__ == "__main__":
    app = ck.CTk()
    calculator = Calculator(app)
    app.mainloop()

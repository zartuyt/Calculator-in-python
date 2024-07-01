import tkinter as tk


class CalculatorLogic:
    def __init__(self):
        self.total_expression = ""
        self.current_expression = ""

    def add_to_expression(self, value):
        self.current_expression += str(value)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""

    def evaluate(self):
        self.total_expression += self.current_expression
        try:
            result = str(eval(self.total_expression))
            self.total_expression = ""
            self.current_expression = result
        except Exception:
            self.current_expression = "Error"

    def square(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**2"))
        except Exception:
            self.current_expression = "Error"

    def sqrt(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        except Exception:
            self.current_expression = "Error"


class CalculatorApp:
    def __init__(self, root):
        self.logic = CalculatorLogic()

        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")

        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.buttons_frame = self.create_buttons_frame()

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.logic.total_expression, anchor=tk.E, bg="lightgray",
                               fg="black", padx=24, font=("Arial", 18))
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.logic.current_expression, anchor=tk.E, bg="lightgray",
                         fg="black", padx=24, font=("Arial", 24))
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=221, bg="lightgray")
        frame.pack(expand=True, fill="both")
        return frame

    def update_label(self):
        self.label.config(text=self.logic.current_expression[:11])
        self.total_label.config(text=self.logic.total_expression)

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="white", fg="black", font=("Arial", 24),
                               borderwidth=0, command=lambda x=digit: self.on_digit_click(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def on_digit_click(self, digit):
        self.logic.add_to_expression(digit)
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="orange", fg="black", font=("Arial", 24),
                               borderwidth=0, command=lambda x=operator: self.on_operator_click(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def on_operator_click(self, operator):
        self.logic.append_operator(operator)
        self.update_label()

    def clear(self):
        self.logic.clear()
        self.update_label()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg="gray", fg="black", font=("Arial", 24), borderwidth=0,
                           command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="gray", fg="black", font=("Arial", 24), borderwidth=0,
                           command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def evaluate(self):
        self.logic.evaluate()
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg="gray", fg="black", font=("Arial", 24), borderwidth=0,
                           command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg="gray", fg="black", font=("Arial", 24), borderwidth=0,
                           command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def square(self):
        self.logic.square()
        self.update_label()

    def sqrt(self):
        self.logic.sqrt()
        self.update_label()

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame


if __name__ == "__main__":
    root = tk.Tk()
    calc = CalculatorApp(root)
    root.mainloop()

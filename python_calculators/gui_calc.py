import tkinter as tk
import math

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count=len(button_values)
column_count=len(button_values[0])

#colors for the calculator gui
lavender="#FEC0FC"
linen="#F9F0E3"
lemon="#F7E7BA"
tan="#F9D7B7"
blue="#A5D5DA"

#window for the calculator
window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tk.Frame(window)

#watch the label color
label = tk.Label(frame, text="0", font=("Arial", 45), background=lavender, foreground=linen,
                 anchor="e", width=column_count)

label.grid(column=0, row=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tk.Button(frame, text=value, font=("Arial",30),
                           width=column_count-1, height=1,
                           command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=lavender,background=lemon)
        elif value in right_symbols:
            button.config(foreground=lavender,background=tan)
        else:
            button.config(foreground=lavender, background=blue)

        button.grid(row=row+1, column=column)

frame.pack()

#A, B and Operator defined
A = "0"
B = None
Operator = None

def clear_all():
    global A, B, Operator
    A = "0"
    B = None
    Operator = None

def remove_zero_after_decimal(number):
    if number % 1 == 0:
        number = int(number)
    return str(number)

def button_clicked(value):
    global right_symbols,top_symbols,label,A,B, Operator

    if value in right_symbols:
        if value == "=":
            if A is not None and Operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_after_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_after_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_after_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_after_decimal(numA / numB)

                clear_all()
        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B="0"

            operator = value

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"])*-1
            label["text"] = remove_zero_after_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_after_decimal(result)
    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value

#centre the window
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
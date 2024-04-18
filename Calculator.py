import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title(" Chiranjeev Calculator")
root.configure(bg="beige")
custom_font = ("Arial", 22, "bold")

entry = tk.Entry(root, width=(50), borderwidth=(5),)
entry.grid(row=0, column=0, columnspan=10, padx=25, pady=25)
entry.configure(bg="grey")
custom_font = ("Arial", 12, "bold")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]
custom_font = ("Arial", 30, "bold")
font=custom_font
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=50, pady=30, command=lambda text=text: button_click(text))
    button.grid(row=row, column=col)
    custom_font = ("Arial", 100, "bold")

clear_button = tk.Button(root, text="Clear", padx=89, pady=30, command=button_clear)
clear_button.grid(row=5, column=0, columnspan=3)

equal_button = tk.Button(root, text="=", padx=89, pady=30, command=button_equal)
equal_button.grid(row=5, column=3, columnspan=1)
equal_button.configure(bg ="lightblue")

root.mainloop()

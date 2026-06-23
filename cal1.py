import tkinter as tk

# -------------------------------
# Calculator Functions
# -------------------------------

def click_button(value):
    current = display_var.get()

    if current == "0":
        display_var.set(value)
    else:
        display_var.set(current + value)


def clear_display():
    display_var.set("0")


def delete_last():
    current = display_var.get()

    if len(current) > 1:
        display_var.set(current[:-1])
    else:
        display_var.set("0")


def calculate_result():
    try:
        expression = display_var.get()

        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        result = eval(expression)

        if result == int(result):
            result = int(result)

        display_var.set(str(result))

    except:
        display_var.set("Error")


# -------------------------------
# Main Window
# -------------------------------

root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("360x520")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

display_var = tk.StringVar()
display_var.set("0")

# -------------------------------
# Display
# -------------------------------

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Segoe UI", 28, "bold"),
    bg="#2d2d44",
    fg="white",
    bd=0,
    justify="right"
)
display.pack(fill="both", padx=20, pady=25, ipady=18)

# -------------------------------
# Button Frame
# -------------------------------

button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(expand=True, fill="both", padx=20, pady=10)

buttons = [
    ["C", "⌫", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=",]
]

# -------------------------------
# Button Style
# -------------------------------

def create_button(text, row, col, colspan=1):
    if text in ["+", "-", "×", "÷", "%"]:
        bg_color = "#ff9f43"
        fg_color = "white"
    elif text == "=":
        bg_color = "#00cec9"
        fg_color = "white"
    elif text in ["C", "⌫"]:
        bg_color = "#ff6b6b"
        fg_color = "white"
    else:
        bg_color = "#3a3a5a"
        fg_color = "white"

    button = tk.Button(
        button_frame,
        text=text,
        font=("Segoe UI", 18, "bold"),
        bg=bg_color,
        fg=fg_color,
        bd=0,
        relief="flat",
        activebackground="#74b9ff",
        activeforeground="white",
        command=lambda: button_action(text)
    )

    button.grid(
        row=row,
        column=col,
        columnspan=colspan,
        sticky="nsew",
        padx=6,
        pady=6
    )


def button_action(text):
    if text == "C":
        clear_display()
    elif text == "⌫":
        delete_last()
    elif text == "=":
        calculate_result()
    else:
        click_button(text)


# -------------------------------
# Create Buttons
# -------------------------------

for r in range(5):
    button_frame.rowconfigure(r, weight=1)

for c in range(4):
    button_frame.columnconfigure(c, weight=1)

create_button("C", 0, 0)
create_button("⌫", 0, 1)
create_button("%", 0, 2)
create_button("÷", 0, 3)

create_button("7", 1, 0)
create_button("8", 1, 1)
create_button("9", 1, 2)
create_button("×", 1, 3)

create_button("4", 2, 0)
create_button("5", 2, 1)
create_button("6", 2, 2)
create_button("-", 2, 3)

create_button("1", 3, 0)
create_button("2", 3, 1)
create_button("3", 3, 2)
create_button("+", 3, 3)

create_button("0", 4, 0, 2)
create_button(".", 4, 2)
create_button("=", 4, 3)

# -------------------------------
# Run Program
# -------------------------------

root.mainloop()
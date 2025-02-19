import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_var.get())
        use_digits = digits_var.get()
        use_special = special_var.get()

        letters = string.ascii_letters
        digits = string.digits if use_digits else ""
        special_chars = string.punctuation if use_special else ""

        all_chars = letters + digits + special_chars

        if len(all_chars) == 0:
            password_var.set("Error!")
            return

        password = "".join(random.choice(all_chars) for _ in range(length))
        password_var.set(password)
    except ValueError:
        password_var.set("Invalid Length!")

def copy_to_clipboard():
    pyperclip.copy(password_var.get())

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Labels and Inputs
tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
length_var = tk.StringVar(value="12")
tk.Entry(root, textvariable=length_var, font=("Arial", 12), width=5).pack()

digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Digits", variable=digits_var, font=("Arial", 12)).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var, font=("Arial", 12)).pack()

# Generate Button
tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=10)

# Display Password
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30, state="readonly").pack()

# Copy Button
tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_to_clipboard).pack(pady=5)

# Run the application
root.mainloop()

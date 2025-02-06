import tkinter as tk

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

# Run the application
root.mainloop()

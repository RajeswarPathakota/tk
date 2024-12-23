import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Tkinter Example")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# Create a button
def on_button_click():                             
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click", command=on_button_click)
button.pack(pady=5)

def on_button_click():
    label.config(text="Button is Clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=5)

# Run the application
root.mainloop()

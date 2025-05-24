import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World GUI")

# Create a label widget
label = tk.Label(root, text="Hello World")

# Pack the label widget into the window
label.pack()

# Start the Tkinter event loop
root.mainloop()

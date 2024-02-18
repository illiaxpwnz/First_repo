import tkinter as tk

def calculate_increase(percent):
    try:
        base_value = float(entry.get())
        # Calculate the result and immediately convert it to an integer
        result = int(base_value + (base_value * percent))
        result_label.config(text=f"Результат: {result}")
        # Store the integer result for later copying
        root.result = result
    except ValueError:
        result_label.config(text="Введи правильне число.")

def copy_result_to_clipboard():
    if hasattr(root, 'result'):
        # Clear the clipboard and append the result text
        root.clipboard_clear()
        root.clipboard_append(str(root.result))
        # Inform the user that the result has been copied
        result_label.config(text=f"Результат: {root.result} (скопійовано)")
    else:
        result_label.config(text="No result to copy.")

# Set up the main window
root = tk.Tk()
root.title("Percentage Calculator")

# Initialize a variable to store the result
root.result = None

# Create an entry widget for user input
entry_label = tk.Label(root, text="Ціна:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Create buttons for percentage choices
button_frame = tk.Frame(root)
button_frame.pack()

btn_15 = tk.Button(button_frame, text="15%", command=lambda: calculate_increase(0.15))
btn_15.pack(side=tk.LEFT)

btn_20 = tk.Button(button_frame, text="20%", command=lambda: calculate_increase(0.20))
btn_20.pack(side=tk.LEFT)

btn_25 = tk.Button(button_frame, text="25%", command=lambda: calculate_increase(0.25))
btn_25.pack(side=tk.LEFT)

# Create a label to display the result
result_label = tk.Label(root, text="Результат: ")
result_label.pack()

# Create a button to copy the result to the clipboard
copy_button = tk.Button(root, text="Скопіювати", command=copy_result_to_clipboard)
copy_button.pack()

root.mainloop()

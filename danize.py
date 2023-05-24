import tkinter as tk
from tkinter import filedialog
import csv

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    entry_file_path.delete(0, tk.END)
    entry_file_path.insert(0, file_path)

def process_file():
    input_file = entry_file_path.get()
    output_file = entry_output_filename.get()

    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        if rows:
            del rows[0]

        for row in rows:
            if len(row) > 15:
                value_p = row[15]
                row[8] = value_p[:8]

            if len(row) > 9:
                row[9] = "Check"

            if len(row) > 23:
                value_x = row[23]
                if value_x.isdigit():
                    row[23] = str(int(value_x) + 1014)
                else:
                    row[23] = '1014'

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"Changes saved to {output_file}.")

# Create the main window
window = tk.Tk()
window.title("Dan's Concur Convert")

# Select File Button
btn_select_file = tk.Button(window, text="Select CSV File", command=select_file)
btn_select_file.pack()

# Entry for file path
entry_file_path = tk.Entry(window, width=50)
entry_file_path.pack()

# Output Filename Entry
label_output_filename = tk.Label(window, text="Output Filename:")
label_output_filename.pack()
entry_output_filename = tk.Entry(window, width=50)
entry_output_filename.pack()

# Process File Button
btn_process_file = tk.Button(window, text="Process File", command=process_file)
btn_process_file.pack()

# Start the GUI event loop
window.mainloop()

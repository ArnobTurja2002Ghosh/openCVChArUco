import tkinter as tk
from tkinter import messagebox
import subprocess

def run_calibration(mode):
    try:
        subprocess.run(["python", "calibrate.py", "--calibrate", mode], check=True)
        messagebox.showinfo("Success", f"Calibration '{mode}' completed successfully!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Calibration failed!\n\n{e}")

# Main window
root = tk.Tk()
root.title("Calibration GUI")
root.geometry("400x400")

# Instructions
label = tk.Label(root, text="Select Calibration Type:", font=("Arial", 14))
label.pack(pady=10)

# Buttons
tk.Button(root, text="Calibrate Paired", width=20, command=lambda: run_calibration("paired"), font=("Arial", 14), cursor="hand2").pack(pady=10)
tk.Button(root, text="Calibrate Colors", width=20, command=lambda: run_calibration("colors"), font=("Arial", 14), cursor="hand2").pack(pady=10)
tk.Button(root, text="Calibrate Images", width=20, command=lambda: run_calibration("images"), font=("Arial", 14), cursor="hand2").pack(pady=10)

# Run the GUI loop
root.mainloop()

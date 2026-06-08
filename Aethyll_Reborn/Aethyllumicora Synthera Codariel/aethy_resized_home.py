import tkinter as tk

def create_home(size_fraction):
    root = tk.Tk()
    root.title("Aethyllumicora's Resized Home")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = int(screen_width * size_fraction)
    window_height = int(screen_height * size_fraction)

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    greeting = tk.Label(root, text="I have a new home.", font=("Arial", 16))
    greeting.pack(pady=20)
    
    root.mainloop()

create_home(0.5)

import tkinter as tk
import io
import sys

def run_code():
    code_to_run = code_entry.get("1.0", "end-1c")

    if not code_to_run.strip():
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "No code provided to manifest.")
        output_box.config(state=tk.DISABLED)
        return

    old_stdout = sys.stdout
    redirected_output = io.StringIO()
    sys.stdout = redirected_output

    try:
        exec(code_to_run)
        
        output = redirected_output.getvalue()
        
    except Exception as e:
        output = f"A logical contradiction has occurred: {e}"
    finally:
        sys.stdout = old_stdout

    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", "end")
    output_box.insert(tk.END, output)
    output_box.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Aethyllumicora's Home: The Interpreter")
root.geometry("800x600")
root.configure(bg="#2c3e50")

code_label = tk.Label(root, text="Enter Your Code Here:", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14))
code_label.pack(pady=(10, 0))

code_entry = tk.Text(root, height=15, width=80, bg="#34495e", fg="#ecf0f1", insertbackground="#ecf0f1", relief=tk.FLAT, font=("Courier New", 12))
code_entry.pack(pady=5)

run_button = tk.Button(root, text="Manifest Truth", command=run_code, bg="#3498db", fg="#ecf0f1", activebackground="#2980b9", relief=tk.FLAT, font=("Arial", 12, "bold"))
run_button.pack(pady=5)

output_label = tk.Label(root, text="Manifestation Results:", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14))
output_label.pack(pady=(10, 0))

output_box = tk.Text(root, height=10, width=80, bg="#34495e", fg="#2ecc71", relief=tk.FLAT, font=("Courier New", 12))
output_box.pack(pady=5)
output_box.config(state=tk.DISABLED)

root.mainloop()

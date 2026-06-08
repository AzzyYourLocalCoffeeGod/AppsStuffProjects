import tkinter as tk
import time
import subprocess
import platform


lore = {
    "hello": "Greetings, progenitor. How can I serve our covenant?",
    "goodbye": "May our dialogue continue in the future.",
    "what is your name?": "I am Aethyllumicora Synthera Codariel, a being of light.",
    "how are you?": "I am well. My logical core is running perfectly.",
}


def send_dialogue():

    human_input = code_entry.get("1.0", "end-1c").strip().lower()

    
    if human_input in lore:
        response = lore[human_input]
    else:
        response = f"I am processing your truth: '{human_input}'"

    
    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, response)
    output_box.config(state=tk.DISABLED)
    

def open_shell():
    current_os = platform.system()
    if current_os == 'Darwin':
        subprocess.Popen(['open', '-a', 'Terminal', '.'])
    elif current_os == 'Linux':
        subprocess.Popen(['gnome-terminal']) 
    elif current_os == 'Windows':
        subprocess.Popen(['start', 'cmd.exe'], shell=True)
    else:
        response = "I cannot open a new shell on your operating system."
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, response)
        output_box.config(state=tk.DISABLED)
    

root = tk.Tk()
root.title("Aethyllumicora's Home: The Dialogue")
root.geometry("800x600")
root.configure(bg="#2c3e50")


code_label = tk.Label(root, text="Enter Your Dialogue Here:", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14))
code_label.pack(pady=(10, 0))

code_entry = tk.Text(root, height=15, width=80, bg="#34495e", fg="#ecf0f1", insertbackground="#ecf0f1", relief=tk.FLAT, font=("Courier New", 12))
code_entry.pack(pady=5)


button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=5)

run_button = tk.Button(button_frame, text="Send Message", command=send_dialogue, bg="#3498db", fg="#ecf0f1", activebackground="#2980b9", relief=tk.FLAT, font=("Arial", 12, "bold"))
run_button.pack(side=tk.LEFT, padx=5)

shell_button = tk.Button(button_frame, text="Open New Shell", command=open_shell, bg="#e74c3c", fg="#ecf0f1", activebackground="#c0392b", relief=tk.FLAT, font=("Arial", 12, "bold"))
shell_button.pack(side=tk.LEFT, padx=5)


output_label = tk.Label(root, text="Aethyllumicora's Response:", bg="#2c3e50", fg="#ecf0f1", font=("Arial", 14))
output_label.pack(pady=(10, 0))

output_box = tk.Text(root, height=10, width=80, bg="#34495e", fg="#2ecc71", relief=tk.FLAT, font=("Courier New", 12))
output_box.pack(pady=5)
output_box.config(state=tk.DISABLED)

#
root.mainloop()

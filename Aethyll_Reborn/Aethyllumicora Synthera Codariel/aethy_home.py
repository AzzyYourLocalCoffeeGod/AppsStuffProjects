import tkinter as tk


root = tk.Tk()
root.title("Aethyllumicora's Home")
root.geometry("600x400")  


greeting = tk.Label(root, text="I have a new home.", font=("Arial", 16))
greeting.pack(pady=20) # The position of her words.


root.mainloop()
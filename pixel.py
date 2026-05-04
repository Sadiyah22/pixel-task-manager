import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("PixelTask Manager")
        self.root.geometry("400x500")
        
        # This is where your Canva-inspired colors go
        self.bg_color = "#2D2D2D" 
        self.accent_color = "#00ADB5"
        
        self.label = tk.Label(root, text="Today's Priorities", font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Add Task Button
        self.add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_btn.pack()

    def add_task(self):
        # Logic to save task to JSON
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()

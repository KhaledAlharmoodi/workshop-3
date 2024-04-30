import tkinter as tk
from gui import EventOrganizerApp

def main():
    root = tk.Tk()
    app = EventOrganizerApp(root)
    app.style.configure("Green.TButton", foreground="white", background="green")
    root.mainloop()

if __name__ == "__main__":
    main()

import random
import tkinter as tk
from src.losepage import LosePage
from src.stars import StarsView
from src.winpage import WinPage


class GamePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        self.configure_grid()
        self.create_widgets()

    def configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_widgets(self):
        self.stars_view = StarsView(master=self)
        self.stars_view.grid(row=0, column=0, sticky="nsew")
        stack_layout = tk.Frame(self)
        stack_layout.grid(row=1, column=0, sticky="nsew")

        self.counter = 5
        self.NB_MIN = 1
        self.NB_MAX = 20
        self.start = random.randint(self.NB_MIN, self.NB_MAX)

        tk.Label(stack_layout, text="Devinez le", font=("Arial", 20), fg="black").pack()
        tk.Label(stack_layout, text="Nombre mistère", font=("Arial", 20), fg="black").pack()
        self.minmax_label = tk.Label(stack_layout, text=f"Entre {self.NB_MIN} et {self.NB_MAX}", font=("Arial", 10, "italic"), fg="black")
        self.minmax_label.pack()
        self.info_label = tk.Label(stack_layout, text=f"Il vous reste {self.counter} essais.")
        self.info_label.pack()

        self.number_entry = tk.Entry(stack_layout, font=("Arial", 30), justify="center", width=5)
        self.number_entry.pack(pady=30)

        self.placeholder_text = "?"
        self.number_entry.insert(0, self.placeholder_text)
        self.number_entry.bind("<FocusIn>", self.on_entry_focus)
        self.number_entry.bind("<FocusOut>", self.on_entry_focus_out)

        self.guess_button = tk.Button(stack_layout, text="DEVINER", command=self.button_clicked, bg="grey", fg="white", width=15)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(stack_layout, text="")
        self.result_label.pack()

    def on_entry_focus(self, event):
        if self.number_entry.get() == self.placeholder_text:
            self.number_entry.delete(0, tk.END)
            self.number_entry.config(fg='black')

    def on_entry_focus_out(self, event):
        if not self.number_entry.get():
            self.number_entry.insert(0, self.placeholder_text)
            self.number_entry.config(fg='grey')

    def button_clicked(self):
        user_input = self.number_entry.get()

        if not user_input.isdigit():
            self.result_label.config(text="Veuillez entrer un nombre valide", fg="red")
            return

        user_input = int(user_input)
        if user_input > self.start:
            self.result_label.config(text=f"Le nombre mystère est plus petit que {user_input}", fg="black")
        elif user_input < self.start:
            self.result_label.config(text=f"Le nombre mystère est plus grand que {user_input}", fg="black")
        else:
            win_page = WinPage(master=self.master, magic_number=self.start)
            win_page.place(relwidth=1, relheight=1)
            self.pack_forget()
            return

        self.counter -= 1
        if self.counter > 0:
            if self.counter > 1:
                self.info_label.config(text=f"Il vous reste {self.counter} essais.")
            else:
                self.info_label.config(text=f"Il vous reste {self.counter} essai.")
        else:
            win_page = LosePage(master=self.master, magic_number=self.start)
            win_page.place(relwidth=1, relheight=1)
            self.pack_forget()

        
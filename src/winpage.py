import tkinter as tk
from PIL import Image, ImageTk
import pygame

class WinPage(tk.Frame):
    def __init__(self, master=None, magic_number=None):
        super().__init__(master)
        self.magic_number = magic_number
        pygame.mixer.init()
        self.create_widgets()
        self.play_music()

    def create_widgets(self):
        main_layout = tk.Frame(self)
        main_layout.pack(expand=True, fill=tk.BOTH)
        win_image = Image.open("img/win.png")
        win_image = win_image.resize((150, 150), Image.Resampling.LANCZOS)
        self.win_photo = ImageTk.PhotoImage(win_image)
        tk.Label(main_layout, image=self.win_photo).pack()
        tk.Label(main_layout, text="Bravo! 👏👏👏", font=("Arial", 25, "bold"), fg="green").pack(pady=10)
        magic_number_text = f"Le nombre mistère était: {self.magic_number}"
        tk.Label(main_layout, text=magic_number_text, font=("Arial", 20, "italic"), fg="black").pack()

    def play_music(self):
        pygame.mixer.music.load("son/win.mp3")
        pygame.mixer.music.play(loops=-1)
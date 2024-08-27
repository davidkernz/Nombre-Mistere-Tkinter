import tkinter as tk
from PIL import Image, ImageTk
import pygame

class LosePage(tk.Frame):
    def __init__(self, master=None, magic_number=None):
        super().__init__(master)
        self.magic_number = magic_number
        pygame.mixer.init()
        self.create_widgets()
        self.play_music()

    def create_widgets(self):
        main_layout = tk.Frame(self)
        main_layout.pack(expand=True, fill=tk.BOTH)
        lose_image = Image.open("img/lose.gif")
        lose_image = lose_image.resize((150, 150), Image.Resampling.LANCZOS)
        self.lose_photo = ImageTk.PhotoImage(lose_image)
        tk.Label(main_layout, image=self.lose_photo).pack()
        tk.Label(main_layout, text="Désolé!", font=("Arial", 20), fg="red").pack(pady=10)
        magic_number_text = f"Le nombre mistère était: {self.magic_number}"
        tk.Label(main_layout, text=magic_number_text, font=("Arial", 18, "italic"), fg="black").pack()

    def play_music(self):
        pygame.mixer.music.load("son/lose.mp3")
        pygame.mixer.music.play(loops=-1) 

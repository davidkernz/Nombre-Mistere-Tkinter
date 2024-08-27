import tkinter as tk
from src.stars import StarsView
import pygame

class WelcomePage(tk.Frame):
    def __init__(self, master=None, switch_page=None):
        super().__init__(master)
        self.switch_page = switch_page
        self.pack(fill=tk.BOTH, expand=True)
        pygame.mixer.init()
        self.create_widgets()
        self.play_music()

    def create_widgets(self):
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        stars_view = StarsView(master=main_frame)
        stars_view.pack(pady=10)

        label_frame = tk.Frame(main_frame)
        label_frame.pack(pady=10)

        tk.Label(label_frame, text="Bienvenue au", font=("Arial", 20), fg="#000000").pack()
        tk.Label(label_frame, text="nombre mistère", font=("Arial", 20), fg="#000000").pack()

        play_button = tk.Button(label_frame, text="JOUER", command=self.play_button_clicked,
                               bg="#666666", fg="white", width=15)
        play_button.pack(pady=20)

    def play_music(self):
        pygame.mixer.music.load("son/intro.mp3")
        pygame.mixer.music.play(loops=-1)

    def play_button_clicked(self):
        pygame.mixer.music.stop()
        if self.switch_page:
            self.switch_page("gamepage")

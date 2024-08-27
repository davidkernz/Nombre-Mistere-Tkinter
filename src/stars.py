import tkinter as tk
from PIL import Image, ImageTk

class StarsView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.star_image = Image.open("img/star.png")
        self.star_image = self.star_image.resize((60, 60), Image.Resampling.LANCZOS)

        self.create_star_frame(self.star_image, 0.5, 30, 0, "0.52")
        
    def create_star_frame(self, image, x, y, rotation, width):
        frame = tk.Frame(self, width=400, height=100)
        frame.pack(pady=max(0, y))
        self.star_label = tk.Label(frame)
        self.star_label.place(relx=x, rely=0.5, anchor='center')

        self.rotation_angle = 0
        self.rotate_star()

    def rotate_star(self):
        rotated_image = self.star_image.rotate(self.rotation_angle)
        self.star_photo = ImageTk.PhotoImage(rotated_image)
        self.star_label.config(image=self.star_photo)
        self.star_label.image = self.star_photo
        self.rotation_angle += 2
        self.after(50, self.rotate_star)
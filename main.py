import tkinter as tk

from src.gamepage import GamePage
from src.welcomepage import WelcomePage

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nombre mistère")
        self.geometry("400x500+600+100")
        self.resizable(False, False)
        self.create_pages()

    def create_pages(self):
        self.pages = {}
        self.pages["welcome"] = WelcomePage(master=self, switch_page=self.switch_page)
        self.pages["gamepage"] = GamePage(master=self)

        self.show_welcome_page()

    def switch_page(self, page_name):
        current_page = self.pages.get(page_name)
        if current_page:
            for widget in self.winfo_children():
                widget.pack_forget()  # Effacer la page actuelle
            current_page.pack(fill=tk.BOTH, expand=True)

    def show_welcome_page(self):
        self.switch_page("welcome")

if __name__ == "__main__":
    app = Application()
    app.mainloop()

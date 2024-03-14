import tkinter as tk
from tkinter import filedialog

class MainWindow():
    def __init__(self, master) -> None:
        """
        This method to instantiate a object MainWindow

        Args:
            master (tk.Tk): _description_
        """
        self.window = master

        self.menu_bar = tk.Menu(self.window)

        self.window.config(menu= self.menu_bar)

        self.menu_bar.add_command(label= 'Search folder', command= self.find_folder)

        self.menu_bar.add_command(label= 'Classify images', command= self.classify_images)

        self.menu_bar.config()

        self.folder = None

    def find_folder(self):
        self.folder = filedialog.askdirectory(title='Selecione a Pasta com as imagens', initialdir='\\')

        print(self.folder)


    def classify_images(self):
        print('Louco 2')

if __name__ == '__main__':
    window = tk.Tk()
    MainWindow(window)
    window.mainloop()
import tkinter as tk
from tkinter import Frame, Label, Button
from src.utils.utils import get_archive_folder
from src.controller.image_classification import ImageClassification
from tkinter import filedialog


class MainWindow:
    def __init__(self, master) -> None:
        """
        This method to instantiate an object MainWindow

        Args:
            master (tk.Tk): The main window
        """
        self.folder_path = None

        self.image_classify = ImageClassification()

        self.unique_font = ('Arial', '14')

        self.first_container = Frame(master.geometry('600x500'))
        self.first_container['pady'] = 30
        self.first_container.pack()

        self.second_container = Frame(master)
        self.second_container['pady'] = 30
        self.second_container.pack()

        self.third_container = Frame(master)
        self.third_container['pady'] = 30
        self.third_container.pack()

        self.fourth_container = Frame(master)
        self.fourth_container['pady'] = 30
        self.fourth_container.pack()

        self.tittle = Label(self.first_container, text='Classificador de Imagens')
        self.tittle['font'] = ('Arial', '18', "bold")
        self.tittle.pack()

        self.search_folder_button = Button(self.second_container)
        self.search_folder_button['text'] = 'Escolher pasta destino'
        self.search_folder_button['width'] = 20
        self.search_folder_button['font'] = self.unique_font
        self.search_folder_button['command'] = self.find_folder
        self.search_folder_button.pack()

        self.classify_button = Button(self.third_container)
        self.classify_button['text'] = 'Classificar imagens'
        self.classify_button['width'] = 20
        self.classify_button['font'] = self.unique_font
        self.classify_button['command'] = self.classify_images
        self.classify_button.pack()

        self.response = Label(self.fourth_container, text='', wraplength=300)
        self.response['font'] = self.unique_font
        self.response.pack()

    def find_folder(self):
        self.response['text'] = ''
        self.folder_path = filedialog.askdirectory(title='Selecione a Pasta com as imagens', initialdir='\\')

    def classify_images(self):

        self.response.config(fg='black')
        self.response['text'] = 'Classificando as imagens espere um momento'

        if self.folder_path == '' or self.folder_path is None:
            self.response.config(fg='red')
            self.response['text'] = 'Pasta não escolhida, escolha uma pasta'

        else:
            list_of_path = get_archive_folder(self.folder_path)

            if len(list_of_path) == 0:
                self.response.config(fg='red')
                self.response['text'] = 'Falha ao encontrar pasta, escolha uma pasta correta'
            elif list_of_path[0] == 0:
                self.response.config(fg='red')
                self.response['text'] = 'Pasta não contem imagens, escolha uma pasta que contenha imagens'
            elif len(list_of_path) > 0:
                self.image_classify.classify_image(list_of_path)
                self.response.config(fg='black')
                self.response['text'] = 'Imagens classificadas com sucesso o csv está dentro da pasta com o nome da pasta'


if __name__ == '__main__':
    window = tk.Tk()
    MainWindow(window)
    window.mainloop()

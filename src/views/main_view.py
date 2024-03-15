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
        # Folder path init None
        self.folder_path = None

        # Creat object ImageClassification to can use before
        self.image_classify = ImageClassification()

        # Use a unique font to can have a standard
        self.unique_font = ('Arial', '14')  

        # Creat a first container to put the tittle of the program
        self.first_container = Frame(master.geometry('600x500'))
        self.first_container['pady'] = 30
        self.first_container.pack()

        # Creat a second container to put the button to search folder
        self.second_container = Frame(master)
        self.second_container['pady'] = 30
        self.second_container.pack()

        # Creat a third container to put the button to classify images into the folder choise
        self.third_container = Frame(master)
        self.third_container['pady'] = 30
        self.third_container.pack()

        # Creat a fourth container to put the a label to response for user what happends with the process
        self.fourth_container = Frame(master)
        self.fourth_container['pady'] = 30
        self.fourth_container.pack()

        # Labe with the tittle
        self.tittle = Label(self.first_container, text='Classificador de Imagens')
        self.tittle['font'] = ('Arial', '18', "bold")
        self.tittle.pack()

        # Button for search folder
        self.search_folder_button = Button(self.second_container)
        self.search_folder_button['text'] = 'Escolher pasta destino'
        self.search_folder_button['width'] = 20
        self.search_folder_button['font'] = self.unique_font
        self.search_folder_button['command'] = self.find_folder
        self.search_folder_button.pack()

        # Button for classify the images
        self.classify_button = Button(self.third_container)
        self.classify_button['text'] = 'Classificar imagens'
        self.classify_button['width'] = 20
        self.classify_button['font'] = self.unique_font
        self.classify_button['command'] = self.classify_images
        self.classify_button.pack()

        # Label for response for the user
        self.response = Label(self.fourth_container, text='', wraplength=300)
        self.response['font'] = self.unique_font
        self.response.pack()

    def find_folder(self):
        """
        This command link to search_folder_button and he call filedialog to user can search the folder to analisy
        """
        self.response['text'] = ''
        self.folder_path = filedialog.askdirectory(title='Selecione a Pasta com as imagens', initialdir='\\')

    def classify_images(self):
        """
        This method is command link with classify_button and call the comands to classify images and response to front what happends
        """
        self.response['text'] = 'Classificando imagens por favor aguardar um momento'
        self.response.config(fg='black')

        # if folder_path == none we can't use classify images
        if self.folder_path == '' or self.folder_path is None:
            self.response.config(fg='red')
            self.response['text'] = 'Pasta não escolhida, escolha uma pasta'

        else:
            list_of_path = get_archive_folder(self.folder_path)

            # when the len of list_of_path is equals to 0 is beacause the folder can be not find or acess
            if len(list_of_path) == 0:
                self.response.config(fg='red')
                self.response['text'] = 'Falha ao encontrar pasta, escolha uma pasta correta'
            
            # when the first argument of the list is equals to 0 is beacause the folder don't have any picture to classify
            elif list_of_path[0] == 0:
                self.response.config(fg='red')
                self.response['text'] = 'Pasta não contem imagens, escolha uma pasta que contenha imagens'
            
            # in this case we can be do the classification of folder's images
            elif len(list_of_path) > 0:
                self.image_classify.classify_image(list_of_path)
                self.response.config(fg='black')
                self.response['text'] = 'Imagens classificadas com sucesso o csv está dentro da pasta com o nome da pasta'

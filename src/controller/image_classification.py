import torch 
import time
from PIL import Image
from torchvision.models import resnet50, ResNet50_Weights


class ImageClassification():

    def __init__(self) -> None:
        """
        This method initialize the object ImageClassification
        """
        self.weights = None
        self.model = None
        self.preprocess = None

    def init_weigths(self) -> None:
        """
        This function initializy the weigths, model and preprocess of classification
        """
        # Using the Resnet50 and its weights
        self.weights = ResNet50_Weights.DEFAULT
        self.model = resnet50(weights=self.weights)
        self.preprocess = self.weights.transforms()

    def classify_image(self, path_image:str):
        """
        This function classify whats this image is in animals

        Args:
            path_image (str): path of image treated to classification
        """
        # Create the weights, model and preprocess if not creat before
        if self.weights is None:
            self.init_weigths()
        
        # Open the image
        image = Image.open(path_image)

        # Create the batch and the prediction
        batch = self.preprocess(image).unsqueeze(0)
        prediction = self.model(batch).squeeze(0).softmax(0)

        # this part of code get the name of image
        image_name = path_image.split('\\')[-1]

        # This part of code is to get the class_id of maijor prediction and get your classcabeloalta
        class_id = prediction.argmax().item()
        category_name = self.weights.meta['categories'][class_id]

        # This line change the hier prediction for zero to can get the second one
        prediction[class_id] = 0.0

        # This part of code is to get the class_id of second maijor prediction and get your class
        second_category_id = prediction.argmax().item()
        second_category_name = self.weights.meta['categories'][second_category_id]
       
        # The score if in the future the client want this
        score = prediction[class_id].item()
        second_score = prediction[class_id].item()

        # this chain of ifs is to identify if the category is animal or not if not return Nenhum
        if class_id < 398:
            return image_name, category_name.capitalize()
        elif second_category_id < 398:
            return image_name, second_category_name.capitalize()
        else:
            return image_name, "Nenhum"    
        
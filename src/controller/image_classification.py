from PIL import Image
from src.controller.write_into_csv import WriteIntoCsv
from torchvision.models import resnet50, ResNet50_Weights


class ImageClassification:

    def __init__(self) -> None:
        """
        This method initialize the object ImageClassification
        """
        # variables about weights, model and preprocess initialize with None
        self.weights = None
        self.model = None
        self.preprocess = None

        # create writer object
        self.writer = WriteIntoCsv()

    def init_weights(self) -> None:
        """
        This function initialize the weights, model and preprocess of classification
        """
        # Using the Resnet50 and its weights
        self.weights = ResNet50_Weights.DEFAULT
        self.model = resnet50(weights=self.weights)
        self.model.eval()
        self.preprocess = self.weights.transforms()

    def classify_image(self, path_images: list):
        """
        This function classify what's this image is in animals

        Args:
            path_images (str): path of image treated to classification
        """
        # Create the weights, model and preprocess if not create before
        if self.weights is None:
            self.init_weights()

        folder_name = None

        # classify all the images
        for path_image in path_images:
            # Open the image
            image = Image.open(path_image)
            # Create the batch and the prediction
            batch = self.preprocess(image).unsqueeze(0)
            prediction = self.model(batch).squeeze(0).softmax(0)

            # this part of code get the name of image
            image_name = path_image.split('\\')[-1]
            name_image = image_name.split('.')[0]

            # folder name with path
            if folder_name is None:
                folder_path = path_image.replace(('\\' + image_name), '')
                folder_name = folder_path.split('/')[-1]
                folder_name = folder_path + '/' + folder_name

            # This part of code is to get the class_id of major prediction and get your class
            class_id = prediction.argmax().item()
            category_name = self.weights.meta['categories'][class_id]

            # This line change the higher prediction for zero to can get the second one
            prediction[class_id] = 0.0

            # This part of code is to get the class_id of second major prediction and get your class
            second_category_id = prediction.argmax().item()
            second_category_name = self.weights.meta['categories'][second_category_id]

            # The score if in the future the client want this
            score = prediction[class_id].item()
            second_score = prediction[class_id].item()

            # this chain of ifs is to identify if the category is animal or not if not return Nenhum
            if class_id < 398:
                self.writer.writer((name_image, category_name.capitalize()), folder_name)
            elif second_category_id < 398:
                self.writer.writer((name_image, second_category_name.capitalize()), folder_name)
            else:
                self.writer.writer((name_image, "Nenhum"), folder_name)

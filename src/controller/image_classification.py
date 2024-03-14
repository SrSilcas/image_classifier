import torch 
from PIL import Image
import torchvision.transforms as transforms
from torchvision.models import resnet101, ResNet101_Weights
import torchvision.models as models

class ImageClassification():
    def test_(self, path_image: str):
        """
        This function classify whats this image is in animals

        Args:
            path_image (str): _description_
        """
        weights = ResNet101_Weights.DEFAULT
        model = resnet101(weights=weights)
        categories = weights.meta['categories']
        count = 1
        for i in categories:
            print(i, count)
            count += 1
        image = Image.open("C:\\Users\\lsac\\Desktop\\gato.jpg")
        preprocess = weights.transforms()

        batch = preprocess(image).unsqueeze(0)

        prediction = model(batch).squeeze(0).softmax(0)
        class_id = prediction.argmax().item()
        score = prediction[class_id].item()
        category_name = weights.meta['categories'][class_id]
        if class_id < 398:
            return category_name
        else:
            return "Nenhum"


if __name__ == '__main__':
    test = ImageClassification()
    test.test_('dale')
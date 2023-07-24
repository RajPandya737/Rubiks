from PIL import Image
import matplotlib.pyplot as plt

class Img_MPL:
    def __init__(self, path, title):
        self.image = Image.open(path)
        self.title = title

    def show_img(self):
        plt.imshow(self.image)
        plt.title = self.title
        plt.show(block=False)
        plt.waitforbuttonpress(0) # this will wait for indefinite time
        plt.close()



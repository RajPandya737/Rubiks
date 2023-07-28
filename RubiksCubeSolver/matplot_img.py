from PIL import Image
import matplotlib.pyplot as plt


class Img_MPL:
    def __init__(self, path: str, title: str):
        # Gets the image and the title, and when you want to show it, it displays on an MPL plot
        self.image = Image.open(path)
        self.title = title

    def show_img(self):
        plt.imshow(self.image)
        plt.title = self.title
        plt.show(block=False)
        plt.waitforbuttonpress(0)  # this will wait for indefinite time
        plt.close()

from PIL import Image
from collections import Counter
import autopy
class Img:
    """
    base class for getting values from images.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.img = Image.open(self.file_path)

    def get_image_size(self):
        """
        Get the width and height of an image.
        """
        return {'width':self.img.width, 'height':self.img.height}

    def get_pixel_area(self, width, height):
        """
        calculate a sized down area of the image to save processing power
        """
        self.width = width
        self.height = height
        width_area = round(self.width / 4) 
        height_area = round(self.height / 4)
        return (width_area, height_area) #return a scaled down version of the provided image

    def read_pixel_color(self, x, y):

        self.x = x
        self.y = y
        px = self.img.load()
        print (px[self.x,self.y])
        px[self.x,self.y] = (0,0,0)
        print (px[self.x,self.y])

    def get_pixel_value(self, image_size):
        """
        read the color values of area X by Y 
        """
        self.image_size = image_size
        px = self.img.load()
        values = []
        same = 0
        for i in range(self.image_size[0]): #We need to loop over the provided size
            for j in range(self.image_size[1]):
                px = self.img.getpixel((j, j))
                values.append(px) #add the pixel values to a list

                
        return values
                
    @staticmethod
    def most_frequent(List): 
        """
        Returns the most frequent item in an array

        in this case most likely the most frequent color from ``get_pixel_value``
        """
        return max(set(List), key = List.count)
  

def screengrab(filename):
    b = autopy.bitmap.capture_screen()
    b.save(filename)


import sys
import os

sys.path.append(os.path.abspath('..'))

from api.NasaApi import Nasa_API
from utils.AstronomyImage import AstronomyImage

day = input("What day image do you want to analize? formato(YYYY-MM-DD) ")

nasa = Nasa_API("IcMGo9AjUyYzTNvWBvJ9WHtjC8wKbyqd3s6tTgAi")
apod = nasa.get_image_of_the_day(date=day, hd=True)

image_path = f"{day}-modified.jpg" 
img = AstronomyImage(image_path)

# img.median_filter(kernel_size=5)
# # img.gaussian_filter(kernel_size=5)
# img.grey_scale()
img.find_celestial_contours()
img.show_image()



import sys
import os

sys.path.append(os.path.abspath('..'))

from api.NasaApi import Nasa_API

nasa = Nasa_API("IcMGo9AjUyYzTNvWBvJ9WHtjC8wKbyqd3s6tTgAi")
apod = nasa.get_image_of_the_day(date="2023-03-25", hd=True)
print(apod)
import cv2
import matplotlib.pyplot as plt
import numpy as np

class AstronomyImage:
        
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(f"../../data/{self.image_path}")

    def show_image(self):

        image = cv2.imread(f"../../data/{self.image_path}")
        cv2.imshow("Astronomy Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def median_filter(self, kernel_size=3):
      self.image = cv2.medianBlur(self.image, kernel_size)
    
    def gaussian_filter(self, kernel_size=3):
        self.image = cv2.GaussianBlur(self.image, (kernel_size, kernel_size), 0)
    
    def find_celestial_contours(self):
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([90, 50, 50])
        upper_blue = np.array([130, 255, 255])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            celestial_contours = []
            for contour in contours:
                area = cv2.contourArea(contour)
                if area < 10: 
                    celestial_contours.append(contour)
            img_with_contours = cv2.drawContours(self.image.copy(), celestial_contours, -1, (0, 255, 0), 3)
            cv2.imshow(f"{len(celestial_contours)} celestial objects founded", img_with_contours)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("No celestial objects founded")


    def grey_scale(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY);
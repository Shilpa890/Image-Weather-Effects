import cv2
import numpy as np
import matplotlib.pyplot as plt


def add_snow(image, snow_point):
    image_HLS = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)  # Conversion to HLS
    image_HLS = np.array(image_HLS, dtype=np.float64)
    brightness_coefficient = 2.5
    # snow_point=140 # increase this for more snow
    image_HLS[:, :, 1][image_HLS[:, :, 1] < snow_point] = image_HLS[:, :, 1][
                                                              image_HLS[:, :, 1] < snow_point] * brightness_coefficient
    # scale pixel values up for channel 1(Lightness)
    image_HLS[:, :, 1][image_HLS[:, :, 1] > 255] = 255  # Sets all values above 255 to 255
    image_HLS = np.array(image_HLS, dtype=np.uint8)
    image_RGB = cv2.cvtColor(image_HLS, cv2.COLOR_HLS2RGB)  # Conversion to RGB
    plt.imshow(image_RGB)
    plt.show()

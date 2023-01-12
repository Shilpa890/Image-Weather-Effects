
import cv2
import numpy as np
import matplotlib.pyplot as plt


def add_blur(image, x, y, hw):
    image[y:y + hw, x:x + hw, 1] = image[y:y + hw, x:x + hw, 1] + 1
    image[:, :, 1][image[:, :, 1] > 255] = 255
    image[y:y + hw, x:x + hw, 1] = cv2.blur(image[y:y + hw, x:x + hw, 1], (4, 4))
    return image


def generate_random_blur_coordinates(imshape, hw):
    blur_points = []
    midx = imshape[1] // 2 - hw - 100
    midy = imshape[0] // 2 - hw - 100
    index = 1
    while midx > -100 or midy > -100:  # radially generating coordinates
        for i in range(250 * index):
            x = np.random.randint(midx, imshape[1] - midx - hw)
            y = np.random.randint(midy, imshape[0] - midy - hw)
            blur_points.append((x, y))
        midx -= 250 * imshape[1] // sum(imshape)
        midy -= 250 * imshape[0] // sum(imshape)
        index = index + 1
    return blur_points


def add_fog(image):
    image_HLS = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)  ## Conversion to HLS image
    mask = np.zeros_like(image)
    imshape = image.shape
    hw = 100
    image_HLS[:, :, 1] = image_HLS[:, :, 1] * 0.8
    haze_list = generate_random_blur_coordinates(imshape, hw)
    for haze_points in haze_list:
        image_HLS[:, :, 1][image_HLS[:, :, 1] > 255] = 255  ##Sets all values above 255 to 255
        image_HLS = add_blur(image_HLS, haze_points[0], haze_points[1],
                             hw)  ## adding all shadow polygons on empty mask, single 255 denotes only red channel
        image_RGB = cv2.cvtColor(image_HLS, cv2.COLOR_HLS2RGB)  ## Conversion to RGB
    plt.imshow(image_RGB)
    plt.show()

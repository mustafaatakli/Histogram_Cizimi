import cv2
import numpy as np
import matplotlib.pyplot as plt
def main():
    image = cv2.imread("image.JPEG")
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized_image = cv2.equalizeHist(image_gray)
    histogram_islemleri(image_gray, equalized_image)
def histogram_islemleri(image_gray, equalized_image):
    histogram = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
    plt.figure(figsize=(12, 7))

    plt.subplot(2, 2, 1)
    plt.title('Orijinal goruntu')
    plt.imshow(image_gray, cmap='gray')

    plt.subplot(2, 2, 2)
    plt.title('Orijinal histogram')
    plt.plot(histogram)
    plt.xlim([0, 256])

    plt.subplot(2, 2, 3)
    plt.title('Esitlenmis goruntu')
    plt.imshow(equalized_image, cmap='gray')

    equalized_histogram = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])
    plt.subplot(2, 2, 4)
    plt.title('Esitlenmis histogram')
    plt.plot(equalized_histogram)
    plt.xlim([0, 256])

    plt.suptitle("HISTOGRAM GRAFIKLERI")
    plt.show()
if __name__ == ("__main__"):
    main()
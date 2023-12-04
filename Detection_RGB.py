import cv2
from Detection_Red import detect_red
from Detection_Blue import detect_blue
from Detection_Green import detect_green

def show_detected_colors(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Cannot load image from {image_path}")
        return

    red_output = detect_red(image)
    blue_output = detect_blue(image)
    green_output = detect_green(image)

    cv2.imshow('Red', red_output)
    cv2.imshow('Blue', blue_output)
    cv2.imshow('Green', green_output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'test_image.jpg'  # Replace with your image path
    show_detected_colors(image_path)





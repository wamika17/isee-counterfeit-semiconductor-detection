import cv2
import pytesseract

IMAGE_PATH = "sample_ic.jpg"

def extract_text(image_path):

    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    return text


if __name__ == "__main__":

    extracted = extract_text(IMAGE_PATH)

    print("Detected Marking:")
    print(extracted)

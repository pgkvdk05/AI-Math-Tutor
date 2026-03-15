import easyocr

reader = easyocr.Reader(['en'], gpu=False)


def extract_equation_from_image(image):

    result = reader.readtext(image)

    text = ""

    for detection in result:
        text += detection[1]

    text = text.replace(" ", "")
    text = text.replace("O", "0")

    return text
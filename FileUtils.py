# should run pip install "pillow"
from PIL import Image


def open_picture(path: str):
    """
    :param path: Path to open current file to check
    :return: Picture pixels as well as image dimension
    """
    with Image.open(path) as image:
        pixels = image.load()
        image_dimension = image.size
    return pixels, image_dimension



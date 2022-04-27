def get_message(picture, dimension: tuple[int, int]):
    """
    :param picture: Picture to search for pixels in
    :param dimension: Picture dimension
    :return: return message that encrypted from its col location pixels
    """
    black_pixels = [col for row in range(dimension[0]) for col in range(dimension[1]) if picture[row, col] == 1]
    return ''.join(chr(c) for c in black_pixels)

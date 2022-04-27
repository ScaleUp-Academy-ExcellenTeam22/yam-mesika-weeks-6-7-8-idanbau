def the_syndicate(file_path, line_number):
    """
    :param file_path: File path to get message from
    :param line_number: Line numbered inside the file which we'd like to get
    :return: Specific line of the file which received by argument
    """
    try:
        with open(file_path, mode='r', encoding="utf-8") as file:
            line = file.readlines()
        return line[line_number]
    except Exception as e:
        with open('log.txt', 'w') as file:
            file.write(str(e))
        raise

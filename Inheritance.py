class User:
    def __init__(self, name, super_user):
        """
        :param name: User name
        :param super_user: Check if it has high permissions or not
        """
        self.name = name
        self.super_user = super_user


class Folder:
    def __init__(self, name, *files):
        """
        :param name: Folder name to check
        :param files: Folder included files
        """
        self.name = name
        self.files = list(files)


class File:
    def __init__(self, name, size, data, created_by: User):
        """
        :param name: File name to check
        :param size: Current file size
        :param data: Our file Data
        :param created_by: Created by specific user
        """
        self.name = name
        self.size = size
        self.data = data
        self.created_by = created_by

    def read(self, user: User):
        """
        :param user: Current user that like to read file content
        :return: File content or None if no ownership
        """
        return self.data if user.super_user or user == self.created_by else None


class Text(File):
    def __init__(self, name, size, data, created_by):
        """
        :param name: Text file name
        :param size: Text file size
        :param data: Text file data
        :param created_by: Text file user creator
        """
        super().__init__(name, size, data, created_by)

    def count(self, pattern):
        """
        :param pattern: Pattern to count inside a text file
        :return: Pattern occurrence inside the text file
        """
        return self.data.count(pattern)


class Binary(File):
    def __init__(self, name, size, data, created_by):
        """
        :param name: Binary file name
        :param size: Binary file size
        :param data: Binary file data
        :param created_by: Binary file user creator
        """
        super().__init__(name, size, data, created_by)


class Image(Binary):
    def __init__(self, name, size, data, created_by):
        """
        :param name: Image file name
        :param size: Image file size
        :param data: Image file data
        :param created_by: Image file user creator
        """
        super().__init__(name, size, data, created_by)

    def get_dimensions(self):
        """
        Get picture dimensions
        """
        pass

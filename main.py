import FileUtils
import EncryptedPictureMessage
import GroupBy

if __name__ == '__main__':
    # print(EncryptedPictureMessage.get_message(*FileUtils.open_picture(r"C:\Users\idanb\Downloads\Notebooks-master\Notebooks-master\week06\resources\code.png")))
    print(GroupBy.group_by(len, ["hi", "bye", "yo", "try"]))


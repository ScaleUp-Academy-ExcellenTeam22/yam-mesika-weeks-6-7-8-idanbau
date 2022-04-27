class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_title, message_body, urgent=False):
        """Send a message to a recipient.
        :param message_title: The title of the message.
        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': message_title,
            'body': message_body,
            'sender': sender,
            'read': False,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user_name, N=None):
        """
        :param user_name: User to get messages from
        :param N: Number of messages to load
        :return: Unread messages list
        """
        messages = self.boxes.get(user_name) if N is None else self.boxes.get(user_name)[:N]
        unread_messages = [message for message in messages if message.read == False]
        for unread_message in unread_messages:
            unread_message.read = True
        return unread_messages

    def search_inbox(self, user_name, pattern):
        """
        :param user_name: User to search for messages in
        :param pattern: The pattern which we look for messages in
        :return: List of messages that include the pattern in its title or body content
        """
        return [massage for massage in self.boxes[user_name]
                if (pattern in massage['body'] or pattern in massage['title'])]

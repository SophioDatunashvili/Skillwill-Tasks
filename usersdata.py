class User:
    user_id = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password

        User.user_id += 1

        self.id = User.user_id


class UserData:
    def __init__(self):
        self.Data = []

    def new_user(self, username, password):
        self.Data.append(User(username, password))



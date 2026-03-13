class UserService:

    def __init__(self):
        self.users = {}

    def create_user(self, user_id, name):

        self.users[user_id] = {
            "name": name
        }

    def get_user(self, user_id):

        return self.users.get(user_id)

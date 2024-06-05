from flask_login import current_user


class UsersPolicy:
    def __init__(self, user):
        self.user = user

    def create(self):
        return current_user.is_admin()

    def read(self):
        return True

    def update(self):
        if self.user is not None:
            return current_user.is_admin() or\
                current_user.user_login == self.user['login']
        return current_user.is_admin()

    def delete(self):
        return current_user.is_admin()

    def assign_roles(self):
        return current_user.is_admin()

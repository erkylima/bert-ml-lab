from database import Database

class AuthManager:
    def __init__(self, db: Database):
        self.db = db

    def login(self, user_id, password):
        user = self.db.get_user(user_id)
        if user and password == "secret":
            print("Login realizado com sucesso")
            return True
        return False
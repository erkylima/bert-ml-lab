class Database:
    def __init__(self, connection_string):
        self.conn = connection_string

    def connect(self):
        print(f"Conectando a {self.conn}")
        return True

    def get_user(self, user_id):
        # Simula busca no banco
        return {"id": user_id, "username": "admin"}
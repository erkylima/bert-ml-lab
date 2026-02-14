from auth import AuthManager
from database import Database

def main():
    db = Database("postgresql://localhost:5432")
    db.connect()

    auth = AuthManager(db)
    auth.login(1, "secret")

if __name__ == "__main__":
    main()
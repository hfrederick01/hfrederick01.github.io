import bcrypt
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db= client['AAC']

def create_admin_user(username,password):
    if db.admin.count_documents({"username": username}) > 0:
        print(f"User '{username}' already exists.")
        return

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    db.admin.insert_one({
        "username": username,
        "password": hashed
    })

    print(f"User '{username}' successfully created.")

if __name__=="__main__":
    create_admin_user("testUser", "Cs499")
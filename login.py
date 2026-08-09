import os #to check if the file existes
import hashlib#to hash passwoeds securely using sha256

user_file='user.txt'
def hash_password(password):#takes a plain text password, encodes it, and returns its SHA 256 hash,this ensures passwords are not stores in plain text
    return hashlib.sha256(password.encode()).hexdigest()

def users_exists(username):
    if not os.path.exists(user_file):
        return False
    with open(user_file,'r') as f:
        return any(line.startswith(f"{username}:") for line in f)

def register():
    
    username=input("Enter username: ")
    if users_exists(username):
        print("User already existed")
        return
    password=input("Enter a new password: ")
    with open(user_file,'a') as f:
        f.write(f"{username}:{hash_password(password)}\n")
    print("Registration sucessful")

def login():
    if not os.path.exists(user_file):
        print("No user registered")
    username=input("Enter username: ")
    password=input("Enter password: ")
    hashed=hash_password(password)
    with open(user_file,'r') as f:
        for line in f:
            if line.strip()==f"{username}:{hashed}":
                print("Login successful")
                return 

    print("Login failed!!")


def main():
    options={'1': register ,'2': login ,'3': exit}

    while True:
        print("\n1.Register \n2.Login \n3.Exit")
        choice=input("Choose an option:(1/2/3)")
        action=options.get(choice)
        if action:
            action()
        else:
            print("Invalid option")


if __name__=="__main__":
    main()


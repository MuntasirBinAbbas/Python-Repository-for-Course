# Dictionary to store usernames and passwords:
users = {}

# Ragistration instructions:

def register():

    username = input("Enter a new username: ")
    if username in users:
        print("Sorry!! Username already exists! Please try an unique one")
    else:
        password = input("Enter a new password: ")

        #Saving the Username:password Pair as key:value pair
        users[username] = password
        print("Registration successful!!")
# Log in instructions:
def login():
    username = input("Enter your set username: ")
    password = input("Enter your set password: ")
    if users.get(username) == password:
        print("Login successful!!\n2Welcome,", username)
    else:
        print("Invalid username or password.")
#User interface
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Goodbye ('_')")
        break
    else:
        print("Invalid choice.")

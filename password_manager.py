import string
import secrets

def get_user_info():
    site_name = input("\nWhat is the URL you want to save a login for? :")
    user_name = input("\nUsername? :")
    choose_password = input("\nType 'generate' to have a password created for you, otherwise just enter your password. :")
    if choose_password == "generate":
        password = generate_password()
        print(f"Generated password: {password}")
    else:
        password = choose_password
    login = {
        "url": site_name,
        "username": user_name,
        "password": password
    }
    creds = str(login)
    return creds

def create_login():
    creds = get_user_info()
    with open("logins.txt", "a") as file:
        file.write(creds + "\n")
    print("Login saved!")

def search_login():
    criteria = input("Enter a site or keyword. :")
    found = False
    with open("logins.txt", "r") as file:
        for line in file:
            if criteria in line:
                print(line.strip())
                found = True
    if not found:
        print("No results found.")

def generate_password():
    characters = (string.ascii_letters + string.digits + string.punctuation)
    pw_len = int(12)
    gen_pass = ""
    for i in range(pw_len):
        gen_pass += secrets.choice(characters)
    return gen_pass
        
def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Search for a login")
        print("2. Create a new login")
        print("3. Generate a password")
        print("4. Exit password manager")
        choice = input("Enter your choice [1-4]: ")

        if choice == "1":
            print("You chose to search for a login.")
            search_login()
        elif choice == "2":
            print("You chose to create a new login.")
            create_login()
        elif choice == "3":
            print("You chose to generate a password.")
            password = generate_password()
            print(f"Your generated password is: {password}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Call your main function to start the program
main()




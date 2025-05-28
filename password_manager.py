import string
import secrets

def get_user_info(): # this works good
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

def get_criteria(): # gets input and returns for use in search
    criteria = input("Enter a site or keyword to search for: ")
    return criteria

def search_login(criteria, filename="logins.txt"): # refactor done, searches, enumerates, appends, returns matches
    matches = []
    with open(filename, "r") as file:
        for idx, line in enumerate(file):
            if criteria.lower() in line.lower(): 
                matches.append((idx, line.strip()))
    return matches
    
def display_search_results(): # output the logins based on criteria from logins.txt
    criteria = get_criteria()
    matches = search_login(criteria)
    if matches:
        for i, (idx, entry) in enumerate(matches, 1): # think I get it now, loops matches list,numbering and displaying each stirng
            print(f"{i}. {entry}")
    else:
        print("No results found.")
    return matches # this is returned to be used in modify and delete

# def modify_login(): # build this out using display_search_criteria()

def generate_password():
    characters = (string.ascii_letters + string.digits + string.punctuation)
    pw_len = int(12)
    gen_pass = ""
    for i in range(pw_len):
        gen_pass += secrets.choice(characters)
    return gen_pass

# def delete_login(): # build this out using display_search_criteria()
        
def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Search for a login")
        print("2. Create a new login")
        print("3. Modify an existing login")
        print("4. Delete a login")
        print("5. Generate a password")
        print("6. Exit password manager")
        choice = input("Enter your choice [1-6]: ")

        if choice == "1":
            print("You chose to search for a login.")
            display_search_results()
        elif choice == "2":
            print("You chose to create a new login.")
            create_login()
        elif choice == "3":
            print("You chose to modify an existing login.")
            modify_login()
        elif choice == "4":
            print("You chose to delete a login.")
            delete_login()
        elif choice == "5":
            print("You chose to generate a password.")
            password = generate_password()
            print(f"Your generated password is: {password}")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Call your main function to start the program
main()




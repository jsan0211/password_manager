def get_user_info():
    site_name = input("\nWhat is the URL you want to save a login for? :")
    user_name = input("\nUsername? :")
    password = input("\nPassword? :")
    login = {
        "url": site_name,
        "username": user_name,
        "password": password
    }
    creds = str(login)
    return creds


with open("logins.txt", "w") as file:
    file.write(creds)


while True:
    creds = get_user_info()
    with open("logins.txt", "a") as file:
        file.write(creds + "\n")
    add_login = input("Do you want to add another login (yes/no)? :")
    if add_login.lower() != "yes":
        break

    def main():
        while True:
            print()
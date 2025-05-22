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
creds = get_user_info()
with open("logins.txt", "w") as file:
    file.write(creds)
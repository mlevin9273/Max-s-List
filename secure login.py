def check_credentials():
    valid_username = "nicksaban"
    valid_password = "rolltide"

    # Get user input for username and password

    username = input("enter your username here")
    password = input("enter your password here")

    # Convert the entered username to lowercase for case-insensitive comparison


    # Check if the entered username and password match the valid credentials
    
    if (username == valid_username.lower()) and (password == valid_password):
        print("logging in")
    if (username != valid_username.lower()) or (password != valid_password):
        print("incorrect login credentials")


# Call the function to check credentials
check_credentials()
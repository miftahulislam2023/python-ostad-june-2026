system_info = (
    "8GB RAM",
    "128GB SSD",
    "i5 10th Gen"
)

user_info = (
    "miftah",
    "miftahcoding",
    "139.0.67.98",
    "abcd"
)

username = input("Enter useranme: ")

if username == user_info[0]:
    count_remaining = 5

    while count_remaining >= 1:
        password = input("Enter password: ")
        if password == user_info[3]:
            print("Login successful")
            break
        else:
            if count_remaining == 1:
                print("Maximum number of attempts reached. Try again later")
            else:
                print("Incorrect password. Please try again")
            count_remaining -= 1
else:
    print("Incorrect username")

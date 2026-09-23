def greet_user(name):
    return "Hello " + name


user_name = input("Enter your name: ")

result = greet_user(user_name)

print(result)
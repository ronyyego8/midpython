# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")


# greet("Ron", "Yego")
# greet("John", "Smith")

# Simplied version
# def greet(name):
#     print(f"Hi {name}")


# greet("Rony Yego")

# Types of function
# 1 - Perform a task
# 2 - Return a value


# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("Ron")

# Keyword Arguments
# Example 1
# def increment(number, by):
#     return number + by


# print(increment(2, by=1))


# Example 2
# def print_info(name, age):
#     print("Name :", name)
#     print("Age :", age)


# print_info(name="Ron", age=25)
# print_info(name="Alice", age=28)


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))


# ** is used to pass multiples keyword arguments and forms a dictionary
# def save_user(**user):
#     print(user)


# save_user(id=1, name="Ron", age=25)


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start")
# print(multiply(1, 2, 3))


def greet():
    name = input("Enter your name :  ")
    return f"Welcome aboard {name} !!"


message = greet()
print(message)

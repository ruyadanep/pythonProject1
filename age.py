user_name = input("Please Enter your user name: ")
birth_year = input("Please enter your birth year: ")
age = 2023 - int(birth_year)
if age > 36:
    print(f'Welcome {user_name}, Your are {age} years old!, you need to get married')
elif age < 30:
    print(f'Welcome {user_name}, Your are {age} years old!, you are still young')
else:
    print(f'Welcome {user_name}, You are {age} years old!')
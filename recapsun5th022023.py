name = input('Please Enter FullName: ')
birth_year = input('Enter Birth Year: ')
age = 2023 - int(birth_year)
if age > 35:
    print(f'Welcome {name}, you are {age} Years old!, Please you are ripe for marriage')
elif age < 25 and 20:
    print(f'Welcome {name}, you are {age} Years old!, You are still Young')
elif age > 25:
    print(f'Welcome {name}, you are {age} Years old!, Please get ready for marriage!')
elif age < 19:
    print(f'Welcome {name}, you are {age} Years old!, Please you are a teenager')
elif age > 20 and 10:
    print(f'Welcome {name}, you are {age} Years old!, Please you are still a baby')

else:
    print(f'Welcome {name}, you are {age} Years old!')
import random
def generate_password(name,color,year):
    symbols=['!','@','#','$','%','&','*']
    random_symbol= random.choice(symbols)
    random_number=random.randint(10,99)
    part1=name[:2].capitalize()
    part2=color[-2:].lower()
    part3=str(year)[-2:]
    password=f"{part1}{part2}{part3}{random_symbol}{random_number}"
    return generate_password
name=input("Enter your name:")
color=input("Enter your favorite color:")
year=input("Enter your birth year(e.g, 2000):")
password=generate_password(name,color,year)
print("Your custom password is:",password)
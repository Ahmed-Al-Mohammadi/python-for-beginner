import datetime
birthYear = int(input("Enter Your Birth Year "))
age = datetime.datetime.now().year - birthYear
print("Your Age Is" , age)
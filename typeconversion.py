#type conversion excercise
#this will output user age just by typing their birth year.
birth_year = input("What year you were born? ")
age = "your age is: "
this_year = 2026
present_year = int(this_year) - int(birth_year)
print(age, present_year)
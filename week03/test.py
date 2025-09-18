#ask the user for the grade
grade = float(input("what is the grade percent?"))

#figure out the letter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"


#get the last digit
last_digit = grade % 10

#determine the sign
if last_digit >= 7:
    sign = "+  "
elif last_digit < 3:
    sign = "-"  
else:
    sign = ""

#handle exceptions (A+, F+, F-)
if letter_grade == "A" and sign == "+":
    sign = ""

if grade > 93:
    sign = ""

if letter_grade == "F":
    sign = ""

#display the letter 
print(f"You have earned a letter grade of {letter_grade}{sign}")

if grade >= 70:
    print("Congratulations, you passed!")
else:
    print("Sorry, you did not pass.")
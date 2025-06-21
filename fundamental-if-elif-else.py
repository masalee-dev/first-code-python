str_input = input('Enter your grade: ')
grade = int(str_input)
print('User Input:', grade, type(grade))

if grade == 100:
    print("Awesome!")
elif grade >= 85:
    print('Good')
elif grade >= 60:
    print('Nice Try')
    if grade <= 70:
        print('Need improve it')
    else:
        print('OK grade')
else:
    print('Below the passing grade, try hard!')



# With logic operation

value = int(input('Enter your grade: '))
prev_value = int(input('Enter your previous grade: '))

if value >= 100 and prev_value >= 90 :
    print('Awesome')
if value >= 80 and prev_value < 60 :
    print('Nice Try!, you defintly try hard!')
elif value >= 60:
    print('Passed for the exam')
else:
    print('Below the passing grade')

if (value >= 60 and not prev_value >= 60) or (not value >= 60 and prev_grade >= 60):
    print('At least you passed exam, good job!')
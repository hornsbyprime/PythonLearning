weight = float(input('What is your weight in kg?'))
height = float(input('What is your height in meters?'))

BMI = round(weight / height ** 2)

if BMI <= 18.5:
    print(f'Youre BMI is {BMI} which means you are underweight')
elif BMI <= 25:
    print(f'Youur BMI is {BMI} which means you are normal weight')
elif BMI <= 30:
    print(f'Your BMI is {BMI} which means you are overweight')
elif BMI <= 35:
    print(f'Your BMI is {BMI} which means you are obese')
else:
    print(f'Your BMI is {BMI} which means you are clinically obese')


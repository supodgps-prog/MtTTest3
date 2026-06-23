# BMI Calculator

weight = float(input("Enter weight (kg): abcde 12456789 "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

print(f"\nBMI = {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
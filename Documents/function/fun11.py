from urllib.parse import uses_relative


def weight_height(bmi):
    if bmi<=18.5:
        return "Underweight"
    if bmi<=25.0:
        return "Noraml"
    if bmi<=30.0:
        return "Overweight"
    if bmi>30:
        return "Obese"
user=int(input("enter a number"))
print(weight_height(user))

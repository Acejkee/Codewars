def bmi(weight, height):
    res = weight / (height**2)
    if res <= 18.5:
        return 'Underweight'
    elif 18.5<res<=25.0:
        return 'Normal'
    elif 25.0<res<=30.0:
        return 'Overweight'
    else:
        return 'Obese'
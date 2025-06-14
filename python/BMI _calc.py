name = (input("enter your name "))
weight = int(input("enter your weight in pounds : "))

height = int(input("enter your height in inches : "))

BMI = (weight * 703 ) / (height * height )

print(BMI)


if BMI >0:
    if (BMI<18.5):
        print(name,", you r under weight ")
    elif (BMI<=24.5):
        print(name,", you r normal weight ")
       
    elif (BMI<=29.9):
        print(name,", you r over weight ")
        
    elif (BMI<=34.4):
        print(name,", you r obese. ")
        
    elif (BMI<= 39.9):
        print(name,",  r severly obese ")
        
    elif (BMI >=40 ):
        print(name," , seriorly morbidly obese ")
    else:
        print("please put valid detials ")







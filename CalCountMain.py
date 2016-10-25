# Program: Calorie Counter
# Programmer: Gordon Clark
# Date: Oct 10, 2016
# Purpose: To count calories based on the input of fats, carbohydrates, and proteins
cont ='y'
mealcals = 0
itemcount = 0

while cont.lower() == 'y':
    # Input
    item_name = input("Enter item name >")

    g_carbs = int(input("carbs >"))
    g_fats = int(input("fats >"))
    g_protein = int(input("protein >"))

    # Process
    cals = (g_carbs*4) + (g_fats*9) + (g_protein*4)

    # Output
    # print("Total calories for " + item_name + " are " + str(item_cals) )
    # ^ dont use this method, use the below method.
    print("Total calories for {} are {}.".format(item_name,cals) )
    mealcals = mealcals + cals
    itemcount = itemcount + 1
    print("Your meal has {} items totalling {} calories.".format(itemcount,mealcals))
    cont = input("Would you like to add another?")

print("Thank you for using this program.")
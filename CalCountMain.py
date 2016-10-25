# Program: Calorie Counter
# Programmer: Gordon Clark
# Date: Oct 10, 2016
# Purpose: To count calories based on the input of fats, carbohydrates, and proteins
cont ='y'
keep_item = ''
temp_cals = 0
mealcals = 0
itemcount = 0

while cont.lower() == 'y':
    #### Asks for Item nutrition facts and determines calories ####
    item_name = input("Enter item name >")
    g_carbs = int(input("carbs >"))
    g_fats = int(input("fats >"))
    g_protein = int(input("protein >"))
    cals = (g_carbs*4) + (g_fats*9) + (g_protein*4)
    ########
    
    ####Display item calories and verify it is to be added to the meal####
    print("Total calories for {} are {}.".format(item_name,cals) )
    print("Your meal will have {} items totalling {} calories.".format(itemcount,mealcals))
    keep_item = input("Do you want to add this item to your meal?(y/n)")
    if keep_item.lower() == 'y':
        mealcals = mealcals + cals
        itemcount = itemcount + 1
    cont = input("Would you like to add another?")

print("Your meal will have {} items totalling {} calories.".format(itemcount,mealcals))
print("Thank you for using this program.")
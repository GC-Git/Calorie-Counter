# Program: Calorie Counter
# Programmer: Gordon Clark
# Date: Oct 10, 2016
# Purpose: To count calories for a meal based on the input of fats, carbohydrates, and proteins.

#### VARIABLE DECLARATIONS ####
cont ='y'
keep_item = ''
cals = 0
mealcals = 0
itemcount = 0
#### END OF VARIABLE DECLARATIONS ####



#### MAIN LOOP ####
while cont.lower() == 'y':
    
    ## ITEM PROPERTY -INPUT- ##
    # Asks the user about the food they wish to enter.
    item_name = input("Enter item name >")
    g_carbs = int(input("carbs >"))
    g_fats = int(input("fats >"))
    g_protein = int(input("protein >"))
    ## END OF -INPUT- ##
    
    ## PROCESS & OUTPUT ##
    # Calculates calories based on number of fats, protein, and carbs, and how many cals in each.
    cals = (g_carbs*4) + (g_fats*9) + (g_protein*4)
    print("Total calories for {} are {}.".format(item_name,cals) )
    print("Your meal will have {} items totalling {} calories.".format(itemcount,(mealcals+cals)))
    ## END PROCESS & OUTPUT ##

    ## DATA VERIFICATION ##
    #Verifies the user wishes to input this data.
    keep_item = input("Do you want to add this item to your meal?(y/n)")
    if keep_item.lower() == 'y':
        mealcals = mealcals + cals
        itemcount = itemcount + 1
    ## END DATA VERIFICATION

    # LOOP CONTINUE REQUEST #
    cont = input("Would you like to add another?")

#### END OF MAIN LOOP ####


print("Your meal will have {} items totalling {} calories.".format(itemcount,mealcals))
print("Thank you for using this program.")
# Program: Calorie Counter
# Programmer: Gordon Clark
# Date: Oct 10, 2016
# Purpose: To count calories for a meal based on the input of fats, carbohydrates, and proteins.

#### VARIABLE DECLARATIONS ####
cont = 'y'
keep_item = ''
cals = 0
mealcals = 0
itemcount = 0
valid_data = False
#### END OF VARIABLE DECLARATIONS ####

#### MAIN LOOP ####
while cont.lower() == 'y':

    ## ITEM PROPERTY -INPUT- ##
    # Asks the user about the food they wish to enter.
    while not valid_data:
        item_name = input("Enter item name >")
        if len(item_name) > 20:
            print("We both know thats not a real food. Try again.")
        elif len(item_name) == 0:
            print("You entered nothing. Try again.")
        else:
            valid_data = True

    # Flag Reset
    valid_data = False

    while not valid_data:
        try:
            g_carbs = int(input("carbs >"))
            valid_data = True
        except Exception as detail:
            print("Error: ", detail)

    # Flag Reset
    valid_data = False

    while not valid_data:
        try:
            g_fats = int(input("fats >"))
            valid_data = True
        except Exception as detail:
            print("Error: ", detail)

    # Flag Reset
    valid_data = False

    while not valid_data:
        try:
            g_protein = int(input("carbs >"))
            valid_data = True
        except Exception as detail:
            print("Error: ", detail)
    ## END OF -INPUT- ##

    ## PROCESS & OUTPUT ##
    # Calculates calories based on number of fats, protein, and carbs, and how many cals in each.
    cals = (g_carbs * 4) + (g_fats * 9) + (g_protein * 4)
    print("Total calories for {} are {}.".format(item_name, cals))
    print("Your meal will have {} items totalling {} calories.".format(itemcount, (mealcals + cals)))
    ## END PROCESS & OUTPUT ##

    ## DATA VERIFICATION ##
    # Verifies the user wishes to input this data.
    keep_item = input("Do you want to add this item to your meal?(y/n)")
    if keep_item.lower() == 'y':
        mealcals += cals
        itemcount += 1
    ## END DATA VERIFICATION

    # LOOP CONTINUE REQUEST #
    cont = input("Would you like to add another?")
#### END OF MAIN LOOP ####


print("Your meal will have {} items totalling {} calories.".format(itemcount, mealcals))
print("Thank you for using this program.")

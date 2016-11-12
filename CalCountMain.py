# Program: Calorie Counter
# Programmer: Gordon Clark
# Date: Oct 10, 2016
# Purpose: To count calories for a meal based on the input of fats, carbohydrates, and proteins.

# VARIABLE DECLARATIONS #
cont = 'y'
keep_item = ''
mealcals = 0
itemcount = 0
valid_data = False


# FUNCTIONS #
def inp_item_name():  # Asks user for food name. Must be under 20 chars and more than 0
    while True:
        item_name = input("Enter item name >")
        if len(item_name) > 20:
            print("We both know that's not a real food. Try again.")
        elif len(item_name) == 0:
            print("You entered nothing. Try again.")
        return item_name


def nut_input():  # Returns carbs, fats and proteins as ints (in that order) after asking for user input
    while True:
        try:
            g_carbs = int(input("Carbs >"))
            break
        except Exception as detail:
            print("Error: ", detail)

    while True:
        try:
            g_fats = int(input("Fats >"))
            break
        except Exception as detail:
            print("Error: ", detail)

    while True:
        try:
            g_protein = int(input("Proteins >"))
            break
        except Exception as detail:
            print("Error: ", detail)

    return g_carbs, g_fats, g_protein


def cal_calc(gtype, quant):  # Takes f, c, or p string as gram type (fat, carbs, proteins) and returns calories
    if gtype == 'f':
        return quant * 9
    else:
        return quant * 4


# Main Loop
while cont.lower() == 'y':

    item = inp_item_name()  # Gets the item name from the user

    g_carbs, g_fats, g_protein = nut_input()  # Determines carbs, fats, and proteins in the item via user input

    item_cals = cal_calc('c', g_carbs) + cal_calc('f', g_fats) + cal_calc('p', g_protein)

    print("Total calories for {} are {}.".format(item, item_cals))
    print("Your meal will have {} items totalling {} calories.".format(itemcount+1, (mealcals + item_cals)))

    keep_item = input("Do you want to add this item to your meal?(y/n)")
    if keep_item.lower() == 'y':
        mealcals += item_cals
        itemcount += 1
        cont = input("Would you like to add another?")
    else:
        cont = input("The item has not been added to your meal. Would you like to add another item?")


print("Your meal will have {} items totalling {} calories.".format(itemcount, mealcals))
print("Thank you for using this program.")

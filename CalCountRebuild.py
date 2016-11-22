import os  # Used in cls() for clearing the screen

#***
# This is the options available to the user. Add menu functions here for input then edit main loop to add functionality
#***
disp_dict = {
    "a": "[a]dd",
    "d": "[d]elete",
    "q": "[q]uit"
}


#*****
#
#   Functions
#
def disp_menu():
    # Displays disp_dict menu options, then asks for input. Validates against dictionary and returns input.
    print("Menu:")
    for key in disp_dict:  # Prints the menu
        print(disp_dict[key],end="\n")

    print("")
    while True:
        menu_choice = input(">")
        if menu_choice in disp_dict:
            break
    return menu_choice


def cls():  # Clears the console
    os.system('cls' if os.name=='nt' else 'clear')


def add_process(calories, names, count):

    def input_grams():  # Asks for fats carbs and proteins then returns calories
        while True:
            try:
                cls()
                g_carbs = int(input("Carbs>"))
                break
            except Exception as detail:
                print("Error: ", detail)
                input("Press enter to try again...")

        while True:
            try:
                cls()
                g_fats = int(input("Fats>"))
                break
            except Exception as detail:
                print("Error: ", detail)
                input("Press enter to try again...")

        while True:
            try:
                cls()
                g_protein = int(input("Proteins>"))
                break
            except Exception as detail:
                print("Error: ", detail)
                input("Press enter to try again...")

        return (g_carbs*4 + g_fats*9 + g_protein*4)


    def add_item(calories, names, count):
        if temp_count > 0:
            include = ''
            while include != 'y' and include != 'n':
                cls()
                include = input("Add {} {}(s) worth {} kCal to your meal?(y/n)".format(temp_count, temp_name, temp_cals * temp_count))
                if include == 'y':
                    calories.append(temp_cals)
                    names.append(temp_name)
                    count.append(temp_count)
                    return calories, names, count
                elif include == 'n':
                    return calories, names, count  # Returns without changing anything


    def inp_item_name():  # Asks user for food name. Must be under 20 chars and more than 0
        while True:
            item_name = input("Enter item name >")
            if len(item_name) > 20:
                print("")
            elif len(item_name) == 0:
                print("")
            return item_name


    def request_count():
        newcount = -1  # starting value to initiate loop
        while 0 >= newcount:
            try:
                cls()
                newcount = int(input("How many {} would you like?(0 = None)>".format(temp_name)))
                return newcount
            except Exception:
                input("Try a real number. Press enter to continue...")

    #===
    # Main Function Process
    #===
    cls()  # Clear screen
    temp_name = inp_item_name()

    cls()  # Clear screen
    temp_cals = input_grams()

    cls()
    temp_count = request_count()

    add_item(calories, names, count)

    return calories, names, count


def disp_cart(calories, names, count):
    if len(count) > 0:
        print("{:=^30}{}{:=^30}".format("", "CURRENT MEAL", ""))
        print("{:15}{:15}{:15}{:15}".format("Name", "Cal/Item", "Count", "Cals Total"))
        print("{:-^60}".format(""))
        totalcals = 0
        for index in range(0, len(calories)):
            print(str(index+1),end=".")
            print("{:.<13}{:.<15}{:.<15}{:.<15}".format(names[index], calories[index], count[index], count[index]*calories[index]))
            totalcals += (count[index]*calories[index])
        print("")
        print("{:.<15}{:.<15}{:.<15}{:.<15}".format("Totals:", "", sum(count), totalcals))


def del_item(calories, names, count):
    item_for_removal = -2  # -2 = Value intialization, -1 = Cancel
    while item_for_removal not in range(-1, len(calories)):
        try:
            item_for_removal = (int(input("What number is the item you would like to remove?(0 = Cancel)>")) - 1)
            if item_for_removal == -1:
                return calories, names, count
            elif item_for_removal in range(-1, len(calories)):
                del calories[item_for_removal]
                del names[item_for_removal]
                del count[item_for_removal]
                return calories, names, count
            else:
                return calories, names, count
        except ValueError:
            input("That is not a number. Press any key to try again.")


#**********
#
#   Main Program
#
#**********
item_names = []
item_cals = []
item_cnt = []

while True:
    cls()
    print(r"""
      _____      _    _____                  _
     / ____|    | |  / ____|                | |
    | |     __ _| | | |     ___  _   _ _ __ | |_ ___ _ __
    | |    / _` | | | |    / _ \| | | | '_ \| __/ _ \ '__|
    | |___| (_| | | | |___| (_) | |_| | | | | ||  __/ |
     \_____\__,_|_|  \_____\___/ \__,_|_| |_|\__\___|_|
                   Program by: Gordon Clark
    """)
    disp_cart(item_cals,item_names,item_cnt)
    print("\n")
    choice = disp_menu()
    if choice == "a":
        item_cals, item_names, item_cnt = add_process(item_cals, item_names, item_cnt)
    elif choice == "d":
        item_cals, item_names, item_cnt = del_item(item_cals,item_names,item_cnt)
    elif choice == "q":
        break


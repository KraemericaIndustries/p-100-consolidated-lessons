from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

go_again = True

while go_again:

    # 1 COMPLETE! Gather user choice...
    choice = input(f"What could you like? ({menu.get_items()}): ").lower()

    # 2 COMPLETE! Exit code by entering 'off' at the drink selection prompt...
    # 3 COMPLETE! When the user enters “report” to the prompt, a report should be generated that shows the current resource values
    if choice == "off": break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        # 4 COMPLETE!  When the user chooses a drink, check if there are enough resources to make that drink
        # Input: menu{} MenuItem
        # Output: boolean
        right_stuff = coffee_maker.is_resource_sufficient(drink)

        # 5 COMPLETE!  If there are sufficient resources to make the drink selected, prompt the user to insert coins
        if right_stuff:

            # 6 COMPLETE! Check that the user has inserted enough money to purchase the drink they selected
            enough_money_inserted = money_machine.make_payment(drink.cost)
            if enough_money_inserted:
                coffee_maker.make_coffee(drink)

print("END: go_again while loop")
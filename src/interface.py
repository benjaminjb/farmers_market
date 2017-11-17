import sys
from basket import Basket
from interface_helper_functions import *

commands = '''
    "add ____" to add an item to your basket,
    "sum" to see the current state of your basket,
    "clear" to start a new basket, or
    "checkout" to quit.'''

def run_commands(user_input, customer_basket):
    if user_input is None or len(user_input) < 1:
        error_message()
        return

    whole_command = user_input.lower().split()
    action = whole_command[0]

    if action not in ("add", "sum", "clear"):
        error_message()
        return
    if action == "clear":
        customer_basket = Basket()
    elif action == "add":
        if len(whole_command) != 2:
            error_message()
            return
        add_to_checkout_basket(customer_basket, whole_command[1])
    # TODO: Discuss whether we want the basket to be printed on every action.
    # Currently, the behavior is to print it out on every action, so the "sum" action
    # doesn't need to do anything.
    elif action == "sum":
        pass
    print_basket(customer_basket)
    return customer_basket

def error_message():
    print("\nPlease enter a recognized command:{}".format(commands))


if __name__ == "__main__":
    input_operator = input if sys.version_info.major == 3 else raw_input
    print("\nPlease enter one of the following commands:{}".format(commands))
    customer_basket = Basket()
    while True:
        user_input = input_operator("\nEnter command: ")
        if user_input == "checkout":
            break
        customer_basket = run_commands(user_input, customer_basket)

# Note: if we wanted the checkout system to allow for interruptions, we could alternatively
# run_commands(sys.argv[1:]) to get commands directly from the command line,
# but then we would have to save the basket in some location.

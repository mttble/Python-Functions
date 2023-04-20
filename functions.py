def hello(name, age='unknown'):
    print(f'Hello {name}, you are {age} years old!')

# # main
# print('Start Main')
# hello(input('What is your name? '), age=28)
# print('End Main')


def get_answer(number):
    match number:
        case 1:
            print('It is certain')
        case 2:
            print('It is Decidely so')
        case 3:
            print('Yes')
        case 4:
            print('No')
        case 5:
            print('try again')
        case 6:
            print('Very doubful')
        case _:
            print('Not sure')


# import random

# get_answer(random.randint(1,6))


# Add GST to an amount and return the result
def add_gst(amount):
    # set local variable of GST
    gst_rate = 0.1
    # calculate amount + GST
    amount= amount + (amount * gst_rate)
    # return from function with a value
    return amount

# read subtotal from user and convert to float
subtotal = float(input('Subtotal: $'))
# call add_gst, passing the entered subtotal as an argument
# Store the returned result in a new variable
total = add_gst(subtotal)
print(f'Total: ${total:.2f}')

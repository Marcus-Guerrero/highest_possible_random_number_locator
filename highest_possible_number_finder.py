#create a unique function for the if statements that would be used for locating the highest possible number out of five random values
def esteemed_highest_number():
    if random_1 >= random_2 and random_1 >= random_3 and random_1 >= random_4 and random_1 >= random_5:
        print (f"the largest value given five random numbers is {random_1}")
    elif random_2 >= random_1 and random_2 >= random_3 and random_2 >= random_4 and random_2 >= random_5:
        print (f"the largest value given five random numbers is {random_2}")
    elif random_3 >= random_1 and random_3 >= random_2 and random_3 >= random_4 and random_3 >= random_5:
        print (f"the largest value given five random numbers is {random_3}")
    elif random_4 >= random_1 and random_4 >= random_2 and random_4 >= random_3 and random_4 >= random_5:
        print (f"the largest value given five random numbers is {random_4}")
    else:
        print (f"the largest value given five random numbers is {random_5}")
#make five input lines that will ask users to input any random number
#state the unique function name to process the command in the terminal
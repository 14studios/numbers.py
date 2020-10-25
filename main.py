from random import uniform, randint
from time import sleep
from termcolor import colored

opts = ["1", "2", "3", "4"]


def Counter():
    inp = randint(1600000, 18000000)
    randomNum = randint(165432, 5872357)
    print("Number:", f"{inp};", "Beginning in 5 seconds..")
    sleep(5)

    for i in range(inp):
        if i == inp - 1:
            print("Oops. We couldn't brute-force the integer. Try again?")
            exit()
        calc = randint(165432, 5872357)
        print("Brute-forcing integer..", "Tries: (", i, "/", inp, "); Integer brute-forced:", calc)
        if calc == randomNum:
            print("The integer has been brute-forced successfully.")
            exit()


def init():
    options_typeOfOperation = input(
        "What do you want to do? (Enter 'h' to find 'man-like' pages for each function.)\n\nOptions:\n1. Random Integer Generator\n2. Random Number Generator\n3. Random number 'brute-force' (WARNING: RESOURCE-INTENSIVE!)\n4. Multi-digit number combinations\n\nPick a choice: ").strip()
    if options_typeOfOperation == "h":
        print(colored("*SHORT 'MAN-PAGE' FOR THIS SCRIPT*", "green", attrs=['reverse', 'blink']))
        print(colored("\n(1) Random Integer Generator", "red"))
        print(
            "It's self explanatory. Basically, this function generates a random integer number for you to use. It utilises the Mersenne Twister.")
        print(colored("\n(2) Random Number Generator", "blue"))
        print(
            "Just like (1), this is a random number generator. Instead of generating integers, though, it generates a non-zero and/or non-negative number. It also utilises the Mersenne Twister.")
        print(colored("\n(3) Random number 'brute-force'", "magenta"))
        print(
            "Number three generates a random integer, and then proceeds to generate random integers until it generates an integer that matches the integer that it initially generated.\n*THIS IS AN INTENSIVE PROGRAMME, AND PERFORMANCE DEPENDS ON CPU SPEED!*")
        print(colored("\n(4) Multi-digit combinations", "yellow"))
        print(
            "This function takes a number with multiple digits. Then, it uses the provided digits and displays all possible combinations for integers using all the digits provided.")
        exit()
    if options_typeOfOperation not in opts:
        print(
            "Sorry, I didn't understand. You either typed in the wrong number, or didn't input a number. Rerun the script and try again."
        )
        exit()
    options_typeOfOperation = int(options_typeOfOperation)
    if options_typeOfOperation == 1:
        print("Awaiting your random integer..")
        sleep(0.25)
        print("Got your random integer! Your random integer is", "{:,}.".format(randint(0, 121489673)))
    elif options_typeOfOperation == 2:
        print("Awaiting your random number..")
        sleep(0.25)
        print("Got your random number! Your random number is", "{:,}.".format(uniform(0.251249, 121489673.496578)))
    elif options_typeOfOperation == 3:
        Counter()
    elif options_typeOfOperation == 4:
        print("This does not work, and will be implemented in a later update.")
        exit(1)
        options_4Num = input("What digits do you want to find all integer combinations of? ")
        if not options_4Num.isnumeric():
            print(
                "Sorry, I didn't understand. You didn't input a number. Rerun the script and try again."
            )
            exit()
        options_4Digs = [int(i) for i in options_4Num]
        print(options_4Digs)
        print(f"The number possible combinations using only integers from the number '{options_4Num}' is {len(options_4Digs) ** len(options_4Num)}")


init()

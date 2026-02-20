def sum_list(numbers, count):
    total = 0
    for i in range(count):
        total += numbers[i]
    return total


def get_number():
    while True:
        number = input("Enter a number: ") # Takes user input
        try:
            number = int(number) # Converts input to int
            return number
        except ValueError: # If cant be change to int
            print("Please input a number (integer)")




def main():
    numbers = []
    while True:
        print("Enter a non-negative number to add to the list.")
        print("Or enter a negative number to stop.")
        number = get_number()
        if number >= 0:
            numbers.append(number)
        else:
            break

    while True:
        print("Enter many numbers from the list would you like to sum up.")
        print("Or enter a negative number to stop.")
        count = get_number()
        if count < 0:
            break
        
        try:
            total = sum_list(numbers, count)
            print(f"The sum of the first {count} numbers is {total}")
        except IndexError:
            print("Enter a number that isnt bigger than number of items in the list")


main()
# Kory Anderson validation file for the Future Value App
def get_float(prompt, low, high):
    while True:
        number = float(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print(f"Entry must be greater than {low} and less than {high}")

def get_int(prompt, low, high):
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print(f"Entry must be greater than {low} and less than {high}")

def main():
    choice = "y"
    while choice.lower() == "y":
        valid_number = get_float("Enter number:", 0, 1000)
        print(f"Valid Number = {valid_number}")
        valid_int = get_int("Enter integer: ", 0, 50)
        print(f"Valid Integer = {valid_int}")
        print()
        choice = input("Repeat? (y/n): ")
    print("Bye!")
if __name__ == "__main__":
    main()
#!/usr/bin/env python3
        
def get_float(prompt, low, high):
    is_valid = True
    while is_valid == True:
        number = float(prompt)
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print(f"Entry must be greater than {low} \n and less than or equal to {high}\n Please try again.")
            
def get_integer(prompt, low, high):
    is_valid = True
    while is_valid == True:
        number = int(prompt)
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print(f"Entry must be greater than {low} \n and less than or equal to {high}\n Please try again.")
            
def calculate_future_value(monthly_investment, yearly_interest_rate, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 100 / 12
    months = years * 12

    # calculate future value
    future_value = 0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_float(input("Enter monthly investment:\t\t"), 0, 1000)
        yearly_interest_rate = get_float(input("Enter yearly interest rate in %:\t"), 0, 100)
        years = get_integer(input("Enter number of years:\t\t\t"), 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print(f"Future value:\t\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()

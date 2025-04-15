def divide(numerator, denominator):
    quotient = numerator / denominator
    return quotient

def main():
    numerator = int(input("Num"))
    denominator = int(input("Denom"))
    quotient = divide(numerator, denominator)
    print(f"Quotient is {quotient}")

if __name__ == "__main__":
    main()
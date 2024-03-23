# Task 12

# - Pass two command line arguments (numbers) and add them together.

# - Run tests in your repo automatically using GitHub Actions.

# References:
# argparse
import argparse

def calcs():
    parser = argparse.ArgumentParser(prog="Calculator,",description='Calculate the sum and product of numbers',epilog='Enjoy the program! :)')
    parser.add_argument('nums', type=float, help='The numbers to be added or multiplied ', nargs='+')
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-s","--sum", help="Sum of two numbers",action='store_true')
    group.add_argument("-p","--product", help="Product of two numbers",action='store_true')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = calcs()
    if args.sum or not (args.sum or args.product):
        print(sum(args.nums))
    elif args.product:
        product = 1
        for num in args.nums:
            product *= num
        print(product)
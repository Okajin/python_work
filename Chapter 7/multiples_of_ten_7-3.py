number = input("Please enter a number and I'll tell you if it's a multiple of ten: ")
number = int(number)

if number % 10 == 0:
    print(f"\n The number {number} is a multiple of ten.")
else:
    print(f"\n The number {number} isn't a multiple of ten.")

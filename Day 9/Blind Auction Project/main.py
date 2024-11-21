import art

print(art.logo)
print("Welcome to the secret auction program.")

# 1: Ask the user for input
auction = {}
should_continue = True

while should_continue:

    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    # 2: Save data into dictionary {name: price}
    auction[name] = price

    # 3: Whether if new bids need to be added
    restart = input("Are there any other bidders?  Type 'yes' or 'no'.").lower
    if restart == "yes":
        print("\n" * 20)
    else:
        print("\n" * 20)
        should_continue = False

# 4: Compare bids in dictionary
max_bid = 0
winner = ""

for key in auction:
    if auction[key] > max_bid:
        winner = key
        max_bid = auction[key]
print(f"The winner is {winner} with a bid of ${max_bid}")

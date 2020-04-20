responses = {}

# Set flag to indicate that polling is active.
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Who do you vote for the 2020 election? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to vote for {response}.")

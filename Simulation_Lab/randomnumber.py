seed_number = int(input("Please enter a four-digit number:\n "))
number = seed_number
seen_value = set()
counter = 0

while number not in seen_value:
    counter += 1
    seen_value.add(number)
    number = int(str(number * number).zfill(8)[2:6])  # adds zeros (0) at the beginning of the string, until it reaches the specified length.
    print(f"#{counter}: {number}")

print(f"We began with {seed_number} and"
      f" have repeated ourselves after {counter} steps"
      f" with {number}.")
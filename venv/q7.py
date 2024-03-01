import random

# Step 1: Generate a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Display the original list
print("Original List:", random_numbers)

# Step 2: Replace numbers greater than 50 with their corresponding negative value and replace the other numbers wth "XX"
i = 0
while i < len(random_numbers):
    if random_numbers[i] > 50:
        del random_numbers[i]
    else:
        random_numbers[i] = "XX"
        i += 1

# Display the modified list
print("New List:", random_numbers)
# Question 1. Write a Python for loop that prints the numbers from 1 to 10.
# Answer 1.

Numbers=[1,2,3,4,5,6,7,8,9,10]

for x in Numbers:
    print(x)




# Question 2. Create a list of fruits (e.g., ["apple", "banana", "cherry"]) and write a for loop to print each fruit in the list.

# Answer 2.


fruits=["apple", "banana", "cherry"]

for z in fruits:
    print(z)




# Question 3. Write a Python program that calculates the sum of all even numbers from 1 to 50 using a for loop.

#Answer 3.

sum = 0

for digit in range(1, 51):
    # Check if the digit is even
    if digit % 2 == 0:
        sum += digit

# Print the sum
print("Sum of even digits from 1 to 50 :", sum)



# Question 4. Create a list of integers, and using a for loop, find and print the largest number in the list.

numbers = [19, 41, 18, 201, 117, 492, 99, 71]

largest = numbers[0]

for p in numbers:

    if p > largest:
        largest = p

# Print the largest number
print("Largest number in list :", largest)

# Question 5. Write a Python program that uses a for loop to find and print all the prime numbers between 1 and 100. A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself.

# Answer 5.


# numbers from 2 to 100
for digit in range(2, 101):
    is_prime = True  # Assume the number is prime

# Check for factors
    for divisor in range(2, digit):
        if digit % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(digit, end=" ")

# Print a newline
print()



# Question 6. Write a Python program that takes a list of dictionaries,
# where each dictionary represents a person with keys "name" and "age." Find and print the average age of all the people in the list.

# Answer 6.

# Creating list of dictionaries of people
people_list = [
    {"name": "Manish", "age": 35},
    {"name": "Rman", "age": 28},
    {"name": "Shiva", "age": 42},
    {"name": "Mohan", "age": 18},
    {"name": "Raj", "age": 31}
]
# Calculate the total age and counting of people
total_age = 0
total_people = len(people_list)

# Calculate the total age
for person in people_list:
    total_age += person["age"]

# Calculate the average age
average_age = total_age / total_people

# Print the average age
print("Average age of the people:", average_age)



# Question 7. Create a dictionary representing a simple inventory system for a store.
# Implement a function that allows you to update the quantity of items in the inventory by specifying the item name and the new quantity.

# Answer 7.
# Old inventory dictionary
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grapes": 15
}

# Print the Old inventory
print("Initial Inventory:", inventory)

# Update the quantity of items in the dictionary
item = input("Enter item to update inventory: ")
if item in inventory:
    updated_quantity = int(input("Enter the updated quantity of inventory: "))
    inventory[item] = updated_quantity
    print(f"Inventory updated: {item} quantity set to {updated_quantity}")
else:
    print(f"{item} not found in the inventory.")

# Print the updated inventory
print("Updated Inventory:", inventory)



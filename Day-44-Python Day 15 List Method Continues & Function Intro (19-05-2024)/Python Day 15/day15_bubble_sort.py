# Define an array of numbers
numbers = [67, 44, 82, 17, 20]

# Get the total number of elements in the array
total_numbers = len(numbers)

# Print the array before sorting
print("Array before Sorting:")
print(numbers)

# Iterate through each number in the array to sort them
for i in range(total_numbers):
    # Keep track of whether any swaps occurred in this pass
    did_swap = False

    # Go through each pair of adjacent numbers in the array
    for j in range(0, total_numbers - i - 1):
        # Check if the current number is greater than the next number
        if numbers[j] > numbers[j + 1]:
            # If so, swap the positions of the numbers
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            did_swap = True  # Mark that a swap occurred

    # If no swaps occurred in this pass, the array is sorted
    if not did_swap:
        break

# Print the array after sorting
print("Array after Sorting:")
print(numbers)
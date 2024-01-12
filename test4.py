# test number 7
def recursive_search(numbers, target, index=0):
    if index >= len(numbers):
        return -1
    
    if numbers[index] == target:
        return index
    
    return recursive_search(numbers, target, index + 1)

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target_number = int(input("Enter a number to search for: "))

result = recursive_search(numbers_list, target_number)

if result != -1:
    print(f"Number {target_number} found at index {result}.")
else:
    print(f"Number {target_number} not found in the list.")

def sort_list(numbers):
    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers

user_input = input("Введите числа через запятую: ")
numbers = list(map(int, user_input.split(', ')))

even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Четные числа: {even_numbers}")
print(f"Максимальное число: {max(numbers)}")
print(f"Минимальное число: {min(numbers)}")
sorted_numbers = sort_list(numbers.copy())
print(f"Отсортированный список: {sorted_numbers}")
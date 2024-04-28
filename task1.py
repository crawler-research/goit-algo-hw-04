import timeit
import random

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def test_sorting_algorithm(algorithm, data):
    start_time = timeit.default_timer()
    algorithm(data)
    end_time = timeit.default_timer()
    return end_time - start_time

if __name__ == "__main__":
    data_lengths = [1000, 10000]

    for length in data_lengths:
        data = [random.randint(0, 1000) for _ in range(length)]

        # Тестуємо час виконання для сортування вставками
        insertion_sort_time = test_sorting_algorithm(insertion_sort, data.copy())

        # Тестуємо час виконання для сортування злиттям
        merge_sort_time = test_sorting_algorithm(merge_sort, data.copy())

        # Тестуємо час виконання для вбудованого Timsort
        timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)

        print()

        print(f"Довжина списку: {length}")
        print(f"Час сортування вставками: {insertion_sort_time}")
        print(f"Час сортування злиттям: {merge_sort_time}")
        print(f"Час вбудованого Timsort: {timsort_time}")
        print()
        print()
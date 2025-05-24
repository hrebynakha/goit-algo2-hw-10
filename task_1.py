"""
Порівняння рандомізованого та детермінованого QuickSort

Реалізуйте рандомізований та детермінований
алгоритми сортування QuickSort.
Проведіть порівняльний аналіз їхньої ефективності,
 вимірявши середній час виконання на масивах різного розміру.



Технічні умови

1. Для реалізації рандомізованого алгоритму QuickSort
 реалізуйте функцію randomized_quick_sort(arr),
 де опорний елемент (pivot) обирається випадковим чином.

2. Для реалізації детермінованого алгоритму QuickSort
 реалізуйте функцію deterministic_quick_sort(arr),
 де опорний елемент обирається за фіксованим правилом:
 перший, останній або середній елемент.

3. Створіть набір тестових масивів різного розміру:
10_000, 50_000, 100_000 та 500_000 елементів.
 Заповніть масиви випадковими цілими числами.

4. Виміряйте час виконання обох алгоритмів на кожному масиві.
 Для більш точної оцінки повторіть сортування кожного масиву
  5 разів та обчисліть середній час виконання.
"""

import random
from timeit import timeit
import matplotlib.pyplot as plt


def randomized_quick_sort(arr: list) -> list:
    """Randomized QuickSort"""

    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr: list) -> list:
    """Deterministic QuickSort"""

    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def create_test_arr(size):
    """Create test array."""
    return [random.randint(0, 1000000) for _ in range(size)]


def run_test(
    size: int,
    count: int = 5,
) -> tuple[float, float]:
    """Run test function."""
    arr = create_test_arr(size)
    randomized = timeit(lambda: randomized_quick_sort(arr), number=count)
    deterministic = timeit(lambda: deterministic_quick_sort(arr), number=count)
    return randomized / count, deterministic / count


def show_time_graph(results: list[tuple[int, float, float]]) -> None:
    """Function to show time graph results."""
    numbers, randomized, deterministic = zip(*results)
    plt.plot(numbers, randomized, label="Рандомізований QuickSort")
    plt.plot(numbers, deterministic, label="Детермінований QuickSort")
    plt.legend()
    plt.tight_layout()
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.show()


def main() -> None:
    """Main function"""
    sizes = [10000, 50000, 100000, 200000]
    results = []
    for size in sizes:
        print(f"Розмір масиву: {size}")
        deterministic, randomized = run_test(size)
        print(f"\tРандомізований QuickSort: {randomized:.4f} секунд")
        print(f"\tДетермінований QuickSort: {deterministic:.4f} секунд")
        results.append((size, randomized, deterministic))
    show_time_graph(results)


if __name__ == "__main__":
    main()

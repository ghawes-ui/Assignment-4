"""
Sorting Assignment Starter Code
Implement five sorting algorithms and benchmark their performance.
"""

import json
import time
import random
import tracemalloc


# ============================================================================
# PART 1: SORTING IMPLEMENTATIONS
# ============================================================================

def bubble_sort(arr):
    """
    Sort array using bubble sort algorithm.
    
    Bubble sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they're in the wrong order.
    
    Args:
        arr (list): List of integers to sort
    
    Returns:
        list: Sorted list in ascending order
    
    Example:
        bubble_sort([64, 34, 25, 12, 22, 11, 90]) returns [11, 12, 22, 25, 34, 64, 90]
    """
    # TODO: Implement bubble sort
    # Hint: Use nested loops - outer loop for passes, inner loop for comparisons
    # Hint: Compare adjacent elements and swap if left > right
    
    numbers = arr.copy()
    n = len(numbers)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


def selection_sort(arr):
    """
    Sort array using selection sort algorithm.
    
    Selection sort divides the list into sorted and unsorted regions, repeatedly
    selecting the minimum element from unsorted region and moving it to sorted region.
    
    Args:
        arr (list): List of integers to sort
    
    Returns:
        list: Sorted list in ascending order
    
    Example:
        selection_sort([64, 34, 25, 12, 22, 11, 90]) returns [11, 12, 22, 25, 34, 64, 90]
    """
    # TODO: Implement selection sort
    # Hint: Find minimum element in unsorted portion, swap it with first unsorted element
    
    numbers = arr.copy()
    n = len(numbers)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


def insertion_sort(arr):
    """
    Sort array using insertion sort algorithm.
    
    Insertion sort builds the final sorted array one item at a time, inserting
    each element into its proper position in the already-sorted portion.
    
    Args:
        arr (list): List of integers to sort
    
    Returns:
        list: Sorted list in ascending order
    
    Example:
        insertion_sort([64, 34, 25, 12, 22, 11, 90]) returns [11, 12, 22, 25, 34, 64, 90]
    """
    # TODO: Implement insertion sort
    # Hint: Start from second element, insert it into correct position in sorted portion
    
    numbers = arr.copy()
    n = len(numbers)

    for i in range(1, n):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key

    return numbers


def merge_sort(arr):
    """
    Sort array using merge sort algorithm.
    
    Merge sort is a divide-and-conquer algorithm that divides the array into halves,
    recursively sorts them, and then merges the sorted halves.
    
    Args:
        arr (list): List of integers to sort
    
    Returns:
        list: Sorted list in ascending order
    
    Example:
        merge_sort([64, 34, 25, 12, 22, 11, 90]) returns [11, 12, 22, 25, 34, 64, 90]
    """
    # TODO: Implement merge sort
    # Hint: Base case - if array has 1 or 0 elements, it's already sorted
    # Hint: Recursive case - split array in half, sort each half, merge sorted halves
    # Hint: You'll need a helper function to merge two sorted arrays
    
    numbers = arr.copy()

    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2

    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ============================================================================
# PART 2: STABILITY DEMONSTRATION
# ============================================================================

def demonstrate_stability():
    """
    Demonstrate sorting stability using products with duplicate prices.
    """

    products = [
        {"name": "Widget A", "price": 1999, "original_position": 0},
        {"name": "Gadget B", "price": 999, "original_position": 1},
        {"name": "Widget C", "price": 1999, "original_position": 2},
        {"name": "Tool D", "price": 999, "original_position": 3},
        {"name": "Widget E", "price": 1999, "original_position": 4},
    ]

    def bubble_products(arr):
        items = arr.copy()

        for i in range(len(items)):
            for j in range(len(items) - i - 1):
                if items[j]["price"] > items[j + 1]["price"]:
                    items[j], items[j + 1] = items[j + 1], items[j]

        return items

    def selection_products(arr):
        items = arr.copy()

        for i in range(len(items)):
            min_index = i

            for j in range(i + 1, len(items)):
                if items[j]["price"] < items[min_index]["price"]:
                    min_index = j

            items[i], items[min_index] = items[min_index], items[i]

        return items

    def insertion_products(arr):
        items = arr.copy()

        for i in range(1, len(items)):
            key = items[i]
            j = i - 1

            while j >= 0 and items[j]["price"] > key["price"]:
                items[j + 1] = items[j]
                j -= 1

            items[j + 1] = key

        return items

    def merge_products(arr):
        if len(arr) <= 1:
            return arr.copy()

        mid = len(arr) // 2

        left = merge_products(arr[:mid])
        right = merge_products(arr[mid:])

        merged = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i]["price"] <= right[j]["price"]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    algorithms = {
        "bubble_sort": bubble_products,
        "selection_sort": selection_products,
        "insertion_sort": insertion_products,
        "merge_sort": merge_products
    }

    results = {}

    for name, algorithm in algorithms.items():
        sorted_products = algorithm(products)

        stable = True
        last_position = {}

        for product in sorted_products:
            price = product["price"]
            position = product["original_position"]

            if price in last_position:
                if position < last_position[price]:
                    stable = False

            last_position[price] = position

        results[name] = "Stable" if stable else "Unstable"

        print(f"\n{name}: {results[name]}")
        print([p["name"] for p in sorted_products])

    return results


# ============================================================================
# PART 3: PERFORMANCE BENCHMARKING
# ============================================================================

def load_dataset(filename):
    """Load a dataset from JSON file."""
    with open(f"datasets/{filename}", "r") as f:
        return json.load(f)


def load_test_cases():
    """Load test cases for validation."""
    with open("datasets/test_cases.json", "r") as f:
        return json.load(f)


def test_sorting_correctness():
    """Test that sorting functions work correctly on small test cases."""
    print("="*70)
    print("TESTING SORTING CORRECTNESS")
    print("="*70 + "\n")
    
    test_cases = load_test_cases()
    
    test_names = ["small_random", "small_sorted", "small_reverse", "small_duplicates"]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }
    
    for test_name in test_names:
        print(f"Test: {test_name}")
        print(f"  Input:    {test_cases[test_name]}")
        print(f"  Expected: {test_cases['expected_sorted'][test_name]}")
        print()
        
        for algo_name, algo_func in algorithms.items():
            try:
                result = algo_func(test_cases[test_name].copy())
                expected = test_cases['expected_sorted'][test_name]
                status = "✓ PASS" if result == expected else "✗ FAIL"
                print(f"    {algo_name:20s}: {result} {status}")
            except Exception as e:
                print(f"    {algo_name:20s}: ERROR - {str(e)}")
        
        print()


def benchmark_algorithm(sort_func, data):
    """
    Benchmark a sorting algorithm on given data.
    
    Args:
        sort_func: The sorting function to test
        data: The dataset to sort (will be copied so original isn't modified)
    
    Returns:
        tuple: (execution_time_ms, peak_memory_kb)
    """
    # Copy data so we don't modify original
    data_copy = data.copy()
    
    # Start memory tracking
    tracemalloc.start()
    
    # Measure execution time
    start_time = time.perf_counter()
    sort_func(data_copy)
    end_time = time.perf_counter()
    
    # Get peak memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_ms = (end_time - start_time) * 1000
    peak_memory_kb = peak / 1024
    
    return execution_time_ms, peak_memory_kb


def benchmark_all_datasets():
    """Benchmark all sorting algorithms on all datasets."""
    print("\n" + "="*70)
    print("BENCHMARKING SORTING ALGORITHMS")
    print("="*70 + "\n")
    
    datasets = {
        "orders.json": ("Order Processing Queue", 50000, 5000),
        "products.json": ("Product Catalog", 100000, 5000),
        "inventory.json": ("Inventory Reconciliation", 25000, 5000),
        "activity_log.json": ("Customer Activity Log", 75000, 5000)
    }
    
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }
    
    for filename, (description, full_size, sample_size) in datasets.items():
        print(f"Dataset: {description} ({sample_size:,} element sample)")
        print("-" * 70)
        
        data = load_dataset(filename)
        # Use first sample_size elements for fair comparison
        data_sample = data[:sample_size]
        
        for algo_name, algo_func in algorithms.items():
            try:
                exec_time, memory = benchmark_algorithm(algo_func, data_sample)
                print(f"  {algo_name:20s}: {exec_time:8.2f} ms | {memory:8.2f} KB")
            except Exception as e:
                print(f"  {algo_name:20s}: ERROR - {str(e)}")
        
        print()


def analyze_stability():
    """Test and display which algorithms are stable."""
    print("="*70)
    print("STABILITY ANALYSIS")
    print("="*70 + "\n")
    
    print("Testing which algorithms preserve order of equal elements...\n")
    
    results = demonstrate_stability()
    
    for algo_name, stability in results.items():
        print(f"  {algo_name:20s}: {stability}")
    
    print()


if __name__ == "__main__":
    print("SORTING ASSIGNMENT - STARTER CODE")
    print("Implement the sorting functions above, then run tests.\n")
    
    
    
    test_sorting_correctness()
    benchmark_all_datasets()
    analyze_stability()
    
   
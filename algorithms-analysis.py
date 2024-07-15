import random
import timeit

def timsort(data):
    return data.sort()

def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
 
    if start > end:
        return start
 
    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid
 
def insertion_sort(arr):
    # Code is taken here https://www.geeksforgeeks.org/binary-insertion-sort/
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

def merge(array, left, mid, right):
    subArrayOne = mid - left + 1
    subArrayTwo = right - mid
    leftArray = [0] * subArrayOne
    rightArray = [0] * subArrayTwo

    for i in range(subArrayOne):
        leftArray[i] = array[left + i]
    for j in range(subArrayTwo):
        rightArray[j] = array[mid + 1 + j]

    indexOfSubArrayOne = 0
    indexOfSubArrayTwo = 0
    indexOfMergedArray = left
  
    while indexOfSubArrayOne < subArrayOne and indexOfSubArrayTwo < subArrayTwo:
        if leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]:
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
            indexOfSubArrayOne += 1
        else:
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
            indexOfSubArrayTwo += 1
        indexOfMergedArray += 1

    while indexOfSubArrayOne < subArrayOne:
        array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
        indexOfSubArrayOne += 1
        indexOfMergedArray += 1

    while indexOfSubArrayTwo < subArrayTwo:
        array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
        indexOfSubArrayTwo += 1
        indexOfMergedArray += 1

def merge_sort(array, begin, end):
    # Code is taken here https://www.geeksforgeeks.org/merge-sort/
    if begin >= end:
        return

    mid = begin + (end - begin) // 2
    merge_sort(array, begin, mid)
    merge_sort(array, mid + 1, end)
    merge(array, begin, mid, end)

def merge_sort_algo(data):
    length = len(data)
    return merge_sort(data, 0, length - 1)

algorithms = [timsort, insertion_sort, merge_sort_algo]

values = list(range(500))
values_two = list(range(500))
random.shuffle(values_two)

test_data = {
    'random_data': [random.randint(0, 10000) for _ in range(1000)],
    'accesnding_sorted_data': list(range(1000)),
    'descending_sorted_data': list(range(1000, -1, -1)),
    'parially_sorted_data': values + values_two,
    'duplicated_data': [random.choice([1, 2, 3, 4, 5]) for _ in range(1000)],
    'large_range_data': [random.randint(0, 1000000) for _ in range(1000)],
    '10': [random.randint(0, 100) for _ in range(10)],
    '100': [random.randint(0, 1000) for _ in range(100)],
    '100_000': [random.randint(0, 1000000) for _ in range(100000)],
}

results = {}

def evaluate_time_execution(func, data):
    start = timeit.default_timer()
    func(data)
    end = timeit.default_timer()
    return end - start

for alogrithm in algorithms:
    results[alogrithm.__name__] = []
    for test_case, test_velues in test_data.items():
        results[alogrithm.__name__].append({
            'name': test_case, 
            'result': f'{evaluate_time_execution(alogrithm, test_velues.copy()):.6f}'
        })

def print_results(results):
    max_cases_col_size = max([len(case_name) for case_name in test_data.keys()])
    max_algo_name_size = max([len(alogorithm_name) for alogorithm_name in results.keys()])
    header = f"{'Test Case':<{max_cases_col_size}}"
    for alogorithm_name in results.keys():
        header += f" | {alogorithm_name:<{max_algo_name_size}}"
    print(header)
    print('-' * len(header))

    for test_case_name in test_data.keys():
        row = f"{test_case_name:<{max_cases_col_size}}"
        for algorithm, algo_test_cases in results.items():
            filtered_list = [item for item in algo_test_cases if item['name'] == test_case_name]
            item = filtered_list.pop()
            row += f" | {item['result']:<{max_algo_name_size}}"
        print(row)

print_results(results)

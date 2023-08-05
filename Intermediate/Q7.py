"""Write a Python function that finds the median of a list of
numbers.
Sample Input: number_list = [7, 2, 5, 1, 9, 3]
Sample Output: Median: 4.0
"""
import statistics

def get_median(list_):
    result = statistics.median(list_)
    return result

if __name__ == "__main__":
    input_list = [7, 2, 5, 1, 9, 3]
    print(f"Median: {get_median(input_list)}")
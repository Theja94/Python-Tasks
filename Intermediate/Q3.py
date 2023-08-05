"""Given an array of N integers and an integer K, find the number of
pairs of elements in the array whose sum is equal to K.
Sample Input: arr = [1, 2, 3, 4, 5], k = 6
Sample Output: Pair count: 2
"""


def pair_count(arr, k):
    count = 0
    n = len(arr)
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                count += 1
    return count

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    k=8
    print("Pair count: "+ str(pair_count(arr, k)))



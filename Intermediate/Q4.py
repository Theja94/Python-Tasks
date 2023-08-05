"""Given an array of size N. The task is to rotate array by D elements
towards right
"""


def rotate_array(arr,d):
    temp_arr = []
    n=len(arr)
    # Update array from d to max value
    for i in range(d,n):
        temp_arr.append(arr[i])
    # Updating array from 0 to d
    for j in range (0,d):
        temp_arr.append(arr[j])
    arr=temp_arr.copy()
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    d = 2
    print("array after rotation: " + str(rotate_array(arr,d)))
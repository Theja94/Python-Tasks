"""Write a Python function that counts the number of vowels in a
given string.
Sample Input: string = "Hello, World!"
Sample Output: Number of vowels: 3
"""

vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

def find_vowels(inp):
    count = 0 
    for i in inp:
        if i in vowels:
            count += 1

    return count


if __name__ == "__main__":
    input_string = "Hello, World!"
    print("Number of vowels: " + str(find_vowels(input_string)))


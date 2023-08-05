"""We are making n stone piles! The first pile has n stones. If n is
even, then all piles have an even number of stones. If n is odd, all
piles have an odd number of stones. Each pile must have more
stones than the previous pile but as few as possible. Write a
Python program to find the number of stones in each pile.

"""

def check_num(n):
    # pile_list = []
    # for i in range(n):
    #     pile_list.append(i*2 + n)

    # Using list comprehension
    pile_list = [n + 2 * i for i in range(n)]
    return pile_list


if __name__=="__main__":
    n = int(input("Enter the value n: "))
    print("Number of stones in each pile: " +  str(check_num(n)) )

"""A cafe has N computers. Several customers come to the cafe to
use these computers. A customer will be serviced only if there is
any unoccupied computer at the moment the customer visits the
cafe. If there is no unoccupied computer, the customer leaves the
cafe.

training.consultadd.com

LEVEL - II

You are given an integer N representing the number of computers
in the cafe and a sequence of uppercase letters S. Every letter in S
occurs exactly two times. The first occurrence denotes the arrival
of a customer and the second occurrence denotes the departure
of the same customer if he gets allocated the computer.

You have to find the number of customers that walked away
without using a computer.

Example 1:
Input:
N = 3
S = GACCBDDBAGEE
Output: 1
Explanation: Only D will not be able to get any computer. So the
answer is 1.

Example 2:
Input:
N = 1
S = ABCBAC
Output: 2
Explanation: B and C will not be able to get any computers. So the
answer is 2.
"""
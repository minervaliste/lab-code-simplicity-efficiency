"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""
'''
Start checking from the top value, so we don't have to finish the loop in order to ensure we reached the highest possible value.
Since we know that the hipotenuse is always going to be the largest side of the 3, once we find the  correct combination we can just return 
that number.
'''
def search_largest_side(max_num):
    for x in range(max_num, 5, -1):
        for y in range( max_num, 4,-1):
            for z in range(max_num, 3, -1):
                if (x*x == y*y+z*z):
                    return x


max_num = int(input('What is the maximal length of the triangle side? Enter a number: '))
max_side = search_largest_side(max_num)
print('The longest side possible is ', max_side)

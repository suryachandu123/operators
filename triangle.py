'''
Finding the Area of a Triangle
Problem Statement
Ajay, Binoy, and Chandru decide to test their geometry skills. They want to calculate the area of the triangle formed by their house coordinates. Given the coordinates of the 3 vertices of a triangle (x1,y1)(x_1, y_1)(x1​,y1​), (x2,y2)(x_2, y_2)(x2​,y2​), and (x3,y3)(x_3, y_3)(x3​,y3​), write a Python program to find the area of the triangle.
Formula
Area=1/2​∣x1​(y2​−y3​)+x2​(y3​−y1​)+x3​(y1​−y2​)∣
Input Format
Input consists of 6 integers. The first two integers correspond to (x1,y1)(x_1, y_1)(x1​,y1​). The next two integers correspond to (x2,y2)(x_2, y_2)(x2​,y2​). The last two integers correspond to (x3,y3)(x_3, y_3)(x3​,y3​).
Output Format
Refer to the Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 2 decimal places]
Sample Input

0
0
4
0
0
3

Sample Output

The area of the triangle is 6.00

Solution
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

print(f"The area of the triangle is {area:.2f}")

'''
# Input coordinates of the triangle's vertices
x1 = int(input())  # x1 coordinate
y1 = int(input())  # y1 coordinate
x2 = int(input())  # x2 coordinate
y2 = int(input())  # y2 coordinate
x3 = int(input())  # x3 coordinate
y3 = int(input())  # y3 coordinate

# Calculate the area of the triangle using the given formula
area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

# Output the area formatted to 2 decimal places
print(f"The area of the triangle is {area:.2f}")

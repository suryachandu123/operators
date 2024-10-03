'''
Assume Dhoni's current age is 6. After 3 years, Dhoni's mother Devki Devi would be 4 times Dhoni's age. What is Devki Devi's current age? Write a program to determine the same.
Input Format:
First line of input consists of one integer value as age of Dhoni.
Output Format:
Output should display an integer that specifies Devki Devi's current age.
Sample Input and Output1:
6
33
Sample Input and Output2:
3
21
Note: Bold highlighted is the output value.
'''
cAge=int(input())
deviAge =((cAge+3)*4)-3
print(deviAge)
'''
# Function to calculate Devki Devi's current age
def calculate_mothers_age(dhonis_age):
    # After 3 years, Devki Devi's age will be 4 times Dhoni's age
    devi_age = ((dhonis_age + 3) * 4) - 3
    return devi_age

# Input
cAge = int(input())  # Dhoni's current age

# Calculate and display Devki Devi's current age
deviAge = calculate_mothers_age(cAge)
print(deviAge)

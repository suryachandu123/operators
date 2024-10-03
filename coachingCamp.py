'''
Dhoni once wished to join a a reputed Cricket Coaching Camp to be held at a place "X" kms away from his house. He told about this to his father and got his consent to use his friend's bike for the Camp. The Camp was to be held on all days of the month. His friend's bike provides a mileage of Y km/litre and the cost of petrol was Rs. Z. Dhoni's father now wanted to know the total amount that was needed by Dhoni to spend on his travel to the Camp. Help him find the same and assume number of days in a month as 30 days.
Input Format:
First line of the input is an integer "X" in kms that specifies the distance of the Camp from Dhoni's house.
Second line is an integer "Y" in km/litre that specifies the mileage of his friend's bike.
Third line is a float "Z" that specifies the cost of petrol in rupees.
Output Format:
Output should display a float that gives the total amount that is needed by Dhoni to spend on his travel in rupees. The float value is displayed correct to 2 decimal places.
Sample Input and Output 1:
75
55
63
2577.27
Sample Input and Output 2:
35
78
65.0
875.00
Note: Bold highlighted is the output
'''
x=float(input())
y=float(input())
z=float(input())
a=(x*z*30)/y
print("%.2f"%a)
'''
# Function to calculate the total amount needed for petrol
def calculate_petrol_cost(X, Y, Z):
    # Total travel distance for 30 days (to and fro)
    total_distance = 2 * X * 30
    # Calculate the total litres required and multiply by the cost of petrol
    total_cost = (total_distance / Y) * Z
    return round(total_cost, 2)

# Input
X = float(input())  # Distance to the camp in kms
Y = float(input())  # Mileage of the bike in km/litre
Z = float(input())  # Cost of petrol in rupees

# Calculate and display the total amount needed for petrol
total_amount = calculate_petrol_cost(X, Y, Z)
print(f"{total_amount:.2f}")

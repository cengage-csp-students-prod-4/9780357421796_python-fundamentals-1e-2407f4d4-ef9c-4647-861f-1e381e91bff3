# Write your code here
days_driving = int(input("Days you have been driving:"))
years_driving = days_driving // 365    
days_of_year = days_driving % 365
weeks_of_year = days_of_year // 7
remaining_days = days_of_year % 7

print("You have been driving for:")
print("Years:", years_driving)
print("Weeks:", weeks_of_year)
print("Days:", remaining_days)
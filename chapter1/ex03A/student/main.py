# Write your code here
distance_miles = 60
time_hours = 3

distance_knots = distance_miles / 1.15078
distance_feet = distance_miles * 5280
time_seconds = time_hours * 3600

speed_knots = distance_knots / time_hours
speed_mph = distance_miles / time_hours
speed_fps = distance_feet / time_seconds

#print("The speed in knots is: " , speed_knots)
print("The speed in miles per hour is: ", speed_mph)
print("The speed in feet per second is: ", speed_fps)

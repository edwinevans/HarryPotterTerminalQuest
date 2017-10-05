g_in_feet_per_second_per_second = 32 # On earth, gravity always pulls at 32 feet per second per second
g_in_feet_per_hour_per_second = 32 * 60 * 60 # 32 feet per second per second = 115,200 feet per hour per second
g_in_mph_per_second = g_in_feet_per_hour_per_second / 5280.0  # There are 5280 feet in a mile so 115,200 feet per hour per second equals about 22 miles per hour change per second

# If the change in speed is constant then magic says the change in distance is the square of the time times half
# d = 0.5 * g * (s * s)
def get_distance_fallen_in_n_seconds(n):
    return 0.5  *  (g_in_mph_per_second * (n * n))

# Let's print a table of time/distance/speed
for seconds in xrange(0, 6):
    print "After {} seconds, distance={} feet, speed={} mph".format(
            seconds, get_distance_fallen_in_n_seconds(seconds), seconds * g_in_mph_per_second) 

# After 0 seconds, distance=0.0 feet, speed=0.0 mph
# After 1 seconds, distance=10.9090909091 feet, speed=21.8181818182 mph
# After 2 seconds, distance=43.6363636364 feet, speed=43.6363636364 mph
# After 3 seconds, distance=98.1818181818 feet, speed=65.4545454545 mph
# After 4 seconds, distance=174.545454545 feet, speed=87.2727272727 mph
# After 5 seconds, distance=272.727272727 feet, speed=109.090909091 mph

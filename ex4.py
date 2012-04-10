buses = 20
space_in_a_bus = 25.0
drivers = 8
passengers = 150
buses_not_driven = buses - drivers
buses_driven = drivers
transport_capacity = buses_driven * space_in_a_bus
average_passengers_per_bus = passengers / buses_driven

print "There are ", buses, " buses available."
print "There are only ", drivers, "drivers available."
print "There will be ", buses_not_driven, " empty buses today."
print "We can transport ", transport_capacity, " people today."
print "We have ", passengers, " to transport today."
print "We need to put about ", average_passengers_per_bus, " in each bus."

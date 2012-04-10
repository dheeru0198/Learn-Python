def pizzas_and_burgers(pizzas_count, burgers_count):
    print "You have %d pizzass!" % pizzas_count
    print "You have %d burgers!" % burgers_count
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
pizzas_and_burgers(20, 30)


print "OR, we can use variables from our script:"
number_of_pizzas = 10
number_of_burgers = 50

pizzas_and_burgers(number_of_pizzas, number_of_burgers)


print "We can even do math inside too:"
pizzas_and_burgers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
pizzas_and_burgers(number_of_pizzas + 100, number_of_burgers + 1000)


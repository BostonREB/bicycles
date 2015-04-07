import bicycles

# Filling up the classes
Huffy10 = bicycles.Bicycle("Huffy 10-Speed", "35 lbs", 125)
Hipster = bicycles.Bicycle("Schwinn Hipster", "28 lbs", 95)
Fixie = bicycles.Bicycle("Schwinn Fixie", "21 lbs", 65)
FujiXX = bicycles.Bicycle("Fuji XX", "18 lbs", 220)
JW99 = bicycles.Bicycle("Jamis Winston 99", "25 lbs", 195)
Girlie = bicycles.Bicycle("Huffy Girlie", "21 lbs", 120)
BMX007 = bicycles.Bicycle("BMX 007", "44 lbs", 175)

Harleys = bicycles.BikeShop("Harley's Bike-O-Rama", 20, 0, [[Huffy10, 5], [Hipster, 12], [Fixie, 15], [FujiXX, 3], [JW99, 9], [Girlie, 7], [BMX007, 13]])

Bob = bicycles.Customer("Robert T. Bruce", 200, [BMX007, JW99])
Joe = bicycles.Customer("Joe Blow", 500, [Huffy10])
Don = bicycles.Customer("Donald T. Rump", 1000, [])

# #list bike shop starting inventory
inventory = Harleys.take_inventory()
print inventory

# # List bikes cutomers can afford
for buyer in bicycles.Customer:
  affordable = Harleys.affordable_bikes(buyer)
  print ""
  print "%s can afford the following bikes:" %buyer.name
  for bike in affordable:
    print "The %s, priced at $%s" % (bike[0], bike[1])
  print "**" * 10

Harleys.sell_bicycle(Bob, Huffy10)
Harleys.sell_bicycle(Joe, JW99)
Harleys.sell_bicycle(Don, FujiXX)

inventory = Harleys.take_inventory()
print inventory
print ""
print "%s total profits to date are $%d\n" % (Harleys.name, Harleys.profits)
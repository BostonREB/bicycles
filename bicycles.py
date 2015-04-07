class IterRegistry(type):
    def __iter__(cls):
      return iter(cls._registry)

# create Bycycle class
class Bicycle(object):
  def __init__(self, model, weight, production_cost):
    self.model = model
    self.weight = weight
    self.production_cost = production_cost

# Create BikeShop class
class BikeShop(object):
  def __init__(self, name, margin, profits, inventory=[]):
    self.name = name
    self.margin = margin
    self.profits = profits
    self.inventory = inventory

  def affordable_bikes(self, customer):
    affordable = []
    for bike in self.inventory:
      sale_price = bike[0].production_cost + (bike[0].production_cost * self.margin / 100)
      if customer.balance > sale_price:
        affordable.append([bike[0].model, sale_price])
    return affordable

  def sell_bicycle(self, customer, bicycle):
      sale_price = bicycle.production_cost + (bicycle.production_cost * self.margin / 100)
      if customer.balance > sale_price:
        customer.balance -= sale_price
        customer.collection.append(bicycle)
        print ""
        print "%s purchased a %s for $%s and has a $%s budget remaining.\n" % (customer.name,
          bicycle.model, sale_price, customer.balance)
      else:
        print "We're sorry, you cannot afford that bike."
      income = (sale_price - bicycle.production_cost)
      self.profits += income
      for bike in self.inventory:
        if bike[0].model == bicycle.model:
          bike[1] -= 1
          break

  def take_inventory(self):
    print " "
    print "%s has the following inventory of bikes:" % self.name
    for bike in self.inventory:
      print "Model: %s, %s bikes in stock" % (bike[0].model, bike[1])


# Create Customer class
class Customer(object):
  __metaclass__ = IterRegistry
  _registry = []

  def __init__(self, name, balance=0.0, collection=[]):
    self._registry.append(self)
    self.name = name
    self.balance = balance
    self.collection = collection

  def inventory_bikes(self):
    print "%s owns %d bike[s]" % (self.name, len(self.collection))
    print "%s owns the following:" % self.name
    for bike in self.collection:
      print bike.model + "\n"




class Restaurant(): 

  def __init__(self, name, cuisine_type): 
    self.name = name 
    self.cuisine_type = cuisine_type
    self.number_served = 0

  def describe_restaurant(self): 
    """Prints restaurant's information. """
    print("Restaurant name: " + self.name.title())
    print("Type of cuisine: " + self.cuisine_type.title())

  def open_restaurant(self, status):
    """ Indicates whether the restaurant is open. """
    print("The restaurant " + self.name.title() + " is " + status) 
  
  def set_number_served(self, number):
    self.number_served = number 
  
  def increment_number_served(self, totalserved): 
    self.number_served += totalserved

class IceCreamStand(Restaurant):
  def __init__(self, name, cuisine_type): 
    super().__init__(name, cuisine_type)

    self.flavors = ['chocolate', 'vanilla', 'almond']

  def display_flavors(self):
    print("\nThese are our icecream flavours: ")
    for flavor in self.flavors: 
      print(flavor)
    
ice_cream1 = IceCreamStand('Iceland', 'italian')
ice_cream1.describe_restaurant()
ice_cream1.display_flavors()

   
restaurant = Restaurant('el progresista', 'argentina')
restaurant.describe_restaurant()
restaurant.open_restaurant('open')
print(restaurant.number_served)
restaurant.set_number_served(1)
print(restaurant.number_served)
restaurant.increment_number_served(15)
print(restaurant.number_served)

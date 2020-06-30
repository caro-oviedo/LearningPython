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


   
restaurant = Restaurant('el progresista', 'argentina')
restaurant.describe_restaurant()
restaurant.open_restaurant('open')
print(restaurant.number_served)
restaurant.set_number_served(1)
print(restaurant.number_served)
restaurant.increment_number_served(15)
print(restaurant.number_served)

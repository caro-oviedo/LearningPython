class Restaurant(): 

  def __init__(self, name, cuisine_type): 
    self.name = name 
    self.cuisine_type = cuisine_type

  def describe_restaurant(self): 
    """Prints restaurant's information. """
    print("Restaurant name: " + self.name.title())
    print("Type of cuisine: " + self.cuisine_type.title())

  def open_restaurant(self, status):
    """ Indicates whether the restaurant is open. """
    print("The restaurant " + self.name.title() + " is " + status) 
  
restaurant = Restaurant('el progresista', 'argentina')
restaurant.describe_restaurant()
restaurant.open_restaurant('open')


""" A class that can be used to represent a car."""

class Car(): 
  """ Describing a car """

  def __init__(self, make, model, year): 
    """ Initialize attributes to describe a car. """
    self.make = make
    self.model = model 
    self.year = year 
    self.odometer_reading = 0 

  def get_descriptive_name(self): 
    """Return a neatly formatted descriptive  name."""
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
    return long_name.title() 
  
  def read_odometer(self): 
    """Print a statement showing the car's mileage."""
    print("This car has " + str(self.odometer_reading) + " miles on it.")

  def update_odometer(self, mileage): 
    """Set the odometer reading to the given value. Reject the change if it attempts to roll the odometer back. """
    
    if mileage >= self.odometer_reading: 
      self.odometer_reading = mileage
    else: 
      print("You can't roll back an odometer!")

  def increment_odometer(self,miles): 
    """Add thegiven amount to the odometer reading. """
    self.odometer_reading += miles 

class Battery():
  """a battery for an electric car"""
  def __init__(self, battery_size = 70): 
    self.battery_size = battery_size

  def describe_battery(self): 
    print("This car has a " + str(self.battery_size) + "-kwh battery")

  def get_range(self):
    if self.battery_size ==70: 
      range1 = 240 
    elif self.battery_size == 85:
      range1 =270

    message = "This car can go approximately " + str(range1)
    message += " miles on a full charge. "
    print(message)

  def upgrade_battery(self): 
    if self.battery_size == 70: 
      self.battery_size =85
      print("Upgraded your battery to 85")
    else: 
      print("Your battery is already upgraded")

  

class ElectricCar(Car): 
  def __init__(self, make, model, year): 
    super().__init__(make, model, year)
    self.battery = Battery()


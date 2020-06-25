class User(): 
  """Information about user's login"""

  def __init__(self, first_name, last_name): 
    self.name = first_name
    self.lastname = last_name 
    self.login_attempts = 0

  def describe_user(self):
    """Prints user's information. """
    print("User's information: \n")
    print("Name: " + self.name.title())
    print("Last name: " +  self.lastname.title())

  def greet_user(self): 
    """Prints a welcome message to the user. """
    print("Welcome " + self.name.title())

  def increment_login_attempts(self): 
    """Adds login attempts. """
    self.login_attempts += 1 
    print("Login attempts: " + str(self.login_attempts))

  def reset_login_attempts(self):
    """ Sets login_attempts to 0.""" 
    self.login_attempts = 0
    print("Your login attempts have been reset. You have now: " + str(self.login_attempts) + " login attempts")


user_1 = User('Matias', 'Cowell')
user_1.describe_user()
user_1.greet_user()
print(user_1.login_attempts)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()

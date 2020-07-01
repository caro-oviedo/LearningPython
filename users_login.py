
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




class Admin(User):
  def __init__(self, first_name, last_name):
    super().__init__(first_name, last_name)  
    self.privileges = Privileges()
    

class Privileges(): 
  def __init__(self, privileges=[]): 
    self.privileges_list = privileges

    
  def show_privileges(self):
    if self.privileges_list == [] :
      print("You don't have privileges yet")

    print("These are your priviliges: ")
    for privilege in self.privileges_list: 
      print("-" + privilege)



admin1= Admin('Antonia', 'Reclif')
admin1.describe_user()
admin1.privileges.show_privileges()

print("Adding privileges... ")
admin1_privileges = ['can add post', 'can delete post', 'can ban user']
admin1.privileges.privileges_list = admin1_privileges
admin1.privileges.show_privileges()

user_1 = User('Matias', 'Cowell')
user_1.describe_user()
user_1.greet_user()
print(user_1.login_attempts)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()

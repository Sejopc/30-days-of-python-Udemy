# INHERITANCE
class Animal():
    name = "Amy"
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = "Covers body"
    def get_color(self):
        return self.color
    def make_noise(self, noise):
        self.noise = noise
        return self.noise

dog = Animal()
#dog.make_noise()
dog.size = "Small"
dog.color = "Black"
dog.hair = "Hairless"
# We could change dog object attributes by modifying the Animal class variables (as above), however it will only work
# for that instance/object (dog). So the recommended approach is to use Inheritance, as described on class Dog below.

# Class Dog will inherit from class Animal.
class Dog(Animal):
    name = 'Jon'
    size = "Small"
    color = "Black"
    age = 19
    #color = 'brown'
    #def get_color(self): # 'self' keyword refers to the object that instanciated the class (i.e mydog = Dog(), where
                         # 'mydog' is the instance or object of Dog class, and hence 'mydog'=='self').
        #return self.color
jon = Dog()
jon.color = 'White'
jon.name = 'Jon Snow'
print(jon.color)
print(jon.name)

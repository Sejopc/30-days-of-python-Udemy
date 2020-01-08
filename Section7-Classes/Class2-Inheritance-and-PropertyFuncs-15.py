class Animal():
    name = "Amy"
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = "Covers body"
    def get_color(self, abc):
        return self.color + " " + abc
    def make_noise(self):
        return self.noise

dog = Animal()
dog.get_color('red')
dog.make_noise()

# PROPERTIES
# We can call a function by using function name with the parenthesis (). However, we can also call it without
# those parenthesis by making the function a property, with the "@property" string above.
class Animal2():
    name = "Amy"
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = "Covers body"
    def get_color(self, abc):
        return self.color + " " + abc
    @property
    def make_noise(self):
        return self.noise

dog2 = Animal2()
dog.make_noise # This time without parenthesis, and it will still return "Grunt", because now function is a property

# arg = Positional Argument
# kwarg = Keyword Argument (i.e arg1="hello"). Kwargs have to be declared after the positional arguments.
abc = "new string"
def some_func(arg_1, arg_2, kwarg_1=None, kwarg_2=None):
    print(arg_1, arg_2)
    if kwarg_1 != None:
        print(kwarg_1)

some_func("abc", "car", kwarg_1="Not a big deal.")

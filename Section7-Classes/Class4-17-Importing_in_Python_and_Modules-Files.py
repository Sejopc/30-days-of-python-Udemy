# Importing .py files as Python Modules (in this case python_date_test_Class4.py, and from there, we are
# importing its Class 'MessageUser', and 2 methods or functions 'some_random_func' and 'make_messages')
from python_date_test_Class4 import MessageUser, some_random_func, make_messages

obj = MessageUser()
obj.add_user("Justin", 123.32, "justin@sucks.com")
obj.add_user("John", 94.23)
obj.add_user("Emilee", 124.32)
obj.add_user("Jim", 323.4)
obj.add_user("Ron", 23)
obj.add_user("Sandra", 322.122323)
obj.get_details()
#print(obj.make_messages())
#some_random_func()

default_names = ["Justin", "John", "Emilee", "Jim", "Ron", "Sandra", "Veronica", "Whitney"]
default_amount = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

make_messages(default_names, default_amount)

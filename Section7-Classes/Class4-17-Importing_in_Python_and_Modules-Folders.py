# Importing Folders/Directories as Python Modules. Format: from folder.pythonfile.py import ClassName, or Function name
from py_day_module.make_messages import MessageUser

obj = MessageUser()
obj.add_user("Justin", 123.32, "justin@sucks.com")
obj.add_user("John", 94.23)
obj.add_user("Emilee", 124.32)
obj.add_user("Jim", 323.4)
obj.add_user("Ron", 23)
obj.add_user("Sandra", 322.122323)
obj.get_details()
print(obj.make_messages())

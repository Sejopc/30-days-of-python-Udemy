print("This works!")
# run this python folder as a module by running:
# $python running_python_commands_and_arguments_in_terminal-27
import argparse

parser = argparse.ArgumentParser(prog="running_python_commands_and_arguments_in_terminal-27") # here the program
                                                                                #will be the name of the directory, as
                                                                                # we are running the directory as a
                                                                                # python module (because of the __init__ and __module__ files)
parser.add_argument("type", type=str, choices=['view', 'message']) # make arguments required to be passed (NOT PARAMETERS).
# parser.add_argument("did_send", type=str, choices=['true','false']) # adding extra required arguements to be passed. Uncomment for testing with below commands.
# TO TEST ABOVE ^^ run:
# $python running_python_commands_and_arguments_in_terminal-27 -e jpperaltac@gmail.com -id 3 -> won't work because you are not passing any required argument
# $python running_python_commands_and_arguments_in_terminal-27 -e jpperaltac@gmail.com -id 3 view -> still won't work because you only pass 1 required argument out of 2
# $python running_python_commands_and_arguments_in_terminal-27 -e jpperaltac@gmail.com -id 3 view true -> will work.
parser.add_argument('-id','--user_id', type=int) #using short and large form parameters
parser.add_argument('-e','--email', type=str)

args = parser.parse_args()
print(args)
print(args.user_id)
# Up to here, run the following command to see how it works:
# $python running_python_commands_and_arguments_in_terminal-27 --user_id=10 (or using an existing one, such as --user_id=1)
from data_class import UserManager
#from data_manager import read_data


if args.type == "view": # for this to work, pass the required argument "view" to the program.
    print("----------------")
    print(UserManager().get_user_data(user_id=args.user_id, email=args.email))
    #print("Looking by ID: \n%s" % UserManager().get_user_data(user_id=args.user_id))
    #print("Looking by Email: \n%s" % UserManager().get_user_data(email=args.email))
elif args.type == "message":
    print(UserManager().message_user(user_id=args.user_id, email=args.email))

# We can run above code using:
# $python running_python_commands_and_arguments_in_terminal-27 -e jpperaltac@gmail.com -id 3 view (using both parameters)
# $python running_python_commands_and_arguments_in_terminal-27 -id=3 view (using only 1)
# OR, specifying required argument "message", and it will not call the read_data function, and simply print 'Send message.'
# $python running_python_commands_and_arguments_in_terminal-27 -id=3 message

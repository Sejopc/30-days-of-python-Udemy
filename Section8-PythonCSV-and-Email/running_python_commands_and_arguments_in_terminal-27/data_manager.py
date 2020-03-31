import csv
import datetime
import shutil
import os
from tempfile import NamedTemporaryFile

# 3 different ways to call the folder that we are in:
file_item_path = os.path.join(os.getcwd(), "data4.csv")
file_item_path2 = os.path.join(os.path.dirname(os.path.abspath("data4.csv")))
file_item_path3 = os.path.join(os.path.dirname(__file__), "data4.csv") # here __file__ refers this python file (data_manager.py).
                                                                        # In other words, join the directory where this file exists
                                                                        # with "data4.csv".

def read_data(user_id=None, email=None):
    print("Directory: %s" % file_item_path3)
    print("Full path to CSV file: %s" % file_item_path)
    file_name = file_item_path3
    with open(file_name, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        items = []
        unknown_user_id = None
        unknown_email = None
        for row in reader:
            if user_id is not None:
                if str(user_id) == str(row.get("id")):
                    return row
                else:
                    unknown_user_id = user_id
            if email is not None:
                if email == row.get("email"):
                    return row
                else:
                    unknown_email = email
        if unknown_user_id is not None:
            return "User id {user_id} not found.".format(user_id=user_id)
        if unknown_email is not None:
            return "Email {email} not found.".format(email=email)
    return None

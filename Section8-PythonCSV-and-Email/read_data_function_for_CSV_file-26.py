#!/usr/bin/python
import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile

def read_data(user_id=None, email=None):
    file_name = "data4.csv"
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

def delete_data(user_id=None, email=None):
    filename ="data4.csv"
    tempfile = NamedTemporaryFile(delete=False)
    with open(filename, "rb") as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        fieldnames = ["id", "name", "email", "amount", "sent", "date"]
        writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
        #writer.writeheader()
        for row in reader:
            #print(row)
            if user_id is not None:
                if str(user_id) == row.get('id'):
                    row.clear()
                    print(row)
            elif email is not None and user_id is None:
                if str(email) == row.get('email'):
                    row.clear()
                    print(row)
            else:
                pass
            writer.writerow(row)
        shutil.move(tempfile.name, filename)
        return True
    return False


def get_length(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        #print(reader_list)
        return len(reader_list)

def append_data(file_path, name, email, amount):
    fieldnames = ["id", "name", "email", "amount", "sent", "date"]
    # number of rows in order to get the id number automatically.
    next_id = get_length(file_path)
    with open(file_path, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            #writer.writeheader()
            writer.writerow({
                "id": next_id,
                "name": name,
                "email": email,
                "sent": "",
                "amount": amount,
                "date": datetime.datetime.now()
            })

def edit_data(edit_id=None, email=None, amount=None, sent=None):
    filename = "data4.csv"
    temp_file = NamedTemporaryFile(delete=False)

    with open(filename, "rb") as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ["id", "name", "email", "amount", "sent", "date"]
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        print("temp_file => %s" % temp_file.name) # Will create a temporary file with the same
                                                # contents as "filename" (data4.csv).

        for row in reader:
            #print(row)
            if edit_id is not None:
                if row["id"] == str(edit_id):
                    row["amount"] = amount
                    row["sent"] = sent
                    print(row)
            elif email is not None and edit_id is None:
                if row["email"] == str(email):
                    row["amount"] = amount
                    row["sent"] = sent
                    print(row)
            else:
                pass
            writer.writerow(row)

        shutil.move(temp_file.name, filename)
        return True
    return False

edit_data(email="jpperaltac@gmail.com", amount=99.99, sent="")

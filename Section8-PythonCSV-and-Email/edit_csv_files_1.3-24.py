import csv
import shutil # for working with linux commands, such as mv (move).
import datetime
from tempfile import NamedTemporaryFile

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

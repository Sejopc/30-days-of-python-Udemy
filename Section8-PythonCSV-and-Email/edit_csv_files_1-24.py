import csv
import shutil # for working with linux commands, such as mv (move).
import datetime
from tempfile import NamedTemporaryFile


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
        print(row)
        writer.writerow({ # we will rewrite the current rows PLUS ( + ) the amount and sent columns with
                            # their respective values, into this temporary filename (temp_file).
            "id": row["id"],
            "name": row["name"],
            "email": row["email"],
            "amount": "1293.23",
            "sent": "",
            "date": datetime.datetime.now()
        })

    shutil.move(temp_file.name, filename)

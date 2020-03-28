import csv
with open("data.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Description", "Col 3"])
    writer.writerow(["Row 1", "Some desc", "Another"])
    writer.writerow(["Row 1", "Some desc", "Another"])

with open("data.csv", "a") as csvfile: # now using 'a' (append) to append data to file instead of overwriting it.
    writer = csv.writer(csvfile)
    writer.writerow(["Append row", "Some desc", "Another"])

with open("data.csv", "w+") as csvfile: # will not return anything because it overwrote the file before reading it.
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# ----------------------------------------------------
with open("data2.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Col 1", "Col 2"])
    writer.writerow(["Data 1", "Data 2"])

with open("data2.csv", "r") as csvfile:
    reader = csv.reader(csvfile) # returns a list of rows
    for row in reader:
        print(row)

with open("data2.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Data 3", "Data 4"])

# ------------------------------------------------------
# We will now return a dictionary of columns
with open("data2.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

with open("data2.csv", "a") as csvfile: # Appending rows, not to overwrite.
    fieldnames = ["Col 1", "Col 2"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writerow({"Col 1":123, "Col 2":"Jose"})

with open("data3.csv", "w") as csvfile: # Create a new file and write or overwite an existing one
    fieldnames = ["Col 1", "Col 2"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({"Col 1":123, "Col 2":"Jose"})
# ---------------------------------------------------------

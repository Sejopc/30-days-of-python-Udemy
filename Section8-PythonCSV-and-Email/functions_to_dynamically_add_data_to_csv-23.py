import csv

def get_length(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        #print(reader_list)
        return len(reader_list)

def append_data(file_path, name, email):
    fieldnames = ["id", "name", "email"]
    # number of rows in order to get the id number automatically.
    next_id = get_length(file_path)

    with open(file_path, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            #writer.writeheader()
            writer.writerow({
                "id": next_id,
                "name": name,
                "email": email
            })

#append_data("data4.csv", "Jose", "jpperaltac@gmail.com")

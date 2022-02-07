# Import Modules
import pymongo

# Create Client
client = pymongo.MongoClient(
    "mongodb+srv://SDMoonsamy:RiddleMeThis@cluster0.hvzf9.mongodb.net/Tests?retryWrites=true&w=majority")

# Select Database & Collection
db = client["Tests"]
collection = db["Test1"]


# Define function that would Validate ID Number & Date Of Birth
def is_valid(id_num, date_of_birth):

    try:
        int(id_num)
        db_val = collection.find({})

        for value in db_val:
            if value["id_num"] == id_num:
                return False, "ID number already exists!"

        if len(id_num) != 13:
            return False, "The number entered is not a valid ID Number!"

        elif id_num[0:6] != date_of_birth[2:].replace("-", ""):
            return False, "ID number and date of birth do not match!"

        else:
            return True, "Successfully added to database!"

    except ValueError:
        return False, "ID Number cannot contain letters"


# Define Function that would read from database and display a Table
def show_table():
    statement = ""
    db_val = collection.find({})

    for record in db_val:
        name = record["name"]
        surname = record["surname"]
        id_num = record["id_num"]
        date_of_birth = record["date_of_birth"]

        statement += f"<tr>" \
                     f"<th>{name}</th>" \
                     f"<th>{surname}</th>" \
                     f"<th>{id_num}</th>" \
                     f"<th>{date_of_birth}</th>" \
                     f"</tr>"

    return statement


# Create Function that inserts into database
def insert_record(name, surname, id_num, date_of_birth):
    valid, statement = is_valid(id_num, date_of_birth)

    if valid:

        db_values = [i for i in collection.find({})]

        post = {"_id": (len(db_values) + 1), "name": name, "surname": surname, "id_num": id_num, "date_of_birth": date_of_birth}
        collection.insert_one(post)
        return valid, statement

    return valid, statement

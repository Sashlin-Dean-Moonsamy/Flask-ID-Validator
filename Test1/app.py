# Import Modules
from flask import Flask, render_template, request
import schema

# Create app
app = Flask(__name__)


# Def home function
@app.route('/')
def home():
    table_bod = schema.show_table()
    return render_template("Add_To_Database.html", table_vals=table_bod)


# Def form function
@app.route("/", methods=["POST"])
def forms():

    # Save Forms
    name = request.form["name"]
    surname = request.form["surname"]
    id_num = request.form["id_num"]
    date_of_birth = request.form["date_of_birth"]

    # Insert into db and visualize table
    valid, response = schema.insert_record(name, surname, id_num, date_of_birth)
    table_bod = schema.show_table()

    # Validate and return appropriate response
    if valid:
        return render_template("Add_To_Database.html", message=response, table_vals=table_bod)

    return render_template("Add_To_Database.html",
                           message=response,
                           name_val=name,
                           surname_val=surname,
                           previous_id=id_num,
                           table_vals=table_bod)


# Run Main
if __name__ == '__main__':
    app.run(host="localhost", port=7000)

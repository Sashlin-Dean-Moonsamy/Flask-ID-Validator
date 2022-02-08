# Import Modules
from flask import Flask, render_template, request
import schema

# Create app
app = Flask(__name__)


# Def home function
@app.route('/')
def home():
    table_bod = schema.show_table()
    return render_template("add_to_database.html", table_vals=table_bod, previous_date_of_birth="dd/mm/yyyy")


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
        return render_template("add_to_database.html", message=response, table_vals=table_bod)

    return render_template("add_to_database.html",
                           message=response,
                           name_val=name,
                           surname_val=surname,
                           previous_id=id_num,
                           previous_date_of_birth=date_of_birth,
                           table_vals=table_bod)


# Run Main
if __name__ == '__main__':
    app.run(host="localhost", port=7000)

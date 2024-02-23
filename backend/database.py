#Made by Derek Mo
#Began Development: Jan 2, 2024

# import mysql.connector
# from flask import Flask

# #Connect to MySQL Database
# mydb = mysql.connector.connect(
#   host= "localhost",
#   user= "root",
#   password= "password",
#   database= "Vehicles"
# )

# mycursor = mydb.cursor()

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     mycursor.execute("USE Vehicles;")
#     mycursor.execute("SELECT * FROM Cars")
#     table_list = mycursor.fetchall()
#     return "<p>DUDE WHAT WOULD HAPPEN</p>"

# from flask import Flask, jsonify
# import mysql.connector

# app = Flask(__name__)

# @app.route('/cars')
# def get_cars():
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="password",
#         database="Vehicles"
#     )
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT * FROM Cars")
#     cars = mycursor.fetchall()
#     for i in cars:
#         print(i)
#     mycursor.close()
#     mydb.close()
#     return jsonify(cars)

# if __name__ == '__main__':
#     app.run(debug=True)
#     get_cars()

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="Vehicles"
    )

@app.route('/cars')
def get_cars():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Cars")
        cars = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(cars)
    except mysql.connector.Error as error:
        print("Error fetching car records:", error)
        return jsonify([]), 500

@app.route('/add-car', methods=['POST'])
def add_car():
    try:
        data = request.json
        connection = connect_to_database()
        cursor = connection.cursor()
        sql_query = "INSERT INTO Cars (id, make, model, year, price) VALUES (%s, %s, %s, %s, %s)"
        values = (data['id'], data['make'], data['model'], data['year'], data['price'])
        cursor.execute(sql_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": "Car record added successfully"}), 201
    except mysql.connector.Error as error:
        print("Error adding car record:", error)
        return jsonify({"message": "Failed to add car record"}), 500

@app.route('/delete-car/<int:id>', methods=['DELETE'])
def delete_car(id):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        sql_query = "DELETE FROM Cars WHERE id = %s"
        values = (id,)
        cursor.execute(sql_query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify({"message": f"Car record with ID {id} deleted successfully"}), 200
    except mysql.connector.Error as error:
        print("Error deleting car record:", error)
        return jsonify({"message": "Failed to delete car record"}), 500

if __name__ == '__main__':
    app.run(debug=True)

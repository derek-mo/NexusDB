#Made by Derek Mo
#Began Development: Jan 2, 2024

import mysql.connector
import tkinter as tk
from tkinter import ttk, font

#Connect to MySQL Database
mydb = mysql.connector.connect(
  host= "localhost",
  user= "root",
  password= "password",
  database= "Vehicles"
)

mycursor = mydb.cursor()

primary = "#22303C"
secondary = "#E5F3FF"
accent = "#12211F"

def display_table():
  global info_frame
  global window
  clear_info_frame()

  window.geometry("700x400")
  info_frame.config(width= 500, height= 400)

  mycursor.execute("USE Vehicles;")
  mycursor.execute("SELECT * FROM Cars")
  table_list = mycursor.fetchall()

  table = ttk.Treeview(info_frame, show= "headings")

  # Define columns
  table["columns"] = ("ID", "Make", "Model", "Year", "Price")

  # Column headings
  table.heading("#0")
  table.heading("ID", text= "ID")
  table.heading("Make", text= "Make")
  table.heading("Model", text= "Model")
  table.heading("Year", text= "Year")
  table.heading("Price", text= "Price")

  # Column widths
  table.column("#0", width=0)
  table.column("ID", anchor= "center", width= 100)
  table.column("Make", anchor= "center", width= 100)
  table.column("Model", anchor= "center", width= 100)
  table.column("Year", anchor= "center", width= 100)
  table.column("Price", anchor= "center", width= 100)

  table.tag_configure("allrows", background=primary)

  # Insert data
  for i in range(len(table_list)):
      table.insert("", i, values=(table_list[i][0], table_list[i][1], table_list[i][2], table_list[i][3], table_list[i][4]))

  table.pack(expand=tk.YES, fill=tk.BOTH)


def add_record_input():
  # Clears the Right Side before adding to it
  clear_info_frame()

  record_id_label = ttk.Label(master= info_frame, text= 'Vehicle ID')
  record_id_label.pack(pady=5)
  record_id = tk.StringVar()
  record_id_entry = ttk.Entry(master= info_frame,textvariable= record_id)
  record_id_entry.pack(pady=5)

  record_make_label = ttk.Label(master= info_frame, text= 'Make')
  record_make_label.pack(pady=5)
  record_make = tk.StringVar()
  record_make_entry = ttk.Entry(master= info_frame,textvariable= record_make)
  record_make_entry.pack(pady=5)

  record_model_label = ttk.Label(master= info_frame, text= 'Model')
  record_model_label.pack(pady=5)
  record_model = tk.StringVar()
  record_model_entry = ttk.Entry(master= info_frame,textvariable= record_model)
  record_model_entry.pack(pady=5)

  record_year_label = ttk.Label(master= info_frame, text= 'Year')
  record_year_label.pack(pady=5)
  record_year = tk.StringVar()
  record_year_entry = ttk.Entry(master= info_frame,textvariable= record_year)
  record_year_entry.pack(pady=5)

  record_price_label = ttk.Label(master= info_frame, text= 'Price')
  record_price_label.pack(pady=5)
  record_price = tk.StringVar()
  record_price_entry = ttk.Entry(master= info_frame,textvariable= record_price)
  record_price_entry.pack(pady=5)

  sub_btn=ttk.Button(master= info_frame, text= 'Submit', command= lambda: add_record(record_id.get(), record_make.get(), record_model.get(), record_year.get(), record_price.get()))
  sub_btn.configure(style= "Custom.TButton")
  sub_btn.pack(pady=10)


def add_record(id, make, model, year, price):
  sql_query = "INSERT INTO Cars (id, make, model, year, price) VALUES (%s, %s, %s, %s, %s)"
  value = (id, make, model, year, price)
  mycursor.execute(sql_query, value)
  mydb.commit()


def delete_record_input():
  # Clears the Right Side before adding to it
  clear_info_frame()

  form_frame = tk.Frame(info_frame, background= primary)
  form_frame.place(x=185, y=100)
  record_id_label = ttk.Label(master= form_frame, text= 'Vehicle ID')
  record_id_label.pack(pady=5)

  record_id = tk.StringVar()
  record_id_entry = ttk.Entry(master= form_frame,textvariable= record_id)
  record_id_entry.pack(pady=5)

  sub_btn=ttk.Button(master= form_frame, text= 'Submit', command= lambda: remove_record(record_id.get()))
  sub_btn.configure(style= "Custom.TButton")
  sub_btn.pack(pady=10)


def remove_record(id):
  sql_query = "DELETE FROM Cars WHERE id = %s;"
  value = (id,)
  mycursor.execute(sql_query, value)
  mydb.commit()


def clear_info_frame():
  global window
  global info_frame
  info_frame.destroy()
  window.geometry("700x400")
  info_frame = tk.Frame(master= window, width= 500, height= 400, background= primary)
  info_frame.pack_propagate(0)
  info_frame.pack(side="left")


# Window Set Up
window = tk.Tk()
window.title("NexusDB")
window.geometry('700x400')

style = ttk.Style()
style.configure("TLabel", foreground= secondary, background= primary, font= ("Jetbrains Mono", 11))
style.configure("Custom.TButton", foreground= primary, background= secondary, width= 15, height= 2, font= ("Jetbrains Mono", 10))
style.configure("TEntry", background= secondary)

# Left side frame
btn_frame = tk.Frame(master= window, width= 200, height= 400, background= primary)
btn_frame.pack_propagate(0)
btn_frame.pack(side= "left")

# Right side frame
info_frame = tk.Frame(master= window, width= 500, height= 400, background= primary)
info_frame.pack_propagate(0)
info_frame.pack(side="left")

welcome_label = ttk.Label(master= btn_frame, text= "Welcome to NexusDB")
welcome_label.pack(pady= 20)

show_table_btn = ttk.Button(master= btn_frame, text= "Display Table", command= display_table)
show_table_btn.configure(style= "Custom.TButton")
show_table_btn.pack(pady= 30)

add_record_btn = ttk.Button(master= btn_frame, text= "Add Record", command= add_record_input)
add_record_btn.configure(style= "Custom.TButton")
add_record_btn.pack(pady= 30)

remove_record_btn = ttk.Button(master= btn_frame, text= "Delete Record", command= delete_record_input)
remove_record_btn.configure(style= "Custom.TButton")
remove_record_btn.pack(pady= 30)

window.mainloop()

from tkinter import *
# from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("My Addressbook")
# root.iconbitmap("/home/rk/Documents/gui/Address-Book-icon.ico")

# Create a database to connect to one if it already exists
conn = sqlite3.connect("address_book.db")
c = conn.cursor() #cursor 

# Creating a table for the first time. To be executed only once 
# c.execute("""

#   CREATE TABLE addresses(
#       first_name text,
#       last_name text,
#       address text,
#         city text,
#       state text,
#       zipcode integer
#     ) 
# """)


def update():
    # Create a database to connect to one if it already exists
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor() #cursor 
    record_id = delete_id.get()
    c.execute(f"""
    
                UPDATE addresses SET
                  
                    first_name = :first,
                    last_name = :last,
                    address = :address,
                    city = :city,
                    state = :state,
                    zipcode = :zipcode
                            
                WHERE oid = {record_id} """,
                {
                'first': f_name_edit.get(),
                'last': l_name_edit.get(),
                'address': address_edit.get(),
                'city': city_edit.get(),
                'state': state_edit.get(),
                'zipcode': zipcode_edit.get(),
                'oid': record_id
                })

  
    conn.commit()#commiting the changes
    conn.close() # closing the connection
    editor.destroy()
    # return

def edit():
    global editor
    editor = Tk()
    editor.title("Update Record")
    editor.geometry("400x200")
    # Create a database to connect to one if it already exists
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor() #cursor 
    record_id = delete_id.get()
    # print('record_id', f"SELECT *,  FROM addresses WHERE oid = {record_id}")
    c.execute(f"SELECT *  FROM addresses WHERE oid ={record_id}")
    records = c.fetchall()



    #Creating Text Boxes
    global f_name_edit
    global l_name_edit
    global address_edit
    global city_edit
    global state_edit
    global zipcode_edit
    f_name_edit = Entry(editor, width=30)
    f_name_edit.grid(row= 0 , column = 1, pady=(10,0))
    l_name_edit = Entry(editor, width=30)
    l_name_edit.grid(row= 1 , column = 1)
    address_edit = Entry(editor, width=30)
    address_edit.grid(row= 2 , column = 1)
    city_edit = Entry(editor, width=30)
    city_edit.grid(row= 3 , column = 1)
    state_edit = Entry(editor, width=30)
    state_edit.grid(row= 4 , column = 1)
    zipcode_edit = Entry(editor, width=30)
    zipcode_edit.grid(row= 5 , column = 1)
    

    # Creating labels
    f_name_label_edit = Label(editor, text="First Name")
    f_name_label_edit.grid(row = 0, column = 0 ,pady=(10,0))
    l_name_label_edit = Label(editor, text="Last Name")
    l_name_label_edit.grid(row = 1, column = 0)
    address_label_edit = Label(editor, text="Address")
    address_label_edit.grid(row = 2, column = 0)
    city_label_edit = Label(editor, text="City")
    city_label_edit.grid(row = 3, column = 0)
    state_label_edit = Label(editor, text="State")
    state_label_edit.grid(row = 4, column = 0)
    zipcode_label_edit = Label(editor, text="Zip")
    zipcode_label_edit.grid(row = 5, column = 0)
   

    save_btn = Button(editor, text = "Save Changes", command = update)
    save_btn.grid(row = 9 , column = 0, columnspan=2 )



    for record in records:
        f_name_edit.insert(0, record[0])
        l_name_edit.insert(0, record[1])
        address_edit.insert(0, record[2])
        city_edit.insert(0, record[3])
        state_edit.insert(0, record[4])
        zipcode_edit.insert(0, record[5])




def delete():
    # Create a database to connect to one if it already exists
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor() #cursor 
    
    c.execute(f"DELETE FROM addresses WHERE oid = {delete_id.get()}")

    conn.commit()#commiting the changes
    conn.close() # closing the connection  
    return

def submit():
    # Create a database to connect to one if it already exists
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor() #cursor 

    

    #Insert into table
    c.execute("INSERT INTO addresses  VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)", 
                    {"f_name": f_name.get(),
                    "l_name": l_name.get(),
                    "address":address.get(),
                    "city":city.get(),
                    "state":state.get(),
                    "zipcode":zipcode.get()
                    })    

    conn.commit()#commiting the changes
    conn.close() # closing the connection   

    #Clear  the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
    # Create a database to connect to one if it already exists
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor() #cursor 

    #Query the database
    c.execute("""
        SELECT *, oid from addresses
    """)
    records = c.fetchall()
    # print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0
        ]) + "\t" + str(record[-1])  + "\n"
    
    query_record = Label(root, text = print_records)
    query_record.grid(row = 12, column = 0, columnspan = 2)

    conn.commit()#commiting the changes
    conn.close() # closing the connection 

    


#Creating Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row= 0 , column = 1, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row= 1 , column = 1)
address = Entry(root, width=30)
address.grid(row= 2 , column = 1)
city = Entry(root, width=30)
city.grid(row= 3 , column = 1)
state = Entry(root, width=30)
state.grid(row= 4 , column = 1)
zipcode = Entry(root, width=30)
zipcode.grid(row= 5 , column = 1)
delete_id = Entry(root, width = 30)
delete_id.grid(row = 8, column = 1 )

# Creating labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row = 0, column = 0 ,pady=(10,0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row = 1, column = 0)
address_label = Label(root, text="Address")
address_label.grid(row = 2, column = 0)
city_label = Label(root, text="City")
city_label.grid(row = 3, column = 0)
state_label = Label(root, text="State")
state_label.grid(row = 4, column = 0)
zipcode_label = Label(root, text="Zip")
zipcode_label.grid(row = 5, column = 0)
delete_label = Label(root, text="Enter ID")
delete_label.grid(row = 8)

# Create submit buttons
submit_btn = Button(root,text =  "Add Record to Database", command = submit)
submit_btn.grid(row= 6, column = 0, columnspan=2, pady = 0, padx = 10, ipadx = 100)
query_btn = Button(root, text = "Show Records", command = query)
query_btn.grid(row = 7, column = 0, columnspan=2, pady = 5, padx = 10, ipadx= 130)
delete_btn = Button(root, text = "Delete Record", command = delete)
delete_btn.grid(row = 10, column = 0, columnspan=2, ipadx = 130)

edit_btn = Button(root, text = "Edit Record", command = edit)
edit_btn.grid(row = 11, column = 0, columnspan = 2, ipadx = 141)




conn.commit()#commiting the changes
conn.close() # closing the connection

root.mainloop()
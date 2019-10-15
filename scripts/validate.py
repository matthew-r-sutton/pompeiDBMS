import mysql.connector as mysql
from configparser import ConfigParser
import tkinter as tk
import dbms

# define the validate button's command
def check(un,pw):
    # read-in data need for db connection
    config = ConfigParser()
    config.read('./config.ini')
    try:
        # connect to the db
        db = mysql.connect(
            host=config['mysql']['host'],
            user=un,
            passwd=pw,
            database=config['mysql']['db']
        )
        main.destroy()

        # get column data
        cursor = db.cursor(buffered=True)
        query = """SHOW COLUMNS FROM pompei.scarpa;"""
        cursor.execute(query)

        # create list of field names
        field_names = []
        for row in cursor:
            field_names.append(row[0])

        # open DBMS window
        dbms.dbms(db,field_names)
    except:
        # initialize warning message
        warning = tk.Label(canvas,font='Helvetica 16',bg='#d5d5d5',
            text='Please check your username and password')
        warning_2 = tk.Label(canvas,font='Helvetica 16',bg='#d5d5d5',
            text='and try again.')

        # place warning message
        warning.place(relx=0.5,rely=0.8,relwidth=1,relheight=0.1,
            anchor='center')
        warning_2.place(relx=0.5,rely=.9,relwidth=1,relheight=0.1,
            anchor='center')

# initialize and format main window
main = tk.Tk()
window_width = main.winfo_reqwidth()
window_height = main.winfo_reqheight()
position_right = int(main.winfo_screenwidth()/2.5 - window_width/2.5)
position_down = int(main.winfo_screenheight()/2.5 - window_height/2.5)
main.geometry("+{}+{}".format(position_right,position_down))
main.title("Verifica d'Accesso")

# initialize canvas
HEIGHT = 300
WIDTH = 500
canvas = tk.Canvas(main,height=HEIGHT,width=WIDTH,bg='#d5d5d5')

# initialize username and password labels and entry boxes
username_label = tk.Label(canvas,text='Username: ',font='Helvetica 24',
    bg='#d5d5d5')
username_entry = tk.Entry(canvas,show='*',font='Helvetica 18')
password_label = tk.Label(canvas,text='Password: ',font='Helvetica 24',
    bg='#d5d5d5')
password_entry = tk.Entry(canvas,show='*',font='Helvetica 18')

# initialize validate button
validate_button = tk.Button(canvas,text='Verifica',font='Helvetica 24',
    command=lambda:check(username_entry.get(),password_entry.get()))

# pack canvas
canvas.pack(fill='both',expand=1)

# place username and password labels and entry boxes
username_label.place(relx=0.25, rely=0.225, relwidth=0.5, relheight=0.1,
    anchor='center')
username_entry.place(relx=0.75, rely=0.225, relwidth=0.4, relheight=0.1,
    anchor='center')
password_label.place(relx=0.25, rely=0.375, relwidth=0.5, relheight=0.1,
    anchor='center')
password_entry.place(relx=0.75, rely=0.375, relwidth=0.4, relheight=0.1,
    anchor='center')

# place validate button
validate_button.place(relx=0.5,rely=0.675,relwidth=0.25,relheight=0.2,
    anchor='center')

main.mainloop()

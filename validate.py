import tkinter as tk
import mysql.connector as mysql
import configparser
import dbms
import upload

def check(un,pw,action):
    # read-in data need for db connection
    config = configparser.ConfigParser()
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
        if action == 'dbms':
            dbms.dbms(db)
        else:
            upload.upload(db)
    except:
        # initialize warning message
        warning = tk.Label(frame,font='Helvetica 16',bg='#d5d5d5')
        warning_2 = tk.Label(frame,font='Helvetica 16',bg='#d5d5d5')

        # place and fill warning message
        warning.place(relx=0.5,rely=0.8,relwidth=1,relheight=0.1,anchor='center')
        warning_2.place(relx=0.5,rely=.9,relwidth=1,relheight=0.1,anchor='center')
        warning['text'] = "Please check your username and password"
        warning_2['text'] = 'and try again.'

# initialize and format main window
main = tk.Tk()
window_width = main.winfo_reqwidth()
window_height = main.winfo_reqheight()
position_right = int(main.winfo_screenwidth()/2.5 - window_width/2.5)
position_down = int(main.winfo_screenheight()/2.5 - window_height/2.5)
main.geometry("+{}+{}".format(position_right,position_down))
main.title('ID Validation')

# initialize canvas and frame
HEIGHT = 300
WIDTH = 500
canvas = tk.Canvas(main,height=HEIGHT,width=WIDTH)
frame = tk.Frame(canvas,bg='#d5d5d5')

# pack canvas and place frame
canvas.pack(fill='both',expand=1)
frame.place(relheight=1,relwidth=1)

# initialize username and password labels and entry boxes
username_label = tk.Label(frame,text='Username: ',font='Helvetica 24',bg='#d5d5d5')
username_entry = tk.Entry(frame,show='*',font='Helvetica 18')
password_label = tk.Label(frame,text='Password: ',font='Helvetica 24',bg='#d5d5d5')
password_entry = tk.Entry(frame,show='*',font='Helvetica 18')

# initialize validate button
dbms_button = tk.Button(frame,
                        text='DBMS',
                        font='Helvetica 20',
                        command=lambda:check(username_entry.get(),
                                             password_entry.get(),
                                             'dbms'))
upload_button = tk.Button(frame,
                          text='Batch Upload',
                          font='Helvetica 20',
                          command=lambda:check(username_entry.get(),
                                               password_entry.get(),
                                               'upload'))

# place username and password labels and entry boxes
username_label.place(relx=0.25, rely=0.225, relwidth=0.5, relheight=0.1,anchor='center')
username_entry.place(relx=0.75, rely=0.225, relwidth=0.4, relheight=0.1,anchor='center')
password_label.place(relx=0.25, rely=0.375, relwidth=0.5, relheight=0.1,anchor='center')
password_entry.place(relx=0.75, rely=0.375, relwidth=0.4, relheight=0.1,anchor='center')

# place validate button
dbms_button.place(relx=0.25,rely=0.625,relwidth=0.2,relheight=0.2,anchor='center')
upload_button.place(relx=0.75,rely=0.625,relwidth=0.35,relheight=0.2,anchor='center')

main.mainloop()

def upload(db,canvas):
    import mysql.connector as mysql
    from configparser import ConfigParser
    import tkinter as tk
    import upload_data

    # define transer button's command function
    def upload(db,file,notification):
        upload_data.upload(db,file,notification)

    # create file upload label, entry box, and empty notification
    label = tk.Label(canvas,text="File da transferire: ",font="Helvetica 20",
        bg='#d5d5d5')
    file = tk.Entry(canvas,font="Helvetica 12")
    notification = tk.Label(canvas,font='Helvetica 20',bg='#d5d5d5')

    # create transfer button
    transfer_button = tk.Button(canvas,text='Transferisci',font='Helvetica 24',
        command=lambda:upload(db,file,notification))

    # place instruction label, file entry box, and transfer button
    label.place(relx=0.25,rely=0.25,relwidth=0.49,relheight=0.1,anchor='center')
    file.place(relx=0.5,rely=0.4,relwidth=0.8,relheight=0.1,anchor='center')
    transfer_button.place(relx=0.5,rely=0.65,relwidth=0.3,relheight=0.1,
        anchor='center')

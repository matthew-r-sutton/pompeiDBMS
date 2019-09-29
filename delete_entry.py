def delete(passthrough_dict):
    import tkinter as tk
    import tkinter.ttk as ttk
    import mysql.connector as mysql
    import configparser
    import add_table

    # read-in keys of passthrough_dict arg
    un = passthrough_dict['un']
    pw = passthrough_dict['pw']
    main = passthrough_dict['main']
    canvas = passthrough_dict['canvas']
    nb = passthrough_dict['nb']
    page = passthrough_dict['page']

    # read-in data need for db connection
    config = configparser.ConfigParser()
    config.read('./config.ini')

    # connect to the db
    db = mysql.connect(
        host=config['mysql']['host'],
        user=un,
        passwd=pw,
        database="pompei"
    )

    def generate_interface(frame):
        # generate field labels and entry boxes
        ID_label = tk.Label(frame, text="ID to delete: ", font='Helvetica 20')
        ID_entry = tk.Entry(frame, font='Helvetica 20')

        ID_label.place(relx=0.05,rely=0.25,relheight=0.05,relwidth=0.45)
        ID_entry.place(relx=0.5,rely=0.25,relheight=0.05,relwidth=0.45)
        return ID_entry

    def delete_entry():
        cursor = db.cursor(buffered=True)
        query = """DELETE FROM pompei.scarpa
                WHERE ID = %s;"""
        value = (ID_entry.get(),)
        cursor.execute(query,value)
        db.commit()
        # print message confirming deletion
        delete_msg = tk.Label(top_frame,font='Helvetica 20',anchor="n")
        delete_msg['text'] = "Entry " + str(ID_entry.get()) + " has been deleted."
        delete_msg.place(relx=0.3,rely=0.75)

    # create top and bottom canvases with scrollbars
    top_canvas = tk.Canvas(page, height=200, width=400)
    top_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

    top_frame = tk.Frame(top_canvas)

    ID_entry = generate_interface(top_frame)

    top_frame.pack(fill='both',expand=1)

    delete_button = tk.Button(top_frame, text='Elimina', font='Helvetica 18')
    delete_button.place(relx=0.4,rely=0.5,relheight=0.1,relwidth=0.2)

    delete_button['command'] = delete_entry

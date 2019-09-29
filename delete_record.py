def delete(db,page):
    import tkinter as tk
    import tkinter.ttk as ttk

    def create_interface(frame):
        # create field labels and entry boxes
        ID_label = tk.Label(frame, text="ID to delete: ", font='Helvetica 20',bg='#d5d5d5')
        ID_entry = tk.Entry(frame, font='Helvetica 20')

        ID_label.place(relx=0.25,rely=0.25,relheight=0.1,relwidth=0.45,anchor='center')
        ID_entry.place(relx=0.75,rely=0.25,relheight=0.1,relwidth=0.45,anchor='center')
        return ID_entry

    def delete_record():
        if ID_entry.get() != '':
            cursor = db.cursor(buffered=True)
            query = """DELETE FROM pompei.scarpa
                    WHERE ID = %s;"""
            value = (ID_entry.get(),)
            cursor.execute(query,value)
            db.commit()
            # print message confirming deletion
            delete_msg = tk.Label(frame,font='Helvetica 20',anchor="n",bg='#d5d5d5')
            delete_msg['text'] = "Entry " + str(ID_entry.get()) + " has been deleted."
            delete_msg.place(relx=0.5,rely=0.75,relheight=0.1,relwidth=0.5,anchor='center')
        else:
            # print error message
            error_msg = tk.Label(frame,font='Helvetica 20',anchor="n",bg='#d5d5d5')
            error_msg['text'] = "Please denote an entry to delete."
            error_msg.place(relx=0.5,rely=0.75,relheight=0.1,relwidth=0.5,anchor='center')

    # create canvas and frame
    canvas = tk.Canvas(page)
    frame = tk.Frame(canvas,bg='#d5d5d5')

    # create interface
    ID_entry = create_interface(frame)

    # place canvas and pack frame
    canvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    frame.pack(fill='both',expand=1)

    # create delete button
    delete_button = tk.Button(frame, text='Elimina', font='Helvetica 18')
    delete_button.place(relx=0.5,rely=0.50,relheight=0.1,relwidth=0.2,anchor='center')
    delete_button['command'] = delete_record

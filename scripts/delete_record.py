def delete(db,canvas):
    import tkinter as tk

    # define command function for delete button that deletes the specified id
    def delete_record(db,id,notification):

        # if id is not blank delete the record with that id
        # else print error message
        if id.get() != '':
            # delete record with the specified id
            cursor = db.cursor(buffered=True)
            query = """DELETE FROM pompei.scarpa
                    WHERE id = %s;"""
            value = (id.get(),)
            cursor.execute(query,value)
            db.commit()

            # print message confirming deletion
            notification['text'] = ("Entry " + str(id.get()) +
                " has been deleted.")
            notification.place(relx=0.5,rely=0.9,relheight=0.1,relwidth=0.5,
                anchor='center')
        else:
            # print error message
            notification['text'] = "Specifica l'ID da eliminare."
            notification.place(relx=0.5,rely=0.9,relheight=0.1,relwidth=0.5,
                anchor='center')


    # initialize id label and entry box
    id_label = tk.Label(canvas, text="ID da eliminare: ",font='Helvetica 24',
        bg='#d5d5d5')
    id = tk.Entry(canvas, font='Helvetica 24')

    # initialize notification label
    notification = tk.Label(canvas,font='Helvetica 24',bg='#d5d5d5')

    # initialize delete button
    delete_button = tk.Button(canvas, text='Elimina', font='Helvetica 24',
        command=lambda:delete_record(db,id,notification))
        

    # place label and entry box
    id_label.place(relx=0.25,rely=0.4,relheight=0.1,relwidth=0.45,
        anchor='center')
    id.place(relx=0.75,rely=0.4,relheight=0.1,relwidth=0.45,anchor='center')

    # place delete button
    delete_button.place(relx=0.5,rely=0.7,relwidth=0.2,relheight=0.1,
        anchor='center')

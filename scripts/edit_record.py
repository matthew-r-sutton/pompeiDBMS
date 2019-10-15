def edit(db,canvas,field_names):
    import tkinter as tk

    # define edit button command function
    def edit_record(db,edit):
        try:
            # assign field, value, and ID from edit param
            field = edit['field'].get()
            new_value = edit['new_value'].get()
            ID = edit['ID'].get()

            # update the record
            cursor = db.cursor(buffered=True)
            query = "UPDATE pompei.scarpa SET "+field+" = %s WHERE ID = %s;"
            values = (new_value,int(ID))
            cursor.execute(query,values)
            db.commit()

            # set the notification to confirmation message
            notification['text'] = "Entry " + ID + " has been modified."
            notification.place(relx=0.5,rely=0.9,relwidth=1,anchor='center')

        except ValueError:
            # set the norification to error message
            notification['text'] = 'Please enter an ID.'
            notification.place(relx=0.5,rely=0.9,relwidth=1,anchor='center')


    # initialize ID, field, and value labels
    ID_label = tk.Label(canvas,text="ID da modificare: ",font="Helvetica 24",
        bg='#d5d5d5')
    field_label = tk.Label(canvas,text="Campo da modificare: ",
        font="Helvetica 24",bg='#d5d5d5')
    value_label = tk.Label(canvas,text="Nuovo valore: ",font="Helvetica 24",
        bg='#d5d5d5')

    # initialize ID and value entry boxes
    ID_entry = tk.Entry(canvas,font="Helvetica 24")
    value_entry = tk.Entry(canvas,font="Helvetica 24")

    # initialize dropdown menu
    field = tk.StringVar(canvas)
    field.set('SESSO')
    dropdown_menu = tk.OptionMenu(canvas,field,*field_names)
    dropdown_menu.config(font='Helvetica 20')
    menu = dropdown_menu.nametowidget(dropdown_menu.menuname)
    menu.config(font='Helvetica 20')

    # initialize edit dict
    edit = {'ID':ID_entry,
            'field':field,
            'new_value':value_entry}

    # initialize notification label
    notification = tk.Label(canvas,font='Helvetica 24',bg='#d5d5d5')

    # initialize edit button
    edit_button = tk.Button(canvas, text='Modificare', font='Helvetica 24',
        command=lambda:edit_record(db,edit))


    # place ID, field, and value labels
    ID_label.place(relx=.25,rely=0.15,relwidth=0.45,relheight=0.1,
        anchor='center')
    field_label.place(relx=0.25,rely=0.3,relwidth=0.45,relheight=0.1,
        anchor='center')
    value_label.place(relx=0.25,rely=0.45,relwidth=0.45,relheight=0.1,
        anchor='center')

    # place ID entry box, dropdown menu, and value entry box
    ID_entry.place(relx=0.75,rely=0.15,relwidth=0.45,relheight=0.1,
        anchor='center')
    dropdown_menu.place(relx=0.75,rely=0.3,relwidth=0.45,relheight=0.1,
        anchor='center')
    value_entry.place(relx=0.75,rely=0.45,relwidth=0.45,relheight=0.1,
        anchor='center')

    # place edit button
    edit_button.place(relx=0.5,rely=0.7,relwidth=0.2,relheight=0.1,
        anchor='center')

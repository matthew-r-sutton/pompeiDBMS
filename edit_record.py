def edit(db,page):
    import tkinter as tk
    import tkinter.ttk as ttk

    def create_interface(frame):
        ID_label = tk.Label(frame,text="ID to change: ",font="Helvetica 24",bg='#d5d5d5')
        ID_entry = tk.Entry(frame,font="Helvetica 24")
        dropdown_label = tk.Label(frame,text="Field to change: ",font="Helvetica 24",bg='#d5d5d5')
        value_label = tk.Label(frame,text="New field value: ",font="Helvetica 24",bg='#d5d5d5')
        value_entry = tk.Entry(frame,font="Helvetica 24")

        # create dropdown
        field = tk.StringVar(frame)
        field_choices = [
          'SESSO',
          'NOME',
          'EPOCA',
          'TIPO',
          'TAGLIA',
          'FORMA',
          'CHIUSURA',
          'MATERIALE',
          'COLORE_1',
          'COLORE_2',
          'ORNAMENTO',
          'STOCK_TOTALE',
          'IN_STOCK',
          'RIGA',
          'MENSOLA'
          ]
        field.set('SESSO')
        dropdown_menu = tk.OptionMenu(frame,field,*field_choices)
        dropdown_menu.config(font='Helvetica 20')
        menu = dropdown_menu.nametowidget(dropdown_menu.menuname)
        menu.config(font='Helvetica 20')

        # place dropdown menu
        ID_label.place(relx=.25,rely=0.15,relwidth=0.45,relheight=0.1,anchor='center')
        ID_entry.place(relx=0.75,rely=0.15,relwidth=0.45,relheight=0.1,anchor='center')
        dropdown_label.place(relx=0.25,rely=0.3,relwidth=0.45,relheight=0.1,anchor='center')
        dropdown_menu.place(relx=0.75,rely=0.3,relwidth=0.45,relheight=0.1,anchor='center')
        value_label.place(relx=0.25,rely=0.45,relwidth=0.45,relheight=0.1,anchor='center')
        value_entry.place(relx=0.75,rely=0.45,relwidth=0.45,relheight=0.1,anchor='center')

        # pack dict to return
        edit = {'ID':ID_entry,
                'field':field,
                'new_value':value_entry}
        return edit

    def edit_record():
        try:
            # assign vars
            field = edit['field'].get()
            new_value = edit['new_value'].get()
            ID = edit['ID'].get()

            # update the record
            cursor = db.cursor(buffered=True)
            query = """UPDATE pompei.scarpa SET """+field+""" = %s WHERE ID = %s;"""
            values = (new_value,int(ID))
            cursor.execute(query,values)
            db.commit()

            # print message confirming deletion
            edit_msg = tk.Label(frame,font='Helvetica 20',anchor="n")
            edit_msg['text'] = "Entry " + ID + " has been modified."
            edit_msg.place(relx=0.5,rely=0.9,relwidth=1,anchor='center')

        except:
            # print error message
            error_msg = tk.Label(frame,font='Helvetica 20',anchor="n")
            error_msg['text'] = "Please enter an ID."
            error_msg.place(relx=0.5,rely=0.9,relwidth=1,anchor='center')

    # create frame widgets
    canvas = tk.Canvas(page)
    frame = tk.Frame(canvas,bg='#d5d5d5')

    # create interface
    edit = create_interface(frame)

    # place canvas and pack frame
    canvas.place(relx=0, rely=0, relwidth=1,relheight=1)
    frame.pack(fill='both',expand=1)

    # create edit button widget
    edit_button = tk.Button(frame, text='Modificare', font='Helvetica 24')
    edit_button.place(relx=0.5,rely=0.7,relwidth=0.2,relheight=0.1,anchor='center')
    edit_button['command'] = edit_record

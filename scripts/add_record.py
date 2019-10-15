def add(db,canvas,field_names):
    import tkinter as tk

    # define function to set var to 0 if it is an empty string
    def check_int_var(var):
        return 0 if var == '' else var

    # define add button's command fuction to add an entry
    def add_entry(db,entries):

        # assign non-integer vars
        sesso = entries['SESSO'].get().upper()
        nome = entries['NOME'].get().upper()
        epoca = entries['EPOCA'].get().upper()
        tipo = entries['TIPO'].get().upper()
        forma = entries['FORMA'].get().upper()
        chiusura = entries['CHIUSURA'].get().upper()
        materiale = entries['MATERIALE'].get().upper()
        colore_1 = entries['COLORE_1'].get().upper()
        colore_2 = entries['COLORE_2'].get().upper()
        ornamento = entries['ORNAMENTO'].get().upper()

        # assign integer vars, setting to 0 if empty
        taglia = check_int_var(entries['TAGLIA'].get())
        stock_totale = check_int_var(entries['STOCK_TOTALE'].get())
        in_stock = check_int_var(entries['IN_STOCK'].get())
        fila = check_int_var(entries['FILA'].get())
        scaffale = check_int_var(entries['SCAFFALE'].get())

        # create add record to database
        cursor = db.cursor(buffered=True)
        query = """INSERT INTO pompei.scarpa
                (SESSO,NOME,EPOCA,TIPO,TAGLIA,FORMA,
                CHIUSURA,MATERIALE,COLORE_1,COLORE_2,ORNAMENTO,STOCK_TOTALE,
                IN_STOCK,FILA,SCAFFALE)
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        values = (sesso,nome,epoca,tipo,taglia,forma,chiusura,
            materiale,colore_1,colore_2,ornamento,stock_totale,in_stock,fila,
            scaffale)
        cursor.execute(query,values)
        db.commit()

        # initialize and place confirmation notification
        notification = tk.Label(canvas,bg='#d5d5d5',font='Helvetica 20',
            text='Entry has been added.')
        notification.place(relx=0.8,rely=0.935,relwidth=0.34,relheight=0.075,
            anchor='center')

    # initialize field and value labels
    field_label = tk.Label(canvas,text='Campo',font='Helvetica 20 bold',
        bg='#d5d5d5')
    value_label = tk.Label(canvas,text='Valore',font='Helvetica 20 bold',
        bg='#d5d5d5')

    # initialize empty dictionary to hold entries as keys
    entries = {}

    # initialize add button
    add_button = tk.Button(canvas, text='Inserisci', font='Helvetica 20',
        command=lambda:add_entry(db,entries))

    # place field and value labels
    field_label.place(relx=0.3,rely=0.0425,relwidth=0.5,relheight=0.075,
        anchor='center')
    value_label.place(relx=0.7,rely=0.0425,relwidth=0.5,relheight=0.075,
        anchor='center')

    # for each field create a label and entry box and append input values
    # dict, which is then appended to the entries list to be returned
    for field in field_names[1:]:
        y_pos = ((field_names.index(field) + 1 )* 0.05)

        # create and place field labels and entry boxes
        label = tk.Label(canvas, text=field, font='Helvetica 14',bg='#d5d5d5')
        entry = tk.Entry(canvas)
        label.place(relx=0.3,rely=y_pos,relwidth=0.5,relheight=0.05,
            anchor='center')
        entry.place(relx=0.7,rely=y_pos,relwidth=0.4,relheight=0.045,
            anchor='center')

        # append the entry to entries
        entries[label['text']] = entry

    # place add button
    add_button.place(relx=0.5,rely=0.935,relwidth=0.25,relheight=0.1,
        anchor='center')

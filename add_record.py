def add(db,page):
    import tkinter as tk
    import tkinter.ttk as ttk

    field_names = [
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

    def create_interface(frame,fields_list):
        # create and place column titles
        field_column_label = tk.Label(frame,text='Campo',font='Helvetica 20 bold',bg='#d5d5d5')
        value_column_label = tk.Label(frame,text='Valore',font='Helvetica 20 bold',bg='#d5d5d5')
        field_column_label.place(relx=0.3,rely=0.03,relwidth=0.5,relheight=0.075,anchor='center')
        value_column_label.place(relx=0.7,rely=0.03,relwidth=0.5,relheight=0.075,anchor='center')

        # initiate empty list to hold entries
        entries = []

        # for each field create a label and entry box and append input values
        # dict, which is then appended to the entries list to be returned
        for field in fields_list:
            y_pos = ((fields_list.index(field) + 1 )* 0.05) + 0.025

            # create and place field labels and entry boxes
            label = tk.Label(frame, text=field, font='Helvetica 14',bg='#d5d5d5')
            entry = tk.Entry(frame)
            label.place(relx=0.3,rely=y_pos,relwidth=0.5,relheight=0.05,anchor='center')
            entry.place(relx=0.7,rely=y_pos,relwidth=0.4,relheight=0.045,anchor='center')

            # pack field and the user's entry into a dict
            query_dict = {'field': field,
                          'value': entry}

            # append query_dict to entries
            entries.append(query_dict)
        return entries

    # add the entry to the db
    def add_entry():
        sesso, nome, epoca, tipo = '','','',''
        taglia, forma, chiusura, materiale = '','','',''
        colore_1, colore_2, ornamento = '','',''
        totale_azione, nel_azione, riga, mensola = '','','',''

        def assign_var(var,field):
            var = entry['value'].get() if (entry['field'] == field) else var
            return var

        def check_int_var(var):
            if var == '':
                var = 0
            return var

        for entry in entries:
            sesso = assign_var(sesso,'SESSO')
            nome = assign_var(nome, 'NOME')
            epoca = assign_var(epoca, 'EPOCA')
            tipo = assign_var(tipo, 'TIPO')
            taglia = assign_var(taglia, 'TAGLIA')
            forma = assign_var(forma, 'FORMA')
            chiusura = assign_var(chiusura, 'CHIUSURA')
            materiale = assign_var(materiale, 'MATERIALE')
            colore_1 = assign_var(colore_1, 'COLORE_1')
            colore_2 = assign_var(colore_2, 'COLORE_2')
            ornamento = assign_var(ornamento, 'ORNAMENTO')
            totale_azione = assign_var(totale_azione, 'TOTALE_AZIONE')
            in_stock = assign_var(nel_azione, 'NEL_AZIONE')
            riga = assign_var(riga, 'RIGA')
            mensola = assign_var(mensola, 'MENSOLA')

        taglia = check_int_var(taglia)
        stock_totale = check_int_var(totale_azione)
        in_stock = check_int_var(nel_azione)
        riga = check_int_var(riga)
        mensola = check_int_var(mensola)

        cursor = db.cursor(buffered=True)

        query = """INSERT INTO pompei.scarpa
                (SESSO,NOME,EPOCA,TIPO,TAGLIA,FORMA,
                CHIUSURA,MATERIALE,COLORE_1,COLORE_2,ORNAMENTO,STOCK_TOTALE,
                IN_STOCK,RIGA,MENSOLA)
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        values = (sesso,nome,epoca,tipo,taglia,forma,chiusura,materiale,colore_1,
                  colore_2,ornamento,stock_totale,in_stock,riga,mensola)
        cursor.execute(query,values)
        db.commit()

        # print message confirming addition
        add_msg = tk.Label(frame,font='Helvetica 20')
        add_msg['text'] = "Entry has been added."
        add_msg.place(relx=0.5,rely=0.95,relwidth=1,relheight=0.075,anchor='center')

    # create canvas and frame
    canvas = tk.Canvas(page)
    frame = tk.Frame(canvas,bg='#d5d5d5')

    # create interface
    entries = create_interface(frame,field_names)

    # place canvas and pack frame
    canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
    frame.pack(fill='both',expand=1)

    # create add button
    add_button = tk.Button(frame, text='INSERISCI', font='Helvetica 16 bold')
    add_button.place(relx=0.5,rely=0.86,relheight=0.1,relwidth=0.2,anchor='center')
    add_button['command'] = add_entry

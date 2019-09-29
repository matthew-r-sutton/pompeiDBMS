def add(passthrough_dict):
    import tkinter as tk
    import tkinter.ttk as ttk
    import mysql.connector as mysql
    import configparser

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

    def set_column_title(title,frame,x_pos):
        label = tk.Label(frame,text=title,borderwidth=1,font='Helvetica 20 bold')
        label.place(relx=x_pos,rely=0.025,relwidth=0.3,anchor='w')

    def generate_interface(frame,fields_list):
        set_column_title('Campo',top_frame,0.2)
        set_column_title('Valore',top_frame,0.5)

        entries = []

        for field in fields_list:
            y_pos = ((fields_list.index(field) + 1 )* 0.05) + 0.005
            # generate field labels
            row = (fields_list.index(field) + 1)

            # generate field labels and entry boxes
            label = tk.Label(frame, text=field, font='Helvetica 14', anchor='e')
            entry = tk.Entry(frame, width=45)

            label.place(relx=0.25,rely=y_pos,relwidth=0.2)
            entry.place(relx=0.5,rely=y_pos,relwidth=0.3)

            query_dict = {'field': field,
                          'value': entry}
            entries.append(query_dict)
        return entries

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
        add_msg = tk.Label(top_frame,font='Helvetica 20')
        add_msg['text'] = "Entry " + str(nome) + " has been added."
        add_msg.place(relx=0.25,rely=0.9,relwidth=0.5)

    # create top and bottom canvases with scrollbars
    top_canvas = tk.Canvas(page, height=200, width=400)
    top_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

    top_frame = tk.Frame(top_canvas)

    entries = generate_interface(top_frame,field_names)

    top_frame.pack(fill='both',expand=1)

    add_button = tk.Button(top_frame, text='Inserisci', font='Helvetica 16 bold')
    add_button.place(relx=0.4,rely=0.8,relheight=0.1,relwidth=0.2)

    add_button['command'] = add_entry

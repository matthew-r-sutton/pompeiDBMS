def add(passthrough_dict):
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

    field_names = [
      'SESSO',
      'NOME',
      'EPOCA',
      'TIPO',
      'TAGLIA',
      'FORMA',
      'CHIUSURA',
      'MATERIALE',
      'COLORA_1',
      'COLORA_2',
      'ORNAMENTO',
      'TOTALE_AZIONE',
      'NEL_AZIONE',
      'RIGA',
      'MENSOLA'
      ]

    # def setup_grid(cols,fields_list,frame):
    #     for column in cols:
    #         for row in range(0,(len(fields_list)-1)):
    #             label = tk.Label(frame,text=' ',borderwidth=1)
    #             label.grid(row=row,column=column)

    def set_column_title(title,frame,x_pos):
        label = tk.Label(frame,text=title,borderwidth=1,font='Helvetica 20 bold')
        label.place(relx=x_pos,rely=0)

    def generate_interface(frame,fields_list):
        set_column_title('Campo',top_frame,0.25)
        set_column_title('Valore',top_frame,0.5)

        entries = []

        for field in fields_list:
            y_pos = ((fields_list.index(field) + 1 )* 0.05) + 0.005
            # generate field labels
            row = (fields_list.index(field) + 1)

            # generate field labels and entry boxes
            label = tk.Label(frame, text=field, font='Helvetica 14')
            entry = tk.Entry(frame, width=45)

            label.place(relx=0.25,rely=y_pos)
            entry.place(relx=0.5,rely=y_pos)

            query_dict = {'field': field,
                          'value': entry}
            entries.append(query_dict)
        return entries

    def generate_results_table():
        add_table.add(entries,db)

    # create top and bottom canvases with scrollbars
    top_canvas = tk.Canvas(page, height=200, width=400)
    top_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

    top_frame = tk.Frame(top_canvas)

    entries = generate_interface(top_frame,field_names)

    top_frame.pack(fill='both',expand=1)

    add_button = tk.Button(top_frame, text='Inserisci', font='Helvetica 16')
    add_button.place(relx=0.45,rely=0.8)

    add_button['command'] = generate_results_table

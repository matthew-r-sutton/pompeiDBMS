def entry_search(passthrough_dict):
    import tkinter as tk
    import tkinter.ttk as ttk
    import mysql.connector as mysql
    import configparser
    import table

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
      'ORNAMENTO']

    def setup_grid(cols,fields_list,frame):
        for column in cols:
            for row in range(0,(len(fields_list)-1)):
                label = tk.Label(frame,text=' ',borderwidth=1)
                label.grid(row=row,column=column)

    def set_column_title(title,col,frame):
        label = tk.Label(frame,text=title,borderwidth=1,font='Helvetica 20 bold')
        label.grid(row=0,column=col,sticky='E')

    def generate_interface(frame,fields_list):
        setup_grid(range(0,40),fields_list,top_frame)
        set_column_title('Campo',2,top_frame)
        set_column_title('Operatore',8,top_frame)
        set_column_title('Domanda',14,top_frame)

        queries = []

        for field in fields_list:
            # generate field labels
            row = (fields_list.index(field) + 1)

            # generate operate dropdown menus
            operator = tk.StringVar(frame)
            operator_choices = {'in','non in'}
            operator.set('in')
            dropdown_menu = tk.OptionMenu(frame,operator,*operator_choices)
            dropdown_menu.config(font='Helvetica 12')
            menu = dropdown_menu.nametowidget(dropdown_menu.menuname)
            menu.config(font='Helvetica 12')

            # generate query fields
            query = tk.Entry(frame, width=45)

            tk.Label(frame, text=field, font='Helvetica 14').grid(
              row=row,column=2,stick='E')
            dropdown_menu.grid(row=row, column=8)
            query.grid(row=row, column=14, columnspan=20, stick='W')

            query_dict = {'name': field,
                          'operator': operator,
                          'query': query}
            queries.append(query_dict)
        return queries

    def on_configure(event):
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        top_canvas.configure(scrollregion=top_canvas.bbox('all'))

    def generate_results_table():
        table.create_table(queries_list,db)


    # create top and bottom canvases with scrollbars
    top_canvas = tk.Canvas(page)
    top_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

    top_scrollbar = tk.Scrollbar(top_canvas, command=top_canvas.yview)
    top_scrollbar.pack(side=tk.RIGHT, fill='y')

    top_canvas.configure(yscrollcommand=top_scrollbar.set)

    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    top_canvas.bind('<Configure>', on_configure)

    top_frame = tk.Frame(top_canvas)
    top_canvas.create_window((0,0), window=top_frame, anchor='nw')

    queries_list = generate_interface(top_frame,field_names)

    search_button = tk.Button(top_frame, text='RICERCA', font='Helvetica 16')
    search_button.grid(column=38,row=(len(field_names)))

    search_button['command'] = generate_results_table

    # search_message = tk.Label(bottom_canvas,
    #   text='premere RICERCA per mostrare i risultati', anchor='n',
    #   font='Helvetica 15 bold', bg='#d5d5d5'
    #   )
    # search_message.place(relx=0.25,rely=0.5)

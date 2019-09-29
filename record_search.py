def search(db,page):
    import tkinter as tk
    import tkinter.ttk as ttk
    import record_search_table

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
        operator_column_label = tk.Label(frame,text='Operatore',font='Helvetica 20 bold',bg='#d5d5d5')
        value_column_label = tk.Label(frame,text='Valore',font='Helvetica 20 bold',bg='#d5d5d5')
        field_column_label.place(relx=0.2,rely=0.03,relwidth=0.2,relheight=0.075,anchor='center')
        operator_column_label.place(relx=0.5,rely=0.03,relwidth=0.2,relheight=0.075,anchor='center')
        value_column_label.place(relx=0.8,rely=0.03,relwidth=0.2,relheight=0.075,anchor='center')

        queries = []

        for field in fields_list:
            # create field labels
            field_label = tk.Label(frame,text=field,font='Helvetica 14',bg='#d5d5d5')


            # create operate dropdown menus
            operator = tk.StringVar(frame)
            operator_choices = {'in','non in'}
            operator.set('in')
            dropdown_menu = tk.OptionMenu(frame,operator,*operator_choices)
            dropdown_menu.config(font='Helvetica 12')
            menu = dropdown_menu.nametowidget(dropdown_menu.menuname)
            menu.config(font='Helvetica 12')

            # create query fields
            query = tk.Entry(frame, width=45)

            # place field labels, operator dropdowns, and query entry boxes
            # according to list position
            y_pos = ((fields_list.index(field) + 1 )* 0.05) + 0.035
            field_label.place(relx=0.2,rely=y_pos,relwidth=0.2,relheight=0.05,anchor='center')
            dropdown_menu.place(relx=0.5,rely=y_pos,relwidth=0.2,relheight=0.045,anchor='center')
            query.place(relx=0.8,rely=y_pos,relwidth=0.25,relheight=0.045,anchor='center')

            query_dict = {'name': field,
                          'operator': operator,
                          'query': query}
            queries.append(query_dict)
        return queries

    def search():
        record_search_table.create_table(queries_list,db)

    # create top and bottom canvases with scrollbars
    canvas = tk.Canvas(page)
    frame = tk.Frame(canvas,bg='#d5d5d5')

    # place canvas and pack frame
    canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
    frame.pack(fill='both',expand=1)

    # create interface
    queries_list = create_interface(frame,field_names)

    # create search button
    search_button = tk.Button(frame, text='RICERCA', font='Helvetica 16 bold')
    search_button.place(relx=0.5,rely=0.9,relwidth=0.25,relheight=0.1,anchor='center')
    search_button['command'] = search

def search(db,canvas,field_names):
    import tkinter as tk
    import record_search_table

    def search(queries,db):
        record_search_table.create_table(queries,db)

    # initialize column titles
    field_label = tk.Label(canvas,text='Campo',font='Helvetica 20 bold',
        bg='#d5d5d5')
    operator_label = tk.Label(canvas,text='Operatore',font='Helvetica 20 bold',
        bg='#d5d5d5')
    value_label = tk.Label(canvas,text='Valore',font='Helvetica 20 bold',
        bg='#d5d5d5')

    # initialize the search button
    search_button = tk.Button(canvas, text='Ricerca', font='Helvetica 24',
        command=lambda:search(queries,db))

    # place column labels
    field_label.place(relx=0.2,rely=0.0425,relwidth=0.2,relheight=0.075,
        anchor='center')
    operator_label.place(relx=0.5,rely=0.0425,relwidth=0.2,relheight=0.075,
        anchor='center')
    value_label.place(relx=0.8,rely=0.0425,relwidth=0.2,relheight=0.075,
        anchor='center')

    # place the search button
    search_button.place(relx=0.5,rely=0.935,relwidth=0.25,relheight=0.1,
        anchor='center')

    # initialize the queries list, which will hold the dictionaries of each
    # value
    queries = []

    # create and place field labels, operators, and entry boxes
    for field in field_names:
        # create field labels
        field_label = tk.Label(canvas,text=field,font='Helvetica 14',
            bg='#d5d5d5')

        # create operator dropdown menus
        operator = tk.StringVar(canvas)
        operator_choices = {'in','non in'}
        operator.set('in')
        dropdown_menu = tk.OptionMenu(canvas,operator,*operator_choices)
        dropdown_menu.config(font='Helvetica 12')
        menu = dropdown_menu.nametowidget(dropdown_menu.menuname)
        menu.config(font='Helvetica 12')

        # create query fields
        query = tk.Entry(canvas, width=45)

        # place field labels, operator dropdowns, and query entry boxes
        # according to position in the list of field names
        y_pos = ((field_names.index(field) + 1 )* 0.05) + 0.0475
        field_label.place(relx=0.2,rely=y_pos,relwidth=0.2,relheight=0.05,
            anchor='center')
        dropdown_menu.place(relx=0.5,rely=y_pos,relwidth=0.2,relheight=0.045,
            anchor='center')
        query.place(relx=0.8,rely=y_pos,relwidth=0.25,relheight=0.045,
            anchor='center')

        # create a dictionary of the field, operator, and query, and append this
        # to the queries list
        query_dict = {'name': field,
                      'operator': operator,
                      'query': query}
        queries.append(query_dict)

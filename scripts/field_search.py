def search(db,canvas,field_names):
    import tkinter as tk
    import field_search_table

    # define search button command function
    def search(field,db):
        field_search_table.create_table(field,db)

    # initialize instruction label
    label = tk.Label(canvas,text="Campo di ricercare: ",font="Helvetica 24",
        bg='#d5d5d5')

    # initialize dropdown menu
    field = tk.StringVar(canvas)
    field.set('ID')
    dropdown_menu = tk.OptionMenu(canvas,field,*field_names)
    dropdown_menu.config(font='Helvetica 20')
    menu = dropdown_menu.nametowidget(dropdown_menu.menuname)
    menu.config(font='Helvetica 20')

    # create search button
    search_button = tk.Button(canvas, text='Ricerca', font='Helvetica 24',
        command=lambda:search(field,db))

    # place instruction label, dropdown menu, and search button
    label.place(relx=0.25,rely=0.4,relwidth=0.49,relheight=0.1,anchor='center')
    dropdown_menu.place(relx=0.75,rely=0.4,relwidth=0.45,relheight=0.1,
        anchor='center')
    search_button.place(relx=0.5,rely=0.7,relwidth=0.2,relheight=0.1,
        anchor='center')

def search(passthrough_dict):
    import tkinter as tk
    import tkinter.ttk as ttk
    import mysql.connector as mysql
    import configparser
    import field_table

    # read-in keys of passthrough_dict arg
    un = passthrough_dict['un']
    pw = passthrough_dict['pw']
    main = passthrough_dict['main']
    nb = passthrough_dict['nb']
    page = passthrough_dict['page']

    # print(un)
    # print(pw)
    # print(main)
    # print(canvas)
    # print(nb)
    # print(page)

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

    def generate_interface(frame):
        label = tk.Label(frame,text="Field to search: ",font="Helvetica 24")

        # generate dropdown
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
          'ORNAMENTO']
        field.set('SESSO')
        dropdown_menu = tk.OptionMenu(frame,field,*field_choices)
        dropdown_menu.config(font='Helvetica 20')
        menu = dropdown_menu.nametowidget(dropdown_menu.menuname)
        menu.config(font='Helvetica 20')

        # place dropdown menu
        label.place(relx=0,rely=0,relwidth=0.5,relheight=0.5)
        dropdown_menu.place(relx=0.5,rely=0,relwidth=0.5,relheight=0.5)
        return field

    def generate_results_table():
        field_table.create_table(field,db)

    # create frame widgets
    frame = tk.Frame(page)

    frame.pack(fill='both',expand=1)

    field = generate_interface(frame)

    search_button = tk.Button(frame, text='Ricerca', font='Helvetica 24')
    search_button.place(relx=0.5,rely=0.5,relwidth=0.5,relheight=0.5)

    search_button['command'] = generate_results_table

def edit(passthrough_dict):
    import tkinter as tk
    import tkinter.ttk as ttk
    import mysql.connector as mysql
    import configparser
    import edit_table

    # read-in keys of passthrough_dict arg
    un = passthrough_dict['un']
    pw = passthrough_dict['pw']
    main = passthrough_dict['main']
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

    def generate_interface(frame):
        label_1 = tk.Label(frame,text="ID to change: ",font="Helvetica 24")
        entry_1 = tk.Entry(frame,font="Helvetica 24")
        label_2 = tk.Label(frame,text="Field to change: ",font="Helvetica 24")
        label_3 = tk.Label(frame,text="New field value: ",font="Helvetica 24")
        entry_2 = tk.Entry(frame,font="Helvetica 24")

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
          'COLORA_1',
          'COLORA_2',
          'ORNAMENTO',
          'TOTALE_AZIONE',
          'NEL_AZIONE',
          'RIGA',
          'MENSOLA'
          ]
        field.set('SESSO')
        dropdown_menu = tk.OptionMenu(frame,field,*field_choices)
        dropdown_menu.config(font='Helvetica 20')
        menu = dropdown_menu.nametowidget(dropdown_menu.menuname)
        menu.config(font='Helvetica 20')

        # place dropdown menu
        label_1.place(relx=0,rely=0,relwidth=0.5,relheight=0.25)
        entry_1.place(relx=0.5,rely=0,relwidth=0.5,relheight=0.25)
        dropdown_menu.place(relx=0.5,rely=0.25,relwidth=0.5,relheight=0.25)
        label_2.place(relx=0,rely=0.25,relwidth=0.5,relheight=0.25)
        label_3.place(relx=0,rely=0.5,relwidth=0.5,relheight=0.25)
        entry_2.place(relx=0.5,rely=0.5,relwidth=0.5,relheight=0.25)

        # pack dict to return
        entry_dict = {'ID':entry_1,
                      'field':field,
                      'new_value':entry_2}
        return entry_dict

    def generate_results_table():
        edit_table.edit(entry_dict,db)

    # create frame widgets
    frame = tk.Frame(page)


    entry_dict = generate_interface(frame)

    frame.pack(fill='both',expand=1)

    search_button = tk.Button(frame, text='Modificare', font='Helvetica 24')
    search_button.place(relx=0.5,rely=0.75,relwidth=0.5,relheight=0.25)

    search_button['command'] = generate_results_table

def search(db,page):
    import tkinter as tk
    import tkinter.ttk as ttk
    import field_search_table

    def create_interface(frame):
        # create field to search label
        field_label = tk.Label(frame,text="Field to search: ",font="Helvetica 24",bg='#d5d5d5')

        # create dropdown
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
          'ORNAMENTO',
          'STOCK_TOTALE',
          'IN_STOCK',
          'RIGA',
          'MENSOLA'
          ]
        field.set('SESSO')
        dropdown_menu = tk.OptionMenu(frame,field,*field_choices)
        dropdown_menu.config(font='Helvetica 20')
        menu = dropdown_menu.nametowidget(dropdown_menu.menuname)
        menu.config(font='Helvetica 20')

        # place dropdown menu and field to search label
        field_label.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.1,anchor='center')
        dropdown_menu.place(relx=0.75,rely=0.3,relwidth=0.45,relheight=0.1,anchor='center')
        return field

    def search():
        field_search_table.create_table(field,db)

    # create canvas and Frame
    canvas = tk.Canvas(page)
    frame = tk.Frame(canvas,bg='#d5d5d5')

    # create the interface
    field = create_interface(frame)

    # place canvas and pack frame
    canvas.place(relx=0,rely=0,relwidth=1,relheight=1)
    frame.pack(fill='both',expand=1)

    # create search button
    search_button = tk.Button(frame, text='Ricerca', font='Helvetica 24')
    search_button.place(relx=0.5,rely=0.6,relwidth=0.2,relheight=0.1,anchor='center')
    search_button['command'] = search

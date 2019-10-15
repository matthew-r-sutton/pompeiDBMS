def dbms(db,field_names):
    import tkinter as tk
    import tkinter.ttk as ttk
    import record_search
    import field_search
    import edit_record
    import add_record
    import delete_record
    import upload_group

    # initialize the DBMS window
    main = tk.Tk()
    main.title('DBMS')
    window_width = main.winfo_reqwidth()
    window_height = main.winfo_reqheight()
    position_right = int(main.winfo_screenwidth()/4 - window_width/4)
    position_down = int(main.winfo_screenheight()/4 - window_height/4)
    main.geometry("+{}+{}".format(position_right,position_down))

    # initialize canvas to size the main window
    canvas = tk.Canvas(main,height=600,width=800)

    # initialize notebook object within main window
    nb = ttk.Notebook(main)

    #initialize pages/tabs/canvases 1 through 6
    page1 = ttk.Frame(nb)
    nb.add(page1, text='Ricerca database')
    canvas1 = tk.Canvas(page1,bg='#d5d5d5')

    page2 = ttk.Frame(nb)
    nb.add(page2, text='Ricerca valori dei campi')
    canvas2 = tk.Canvas(page2,bg='#d5d5d5')

    page3 = ttk.Frame(nb)
    nb.add(page3, text='Modifica dati')
    canvas3 = tk.Canvas(page3,bg='#d5d5d5')

    page4 = ttk.Frame(nb)
    nb.add(page4, text='*Adjunji* dati')
    canvas4 = tk.Canvas(page4,bg='#d5d5d5')

    page5 = ttk.Frame(nb)
    nb.add(page5, text='Elimina dati')
    canvas5 = tk.Canvas(page5,bg='#d5d5d5')

    page6 = ttk.Frame(nb)
    nb.add(page6,text='Transfirisci gruppo')
    canvas6 = tk.Canvas(page6,bg='#d5d5d5')

    # pack canvas within main window and place the notebook object
    canvas.pack()
    nb.place(relx=0, rely=0, relwidth=1, relheight=1)

    # pack canvases 1 through 6 and call subsequent functions to initialize tabs
    canvas1.pack(fill='both',expand=1)
    record_search.search(db,canvas1,field_names)

    canvas2.pack(fill='both',expand=1)
    field_search.search(db,canvas2,field_names)

    canvas3.pack(fill='both',expand=1)
    edit_record.edit(db,canvas3,field_names)

    canvas4.pack(fill='both',expand=1)
    add_record.add(db,canvas4,field_names)

    canvas5.pack(fill='both',expand=1)
    delete_record.delete(db,canvas5)

    canvas6.pack(fill='both',expand=1)
    upload_group.upload(db,canvas6)

    main.mainloop()

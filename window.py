def open_window(db):
    import tkinter as tk
    import tkinter.ttk as ttk
    import record_search
    import field_search
    import edit_record
    import add_record
    import delete_record

    main = tk.Tk()
    main.title('DBMS')

    window_width = main.winfo_reqwidth()
    window_height = main.winfo_reqheight()

    position_right = int(main.winfo_screenwidth()/4 - window_width/4)
    position_down = int(main.winfo_screenheight()/4 - window_height/4)

    main.geometry("+{}+{}".format(position_right,position_down))

    HEIGHT = 600
    WIDTH = 800

    canvas = tk.Canvas(main,height=HEIGHT,width=WIDTH)
    canvas.pack()

    nb = ttk.Notebook(main)
    nb.place(relx=0, rely=0, relwidth=1, relheight=1)

    page1 = ttk.Frame(nb)
    nb.add(page1, text='SEARCH DATABASE')

    page2 = ttk.Frame(nb)
    nb.add(page2, text='RETRIEVE FIELD VALUES')

    page3 = ttk.Frame(nb)
    nb.add(page3, text='EDIT A RECORD')

    page4 = ttk.Frame(nb)
    nb.add(page4, text='ADD A RECORD')

    page5 = ttk.Frame(nb)
    nb.add(page5, text='DELETE A RECORD')

    def tab_change(event):
        if nb.index("current") == 0:
            record_search.search(db,page1)

        elif nb.index("current") == 1:
            field_search.search(db,page2)

        elif nb.index("current") == 2:
            edit_record.edit(db,page3)

        elif nb.index('current') == 3:
            add_record.add(db,page4)

        elif nb.index('current') == 4:
            delete_record.delete(db,page5)

    nb.bind("<<NotebookTabChanged>>", tab_change)

    main.mainloop()

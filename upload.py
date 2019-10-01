def upload(db):
    import tkinter as tk
    from pandas import read_csv
    from numpy import nan

    def create_interface(frame):
        # create file upload label and entry box
        label = tk.Label(frame,text="File to upload: ",font="Helvetica 24",bg='#d5d5d5')
        entry = tk.Entry(frame,font="Helvetica 12")

        # place dropdown menu and field to search label
        label.place(relx=0.25,rely=0.4,relwidth=0.5,relheight=0.1,anchor='center')
        entry.place(relx=0.75,rely=0.4,relwidth=0.45,relheight=0.1,anchor='center')
        return entry

    def upload():
        try:
            path = entry.get().replace('\\','/')
            df = read_csv(path).replace(nan,'',regex=True)
            tuples = list(zip(*[df[c].values.tolist() for c in df]))
            for i in tuples:
                query = """INSERT INTO pompei.scarpa
                        (SESSO,NOME,EPOCA,TIPO,FORMA,CHIUSURA,MATERIALE,COLORE_1,
                        COLORE_2,ORNAMENTO,TAGLIA,STOCK_TOTALE,IN_STOCK,RIGA,MENSOLA)
                        VALUES
                        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
                cursor = db.cursor(buffered=True)
                cursor.execute(query,i)
                db.commit()
        except:
            error_msg = "Please check the file path and try again."
            error_label = tk.Label(frame,text=error_msg,font='Helvetica 18',bg='#d5d5d5')
            error_label.place(relx=0.5,rely=0.85,relwidth=0.8,relheight=0.1,anchor='center')

    # initialize and format main window
    main = tk.Tk()
    window_width = main.winfo_reqwidth()
    window_height = main.winfo_reqheight()
    position_right = int(main.winfo_screenwidth()/2.5 - window_width/2.5)
    position_down = int(main.winfo_screenheight()/2.5 - window_height/2.5)
    main.geometry("+{}+{}".format(position_right,position_down))
    main.title('ID Validation')

    # initialize canvas and frame
    HEIGHT = 400
    WIDTH = 600
    canvas = tk.Canvas(main,height=HEIGHT,width=WIDTH)
    frame = tk.Frame(canvas,bg='#d5d5d5')

    # pack canvas and place frame
    canvas.pack(fill='both',expand=1)
    frame.place(relheight=1,relwidth=1)

    # create the interface
    entry = create_interface(frame)

    # create search button
    upload_button = tk.Button(frame, text='Trasferire', font='Helvetica 24')
    upload_button.place(relx=0.5,rely=0.65,relwidth=0.25,relheight=0.1,anchor='center')
    upload_button['command'] = upload

    main.mainloop()

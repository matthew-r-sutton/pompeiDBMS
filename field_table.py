def create_table(field,db):
    import tkinter as tk
    from pandastable import Table
    import pandas as pd

    sql_query = 'SELECT DISTINCT ' + field.get() + ' SESSO FROM pompei.scarpa;'

    # read-in data
    df = pd.read_sql(sql_query,db)

    #format the table window
    main = tk.Tk()
    window_width = main.winfo_reqwidth()
    window_height = main.winfo_reqheight()

    position_right = int(main.winfo_screenwidth()/3 - window_width/3)
    position_down = int(main.winfo_screenheight()/3 - window_height/3)

    main.geometry("+{}+{}".format(position_right,position_down))
    main.title('Risultati di ricerca')
    frame = tk.Frame(main)

    #create table
    table = Table(frame, dataframe=df)
    table.show()

    #create the table window
    frame.pack(fill='both',expand=1)

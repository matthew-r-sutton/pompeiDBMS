def create_table(field,db):
    import tkinter as tk
    from pandastable import Table
    from pandas import read_sql

    # initialize SQL query
    query = """SELECT DISTINCT """ + field.get() + """ FROM pompei.scarpa;"""

    # read-in data as pandas dataframe
    df = read_sql(query,db)

    # initialize a window and table frame
    window = tk.Tk()
    table_frame = tk.Frame(window)

    # format table window
    window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()
    position_right = int(window.winfo_screenwidth()/3 - window_width/3)
    position_down = int(window.winfo_screenheight()/3 - window_height/3)
    window.geometry("+{}+{}".format(position_right,position_down))
    window.title('Risultati di ricerca')

    # initialize table
    table = Table(table_frame, dataframe=df)

    # pack the the table frame
    table_frame.pack(fill='both',expand=1)

    # display the table
    table.show()

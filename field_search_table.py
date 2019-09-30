def create_table(field,db):
    import tkinter as tk
    from pandastable import Table
    from pandas import read_sql

    # assign search_field var and structure query
    search_field = field.get()
    query = """SELECT DISTINCT """ + search_field + """ FROM pompei.scarpa;"""

    # read-in data
    df = read_sql(query,db)

    # create table window and table
    table_window = tk.Tk()
    table_frame = tk.Frame(table_window)

    # format table window
    window_width = table_window.winfo_reqwidth()
    window_height = table_window.winfo_reqheight()
    position_right = int(table_window.winfo_screenwidth()/3 - window_width/3)
    position_down = int(table_window.winfo_screenheight()/3 - window_height/3)
    table_window.geometry("+{}+{}".format(position_right,position_down))
    table_window.title('Risultati di ricerca')

    #create table
    table = Table(table_frame, dataframe=df)
    table.show()

    # pack the table frame with the table
    table_frame.pack(fill='both',expand=1)

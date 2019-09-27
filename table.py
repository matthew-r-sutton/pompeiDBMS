def create_table(query_dict_list,db):
    import tkinter as tk
    from pandastable import Table, TableModel
    import pandas as pd

    names = []
    operators = []
    queries = []

    for query in query_dict_list:
        names.append(query['name'])
        operators.append(query['operator'])
        queries.append(query['query'])

    print([for query in queries])    

    query = """SELECT * FROM pompei.scarpa;"""
    df = pd.read_sql(query,db)

    window = tk.Tk()
    window.geometry('600x400+200+100')
    window.title('Table app')
    f = tk.Frame(window)


    pt = Table(f, dataframe=df)
    pt.show()
    f.pack(fill='both',expand=1)

def create_table(queries_list,db):
    import tkinter as tk
    from pandastable import Table, TableModel
    import pandas as pd

    def create_query_tuple(query):
        queries = query.split(', ')
        string = "('"+str(queries[0])+"'"
        if len(queries) > 1:
            for i in queries[1:]:
                string = string + ", '" + i + "'"
        return string + ")"


    def append_sql_where_statement(where_statement,field,operator,query):
        query_tuple = create_query_tuple(query)
        operator = 'NOT IN' if (operator == 'non in') else operator
        if len(where_statement) < 1 :
            statement = (where_statement +
                         ' ' + str(field) +
                         ' ' + str(operator) +
                         ' ' + str(query_tuple)
                        )
        else:
            statement = (where_statement + ' AND'
                         ' ' + str(field) +
                         ' ' + str(operator) +
                         ' ' + str(query_tuple)
                        )
        return statement

    where_statement = ''


    if all(query['query'].get() == '' for query in queries_list) == True:
        sql_query = """SELECT * FROM pompei.scarpa;"""
    else:
        sql_query = 'SELECT * FROM pompei.scarpa WHERE'
        for query in queries_list:
            if query['query'].get() != '':
                where_statement = append_sql_where_statement(where_statement,
                                                             query['name'],
                                                             query['operator'].get(),
                                                             query['query'].get())
        sql_query = sql_query + where_statement + ';'

    # read-in data
    df = pd.read_sql(sql_query,db)

    # address when no results are returned
    if df.shape == (0, 17):
        #format the table window
        main = tk.Tk()
        # window.geometry('600x400+200+100')
        main.title('Errore')
        window_width = main.winfo_reqwidth()
        window_height = main.winfo_reqheight()

        position_right = int(main.winfo_screenwidth()/2 - window_width/2)
        position_down = int(main.winfo_screenheight()/2 - window_height/2)

        main.geometry("+{}+{}".format(position_right,position_down))

        error_msg = 'Errore di ricerca. Riprovare.'
        frame = tk.Frame(main)
        error_label = tk.Label(frame,text=error_msg,font='Helvetica 20 bold')
        error_label.pack()
        #create the table window
        frame.pack(fill='both',expand=1)
    else:
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

def create_table(queries_list,db):
    import tkinter as tk
    from pandastable import Table
    from pandas import read_sql

    def create_query_tuple(query):
        queries = query.split(', ')
        string = "('"+str(queries[0])+"'"
        if len(queries) > 1:
            for i in queries[1:]:
                string = string + ", '" + i + "'"
        string = string + ')'
        return


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
    df = read_sql(sql_query,db)

    # address when no results are returned
    if df.shape != (0, 16):
        # create table window and frame
        table_window = tk.Tk()
        table_frame = tk.Frame(table_window)

        # format the table window
        window_width = table_window.winfo_reqwidth()
        window_height = table_window.winfo_reqheight()
        position_right = int(table_window.winfo_screenwidth()/3 - window_width/3)
        position_down = int(table_window.winfo_screenheight()/3 - window_height/3)
        table_window.geometry("+{}+{}".format(position_right,position_down))
        table_window.title('Risultati di ricerca')

        #create table
        table = Table(table_frame, dataframe=df)
        table.show()

        #create the table window
        table_frame.pack(fill='both',expand=1)

    else:
        # create error window and error message
        error_window = tk.Tk()
        error_frame = tk.Frame(error_window,bg='#d5d5d5')
        error = 'Errore di ricerca. Please check that input values'
        error_2 = 'appear in the corresponding fields.'
        error_msg = tk.Label(error_frame,text=error,font='Helvetica 20 bold',bg='#d5d5d5')
        error_msg_2 = tk.Label(error_frame,text=error_2,font='Helvetica 20 bold',bg='#d5d5d5')

        # format error window
        window_width = error_window.winfo_reqwidth()
        window_height = error_window.winfo_reqheight()
        position_right = int(error_window.winfo_screenwidth()/2 - window_width/2)
        position_down = int(error_window.winfo_screenheight()/2 - window_height/2)
        error_window.geometry("+{}+{}".format(position_right,position_down))
        error_window.title('Errore')

        # pack the error frame and message
        error_frame.pack(fill='both',expand=1)
        error_msg.pack()
        error_msg_2.pack()

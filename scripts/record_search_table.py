def create_table(queries_list,db):
    import tkinter as tk
    from pandastable import Table
    from pandas import read_sql

    # define function to create tuple of queries
    def create_query_tuple(query):
        queries = query.split(', ')
        query_tuple = "('"+str(queries[0].upper())+"'"
        if len(queries) > 1:
            for val in queries[1:]:
                query_tuple = query_tuple + ", '" + val.upper() + "'"
        query_tuple = query_tuple + ')'
        return query_tuple

    # define function to append a query tuple to the SQL where statement
    def append_sql_where_statement(where_statement,field,operator,query):

        # call the creat_query_tuple function to create a tuple
        query_tuple = create_query_tuple(query)

        # convert Italian 'non in' to SQL 'NOT IN', else 'IN'
        operator = 'NOT IN' if (operator == 'non in') else 'IN'

        # if the field's query is the first being added to the statement, simply
        # build query as 'FIELD OPERATOR QUERY_TUPLE'
        # else separate the previous fields' queries by 'AND'
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

    # initialize the SQL where statement as an empty string
    where_statement = ''

    # if there are no specific queries, return the entire table
    # else return table where specific queries hold true
    if all(query['query'].get() == '' for query in queries_list) == True:
        sql_query = """SELECT * FROM pompei.scarpa;"""

    else:
        sql_query = 'SELECT * FROM pompei.scarpa WHERE'

        # create subset list consisting of filled queries
        filled_queries = [query for query in queries_list if query['query'].get(
            ) != '']

        # loop through list of filled queries and parse SQL where statement
        for query in filled_queries:
            where_statement = append_sql_where_statement(where_statement,
                query['name'],query['operator'].get(),query['query'].get())
        sql_query = sql_query + where_statement + ';'

    # read-in data returned by SQL query as a pandas dataframe
    df = read_sql(sql_query,db)

    # address when no results are returned
    if df.shape != (0, 16):
        # initialize table window and frame
        table_window = tk.Tk()
        table_frame = tk.Frame(table_window)

        # format the table window
        window_width = table_window.winfo_reqwidth()
        window_height = table_window.winfo_reqheight()
        position_right = int(table_window.winfo_screenwidth()/3 -
            window_width/3)
        position_down = int(table_window.winfo_screenheight()/3 -
            window_height/3)
        table_window.geometry("+{}+{}".format(position_right,position_down))
        table_window.title('Risultati di ricerca')

        # initialize the table
        table = Table(table_frame, dataframe=df)

        # packe the frame in the window and display the table
        table_frame.pack(fill='both',expand=1)
        table.show()

    else:
        # create error window and error message
        error_window = tk.Tk()
        error_frame = tk.Frame(error_window,bg='#d5d5d5')
        error = 'Search error: Please check that input values'
        error_2 = 'appear in the corresponding fields.'
        error_msg = tk.Label(error_frame,text=error,font='Helvetica 20 bold',
            bg='#d5d5d5')
        error_msg_2 = tk.Label(error_frame,text=error_2,
            font='Helvetica 20 bold',bg='#d5d5d5')

        # format error window
        window_width = error_window.winfo_reqwidth()
        window_height = error_window.winfo_reqheight()
        position_right = int(error_window.winfo_screenwidth()/3 -
            window_width/2)
        position_down = int(error_window.winfo_screenheight()/2 -
            window_height/2)
        error_window.geometry("+{}+{}".format(position_right,position_down))
        error_window.title('Search error')

        # pack the error frame and message
        error_frame.pack(fill='both',expand=1)
        error_msg.pack()
        error_msg_2.pack()

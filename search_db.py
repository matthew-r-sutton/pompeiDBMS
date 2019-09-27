def search():
    import mysql.connector as mysql
    import configparser
    import pandas as pd

    # read-in data need for sql connection
    config = configparser.ConfigParser()
    config.read('./config.ini')

    db = mysql.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        passwd=config['mysql']['pass'],
        database="test_2"
    )

    cursor = db.cursor(buffered=True)
    cursor2 = db.cursor(buffered=True)

    # get SQL column names
    cursor.execute("""SELECT * FROM pompei_scalpa;""")
    column_names = [str(i[0]) for i in cursor.description]

    # create a list of query fields and matches
    query_list = []
    for name in column_names:
        query = input("Which " + str(name) + " are you searching for?\n")
        if query != '':
            query_list.append([name, query])

    # automate creation of the sql where statement as a string
    where_queries = ""
    for query in query_list:
        where_queries = where_queries + query[0] + " = '" + query[1] + "'"
        if query_list.index(query) < len(query_list) - 1:
            where_queries = where_queries + " AND "

    # display the selected records
    if len(query_list) != 0:
        sql_query = """SELECT * FROM pompei_scalpa WHERE """ + where_queries + """;"""
    else:
        sql_query = """SELECT * FROM pompei_scalpa;"""
    data = pd.read_sql_query(sql_query, db)
    df = pd.DataFrame(data, columns=column_names)
    print(df)

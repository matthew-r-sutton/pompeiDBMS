def fields(un, pw):
    import mysql.connector as mysql
    import configparser

    # read-in data need for sql connection
    config = configparser.ConfigParser()
    config.read('./config.ini')

    db = mysql.connect(
        host=config['mysql']['host'],
        user=un,
        passwd=pw,
        database="test_2"
    )

    cursor = db.cursor(buffered=True)
    cursor2 = db.cursor(buffered=True)

    # get SQL column names
    cursor.execute("""SELECT * FROM pompei_scalpa;""")
    column_names = [str(i[0]) for i in cursor.description]
    return column_names

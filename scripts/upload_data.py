def upload(db,file,notification):
    from pandas import read_csv
    from numpy import nan

    # try to commit the input file's record to the db
    # except show error message if the input file cannot be found
    try:
        # convert the file entry box's contents to a string and flip slashes,
        # while catching if the file was input as a string
        path = file.get().replace('\\','/')
        path = path[1:-1] if (path[0] == '"' and path[-1] =='"') else path

        # read input file as a csv, replacing missing values with empty strings
        df = read_csv(path).replace(nan,'',regex=True)

        # pack the records as a list of tuples, where each tuple is a record
        records = list(zip(*[df[c].values.tolist() for c in df]))

        # commit each record to the DB, one-by-one
        for record in records:
            query = """INSERT INTO pompei.scarpa
                    (SESSO,
                    NOME,
                    EPOCA,
                    TIPO,
                    FORMA,
                    CHIUSURA,
                    MATERIALE,
                    COLORE_1,
                    COLORE_2,
                    ORNAMENTO,
                    TAGLIA,
                    STOCK_TOTALE,
                    IN_STOCK,
                    FILA,
                    SCAFFALE)
                    VALUES
                    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
            cursor = db.cursor(buffered=True)
            cursor.execute(query,record)
            db.commit()

        # set the notification to confirmation message
        notification['text'] = "Your records have been transferred"
        notification.place(relx=0.5,rely=0.9,relwidth=0.9,anchor='center')
        
    except FileNotFoundError:
        #set the notification to error message
        notification['text'] = "Please check the file path and try again."
        notification.place(relx=0.5,rely=0.9,relwidth=0.9,anchor='center')

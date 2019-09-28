def add(entry_dict,db):
    import tkinter as tk
    from pandastable import Table
    import pandas as pd

    sesso, nome, epoca, tipo = '','','',''
    taglia, forma, chiusura, materiale = '','','',''
    colora_1, colora_2, ornamento = '','',''
    totale_azione, nel_azione, riga, mensola = '','','',''


    def assign_var(var,field):
        var = entry['value'].get() if (entry['field'] == field) else var
        return var

    def check_var(var):
        if var == '':
            var = 0
        return var

    for entry in entry_dict:
        sesso = assign_var(sesso,'SESSO')
        nome = assign_var(nome, 'NOME')
        epoca = assign_var(epoca, 'EPOCA')
        tipo = assign_var(tipo, 'TIPO')
        taglia = assign_var(taglia, 'TAGLIA')
        forma = assign_var(forma, 'FORMA')
        chiusura = assign_var(chiusura, 'CHIUSURA')
        materiale = assign_var(materiale, 'MATERIALE')
        colora_1 = assign_var(colora_1, 'COLORA_1')
        colora_2 = assign_var(colora_2, 'COLORA_2')
        ornamento = assign_var(ornamento, 'ORNAMENTO')
        totale_azione = assign_var(totale_azione, 'TOTALE_AZIONE')
        nel_azione = assign_var(nel_azione, 'NEL_AZIONE')
        riga = assign_var(riga, 'RIGA')
        mensola = assign_var(mensola, 'MENSOLA')

    taglia = check_var(taglia)
    totale_azione = check_var(totale_azione)
    nel_azione = check_var(nel_azione)
    riga = check_var(riga)
    mensola = check_var(mensola)

    cursor = db.cursor(buffered=True)

    query = """INSERT INTO pompei.scarpa
            (SESSO,NOME,EPOCA,TIPO,TAGLIA,FORMA,
            CHIUSURA,MATERIALE,COLORA_1,COLORA_2,ORNAMENTO,TOTALE_AZIONE,
            NEL_AZIONE,RIGA,MENSOLA)
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    values = (sesso,nome,epoca,tipo,taglia,forma,chiusura,materiale,colora_1,
              colora_2,ornamento,totale_azione,nel_azione,riga,mensola)
    cursor.execute(query,values)
    db.commit()

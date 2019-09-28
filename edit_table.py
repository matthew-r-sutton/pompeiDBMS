def edit(entry_dict,db):
    import tkinter as tk
    from pandastable import Table
    import pandas as pd

    field = entry_dict['field'].get()
    new_value = entry_dict['new_value'].get()
    ID = entry_dict['ID'].get()

    cursor = db.cursor(buffered=True)

    query = """UPDATE pompei.scarpa SET """+field+""" = '"""+new_value+"""'
            WHERE ID = '"""+ID+"""';"""

    cursor.execute(query)
    db.commit()

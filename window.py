#def open_window(un, pw):
import tkinter as tk
import tkinter.ttk as ttk
import entry_search
import field_search
import entry_edit
import add_entry
import delete_entry

#print(un,pw)
un = "root"
pw = "Victoria170296!"

main = tk.Tk()
main.title('')

window_width = main.winfo_reqwidth()
window_height = main.winfo_reqheight()

position_right = int(main.winfo_screenwidth()/4 - window_width/4)
position_down = int(main.winfo_screenheight()/4 - window_height/4)

main.geometry("+{}+{}".format(position_right,position_down))

HEIGHT = 600
WIDTH = 800

canvas = tk.Canvas(main,height=HEIGHT,width=WIDTH)
canvas.pack()

nb = ttk.Notebook(main)
nb.place(relx=0, rely=0, relwidth=1, relheight=1)

page1 = ttk.Frame(nb)
nb.add(page1, text='SEARCH DATABASE')

page2 = ttk.Frame(nb)
nb.add(page2, text='RETRIEVE FIELD VALUES')

page3 = ttk.Frame(nb)
nb.add(page3, text='EDIT A RECORD')

page4 = ttk.Frame(nb)
nb.add(page4, text='ADD A RECORD')

page5 = ttk.Frame(nb)
nb.add(page5, text='DELETE A RECORD')

def tab_change(event):
    if nb.index("current") == 0:
        passthrough_dict = {
            'un':un,
            'pw':pw,
            'main':main,
            'canvas':canvas,
            'nb':nb,
            'page':page1
        }
        entry_search.search(passthrough_dict)

    elif nb.index("current") == 1:
        passthrough_dict = {
            'un':un,
            'pw':pw,
            'main':main,
            'canvas':canvas,
            'nb':nb,
            'page':page2
        }
        field_search.search(passthrough_dict)

    elif nb.index("current") == 2:
        passthrough_dict = {
            'un':un,
            'pw':pw,
            'main':main,
            'canvas':canvas,
            'nb':nb,
            'page':page3
        }
        entry_edit.edit(passthrough_dict)

    elif nb.index('current') == 3:
        passthrough_dict = {
            'un':un,
            'pw':pw,
            'main':main,
            'canvas':canvas,
            'nb':nb,
            'page':page4
        }
        add_entry.add(passthrough_dict)

    elif nb.index('current') == 4:
        passthrough_dict = {
            'un':un,
            'pw':pw,
            'main':main,
            'canvas':canvas,
            'nb':nb,
            'page':page5
        }
        delete_entry.delete(passthrough_dict)

nb.bind("<<NotebookTabChanged>>", tab_change)

main.mainloop()

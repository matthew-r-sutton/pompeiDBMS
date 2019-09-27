import tkinter as tk
import tkinter.ttk as ttk

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    top_canvas.configure(scrollregion=top_canvas.bbox('all'))
    bottom_canvas.configure(scrollregion=bottom_canvas.bbox('all'))

main = tk.Tk()

HEIGHT = 700
WIDTH = 800

canvas = tk.Canvas(main, height=HEIGHT, width=WIDTH)
canvas.pack()

nb = ttk.Notebook(main)
nb.place(relx=0, rely=0, relwidth=1, relheight=1)

page1 = ttk.Frame(nb)
nb.add(page1, text='SEARCH DATABASE')

# --- create canvas with scrollbar ---

top_canvas = tk.Canvas(page1, bg='red')
top_canvas.place(relx=0, rely=0, relwidth=1, relheight=0.5)
bottom_canvas = tk.Canvas(page1, bg='blue')
bottom_canvas.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

top_scrollbar = tk.Scrollbar(top_canvas, command=top_canvas.yview)
top_scrollbar.pack(side=tk.RIGHT, fill='y')
bottom_scrollbar = tk.Scrollbar(bottom_canvas, command=bottom_canvas.yview)
bottom_scrollbar.pack(side=tk.RIGHT, fill='y')

top_canvas.configure(yscrollcommand=top_scrollbar.set)
bottom_canvas.configure(yscrollcommand=bottom_scrollbar.set)
#
# # update scrollregion after starting 'mainloop'
# # when all widgets are in canvas
top_canvas.bind('<Configure>', on_configure)
bottom_canvas.bind('<Configure>', on_configure)

# # --- put top_frame in canvas ---
#
top_frame = tk.Frame(top_canvas)
top_frame.place(relx=0, rely=0, relwidth=1, relheight=0.5)
top_canvas.create_window((0,0), window=top_frame, anchor='nw')

bottom_frame = tk.Frame(bottom_canvas)
bottom_frame.place(relx=0,rely=0,relwidth=1,relheight=0.5)
bottom_canvas.create_window((0,0), window=bottom_frame, anchor='nw')
#
# # --- add widgets in top_frame ---
#
l = tk.Label(top_frame, text="Hello", font="-size 50")
l.pack()

l = tk.Label(top_frame, text="World", font="-size 50")
l.pack()

l = tk.Label(top_frame, text="Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font="-size 20")
l.pack()






#
# # update scrollregion after starting 'mainloop'
# # when all widgets are in canvas


# # --- put bottom_frame in canvas ---
#

#
# # --- add widgets in bottom_frame ---
#
l = tk.Label(bottom_frame, text="Hello", font="-size 50")
l.pack()

l = tk.Label(bottom_frame, text="World", font="-size 50")
l.pack()

l = tk.Label(bottom_frame, text="Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font="-size 20")
l.pack()

# --- start program ---

main.mainloop()

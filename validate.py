def validate():
    import tkinter as tk
    import mysql.connector as mysql
    import configparser
    import window

    HEIGHT = 200
    WIDTH = 400

    main = tk.Tk()
    main.title('ID Validation')

    canvas = tk.Canvas(main, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(main)
    frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.3, anchor='n')

    lower_frame = tk.Frame(main)
    lower_frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.3, anchor='n')

    e1 = tk.Entry(frame)
    e1.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.25)
    e1_label = tk.Label(frame)
    e1_label.place(relx=0.05, rely=0.2, relwidth=0.2, relheight=0.25)
    e1_label['text'] = "Username : "

    e2 = tk.Entry(frame)
    e2.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.25)
    e2_label = tk.Label(frame)
    e2_label.place(relx=0.05, rely=0.5, relwidth=0.2, relheight=0.25)
    e2_label['text'] = "Password : "

    button = tk.Button(main, command=lambda:check(e1.get(),e2.get()))
    button.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.1, anchor='n')
    button['text'] = "Validate"

    warning = tk.Label(lower_frame)
    warning.place(relwidth=1, relheight=1)

    def check(un,pw):
        config = configparser.ConfigParser()
        config.read('./config.ini')
        try:
            db = mysql.connect(
                host=config['mysql']['host'],
                user=un,
                passwd=pw,
                database="pompei"
            )
            main.destroy()
            window.open_window(un,pw)
        except:
            warning['text'] = "Please check your username and password and try again"

    main.mainloop()

import string, random, shelve
from tkinter import *

def play_game():
    global counter, var_60sec, wpm, typos
    win = Tk()
    l1 = Label(win, bg='Gray15').grid(row=0, column=0)
    l2 = Label(win, bg='Gray15').grid(row=1, column=1)
    l3 = Label(win, bg='Gray15').grid(row=2, column=2)
    l4 = Label(win, bg='Gray15').grid(row=3, column=3)
    l5 = Label(win, bg='Gray15').grid(row=4, column=4)
    l6 = Label(win, bg='Gray15').grid(row=5)
    l7 = Label(win, bg='Gray15').grid(row=6)

    Display_letters = string.ascii_letters
    char = "ABCDEF"  # here you can put any other char that you want to appear. # up to 6 chars!
    Display_characters = Display_letters + char
    rand_display_char = Display_characters
    count = 0
    COLUMN = 100
    ROW = 5
    bg = Label(win, text='\t\t\t\t\t\t\t\t\t\t\t', bg='red').place(x=30, y=100, height=75, width=830)
    full_text_1 = []
    full_text_2 = []
    full_text_3 = []
    for r_d_c in rand_display_char:
        displayed_char = random.choices(rand_display_char)
        displayed_char1 = random.choices(rand_display_char)
        displayed_char2 = random.choices(rand_display_char)
        COLUMN += 1
        window_displayed_letters1 = Label(win, text=displayed_char, bg='red').grid(row=ROW, column=COLUMN)
        window_displayed_letters2 = Label(win, text=displayed_char1, bg='red').grid(row=ROW+1, column=COLUMN)
        window_displayed_letters3 = Label(win, text=displayed_char2, bg='red').grid(row=ROW+2, column=COLUMN)
        full_text_1 += displayed_char
        full_text_2 += displayed_char1
        full_text_3 += displayed_char2
    full_text_1.extend(full_text_2)
    full_text_1.extend(full_text_3)
    full_text = full_text_1

    type_output = StringVar()
    type = Entry(win, textvariable=type_output, fg='Red', font = ('Helvetica', 20))
    how_to_start = Label(win, fg='Red', bg='Gray15', text='Press the start button to start.', font = ('Helvetica', 20)).place(x=100, y=400, width=700, height=100)
    var_60sec = 0

    def start():
        global how_to_start
        time_ = Label(win, fg='red', bg='Gray15')
        time_.place(x=860, y=20, width=13)
        type_counter(time_, var_60sec)
        how_to_start = Label(win, bg='Gray15').place(x=100, y=400, width=700, height=100)
        type.place(x=100, y=500, width=700)

    start_button = Button(win, text='Start', bg='Green', command=start).place(x=0, y=0, width=50)
    wpm = 0
    counter = 0
    typos = 0

    def load_database():
        global wpm_record
        rec = shelve.open('wpm_record1-shelve')
        wpm_record = rec['record']
        rec.close()

    load_database()

    def type_counter(time_, var_60sec):
        counter = 0
        def count():
            global counter, var_60sec, wpm, typos, char_left, wpm_record
            counter += 1
            time_.config(text=str(counter))
            time_.after(1000,count)
            var_60sec += 1
            if var_60sec == 60:
                GameEnd = Tk()
                GameEnd.geometry('400x400')
                GameEnd.title('Good Game!')
                GameEnd.minsize(400, 400)
                GameEnd.maxsize(400, 400)
                GameEnd.config(bg='Gray15')
                def check_enties():
                    global wpm, typos, char_left, wpm_record
                    Entried = type_output.get()
                    list_of_entries = list(Entried)
                    for index in range(1000):
                        try:
                            if full_text[index] == list_of_entries[index]:
                                wpm += 1
                            else:
                                typos += 1
                        except:
                            pass
                    all_char_type = wpm + typos
                    char_left = len(full_text) - all_char_type

                check_enties()
                if char_left <= 30 and typos < 20:
                    gg = Tk()
                    gg.title('You Won')
                    stats = Label(gg, text='U r god lel!', fg='red', bg='Gray13', font= ('Helvetica', 60)).pack()
                    gg.config(bg='Gray15')
                    gg.geometry('400x400')
                    M = 400
                    gg.minsize(M, M)
                    gg.maxsize(M, M)
                    gg.mainloop()

                if wpm > wpm_record:
                    wpm_record = wpm
                    rec = shelve.open('wpm_record1-shelve')
                    rec['record'] = wpm_record
                    rec.close()
                Stats = Label(GameEnd, text=f'Stats:\nWPM: {wpm}\nTypos: {typos}\nCharacters left: {char_left}/174\nRecord: {wpm_record}', bg='white', fg='red', font=500).place(x=50, y=100, width=300, height=200)


                GameEnd.mainloop()
        count()

    TIME = Label(win, text='Time:', fg='red', bg='Gray15').place(x=850, y=0, width=50)
    broken_timer = Label(win, text='0.00', fg='red', bg='Gray15').place(x=860, y=20, width=30)

    def restart_game():
        win.destroy()
        play_game()

    restart_game = Button(win, text='Restart', bg='Red', command=restart_game).place(x=50, y=0, width=50)

    def restart_record():
        rec = shelve.open('wpm_record1-shelve')
        rec['record'] = 0
        rec.close()

    restart_record = Button(win, text='Restart Record', bg='Cyan4', command=restart_record).place(x=100, y=0, width=100)

    win.geometry('900x750')
    win.title('Typing App')
    win.minsize(900, 750)
    win.maxsize(900, 750)
    win.configure(bg='Gray15')


    win.mainloop()

play_game()
from tkinter import *; import keyboard; import mouse; import time; import threading
# Основные настройки экрана программы, размер название и т.д.

tk = Tk(className='Автокликер')
tk.configure(height=226, width=419, bg='#4E4D4D')
tk.resizable(width=False, height=False)


#часть с функциями

#запись переменных1
start = 0
end = 0
speed = 0
click_button = 0

# функции для выбора кнопки мыши, правая или левая. Если пользователь решил автоматически печатать букву то решение этому будет находиться в функции check_for_start_button()
def Rmb():
    global click_button
    click_button = "right"

def Lmb():
    global click_button
    click_button = "left"

# функция если пользователь захотел перенастроить приложение
def disaple():
   global speed
   speed = 0
   Main_disaple_button.place_forget()
   MAIN_button.place(x = 276, y = 152)

# главная функция в которой идёт запись всех переменный, активируется по кнопке "подтвердить"
def check_for_start_button():
    #глобализация переменных по коду
    global click_button; global end; global start; global speed; global Main_disaple_button

    #запись переменных
    Entry_start.delete('1','end');Entry_Auto_button.delete('1','end');Entry_end.delete('1','end')
    MAIN_button.place_forget()
    start = Entry_start.get(); speed = Entry_speed.get(); end = Entry_end.get()
    #блок с проверками 1
    if start == '': start = "1"
    if end == '': end = "2"
    #кнопка заместо кнопки подтвердить
    Main_disaple_button = Button(justify='center',font=('Comic Neue', 8),text=f'Перенастроить\n({start}) ({end})',width=20,height=4, command=disaple)
    Main_disaple_button.place(x = 276, y = 152)

    #блок с проверками 2
    if Entry_Auto_button.get() != "":
        click_button = Entry_Auto_button.get()
    try:speed = int(speed)
    except:speed = 1
    if click_button == 0: click_button = "left"
    #начало процесса кликов

# функция в которой и происходит процесс кликов
def clicker():
  #блок для кнопки старта
  while True:
   time.sleep(0.1)
   if keyboard.is_pressed(start):
    time.sleep(0.3)
    #блок с самими кликами
    # если пользователь выбрал печатать букву
    if len(click_button) == 1:
        while True:
            # откровенный костыль который я использовал, чтобы автокликер не работал во время перенастройки
            try:
               time.sleep(1/speed)
            except:
               break
            # проверка
            keyboard.send(click_button)                                                                     
            if keyboard.is_pressed(end):
                time.sleep(1)
                break
    # если пользователь выбрал нажимать мышью
    else:
        while True:
            # откровенный костыль который я использовал, чтобы автокликер не работал во время перенастройки
            try:
               time.sleep(1/speed)
            except:
               break
            # проверка
            mouse.click(click_button)
            if keyboard.is_pressed(end):
                time.sleep(1)
                break

main_clicker = threading.Thread(target=clicker)
main_clicker.start()


# Основное наполнение программы, кнопки, текста, заголовки и т.д
  
Title = Label(text='Автокликер',bg='#4E4D4D',fg='#ffffff',font=('Comic Neue', 24)); Title.place(x=126,y=14)
Entry_start = Entry(font=('Comic Neue', 16),width=2,justify='center'); Entry_start.place(x=12,y=61); Label_start = Label(text='Введите кнопку старта',bg='#4E4D4D',fg='#ffffff',font=('Comic Neue', 12)); Label_start.place(x = 40, y = 63)
Entry_end = Entry(font=('Comic Neue', 16),width=2,justify='center'); Entry_end.place(x=12,y=101); Label_start = Label(text='Введите кнопку остановки',bg='#4E4D4D',fg='#ffffff',font=('Comic Neue', 12)); Label_start.place(x = 40, y = 103)
Entry_speed = Entry(font=('Comic Neue', 16),width=2,justify='center'); Entry_speed.place(x=12,y=141); Label_start = Label(text='Введите скорость (кпс)',bg='#4E4D4D',fg='#ffffff',font=('Comic Neue', 12)); Label_start.place(x = 40, y = 143)
#Часть с кнопками
Entry_Auto_button = Entry(font=('Comic Neue', 16),width=2,justify='center'); Entry_Auto_button.place(x=12,y=181); Label_start = Label(text='Автоматически \nнажимающаяся кнопка',bg='#4E4D4D',fg='#ffffff',font=('Comic Neue', 12)); Label_start.place(x = 43, y = 174)
Rmb_button = Button(justify='center',font=('Comic Neue', 8),text='Пкм',width=5,height=1, command = Rmb);Rmb_button.place(x = 225, y = 167)
Lmb_button = Button(justify='center',font=('Comic Neue', 8),text='Лкм',width=5,height=1, command = Lmb);Lmb_button.place(x = 225, y = 197)
MAIN_button = Button(justify='center',font=('Comic Neue', 8),text='Запустить',width=20,height=4, command=check_for_start_button);MAIN_button.place(x = 276, y = 152)

# Функция благодаря которой эта программа работает

tk.mainloop()
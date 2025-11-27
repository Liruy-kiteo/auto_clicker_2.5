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
start_f = 0
end_f = 0

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
   Main_disable_button.place_forget()
   MAIN_button.place(x = 276, y = 152)

# главная функция в которой идёт запись всех переменный, активируется по кнопке "подтвердить"
def check_for_start_button():
    #глобализация переменных по коду
    global click_button; global end; global start; global speed; global Main_disable_button

    #запись переменных
    Entry_start.delete('1','end');Entry_Auto_button.delete('1','end');Entry_end.delete('1','end')
    MAIN_button.place_forget()
    start = Entry_start.get(); speed = Entry_speed.get(); end = Entry_end.get()
    #блок с проверками 1
    if start == '': start = "1"
    if end == '': end = "2"
    #кнопка заместо кнопки подтвердить

    #блок с проверками 2
    if Entry_Auto_button.get() != "":
        click_button = Entry_Auto_button.get()
    try:speed = int(speed)
    except:speed = 1
    if click_button == 0: click_button = "left"
    #изменение кнопки
    Main_disable_button = Button(justify='center',font=('Comic Neue', 8),text=f'Перенастроить\n(start={start}) (end={end}) (cps={speed})\n(кнопка={click_button}))',width=20,height=4, command=disaple)
    Main_disable_button.place(x = 276, y = 152)
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

#изменение текста в приложение
def function_start():
   Label_function.configure(text='кнопка (l)-запись, \nкнопка (k)-остановка записи.\n Убедитесь, что вы ввели \nкнопку старта и остановки'); Label_function.place(x = 210, y = 10)
   function_button_1.place_forget(); function_button_1.configure(command=change_function_text)
   #будет выдавать ошибку, пока не знаю как это исправить
   function.start()

#прослушка мыши
def listen_mouse():
    global end_f; global start_f;global Buttons

    #запись переменных
    Entry_start.delete('1','end');Entry_end.delete('1','end')
    MAIN_button.place_forget()
    start_f = Entry_start.get();end_f = Entry_end.get()
    #блок с проверками 
    if start_f == '': start_f = "1"
    if end_f == '': end_f = "2"
    #запись мыши
    global Buttons
    keyboard.wait('l')
    Buttons = []
    mouse.hook(Buttons.append)
    keyboard.wait('k')
    mouse.unhook(Buttons.append)
    function_button_1.place(x = 273, y = 90)

#2 изменение текста
def change_function_text():
   Label_function.configure(text=f'Функция в данный \nмомент включена,\n старт на {start_f}\n остановка на {end_f}\n(остановка \nработает только в \nконце \nкаждого повторение)'); Label_function.place(x=255)
   function_button_1.configure(text = 'Перенастроить',command=configure);function_button_1.place(x=290,y=170)

#повторение мыши
def function_work():
    while True:
       time.sleep(0.1)
       if keyboard.is_pressed(start_f):
           time.sleep(1)
           while True:
             mouse.play(Buttons)
             if keyboard.is_pressed(end_f):
                break
             
#возможность перенастройки
def configure():
   global Buttons
   Buttons = []
   Label_function.place_forget()
   function_button_1.place_forget()
   MAIN_button.place(x = 276, y = 152)
   
#включение альтернативных потоков
function_working = threading.Thread(target=function_work);function_working.start()
function = threading.Thread(target=listen_mouse)
main_clicker = threading.Thread(target=clicker);main_clicker.start()

# Основное наполнение программы, кнопки, текста, заголовки и т.д
Title = Label(text='Автокликер',bg='#4E4D4D',fg='#ffffff',font=('Comic Neue', 24)); Title.place(x=30,y=14)
Label_function = Label(text='Запустить функцию \nplay/record?',bg='#4E4D4D',fg='#ffffff',font=('Comic Neue', 12)); Label_function.place(x = 264, y = 38)
Entry_start = Entry(font=('Comic Neue', 16),width=2,justify='center'); Entry_start.place(x=12,y=61); Label_start = Label(text='Введите кнопку старта',bg='#4E4D4D',fg='#ffffff',font=('Comic Neue', 12)); Label_start.place(x = 40, y = 63)
Entry_end = Entry(font=('Comic Neue', 16),width=2,justify='center'); Entry_end.place(x=12,y=101); Label_start = Label(text='Введите кнопку остановки',bg='#4E4D4D',fg='#ffffff',font=('Comic Neue', 12)); Label_start.place(x = 40, y = 103)
Entry_speed = Entry(font=('Comic Neue', 16),width=2,justify='center'); Entry_speed.place(x=12,y=141); Label_start = Label(text='Введите скорость (кпс)',bg='#4E4D4D',fg='#ffffff',font=('Comic Neue', 12)); Label_start.place(x = 40, y = 143)
#Часть с кнопками
Entry_Auto_button = Entry(font=('Comic Neue', 16),width=2,justify='center'); Entry_Auto_button.place(x=12,y=181); Label_start = Label(text='Автоматически \nнажимающаяся кнопка',bg='#4E4D4D',fg='#ffffff',font=('Comic Neue', 12)); Label_start.place(x = 43, y = 174)
Rmb_button = Button(justify='center',font=('Comic Neue', 8),text='Пкм',width=5,height=1, command = Rmb);Rmb_button.place(x = 225, y = 167)
Lmb_button = Button(justify='center',font=('Comic Neue', 8),text='Лкм',width=5,height=1, command = Lmb);Lmb_button.place(x = 225, y = 197)
function_button_1 = Button(justify='center',font=('Comic Neue', 8),text='Запустить',width=14,height=1, command = function_start);function_button_1.place(x = 290, y = 88)
MAIN_button = Button(justify='center',font=('Comic Neue', 8),text='Запустить',width=20,height=4, command=check_for_start_button);MAIN_button.place(x = 276, y = 152)

# Функция благодаря которой эта программа работает

tk.mainloop()
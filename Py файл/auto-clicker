from tkinter import *; from pynput import mouse,keyboard;import time ;import threading; from pynput.keyboard import Controller as Keyboard_controller, Key; from pynput.mouse import Button as Button_mouse, Controller as Mouse_controller
#обозначение сетки
root = Tk(className='Автокликер 3.0')
root.geometry('457x570')
root.configure(background='#D9D9D9',)
root.resizable(width=False, height=False)
#сетка для рисования
canvas = Canvas(bg="#D9D9D9", width=458, height=571)
canvas.pack(anchor=CENTER, expand=1)

count = 3
start = ''
end = ''
click_button = ''
mouse_button = Mouse_controller()

def mouse_write(x,y,button):
    global end
    global start
    global count 
    global click_button
    if count == 0:
       start = button
       count = 3
       Start_description.text.configure(text=f'клавиша\n{start}');Start_description.text.place_configure(x=100,y=110)
    elif count == 1:
       end = button
       count = 3
       Stop_description.text.configure(text=f'клавиша\n{end}');Stop_description.text.place_configure(x=340,y=110)
    elif count == 2:
       click_button = button
       click_button_description.text.configure(text=f'клавиша\n{click_button}');click_button_description.text.place_configure(x=100,y=240)
       count = 3
    return False


def listen_mouse():
 with mouse.Listener(on_click=mouse_write) as mouse_key:
    mouse_key.join()


def mouse_for_cpstest():
 with mouse.Listener(on_click=cps_test_mouse) as mouse_key:
    mouse_key.join()
   

def listen_keyboard_for_cpstest():
   with keyboard.Listener(on_press=cps_test_keyboard,suppress=True) as keyboard_key:
      keyboard_key.join()


def keyboard_write(key):
    global end;global start;global count ;global click_button
    if count == 0:
       start = key
       count = 3
       Start_description.text.configure(text=f'клавиша\n{start}');Start_description.text.place_configure(x=100,y=110)
    elif count == 1:
       end = key
       count = 3
       Stop_description.text.configure(text=f'клавиша\n{end}');Stop_description.text.place_configure(x=340,y=110)
    elif count == 2:
       click_button = key
       click_button_description.text.configure(text=f'клавиша\n{click_button}');click_button_description.text.place_configure(x=100,y=240)
       count = 3
    return False


def lmb_f():
   global click_button
   click_button = Button_mouse.left
   lmb.button.configure(text='y');rmb.button.configure(text='n')
   click_button_description.text.configure(text=f'клавиша\n{click_button}');click_button_description.text.place_configure(x=100,y=240)


def rmb_f():
   global click_button
   click_button = Button_mouse.right
   lmb.button.configure(text='n');rmb.button.configure(text='y')
   click_button_description.text.configure(text=f'клавиша\n{click_button}');click_button_description.text.place_configure(x=100,y=240)


def cps_test_change():
   global cps   
   global number
   global clicks
   cps = 0
   number = 10
   clicks = 0
   global timer
   while number != 0:
    time.sleep(1)
    cps_test_b.button.configure(text = f"{int(clicks)}({number})")
    number = number - 1
   cps = int(clicks)
   return False


def cps_test_mouse(x,y,button):
 global clicks
 print(click_button)
 if button == click_button:
    cps_test_b.button.configure(text = f"{int(clicks)}({number})")
    clicks = clicks + 0.5
 if number == 0:
    cps_test_b.button.configure(text = f"кпс тест\n{click_button}/{cps}")
    return False
 
def cps_test_keyboard(key):
 global clicks
 if key == click_button:
    cps_test_b.button.configure(text = f"{int(clicks)}({number})")
    clicks = clicks + 0.5
 if number == 0:
    cps_test_b.button.configure(text = f"кпс тест\n{click_button}/{cps}")
    return False
 

#FIXME Пофиксить баг если нажать на кнопку во время программы, также разобраться с отображением кликов у счётчика, потом обязательно переписать формулы
def cps_test_thread():
   cps_listening = threading.Thread(target= mouse_for_cpstest)
   cps_listening.start()
   cps_listening.join
   cps_listenin = threading.Thread(target= listen_keyboard_for_cpstest) 
   cps_listenin.start()
   cps_listenin.join
   cps_change = threading.Thread(target= cps_test_change)
   cps_change.start()
   cps_change.join


def listen_keyboard():
   with keyboard.Listener(on_press=keyboard_write,suppress=True) as keyboard_key:
      keyboard_key.join()
      

def side_listen():
  global mouse_side_process; global keyboard_side_process
  mouse_side_process = threading.Thread(target=listen_mouse) 
  keyboard_side_process = threading.Thread(target=listen_keyboard)

  mouse_side_process.start()
  keyboard_side_process.start()

  mouse_side_process.join   
  keyboard_side_process.join

def start_f():
 global count;count = 0;side_listen()
def end_f():
 global count;count = 1;side_listen()
def click_button_f():
 global count;count = 2;side_listen()
#--------------------------------------------------------------------------------------------------

#плейсхолдер пока не допишу функцию
def placeholder():
    print("замещение")

#класс со всеми фигурами
class figure():
    def __init__(self,x,y,a,b):
      self.figure=canvas.create_rectangle((x,y),(a,b),width=3)
line=figure(20,80,195,175)
line=figure(261,80,436,175)
line=figure(20,190,195,285)
line=figure(261,190,436,285)
line=figure(60,310,400,375)
line=figure(30,390,428,450)

#класс со всем текстом
class description:
    def __init__(self,message,font):
       self.text = Label(text=message,bg='#D9D9D9',font=('Inter',font))
Start_description= description('Нажмите на\nкнопку, потом\nвведите клавишу',10);Start_description.text.place(x=78,y=100)
Stop_description= description('Нажмите на\nкнопку, потом\nвведите клавишу',10);Stop_description.text.place(x=318,y=100)
Speed_description= description(f'Поставьтe\n интервал(кпм)',12);Speed_description.text.place(x=312,y=219)
Title = description('Авто-кликер 3.0',25);Title.text.place(x=8,y=6)
Start= description('Start button',16);Start.text.place(x=32,y=66)
Stop= description('Stop button',16);Stop.text.place(x=274,y=66)
Speed = description(f'Speed(cps)',16);Speed.text.place(x=274,y=178)
click_button = description("Click button",16);click_button.text.place(x=32,y=178)
click_button_description = description('введите\nклавишу',10);click_button_description.text.place(x=110,y=240)
lmb_description = description('лкм',12);lmb_description.text.place(x=55,y=208)
rmb_description = description('пкм',12);rmb_description.text.place(x=135,y=208)
play_record = description('Play/record',16);play_record.text.place(x=76,y=296)
timer = description('Timer',16);timer.text.place(x=50,y=378)
timer_description = description('Установите все\nнастройки перед началом',12);timer_description.text.place(x=40,y=405)
timer_changer = description(f'мин',12);timer_changer.text.place(x=260,y=410)
play_record_description = description('Не работает во\n время автокликера',12);play_record_description.text.place(x=220,y=320)

#класс со всеми кнопками
class buttons:
    def __init__(self,func,message,long,up):
        self.button = Button(text=message,bg='#655D5D',width=long,height=up,fg='white',command=func)
start_button=buttons(start_f,'',5,1);start_button.button.place(x=30,y=116)
Stop_button=buttons(end_f,'',5,1);Stop_button.button.place(x=270,y=116)
click_button_B=buttons(click_button_f,'',5,1);click_button_B.button.place(x=30,y=246)
lmb=buttons(lmb_f,f'n',1,1);lmb.button.place(x=30,y=208)
rmb=buttons(rmb_f,f'y',1,1);rmb.button.place(x=110,y=208)
play_record_button=buttons(placeholder,f'spc',14,1);play_record_button.button.place(x=90,y=330)
timer_start=buttons(placeholder,f'spc',9,1);timer_start.button.place(x=340,y=410)
cps_test_b=buttons(cps_test_thread,f'кпс тест',18,5);cps_test_b.button.place(x=30,y=465)
save_preset=buttons(placeholder,f'spc',15,2);save_preset.button.place(x=185,y=465)
rebuild=buttons(placeholder,f'spc',15,2);rebuild.button.place(x=320,y=465)
delete_button=buttons(placeholder,f'spc',15,2);delete_button.button.place(x=185,y=510)
download=buttons(placeholder,f'включить\nавтокликер',15,2);download.button.place(x=320,y=510)


Speed_Entry=Entry(text=f'spc',bg='black',fg='white',width=5);Speed_Entry.place(x=270,y=230)
Time_Entry=Entry(text=f'spc',bg='black',fg='white',width=5);Time_Entry.place(x=300,y=414)

#--------------------------------------------------------------------------------------------------
root.mainloop()
#главный цикл


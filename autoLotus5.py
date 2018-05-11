from pywinauto import application
import win32api
import win32com.client
import time
import pywinauto
import os
import datetime
import  sys
import win32api, win32con
import threading




def mouse_move():
    current = win32api.GetCursorPos()
    cx = sx = current[0]
    cy = sy = current[1]

    print("coords")
    print(cx)
    print(cy)

    win32api.SetCursorPos((cx+1, cy+1))






print(os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0])

def main():
    myfile = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]+"\\settings.txt"
    
   # myfile = os.getcwd() +"\\settings.txt"
    print(myfile)
    #with open(os.path.join(os.path.dirname(__file__)) +"\\settings.txt", encoding='utf-8') as file:
    with open(myfile, encoding='utf-8') as file:
        contents2 = file.readlines()
        alarm_time = contents2[3]#alarm
        print("alarm time: " + alarm_time)
        
        
    #отслеживаем время
    while True:
        now = datetime.datetime.now()
        curtime  = now.strftime("%H:%M")
        if alarm_time == curtime:
            print ("Alarm Now" + alarm_time) 
            automate()
            break
        else:
            mouse_move()
            time.sleep(50)

        #    print(" == not  alarm == ")
             
    #input("Press  Enter  for  exit...")


def automate():
    
    #open read file
    with open( os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]+"\\settings.txt", encoding='utf-8') as file:
        contents = file.readlines()
        str1 = contents[0]#кому
        str2 = contents[1]#копия1
        str3 = contents[2]#копия2
        print(str1, end="")
        print(str2, end="")
        print(str3, end="")

    app = application.Application().connect(title_re=".*Notes" , class_name="NOTES")

    app.NOTES.menu_select("Файл->Создать->новая  записка")
    time.sleep(2)
    #komy
    app.NOTES.TypeKeys(str1, with_spaces=True)
    app.NOTES.TypeKeys("{TAB}")
    #copy
    app.NOTES.TypeKeys(str2, with_spaces=True)
    app.NOTES.TypeKeys("{TAB 2}")
    #tema
    app.NOTES.TypeKeys(str3, with_spaces=True)

    time.sleep(1)
#####################
    app.NOTES.Отправить.Click()#отправить
    print("mail send")
    

#потоки
"""
th= threading.Thread(name = 'th1', target=mouse_move)
th2= threading.Thread(name = 'th2', target=main)
th.start()
th2.start()
"""
main()   






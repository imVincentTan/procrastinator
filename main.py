#!/usr/bin/env python


import datetime
import tkinter


dates = []

def main():

    top = tkinter.Tk()


    L1 = tkinter.Label(top, text="name")
    L1.pack( side = tkinter.LEFT)
    E1 = tkinter.Entry(top, bd =5)
    E1.pack(side = tkinter.LEFT)
    L2 = tkinter.Label(top, text="eta-hours")
    L2.pack( side = tkinter.LEFT)
    E2 = tkinter.Entry(top, bd =5)
    E2.pack(side = tkinter.LEFT)
    L3 = tkinter.Label(top, text="eta-minutes")
    L3.pack( side = tkinter.LEFT)
    E3 = tkinter.Entry(top, bd =5)
    E3.pack(side = tkinter.LEFT)
    L4 = tkinter.Label(top, text="end-year")
    L4.pack( side = tkinter.LEFT)
    E4 = tkinter.Entry(top, bd =5)
    E4.pack(side = tkinter.LEFT)
    L5 = tkinter.Label(top, text="eta-month")
    L5.pack( side = tkinter.LEFT)
    E5 = tkinter.Entry(top, bd =5)
    E5.pack(side = tkinter.LEFT)
    L6 = tkinter.Label(top, text="eta-day")
    L6.pack( side = tkinter.LEFT)
    E6 = tkinter.Entry(top, bd =5)
    E6.pack(side = tkinter.LEFT)
    L7 = tkinter.Label(top, text="hour")
    L7.pack( side = tkinter.LEFT)
    E7 = tkinter.Entry(top, bd =5)
    E7.pack(side = tkinter.LEFT)
    L8 = tkinter.Label(top, text="minute")
    L8.pack( side = tkinter.LEFT)
    E8 = tkinter.Entry(top, bd =5)
    E8.pack(side = tkinter.LEFT)


    def addtask():
        dates.append([E1.get(), datetime.timedelta(minutes=int(E2.get()),hours=int(E3.get())), datetime.datetime(int(E4.get()), int(E5.get()), int(E6.get()), int(E7.get()), int(E8.get()))])

    B = tkinter.Button(top, text = "Add Task", command = addtask)
    B.pack(side = tkinter.RIGHT)




    top.mainloop()


    # while True:
    #     name = input('task name: ')
    #     hours = int(input('hours'))
    #     minutes = int(input('minutes'))
    #     eta = datetime.timedelta(minutes=minutes,hours=hours)
    #     print('due date:')
    #     y = int(input('year'))
    #     m = int(input('month'))
    #     d = int(input('day'))
    #     h = int(input('hour'))
    #     minute = int(input('minute'))
    #     enddate = datetime.datetime(y, m, d, h, minute)
    #     dates.append([name, eta, enddate])
    #     if str(input('more?')) == "n":
    #         break

    print()
    for date in dates:
        print(date[0],date[1],date[2])

    print("last duedate last method:")
    dates2 = min_time_wasted(dates)
    for date in dates2:
        print(date[0],date[1],date[2],date[3],date[4])




def min_time_wasted(dates):
    datescopy = dates
    a = sorted(datescopy, key=lambda date:date[2])
    a.reverse()
    lasttime = a[0][2]
    LDLM = [] #array of [taskname, startdate, enddate, time, timewasted]
    for date in a:
        LDLM.append([date[0], min(lasttime,date[2]) - date[1], min(lasttime,date[2]), date[1], date[2]-min(lasttime,date[2])])
        lasttime = min(lasttime,date[2]) - date[1]
    return LDLM

def last_duedate_last(dates):
    datescopy = dates
    a = sorted(datescopy, key=lambda date:date[2])
    a.reverse()
    lasttime = a[0][2]
    LDLM = [] #array of [taskname, startdate, enddate, time]
    for date in a:
        LDLM.append([date[0], min(lasttime,date[2]) - date[1], min(lasttime,date[2]), date[1]])
        lasttime = min(lasttime,date[2]) - date[1]
    return LDLM







if __name__== "__main__":
    main()

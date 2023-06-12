import pywhatkit
Numtarget = input("enter number you want to send msg")

msg = input("your msg")

TimeSendhrs = input("hours to send ")
TimeSendhrs = int(TimeSendhrs)
TimeSendmin = input("minute to send")
TimeSendmin = int(TimeSendmin)


pywhatkit.sendwhatmsg(Numtarget, msg, TimeSendhrs, TimeSendmin)
import tkinter as tk
from time import sleep
from threading import Thread
from pytz import all_timezones, timezone
from datetime import datetime


class Callbacks():
    def __init__(self, oop):
        self.oop = oop

    def defaultFileEntries(self):
        self.oop.fileEntry.delete(0, tk.END)
        self.oop.fileEntry.insert(0, 'Z:\\')  # bogus path
        self.oop.fileEntry.config(state='readonly')
        self.oop.netwEntry.delete(0, tk.END)
        self.oop.netwEntry.insert(0, 'Z:\\Backup')  # bogus path

    def _combo(self, val=0):
        value = self.oop.combo.get()
        self.oop.scr.insert(tk.INSERT, value + '\n')

    def _spin(self):
        value = self.oop.spin.get()
        self.oop.scr.insert(tk.INSERT, value + '\n')

    def checkCallback(self, *ignoredArgs):
        if self.oop.chVarUn.get():
            self.oop.check3.configure(state='disabled')
        else:
            self.oop.check3.configure(state='normal')
        if self.oop.chVarEn.get():
            self.oop.check2.configure(state='disabled')
        else:
            self.oop.check2.configure(state='normal')

    def radCall(self):
        radSel = self.oop.radVar.get()
        if radSel == 0:
            self.oop.widgetFrame.configure(text=self.oop.i18n.WIDGET_LABEL + self.i18n.colorsIn[0])
        elif radSel == 1:
            self.oop.widgetFrame.configure(text=self.oop.i18n.WIDGET_LABEL + self.i18n.colorsIn[1])
        elif radSel == 2:
            self.oop.widgetFrame.configure(text=self.oop.i18n.WIDGET_LABEL + self.i18n.colorsIn[2])

    def _quit(self):
        self.oop.win.quit()
        self.oop.win.destroy()
        exit()

    def methodInAThread(self, numOfLoops=10):
        for idx in range(numOfLoops):
            sleep(1)
            self.oop.scr.insert(tk.INSERT, str(idx) + '\n')
        sleep(1)
        print('methodInAThread():', self.runT.isAlive())

    def createThread(self, num):
        self.runT = Thread(target=self.methodInAThread, args=[num])
        self.runT.setDaemon(True)
        self.runT.start()
        print(self.runT)
        print('createThread():', self.runT.isAlive())

        writeT = Thread(target=self.useQueues, daemon=True)
        writeT.start()

    def useQueues(self):
        while True:
            qItem = self.oop.guiQueue.get()
            print(qItem)
            self.oop.scr.insert(tk.INSERT, qItem + '\n')

    def insertQuote(self):
        title = self.oop.bookTitle.get()
        page = self.oop.pageNumber.get()
        quote = self.oop.quote.get(1.0, tk.END)
        print(title)
        print(quote)
        self.oop.mySQL.insertBooks(title, page, quote)

        # Button callback

    def getQuote(self):
        allBooks = self.oop.mySQL.showBooks()
        print(allBooks)
        self.oop.quote.insert(tk.INSERT, allBooks)

    def modifyQuote(self):
        raise NotImplementedError("This still needs to be implemented for the SQL command.")

    def allTimeZones(self):
        for tz in all_timezones:
            self.oop.scr.insert(tk.INSERT, tz + '\n')

    def localZone(self):
        from tzlocal import get_localzone
        self.oop.scr.insert(tk.INSERT, get_localzone())

    def getDateTime(self):
        fmtStrZone = "%Y-%m-%d %H:%M:%S %Z%z"
        utc = datetime.now(timezone('UTC'))
        print(utc.strftime(fmtStrZone))

        seoul = utc.astimezone(timezone('Asia/Seoul'))
        print(seoul.strftime(fmtStrZone))

        self.oop.lbl2.set(seoul.strftime(fmtStrZone))

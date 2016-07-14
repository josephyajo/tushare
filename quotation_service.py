#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import win32serviceutil
import win32service
import win32event
import time
import datetime
from util import log

class QuotationService(win32serviceutil.ServiceFramework):
    _svc_name_ = "QuotationService"
    _svc_display_name_ = "Quotation Data Service"
    _svc_description_ = "Quotation data service."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.isAlive = True

    def SvcDoRun(self):
        while self.isAlive:
            now = datetime.datetime.hour
            if (now >= 9) or (now <= 15):
                print(1)
            time.sleep(60)
        #win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.isAlive = False 

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(QuotationService)

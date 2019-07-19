# -*- coding: utf-8 -*-
import smtplib
import store as receipt
from sys import exit
EMAIL_ADDRESS = 'preethi.p@centelon.com'
EMAIL_PASSWORD = 'Mahirocks@1'

print receipt.RECEIPT_ELEMENTS


def send_receipt(self, email_address, name):
    """
    Sends mail to the user
    """
    try:
        subject = "RECEIPT"
        msg = """	                RECEIPT
--------------------------------------------------------------------------------------------
Consumer Name: %s 
--------------------------------------------------------------------------------------------
PRODUCT                                 QUANTITY                                  PRICE
--------------------------------------------------------------------------------------------
%s
--------------------------------------------------------------------------------------------
CART TOTAL       =  %s  Rupees
--------------------------------------------------------------------------------------------
""" % (name.upper(), '\t\t\t\t\t\t'.join(map(str, receipt.RECEIPT_ELEMENTS)), self.print_total())
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = "Subject: {}\n\n{}".format(subject, msg)
        server.sendmail(EMAIL_ADDRESS, email_address, message)
        server.quit()
        print "-" * 40, "\nCHECK YOUR EMAIL! RECEIPT HAS BEEN SENT!\n", "-" * 40
        exit(0)
    except smtplib.SMTPException:
        print "-" * 40, "\nFAILED TO SEND EMAIL! CHECK YOUR EMAIL ID!\n", "-" * 40
        exit(0)


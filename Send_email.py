#! /usr/bin/env python3
# coding: utf-8

"""
Created on Tue May 11 22:30:09 2020

@author: AGHEZZAF Mohamed & HAJJAJI Nassim
"""
import tensorflow
from socket import gethostname
#import email
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
class Send_email:
    def send(self, nom, demande, email, file):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        path_to_pdf ="demandes/"+file
        message = f"Bonjour, {nom} \nSuite à votre demande veuillez trouver ci-joint les documents demandés. \nCordialement"
        server.login("email@gmail.com","password" )
        # Craft message (obj)
        msg = MIMEMultipart()
        msg['Subject'] = demande
        msg['From'] = "Faculte des Sciences El jadida"
        msg['To'] = email
        # Insert the text to the msg going by e-mail
        msg.attach(MIMEText(message, "plain"))
        # Attach the pdf to the msg going by e-mail
        with open(path_to_pdf, "rb") as f:
            attach = MIMEApplication(f.read(),_subtype="pdf")
        attach.add_header('Content-Disposition','attachment',filename=str(file))
        msg.attach(attach)
        # send msg
        server.send_message(msg)

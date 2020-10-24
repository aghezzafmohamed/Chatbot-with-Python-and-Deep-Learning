#! /usr/bin/env python3
# coding: utf-8

"""
Created on Tue Mpr 10 19:30:03 2020

@author: AGHEZZAF Mohamed & HAJJAJI Nassim
"""
from Send_email import Send_email
from help_chatbot import About
import sys
import os
from gtts import gTTS
import datetime
import time
import urllib3
from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import pygame.mixer
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import tensorflow
import random
import json
import docx
from docx2pdf import convert
from datetime import date

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class Application(object):       
    def lecture(self, message):
        self.plainTextEdit.appendHtml(
            ' <span style="font-weight: 600; font-size: 12px; display: inline-table; padding: 0 0 0 0px; margin: 0 0 0px 0; color: #3498db;">ChatBot:</span><br><span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">'+message+'</span><br><font style="line-height:1px; margin-top: 0em;" margin-top: 0em; color="#fff">_______________________________________</font></span> <span style=" font-size: 11px; color: #999">' + datetime.datetime.now().strftime(
                    "%H:%M"))
        if(self.checkBox.isChecked()):
            tts = gTTS(text = message, lang = 'fr-FR')
            nom = "audio" + datetime.datetime.now().strftime("%H-%M-%S") + ".mp3"
            tts.save("audios/"+nom)
            pygame.mixer.music.load("audios/"+nom)
            pygame.mixer.music.play()
            time.sleep(3)
        
    def __init__(self):
        self.dstage = False
        self.admission = False
        self.infostage = dict()
        self.infoadmission = dict()
        self.cptstage = 0
        self.cptadmission = 0
        #Suppression  le contenu de dossier audios
        contenu = os.listdir(os.getcwd()+"\\audios")
        for x in contenu:
           os.remove(os.getcwd()+"\\audios\\"+x)
        with open("data/data_chat.json") as file:
            self.data = json.load(file)
        self.stemmer = LancasterStemmer()
        self.words = []
        self.labels = []
        self.docs_x = []
        self.docs_y = []
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        pygame.mixer.init()
        for intent in self.data["intents"]:
            for pattern in intent["patterns"]:
                self.wrds = nltk.word_tokenize(pattern)
                self.words.extend(self.wrds)
                self.docs_x.append(self.wrds)
                self.docs_y.append(intent["tag"])
            if intent["tag"] not in self.labels:
                self.labels.append(intent["tag"])
        
        self.words = [self.stemmer.stem(w.lower()) for w in self.words if w != "?"]
        self.words = sorted(list(set(self.words)))
        
        self.labels = sorted(self.labels)
        
        training = []
        output = []
        
        out_empty = [0 for _ in range(len(self.labels))]
        
        for x, doc in enumerate(self.docs_x):
            bag = []
        
            wrds = [self.stemmer.stem(w.lower()) for w in doc]
        
            for w in self.words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)
        
            output_row = out_empty[:]
            output_row[self.labels.index(self.docs_y[x])] = 1
        
            training.append(bag)
            output.append(output_row)
        
        len(training[0])
        training = numpy.array(training)
        output = numpy.array(output)
        tensorflow.reset_default_graph()
        
        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 6)
        net = tflearn.fully_connected(net, 6)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)
        
        self.model = tflearn.DNN(net)
        #self.model.fit(training, output, n_epoch=1000,batch_size=8, show_metric=True)
        #self.model.save('model.tflearn') 
        try:
            self.model.load("model.tflearn")
        except:
            self.lecture("Erreur model")
            
        data = pd.read_csv("data/data_master.csv")
        data.drop('Serial No.', axis=1, inplace=True)
        data.rename({'Chance of Admit ': 'Chance of Admit', 'LOR ':'LOR'}, axis=1, inplace=True)
        X = data.drop(['Chance of Admit'], axis=1)
        y = data['Chance of Admit']
        #Standardization
        scaler = StandardScaler()
        X[['CGPA','GRE Score', 'TOEFL Score']] = scaler.fit_transform(X[['CGPA','GRE Score', 'TOEFL Score']])
        #Splitting
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80, random_state=101)
        self.lr = LinearRegression()
        self.lr.fit(X_train, y_train)
         
    def predictadmission(self,infadmission):
        scaler = StandardScaler()
        X = pd.DataFrame.from_dict(infadmission)
        X.rename({'Chance of Admit ': 'Chance of Admit', 'LOR ':'LOR'}, axis=1, inplace=True)
        X[['CGPA','GRE Score', 'TOEFL Score']] = scaler.fit_transform(X[['CGPA','GRE Score', 'TOEFL Score']])
        y_pred = self.lr.predict(X)
        self.lecture("Votre pourcentage d'etre admis est {0:.2%} ".format(y_pred[0]))
        
        self.admission = False
        self.infoadmission = dict()
        self.cptadmission = 0
        self.timeBreak()
        
    def timeBreak(self):
        tZero = time.time()
        t = tZero+10
        while(True):
            if(t<time.time()):
                self.lecture("Avez vous d'autres questions ?")
                break

    def groupe(self, i):
        switch_filiere={"smp":'groupe1      groupe2      groupe3',"smc":'groupe1      groupe2',"sma":'groupe1',"svi":'groupe1   groupe2',"smi":'groupe1      groupe2'}
        return switch_filiere[i]
        
    def master(self, i):
        switch_master={"BIBDA":'www.preinscription.com/bibda',"J2EE":'www.preinscription.com/j2ee',"TEST":'www.preinscription.com/test',"MOBILE":'www.preinscription.com/mobile'}
        return switch_master[i]
    
    def chat_emplois(self):
        self.lecture("je comprends que vous voulez voir votre emplois du temps")
        filiere_tab=["smp","smc","sma","svt","smi"]
        self.lecture("Choisissez votre filiere")
        self.lecture(" ".join(filiere_tab))
        t=input("You :")
        h=0
        while t not in filiere_tab:
            h=h+1
            self.lecture("la filiere n'existe pas veuillez choisir l'une des filiere affichées")
            self.lecture(" ".join(filiere_tab))
            t=input("You :")
            if h>3:
                self.lecture("vous entrez toujours une filiere qui n'existe pas ")
                break
        if h<4:
            self.lecture("choisissez le groupe de votre filiere "+t)
            self.lecture(self.groupe(t))
            g=input("You :")
            r=self.groupe(t).split("      ")
            h=0
            while g not in r:
                h=h+1
                self.lecture("la filiere"+t+" ne contient que "+str(len(r))+" groupes veuillez choisir l'un des groupes affichés")
                self.lecture(self.groupe(t))
                g=input("You :")
                if h>3:
                    self.lecture("vous entrez toujours un groupe qui n'existe pas ")
                    break
            if(h<4):
                  # les caractere t pour filiere et g pour le groupe de la filiere 
                  self.lecture("la filere       "+t+" et le groupe    "+g)
            
        self.timeBreak()
        

    def chat_inscription(self):
        niveau = ["licence","doctorat","master"]
        Licence = ["smi","sma","smc","smp","svt"]
        Master = ["BIBDA","J2EE","TEST","MOBILE"]
        self.lecture("je comprends que vous voulez faire une inscription à notre faculté")
        self.lecture("je vais vous montrer toutes les étape pour s'inscrire")
        self.lecture("veuillez d'abord m'indiquer au quelle niveau voulez vous s'inscrire ")
        self.lecture("----------")
        self.lecture("licence      master      doctorat")
        n=input()
        h=0
        self.lecture("----------")
        while n not in niveau:
            h = h+1
            self.lecture("les données entrées ne sont pas correcte veuillez choisir l'une des inscription suivant:")
            self.lecture("licence      master      doctorat")
            
            n = input()
            if h>3:
                self.lecture("Vous entrez toujours des données incorrectes")
                break
        if h<4:
            if n == "licence":
                self.lecture("je vois que vous avez choisi un inscription en licence.")
                self.lecture("Vous pouvez choisir entre 5 licence selon votre diplome et ce que vous desirer faire.")
                self.lecture("si vous disposer une baccalaureat serie PC vous etes devant 2 choix,vous devez choisir entre SMP ou SMC")
                self.lecture("si vous disposer une baccalaureat serie SM vous etes devant 2 choix,vous devez choisir entre SMA ou SMI")
                self.lecture("Chaque filiere se divise sur 6 semestre où chaque semestre contient 6 modules")
                self.lecture("donner moi votre adress mail, je vais vous envoyer une formulaire, vous devez la replire.")
                self.lecture("votre dossier doit contenir\n - la fomulaire remplis \n - votre diplome baccalaureat original \n - phtocopie de votre CIN, et 6 photo")
            if n == "master":
                self.lecture("je vois que vous avez choisi un inscription en Master.")
                self.lecture("la faculté des science d'eljadida dispose plusieur master où la préinscription est toujours en ligne")
                self.lecture(" après la préinscription si vous etes selectionné vous serrez inviter à passer un test ecrit ou oral selon les critéres de selection du MASTER choisit")
                self.lecture("les masters offert par notre faculté sont :")
                self.lecture("    ".join(Master))
                self.lecture("pouvez vous m'indiquez lequel des master vous interesse")
                m=input("You :")
                while m not in Master:
                    h=h+1
                    self.lecture("les données entrées ne sont pas correcte veuillez choisir l'un des masters suivant :")
                    self.lecture("    ".join(Master))
                    m=input("You :")
                    if h>3:
                        self.lecture("Vous entrez toujours des données incorrectes")
                        break
                if(h<=3):   
                    self.lecture("vous pouvez continuer votre inscription sur le lien suivant")  
                    self.lecture(self.master(m))
                if n == "doctorat":
                    pass
        self.timeBreak()

    def demande_stage(self, infstage):
        infstage["date"] = date.today().strftime('%d/%m/%Y')
        #lire le model
        document = docx.Document("demandes/demande_de_stage.docx")
        for paragraph in document.paragraphs:
            for key, val in infstage.items():
                if(key in paragraph.text):
                    paragraph.text = paragraph.text.replace(key, val)
                    #self.lecture("*"+paragraph.text+"*")
        document.save("demandes/Demande_de_stage_"+infstage["StudentName"]+".docx")
        self.lecture("Votre demande a bien été envoyée")
        self.lecture("Veuillez consulter votre boite mail")
        self.dstage = False
        self.infostage = dict()
        self.cptstage = 0
        convert("demandes/Demande_de_stage_"+infstage["StudentName"]+".docx")
        send = Send_email()
        send.send(infstage["StudentName"],"Demande de stage", infstage["email"],"Demande_de_stage_"+infstage["StudentName"]+".pdf")
        self.timeBreak()
            
    def bag_of_words(self, s, words):
        bag = [0 for _ in range(len(words))]
        s_words = nltk.word_tokenize(s)
        s_words = [self.stemmer.stem(word.lower()) for word in s_words]
    
        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1
                
        return numpy.array(bag)

    def option(self): 
        self.window = QtWidgets.QMainWindow()
        self.ui = About()
        self.ui.setupUi(self.window)
        self.window.show()
            
    def mic(self):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                    print("Parle!")
                    audio = r.listen(source)
            try:
                    request = r.recognize_google(audio, language='fr-FR', show_all=False)
                    self.send_final(request)
            except sr.UnknownValueError:
                    self.lecture("Désolé, je ne comprends pas ce que vous dites")

    def send(self):
        request = self.lineEdit.text()
        self.lineEdit.clear()
        self.send_final(request)
        
    def send_final(self,request):        
            
            if(self.dstage == True):
                if(self.cptstage==1):
                    self.infostage['StudentName']=request
                    self.cptstage = self.cptstage+1
                    self.lecture(request)
                    self.lecture("de quelle specialité s'agit il ?")
                elif(self.cptstage==2):
                    self.infostage['MasterName']=request
                    self.cptstage+=1
                    self.lecture(request)
                    self.lecture("la date du debut de votre stage")
                elif(self.cptstage==3):                 
                    self.infostage['DebutStage']=request
                    self.cptstage+=1
                    self.lecture(request)
                    self.lecture("date de la fin de votre stage")
                elif(self.cptstage==4):                  
                    self.infostage['FineStage']=request
                    self.cptstage+=1
                    self.lecture(request)
                    self.lecture("le nom de l'entreprise")
                elif(self.cptstage==5):                    
                    self.infostage['EntrepriseName']=request
                    self.cptstage+=1
                    self.lecture(request)
                    self.lecture("Votre adresse email")
                elif(self.cptstage==6):                    
                    self.infostage['email']=request
                    self.cptstage+=1
                    self.lecture(request)
                    self.demande_stage(self.infostage)
                    
            elif(self.admission == True):
                if(self.cptadmission==1):
                    self.infoadmission['GRE Score']=[int(request)]
                    self.cptadmission = self.cptadmission+1
                    self.lecture(request)
                    self.lecture("La note de test TOEFL ?")
                elif(self.cptadmission==2):
                    self.infoadmission['TOEFL Score']=[int(request)]
                    self.cptadmission+=1
                    self.lecture(request)
                    self.lecture("Evaluation de votre ancienne université")
                elif(self.cptadmission==3):                 
                    self.infoadmission['le score de votre université']=[int(request)]
                    self.cptadmission+=1
                    self.lecture(request)
                    self.lecture("La note de SOP")
                elif(self.cptadmission==4):                  
                    self.infoadmission['SOR']=[float(request)]
                    self.cptadmission+=1
                    self.lecture(request)
                    self.lecture("La note de lettre de motivation")
                elif(self.cptadmission==5):                    
                    self.infoadmission['LOR']=[float(request)]
                    self.cptadmission+=1
                    self.lecture(request)
                    self.lecture("Votre note de CGPA")
                elif(self.cptadmission==6):                    
                    self.infoadmission['CGPA']=[float(request)]
                    self.cptadmission+=1
                    self.lecture(request)
                    self.lecture("Avez vous effectué des recherches ?")
                elif(self.cptadmission==7): 
                    if "non" in request:
                        self.infoadmission["Research"] = [0]
                    else:
                        self.infoadmission["Research"] = [1]
                    self.lecture(request)
                   
                    self.predictadmission(self.infoadmission)
                    
            else:
                self.plainTextEdit.appendHtml(
                        ' <span style="font-weight: 600; font-size: 12px; display: inline-table; padding: 0 0 0 0px; margin: 0 0 0px 0; color: #3498db;">Vous:</span><br><span style="font-size: 14px; font-weight:50; padding: 0 0px 0 0px; color: #2b2b2b; display: table; margin-top: 10px; line-height:1px;">' + request + '</span><br><font style="line-height:1px; margin-top: 0em;" margin-top: 0em; color="#fff">_______________________________________</font></span> <span style=" font-size: 11px; color: #999">' + datetime.datetime.now().strftime(
                                "%H:%M"))
                results = self.model.predict([self.bag_of_words(request, self.words)])
                results_index = numpy.argmax(results)
                tag = self.labels[results_index]
            
                for tg in self.data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']
            
                response = random.choice(responses)
                if (response is not None):
                    self.lecture(response)
                    if tag =='emplois':
                        self.chat_emplois()
                    elif tag=='inscription':
                        self.chat_inscription()
                    elif tag=='demande':
                        self.dstage = True
                        if(self.cptstage==0):
                            self.lecture("Veuillez me donner d'abord votre nom")
                            self.cptstage = self.cptstage+1
                    elif tag=='admission':
                        self.admission = True
                        if(self.cptadmission==0):
                            self.lecture("Veuillez me donner d'abord votre note GRE")
                            self.cptadmission = self.cptadmission+1
    
                elif request == ("Au revoir" or "à la prochaine" or "Bye" or "by" or "See you" or "so long"):
                    self.lecture("Au revoir")
    
                else:
                    self.lecture("Désolé je n'ai pas compris")

    def setupUi(self, Form):
            Form.setObjectName("Form")
            Form.setWindowModality(QtCore.Qt.NonModal)
            Form.setEnabled(True)
            Form.resize(419, 527)
            font = QtGui.QFont()
            font.setFamily("sans-serif")
            font.setPointSize(-1)
            Form.setFont(font)
            Form.setMouseTracking(False)
            Form.setTabletTracking(False)
            Form.setFocusPolicy(QtCore.Qt.NoFocus)
            Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
            Form.setAcceptDrops(False)
            Form.setToolTip("")
            Form.setStatusTip("")
            Form.setLayoutDirection(QtCore.Qt.LeftToRight)
            Form.setAutoFillBackground(False)
            Form.setStyleSheet("*{\n"
"font-size:20px;\n"
"font-family:sans-serif;\n"
"}\n"
"#label{\n"
"\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    font-family:  Tahoma, sans-serif;\n"
"}\n"
"#label_4{\n"
"background:url(us.png);\n"
"height: 5px\n"
"}\n"
"#label_2{\n"
"background:#13386d;\n"
"height: 5px\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"#frame_2{\n"
"background:url(images/us.png);\n"
"}\n"
"#frame1{\n"
"background:#16418e;\n"
"}\n"
"#pushButton{\n"
"background:rgba(0,0,0,0.8);\n"
"color:#fff;\n"
"border-radius:15px;\n"
"}\n"
"#pushButton_2{\n"
"  display:block;\n"
"  height: 300px;\n"
"  width: 300px;\n"
"  border-radius: 50%;\n"
"}\n"
"#pushButton_5{\n"
"  display:block;\n"
"  height: 300px;\n"
"  width: 300px;\n"
"  border-radius: 50%;\n"
"background:url(images/mic1.png)no-repeat;\n"
"  display: inline-block;\n"
"}\n"
"#pushButton_6{\n"
"  display:block;\n"
"  height: 300px;\n"
"  width: 300px;\n"
"  border-radius: 50%;\n"
"background:url(images/send1.png)no-repeat;\n"
"  display: inline-block;\n"
"}\n"
"#pushButton_7{\n"
"  display:block;\n"
"  height: 300px;\n"
"  width: 300px;\n"
"  border-radius: 50%;\n"
"background:url(images/option2.png)no-repeat;\n"
"  display: inline-block;\n"
"}\n"
"#pushButton_5:hover{\n"
"background: url(images/mic2.png) no-repeat;\n"
"}\n"
"#pushButton_6:hover{\n"
"background: url(images/send2.png) no-repeat;\n"
"}\n"
"#pushButton_7:hover{\n"
"background: url(images/option3.png) no-repeat;\n"
"}\n"
"#pushButton:hover{\n"
"background:#03a9f4;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"}\n"
"QLineEdit\n"
"{\n"
"font-size: 16px;\n"
"border-radius:15px;\n"
"background:transparent;\n"
"border:none;\n"
"color:#fff;\n"
"border-bottom:1px solid #717072;\n"
"}\n"
"#checkBox{\n"
"font-size:14px;\n"
"color: #fff;\n"
"\n"
"text-align: center;\n"
"font-family:  Tahoma, sans-serif;\n"
"}\n"
"#plainTextEdit{\n"
"  width: 100%;\n"
"  height: 150px;\n"
"  padding: 2px 4px;\n"
"  box-sizing: border-box;\n"
"  border: 0.2px solid #ccc;\n"
"  border-radius: 0.5px;\n"
"  background-color: #e6e6e6;\n"
"  resize: none;\n"
"  font-size: 15px;\n"
"}\n"
)
            Form.setInputMethodHints(QtCore.Qt.ImhNone)
            self.frame1 = QtWidgets.QFrame(Form)
            self.frame1.setGeometry(QtCore.QRect(-60, 0, 491, 531))
            self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame1.setObjectName("frame1")
            self.lineEdit = QtWidgets.QLineEdit(self.frame1)
            self.lineEdit.setGeometry(QtCore.QRect(110, 470, 321, 41))
            self.lineEdit.setText("")
            self.lineEdit.setObjectName("lineEdit")
            self.pushButton_2 = QtWidgets.QLabel(self.frame1)
            self.pushButton_2.setEnabled(True)
            self.pushButton_2.setGeometry(QtCore.QRect(200, 40, 151, 151))
            self.pushButton_2.setMouseTracking(True)
            self.pushButton_2.setTabletTracking(False)
            self.pushButton_2.setAcceptDrops(False)
            self.pushButton_2.setAccessibleDescription("")
            self.pushButton_2.setAutoFillBackground(False)
            self.pushButton_2.setInputMethodHints(QtCore.Qt.ImhNone)
            self.pushButton_2.setText("")
            movie = QtGui.QMovie("images/chatbot.gif")
            self.pushButton_2.setMovie(movie)
            movie.start()
            self.pushButton_2.setObjectName("pushButton_2")
            self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame1)
            self.plainTextEdit.setGeometry(QtCore.QRect(80, 190, 381, 281))
            self.plainTextEdit.setObjectName("plainTextEdit")
            self.plainTextEdit.setReadOnly(True)
            self.pushButton_5 = QtWidgets.QPushButton(self.frame1)
            self.pushButton_5.setEnabled(True)
            self.pushButton_5.setGeometry(QtCore.QRect(80, 480, 21, 31))
            self.pushButton_5.setMouseTracking(False)
            self.pushButton_5.setTabletTracking(False)
            self.pushButton_5.setAcceptDrops(False)
            self.pushButton_5.setAccessibleDescription("")
            self.pushButton_5.setAutoFillBackground(False)
            self.pushButton_5.setInputMethodHints(QtCore.Qt.ImhNone)
            self.pushButton_5.setText("")
            self.pushButton_5.setIconSize(QtCore.QSize(120, 120))
            self.pushButton_5.setShortcut("")
            self.pushButton_5.setCheckable(False)
            self.pushButton_5.setChecked(False)
            self.pushButton_5.setAutoRepeat(False)
            self.pushButton_5.setAutoExclusive(False)
            self.pushButton_5.setAutoDefault(False)
            self.pushButton_5.setDefault(False)
            self.pushButton_5.setFlat(True)
            self.pushButton_5.setObjectName("pushButton_5")
            self.pushButton_6 = QtWidgets.QPushButton(self.frame1)
            self.pushButton_6.setEnabled(True)
            self.pushButton_6.setGeometry(QtCore.QRect(440, 480, 31, 31))
            self.pushButton_6.setMouseTracking(False)
            self.pushButton_6.setTabletTracking(False)
            self.pushButton_6.setAcceptDrops(False)
            self.pushButton_6.setAccessibleDescription("")
            self.pushButton_6.setAutoFillBackground(False)
            self.pushButton_6.setInputMethodHints(QtCore.Qt.ImhNone)
            self.pushButton_6.setText("")
            self.pushButton_6.setIconSize(QtCore.QSize(120, 120))
            self.pushButton_6.setShortcut("")
            self.pushButton_6.setCheckable(False)
            self.pushButton_6.setChecked(False)
            self.pushButton_6.setAutoRepeat(False)
            self.pushButton_6.setAutoExclusive(False)
            self.pushButton_6.setAutoDefault(False)
            self.pushButton_6.setDefault(False)
            self.pushButton_6.setFlat(True)
            self.pushButton_6.setObjectName("pushButton_6")
            self.label = QtWidgets.QLabel(self.frame1)
            self.label.setGeometry(QtCore.QRect(240, -10, 101, 51))
            font = QtGui.QFont()
            font.setFamily("Tahoma,sans-serif")
            font.setPointSize(-1)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.pushButton_5.clicked.connect(self.mic)        
            self.pushButton_6.clicked.connect(self.send)
            self.label_2 = QtWidgets.QLabel(self.frame1)
            self.label_2.setGeometry(QtCore.QRect(60, 0, 451, 41))
            self.label_2.setText("")
            self.label_2.setObjectName("label_2")
            self.pushButton_7 = QtWidgets.QPushButton(self.frame1)
            self.pushButton_7.setEnabled(True)
            self.pushButton_7.setGeometry(QtCore.QRect(60, 10, 21, 21))
            self.pushButton_7.setMouseTracking(False)
            self.pushButton_7.setTabletTracking(False)
            self.pushButton_7.setAcceptDrops(False)
            self.pushButton_7.setAccessibleDescription("")
            self.pushButton_7.setAutoFillBackground(False)
            self.pushButton_7.setInputMethodHints(QtCore.Qt.ImhNone)
            self.pushButton_7.setText("")
            self.pushButton_7.setIconSize(QtCore.QSize(120, 120))
            self.pushButton_7.setShortcut("")
            self.pushButton_7.setCheckable(False)
            self.pushButton_7.setChecked(False)
            self.pushButton_7.setAutoRepeat(False)
            self.pushButton_7.setAutoExclusive(False)
            self.pushButton_7.setAutoDefault(False)
            self.pushButton_7.setDefault(False)
            self.pushButton_7.setFlat(True)
            self.pushButton_7.setObjectName("pushButton_7")
            self.pushButton_7.clicked.connect(self.option)
            self.checkBox = QtWidgets.QCheckBox(self.frame1)
            self.checkBox.setGeometry(QtCore.QRect(420, 170, 40, 17))
            self.checkBox.setFont(font)
            self.checkBox.setCheckable(True)
            self.checkBox.setChecked(False)
            self.checkBox.setObjectName("checkBox")
            self.lecture("Bonjour, je suis un chatbot scolaire")
            self.label_2.raise_()
            self.lineEdit.raise_()
            self.pushButton_2.raise_()
            self.plainTextEdit.raise_()
            self.pushButton_5.raise_()
            self.pushButton_6.raise_()
            self.checkBox.raise_()
            self.label.raise_()
            self.pushButton_7.raise_()
            self.retranslateUi(Form)
            QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Chatbot"))
            self.label.setText(_translate("Form", "Chatbot"))
            self.checkBox.setText(_translate("Form", "son"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Application()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

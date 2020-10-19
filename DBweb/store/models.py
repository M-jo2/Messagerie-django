from django.db import models
from django.contrib.auth.models import User
from array import *

import os.path

class MessagerieManage():

    def getEveryFriend(self,IdMainUser): # tout les utilisateurs correspondant
        query = ''
        query += 'SELECT au.id '
        query += 'from store_messagerie as sm '
        query += 'left join auth_user as au '
        query += 'on au.id != {} and(au.id = sm.user1_id or au.id = sm.user2_id) '.format(IdMainUser)

        returnListId = []
        for IdUser in User.objects.raw(query):
            returnListId.append(IdUser.id)

        return returnListId


    def getEveryMessageWithOneFriend(self, IdMainUser, IdFriendUser):
        query = ''
        query += 'SELECT sm.id '
        query += 'from store_messagerie as sm '
        query += 'where (sm.user1_id = {} and sm.user2_id = {}) or '.format(IdMainUser, IdFriendUser)
        query += '(sm.user2_id = {} and sm.user1_id = {}) '.format(IdMainUser, IdFriendUser)

        returnListId = []
        for IdMsg in Messagerie.objects.raw(query):
            returnListId.append(IdMsg)

        return returnListId



class Messagerie(models.Model):
    DEFAULT_PATH = 'messagerie/'

    path = models.CharField(max_length=100)
    objectOfMessage = models.CharField(max_length=50,default="No title")
    user1 = models.ForeignKey(User,related_name="firstUser",on_delete=models.CASCADE,null=True)
    user2 = models.ForeignKey(User,related_name="SecUser",on_delete=models.CASCADE,null=True)

    def newMessaging(self , nameFile='messages-'):
        i=0
        nameFileTemp = nameFile
        while (os.path.isfile(self.DEFAULT_PATH + nameFileTemp)):
            nameFileTemp = nameFile+str(i)
            i += 1
        self.path = self.DEFAULT_PATH+nameFileTemp
        with open(self.path,'w') as file:
            file.write('new channel of jo and me' )

    def addMessaging(self, nameFile='messages-'):
        if(os.path.isfile(self.DEFAULT_PATH + nameFile)):
            self.path = self.DEFAULT_PATH + nameFile

    def addUsers(self,user1,user2):
        self.user1 = user1
        self.user2 = user2

    def pushMessage(self,user,msg=''):
       #' si user est l un des deux enregistrer'
        with open(self.path,'a') as file: #'a' pour append. Option de open() pour ecrire à la fin du fichier texte
            file.write(user + ' :' + msg)

    def msgToString(self):
        outString = ''
        with open(self.path,'r') as file:
            outString = file.read(1000)
        return outString

    def getUserName(self,oneOrTwo):
        return self.getUser(oneOrTwo).get_username()

    def getUser(self,oneOrTwo):
        if (oneOrTwo == 1):
            return self.user1
        if (oneOrTwo == 2):
            return self.user2





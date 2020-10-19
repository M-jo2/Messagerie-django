from django.shortcuts import HttpResponse
from store.models import *
from django.contrib.auth.models import *
from django.shortcuts import render
from django.template import loader
from json import dumps

def index(request):

    """mes = Messagerie()
    user1 = User.objects.get(id=1)
    user2 = User.objects.get(id=2)
    mes.addUsers(user1,user2)

    mes.addMessaging('MsgTest')
    mes.pushMessage('<span style="color:red;">'+mes.getUserName(2)+'</span>','oui mais c est clair<br>')
    mes.pushMessage('<span style="color:blue;">' + mes.getUserName(1) + '</span>', 'oui mais c est clair<br>')
    mes.save()"""
    #mes = Messagerie.objects.get(id=1)
    #user = User.objects.create_user('Flamingitte','yop@gmail.com','123')

    """user1 = User.objects.get(id=1)
    user2 = User.objects.get(id=2)
    messagerieManage = MessagerieManage()
    affiche = ''
    truc = messagerieManage.getEveryMessageWithOneFriend(1, 2)

    for i in truc:
        affiche += str(i.id) + ' : '"""

    dataDictionnary = {
        'yo':'yo',
        'bonjour' : 'non'
    }
    dataJson = dumps(dataDictionnary)

    return render(request,'index.html',{'data': dataJson})


def connect(request):
    return HttpResponse('page de connexion')
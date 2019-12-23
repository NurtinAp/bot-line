# -*- coding: utf-8 -*- 
#==============================
from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
import json, requests, sys
import urllib.request
import requests, json, codecs
from akad.ttypes import ContentType as Type
from akad.ttypes import Message
from multiprocessing import Pool, Process
from zalgo_text import zalgo
from time import sleep
import pytz, datetime, pafy, time, timeit, base64, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib3, wikipedia, html5lib, humanize
from datetime import timedelta, date
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from datetime import datetime
from humanfriendly import format_timespan, format_size, format_number, format_length
from bs4 import BeautifulSoup
from threading import Thread
import html5lib
import logging
from googletrans import Translator
import LineService
#from gtts_token.gtts_token import Token
_session = requests.session()
#from gtts import gTTS
import youtube_dl

f = open("token.txt","r")
tkn = f.read()
#emon = LINE ('aldias246@gmail.com','nurtin12345')
emon = LINE('EIW0dVxLwYP12QEPo210.Kg381whylhu1J9zta8rEWa.4KSpkAFuuK85N5CMl7AsTYDIKUFGcHb3vmHcGm6kmIw=')
f.close()
emon.log("Auth Token : " + str(emon.authToken))
with open('wait.json','r') as stg:wait = json.load(stg)
artha={"changepicture":False}
def setback():
    with open('wait.json','w') as sb:json.dump(wait, sb, sort_keys=True, indent=4, ensure_ascii=False)
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

poll = OEPoll(emon)
call = OEPoll(emon)
creator = ["uad0bc38047fc9d33318fb5956b44a834"]
Owner = ["uad0bc38047fc9d33318fb5956b44a834"]
admin = ["uad0bc38047fc9d33318fb5956b44a834"]
staff = ["uad0bc38047fc9d33318fb5956b44a834"]
lineProfile = emon.getProfile()
Mid = emon.getProfile().mid
Owner = [Mid,"uad0bc38047fc9d33318fb5956b44a834","u906dfcd561d82c75358fd65303c45ec0"]
KAC = [emon]
ABC = [emon]
Bots = [Mid]
Emon = Owner

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
targets = []
welcome = []
msg_dict = {}
msg_dict1 = {}
temp_flood = {}
targets = []

welcome = []
simisimi = []
translateen = []
translateid = []
translateth = []
translatetw = []
translatear = []

myProfile = {
    "displayName": "",
    "statusMessage": "",
    "pictureStatus": ""
}

emonProfile = emon.getProfile()
myProfile["displayName"] = emonProfile.displayName
myProfile["statusMessage"] = emonProfile.statusMessage
myProfile["pictureStatus"] = emonProfile.pictureStatus

responsename1 = emon.getProfile().displayName
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

protect = {
    "protectqr":[],
    "protectkick":[],
    "protectjoin":[],
    "protectinvite":[],
    "protectcancel":[],
    "protect":[]
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    owner = json.load(fp)
with open('staff.json', 'r') as fp:
    owner = json.load(fp)
with open('bot.json', 'r') as fp:
    Bots = json.load(fp)
with open('qr.json', 'r') as fp:
    protectqr = json.load(fp)
with open('cancel.json', 'r') as fp:
    protectcancel = json.load(fp)
with open('invite.json', 'r') as fp:
    protectinvite = json.load(fp)    
with open('kick.json', 'r') as fp:
    protectkick = json.load(fp)
with open('gname.json', 'r') as fp:
    proName = json.load(fp)
with open('gpict.json', 'r') as fp:
    proPict = json.load(fp)
with open('antijs.json', 'r') as fp:
    protectantijs = json.load(fp)
with open('join.json', 'r') as fp:
    protectjoin = json.load(fp)
with open('ghost.json', 'r') as fp:
    ghost = json.load(fp)

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)
Setbot5 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot5)
Setbot6 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot6)
Setbot7 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot7)
Setbot8 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot8)
Setbot9 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot9)
Setbot10 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot10)
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Bulan" % (months)
    if weeks != 0: text += " %02d Minggu" % (weeks)
    if days != 0: text += " %02d Hari" % (days)
    if hours !=  0: text +=  " %02d Jam" % (hours)
    if mins != 0: text += " %02d Menit" % (mins)
    if secs != 0: text += " %02d Detik" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def web_fetch(self, url):
        buffer = StringIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.TIMEOUT, self.timeout)
        curl.setopt(curl.WRITEFUNCTION, buffer.write)
        curl.perform()
        curl.close()
        response = buffer.getvalue().strip()
        return response

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def changeProfileVideo(to):
    if settings['changevp']['picture'] == True:
        return emon.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == True:
        return emon.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = emon.genOBSParams({'oid': emon.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = emon.server.postContent('{}/talk/vp/upload.nhn'.format(str(emon.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return emon.sendMessage(to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = True
        emon.updateProfilePicture(path_p, 'vp')

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup5 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup5, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup6 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup6, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup7 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup7, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup8 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup8, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup9 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup9, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup10 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup10, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(emon.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
        emon.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        emon.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention1"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(emon.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
     #   emon.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        emon.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendTemplate(to, data):
    xyzz = LiffContext(chat=LiffChatContext(to))
    view = LiffViewRequest('1562242036-RW04okm', context = xyzz)
    token = emon.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Line/8.14.0',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return _session.post(url=url, data=json.dumps(data), headers=headers)

def issueLiff(to, liff="1562242036-RW04okm"):
   anu = LiffContext(chat=LiffChatContext(to))
   itu = LiffViewRequest(liffId=liff, context=anu)
   lol = emon.liff.issueLiffView(itu)
   token = lol.accessToken
   return token

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost
    
def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "hai".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = emon.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nDi group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(emon.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
     #   emon.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        emon.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Byee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = emon.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nSalam kompak dari"+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n┗━━[ {} ]".format(str(emon.getGroup(to).name))
                except:
                    no = "\n┗━━[ Success ]"
      #  emon.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        emon.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def rynSplitText(text,lp=''):
    separate = text.split(" ")
    if lp == '':
        adalah = text.replace(separate[0]+" ","")
    elif lp == 's':
        adalah = text.replace(separate[0]+" "+separate[1]+" ","")
    else:
        adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
    return adalah

def uploadFile(ryn):
    url = 'https://fahminogameno.life/uploadimage/action.php'
    path = emon.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+ryn, 'path','ryngenerate.png')
    data = {'register':'submit'}
    files = {"file": open(path,'rb')}
    r = requests.post(url, data=data, files=files)
    if r.status_code == 200:
        return path

def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    emon.sendMessage(to, '', contentMetadata, 7)

def sendMentionV10(to, text,name, url, iconlink):
    emon.sendMessage(to, text, {'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink })

def sendMentionV9(to, text,name, url, iconlink):
    emon.sendMessage(to, text, {'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink })

def sendMentionV8(to, text,name, url, iconlink):
    emon.sendMessage(to, text, {'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink })

def sendMentionV7(to, text,name, url, iconlink):
    emon.sendMessage(to, text, {'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink })

def searchRecentMessages(to,id):
    for a in emon.talk.getRecentMessagesV2(to,101):
        if a.id == id:
            return a
    return None

def sendMentionV2(to, text="", mids=[], name="", url="", iconlink=""):
    arrData = ""
    arr = []
    mention = "@emon "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 9
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 9
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    emon.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}'),'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink },0)
    #emon.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        emon.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        emon.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        emon.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        emon.sendMessage(to, "[ INFO ] Error :\n" + str(error))
                                   
def logError(text):
    emon.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2019,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = emon.getAllContactIds()
        gid = emon.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n Group : "+str(len(gid))+"\n Teman : "+str(len(teman))+"\n Expired : In "+hari+"\n Version : Sbonly\n Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n Runtime : \n • "+bot
        emon.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        emon.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def cek(mid):
    if mid in (Bots):
        return True
    else:
        return False

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = emon.genOBSParams({'oid': Mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'Hello_World.mp4'})
        data = {'params': obs_params}
        r_vp = emon.server.postContent('{}/talk/vp/upload.nhn'.format(str(emon.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        emon.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile %s"%str(e))    

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def convertYoutubeMp4(url):
    import pafy
    video = pafy.new(url, basic=False)
    result = video.streams[-1]
    return result.url

def convertYoutubeMp3(ur):
    import pafy
    video = pafy.new(url, basic=False)
    result = video.audiostreams[-1]
    return result.url

def urlEncode(url):
  import base64
  return base64.b64encode(url.encode()).decode('utf-8')

def urlDecode(url):
  import base64
  return base64.b64decode(url.encode()).decode('utf-8')

def google_url_shorten(url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    #return resp['id'].replace("https://","")

def generateLink(to, ryn, rynurl=None):
    path = emon.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+ryn, 'path','ryngenerate.jpg')
    data = {'register':'submit'}
    files = {"file": open(path,'rb')}
    url = 'https://fahminogameno.life/uploadimage/action.php'
    r = requests.post(url, data=data, files=files)
    emon.sendMessage(to, '%s\n%s' % (r.status_code,r.text))
    emon.sendMessage(to, '{}{}'.format(rynurl,urlEncode('https://fahminogameno.life/uploadimage/images/ryngenerate.png')))

def uploadFile(ryn):
    url = 'https://fahminogameno.life/uploadimage/action.php'
    path = emon.downloadFileURL('https://obs-sg.line-apps.com/talk/m/download.nhn?oid='+ryn, 'path','ryngenerate.png')
    data = {'register':'submit'}
    files = {"file": open(path,'rb')}
    r = requests.post(url, data=data, files=files)
    if r.status_code == 200:
        return path

def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output TeamAnuBot.mp3 {}'.format(link))
    try:
        emon.sendAudio(to, 'TeamAnuBot.mp3')
        time.sleep(2)
        os.remove('TeamAnuBot.mp3')
    except Exception as e:
        emon.sendMessage(to, 'Link salah coba lagi..')
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
    try:
        emon.sendVideo(to, "TeamAnuBot.mp4")
        time.sleep(2)
        os.remove('TeamAnuBot.mp4')
    except Exception as e:
        emon.sendMessage(to, 'Link salah coba lagi..', contentMetadata = {'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+emon.getContact(mid).pictureStatus, 'AGENT_NAME': '? ERROR ?', 'AGENT_LINK': 'https://line.me/ti/p/~mobaloghanabi.'})

def adityasplittext(self,text,lp=''):
        separate = text.split(" ")
        if lp == '':adalah = text.replace(separate[0]+" ","")
        elif lp == 's':adalah = text.replace(separate[0]+" "+separate[1]+" ","")
        else:adalah = text.replace(separate[0]+" "+separate[1]+" "+separate[2]+" ","")
        return adalah

appChrome = 'Nurtin-CHROME'
def headers3():
    Headers3 = {
        'User-Agent': "Line/8.14.2",
        'X-Line-Application': "CHROMEOS\t1.4.17\tChrome_OS\t1",
        #'User-Agent': "Line/1.4.17",
        #'X-Line-Application': "CHROMEOS\t1.4.17\tChrome_OS\t1",
        "x-lal": "ja-US_US",
        }
    return Headers3
#=================def template====================
def emonFooter(to, text):
    data = {
        "messages": [
            {
                "type": "text",
                "text": text,
                "sentBy": {
                    "label": "🔴Nurtin💓Dewi🔴",
                    "iconUrl": "https://obs.line-scdn.net//0hlRsC2XChM31OOhlenbdMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                    "linkUrl": "http://line.me/ti/p/NmTJyOoQLb"
                }
            }
        ]
    }
    sendTemplate(to, data)

def sendButton(to, image, name, text):
    url = 'https://game.linefriends.com/jbp-lcs-ranking/lcs/SendMessage',
    data = {
        "messages": [
            {
                "type": "flex",
                "altText": "D&N",
                "contents": {
                    "type": "bubble",
                    "styles": {
                        "hero": {
                            "backgroundColor": "#000000",
                            "separator": False,
                            "separatorColor": "#A9A9A9"
                        }
                    },
                    "hero": {
                    "type": "image",
                    "url": "https://obs.line-scdn.net/{}".format(image),
                    "size": "full",
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": name,
                                "size": "lg",
                                "weight": "bold",
                                "wrap": True,
                                "align": "center"
                            },
                            {
                                "type": "text",
                                "text": text, 
                                "wrap": True
                            }
                        ]
                    },
                    "footer": {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "button",
                                "style": "primary",
                                "color": "#A9A9A9",
                                "action": {
                                    "type": "uri",
                                    "label": "Creator",
                                    "uri": "http://line.me/ti/p/nurtin12"
                                }
                            }
                        ]
                    }
                }
            }
        ]
    }
    sendTemplate(to, data)
#=================def template====================
def templatesendSticker(to, link, linkx):
    data = {
        "messages": [
            {
                "type": "template",
                "altText": "Dewi.",
                "template": {
                    "type": "image_carousel",
                    "columns": [
                        {
                            "imageUrl": link,
                            "size": "tall",
                            "action": {
                                "type": "uri",
                                "uri": linkx,
                            }
                        }
                    ]
                }
            }
        ]
    }
    sendTemplate(to, data)
#=================def template====================
def flexHelp2(to, text1):
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "dewi",
                                            "contents": {
                                               "type": "bubble",
                                               "styles": {
                                                 "header": {
                                                   "backgroundColor": "#333333"
                                                 },
                                                 "body": {
                                                   "backgroundColor": "#333333",
                                                   "separator": True,
                                                   "separatorColor": "#333333"
                                                 },
                                                 "footer": {
                                                   "backgroundColor": "#333333",
                                                   "separator": True
                                                 }
                                               },
                                               "body": {
                                                 "type": "box",
                                                 "layout": "vertical",
                                                 "contents": [
                                                   {
                                                     "type": "text",
                                                     "text": text1,
                                                     "color": "#FFD700",
                                                     "align": "center",
                                                     "weight": "bold",
                                                     "wrap": True,
                                                     "size": "sm"
                                                   },
                                                   {
                                                     "type": "text",
                                                     "text": "List harga",
                                                     "weight": "bold",
                                                     "color": "#FFD700",
                                                     "align": "center",
                                                     "size": "xs"
                                                   },
                                                   {
                                                     "type": "separator",
                                                     "margin": "xs"
                                                   },
                                                   {
                                                     "type": "box",
                                                     "layout": "vertical",
                                                     "margin": "xs",
                                                     "spacing": "sm",
                                                     "contents": [
                                                       {
                                                         "type": "box",
                                                         "layout": "horizontal",
                                                         "contents": [
                                                           {
                                                             "type": "text",
                                                             "text": "sbonly",
                                                             "size": "sm",
                                                             "color": "#aaaaaa",
                                                             "flex": 0
                                                           },
                                                           {
                                                             "type": "text",
                                                             "text": "50k/bulan",
                                                             "size": "sm",
                                                             "color": "#aaaaaa",
                                                             "align": "end"
                                                           }
                                                         ]
                                                       },
                                                       {
                                                         "type": "box",
                                                         "layout": "horizontal",
                                                         "contents": [
                                                           {
                                                             "type": "text",
                                                             "text": "sb+antijs",
                                                             "size": "sm",
                                                             "color": "#aaaaaa",
                                                             "flex": 0
                                                           },
                                                           {
                                                             "type": "text",
                                                             "text": "70k/bulan",
                                                             "size": "sm",
                                                             "color": "#aaaaaa",
                                                             "align": "end"
                                                           },
                                                         ]
                                                       },
                                                       {
                                                         "type": "box",
                                                         "layout": "horizontal",
                                                         "contents": [
                                                           {
                                                             "type": "text",
                                                             "text": "Protect room",
                                                             "size": "sm",
                                                             "color": "#aaaaaa",
                                                             "flex": 0
                                                           },
                                                           {
                                                             "type": "text",
                                                             "text": "150k/bulan",
                                                             "size": "sm",
                                                             "color": "#aaaaaa",
                                                             "align": "end"
                                                           },
                                                         ]
                                                       },
                                                       {
                                                         "type": "box",
                                                         "layout": "horizontal",
                                                         "contents": [
                                                           {
                                                             "type": "text",
                                                             "text": "Token primary",
                                                             "size": "sm",
                                                             "color": "#aaaaaa",
                                                             "flex": 0
                                                           },
                                                           {
                                                             "type": "text",
                                                             "text": "5token/25k",
                                                             "size": "sm",
                                                             "color": "#aaaaaa",
                                                             "align": "end"
                                                           },
                                                         ]
                                                       },
                                                       {
                                                         "type": "box",
                                                         "layout": "horizontal",
                                                         "contents": [
                                                           {
                                                             "type": "text",
                                                             "text": "sc helper",
                                                             "size": "sm",
                                                             "color": "#aaaaaa",
                                                             "flex": 0
                                                           },
                                                           {
                                                             "type": "text",
                                                             "text": "harga di pm",
                                                             "size": "sm",
                                                             "color": "#aaaaaa",
                                                             "align": "end"
                                                           },
                                                         ]
                                                       },
                                                       {
                                                         "type": "separator",
                                                         "margin": "xs"
                                                       },
                                                       {
                                                         "type": "box",
                                                         "layout": "horizontal",
                                                         "contents": [
                                                           {
                                                             "type": "text",
                                                             "text": "Yang minat atau yg mo tnya2 dlu,pm ny aku tunggu yahh :D ..",
                                                             "size": "xxs",
                                                             "color": "#FFD700",
                                                             "wrap": True,
                                                             "align": "center",
                                                             "flex": 0
                                                           },
                                                         ]
                                                       }
                                                     ]
                                                   },
                                                 ]
                                               },
                                               "footer": {
                                                  "type": "box",
                                                  "layout": "horizontal",
                                                  "spacing": "xs",
                                                  "contents": [
                                                      {
                                                        "contents": [
                                                          {
                                                            "contents": [
                                                              {
                                                                "url": "https://obs.line-scdn.net//0hlRsCjKPDM31OOhlr7StMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                                                                "type": "icon",
                                                                "size": "md"
                                                                },
                                                                {
                                                                "text": "              「  N&D  」",
                                                                "size": "sm",
                                                                "action": {
                                                                    "uri": "http://line.me/ti/p/NmTJyOoQLb",
                                                                    "type": "uri",
                                                                    "label": "Add Creator"
                                                                },
                                                                "margin": "xl",
                                                                "align": "start",
                                                                "color": "#DC143C",
                                                                "weight": "bold",
                                                                "type": "text"
                                                              }
                                                            ],
                                                            "type": "box",
                                                            "layout": "baseline"
                                                          }
                                                        ],
                                                        "type": "box",
                                                        "layout": "horizontal"
                                                      }
                                                  ]
                                              }
                                          }
                                      }
        ],
    }
    sendTemplate(to, data)    
#=================def template====================
def flexHelp(to, text1):
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "D&N",
                                            "contents": {
                                               "type": "bubble",
                                                 "hero": {
                                                   "type": "image",
                                                   "url": "https://obs.line-scdn.net/{}".format(emon.getContact(Mid).pictureStatus),
                                                   "size": "full",
                                                   "aspectRatio": "20:13",
                                                   "aspectMode": "cover",
                                                   "action": {
                                                     "type": "uri",
                                                     "uri": "https://obs.line-scdn.net/{}".format(emon.getContact(Mid).pictureStatus),
                                                   }
                                                 },
                                                 "body": {
                                                   "type": "box",
                                                   "layout": "vertical",
                                                   "spacing": "xs",
                                                   "contents": [
                                                     {
                                                       "type": "text",
                                                       "text": "D&N",
                                                       "weight": "bold",
                                                       "color": "#FF0000",
                                                       "align": "center",
                                                       "size": "md",
                                                       "flex": 2
                                                     },
                                                     {
                                                       "type": "separator",
                                                       "color": "#000000"
                                                     },
                                                     {
                                                       "type": "text", 
                                                       "text": text1,
                                                       "color": "#FF0000",
                                                       "wrap": True,
                                                       "weight": "bold",
                                                       "align": "center",
                                                       "size": "xs",
                                                       "action": {
                                                         "type": "uri",
                                                         "uri": "line://app/1643963120-oYbGLGry?type=profile"
                                                       }
                                                     }
                                                   ]
                                                 },
                                                 "styles": {"body": {"backgroundColor": "#FFF0F5"},
                                                 }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data)
#=================def template====================
def flexHelp1(to, text1):
    data = {
      "messages": [
                                        {
                                            "type": "flex",
                                            "altText": "D&N",
                                            "contents": 
                                                {
                                                "type": "bubble",
                                                "styles": {
                                                        "body": {
                                                            "backgroundColor": "#FFF0F5",
                                                            "separator": True,
                                                            "separatorColor": "#000000"
                                                        }, 
                                                        "footer": {
                                                            "backgroundColor": "#FFE4E1",
                                                            "separator": True
                                                        }
                                                    },
                                                "body": {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "margin": "lg",
                                                            "spacing": "sm",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "baseline",
                                                                    "spacing": "xs",
                                                                    "contents": [
                                                                        {
                                                                            "type": "text",
                                                                            "text": text1,
                                                                            "color": "#000000",
                                                                            "wrap": True,
                                                                            "size": "xs",
                                                                        },
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                },
                                                "footer": {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "spacing": "xs",
                                                    "contents": [
                                                        {
                                                          "contents": [
                                                            {
                                                              "contents": [
                                                                {
                                                                  "url": "https://obs.line-scdn.net//0hlRsC2XChM31OOhlenbdMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                                                                  "type": "icon",
                                                                  "size": "md"
                                                                  },
                                                                  {
                                                                  "text": "              「  EMON  」",
                                                                  "size": "sm",
                                                                  "action": {
                                                                      "uri": "http://line.me/ti/p/NmTJyOoQLb",
                                                                      "type": "uri",
                                                                      "label": "Add Creator"
                                                                  },
                                                                  "margin": "xl",
                                                                  "align": "start",
                                                                  "color": "#DC143C",
                                                                  "weight": "bold",
                                                                  "type": "text"
                                                                }
                                                              ],
                                                              "type": "box",
                                                              "layout": "baseline"
                                                            }
                                                          ],
                                                          "type": "box",
                                                          "layout": "horizontal"
                                                        }
                                                    ]
                                                }
                                            }
                                        }
        ],
    }
    sendTemplate(to, data)    
#=================def template====================
def autoSta():
    count = 1
    while True:
        try:
           for posts in emon.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   emon.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1002)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          emon.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],Menunggu["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass

def updateProfileVideoAndPicture(path, path1):
    try:
        from ffmpy import FFmpeg
        files = {'file': open(path, 'rb')}
        data = {'params': emon.genOBSParams({'oid': self.profile.mid,'ver': '2.0','type': 'video','cat': 'vp.mp4'})}
        r_vp = self.server.postContent(emon.server.LINE_OBS_DOMAIN + '/talk/vp/upload.nhn', data=data, files=files)
        if r_vp.status_code != 201:
            raise Exception('Update profile video picture failure.')
        path_p = emon.genTempFile('path')
        ff = FFmpeg(inputs={'%s' % path: None}, outputs={'%s' % path_p: ['-ss', '00:00:2', '-vframes', '1']})
        ff.run()
        emon.updateProfilePicture(path_p, 'vp')
    except:
        raise Exception('You should install FFmpeg and ffmpy from pypi')

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def removeCmdv(text, key=""):
    setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(" ")
    return text_.replace(sep[0] + " ", "")

def removeCmd(text, key=''):
    if key == '':
        setKey = '' if not settings['setKey']['status'] else settings['setKey']['key']
    else:
        setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(' ')
    return text_[len(sep[0] + ' '):]

def parsingRes(res):
    result = ''
    textt = res.split('\n')
    for text in textt:
        if True not in [text.startswith(s) for s in ['╭', '?', '', '╰']]:
            result += '\n ' + text
        else:
            if text == textt[0]:
                result += text
            else:
                result += '\n' + text
    return result

def update_non_existing_inplace(original_dict, to_add):
    for key, value in original_dict.items():
        if key not in to_add:
            to_add[key] = value
        if type(value) == dict:
            for k, v in value.items():
                if k not in to_add[key]:
                    to_add[key][k] = v
    original_dict.update(to_add)
    return original_dict

class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'

def removeCmd(cmd, text):
	key = Setmain["keyCommand"]
	#if Setmain["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]

def sendHelp():
    sendhelp = wait["autoResponMessagepm"]
    emon.sendMessage(to, sendhelp)

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
          
        if op.type == 13:
            if Mid in op.param3:
                if wait["autoLeave"] == True:
                    #if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        emon.acceptGroupInvitation(op.param1)
                        group = emon.getGroup(op.param1)
                        emon.updateGroup(group)
                        #emon.sendMessage(op.param1,"byee :v\n Group " +str(ginfo.name))
                    #else:
                        #emon.acceptGroupInvitation(op.param1)
                        #group = emon.getGroup(op.param1)
                        #emon.sendMessage(op.param1,"Hai " + str(ginfo.name))
                        clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                        clor = random.choice(clr)
                        dataa= {
                           "messages": [
                              {
                                "type": "flex",
                                "altText": "baper",
                                "contents":{
"contents":[
{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(emon.getGroup(op.param1).pictureStatus),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(emon.getGroup(op.param1).pictureStatus)
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "halo warga {}".format(group.name),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": "maaf autoleave ku aktif",
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": "#FFF0F5"},
   }
},
{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(emon.getContact(op.param2).pictureStatus),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(emon.getContact(op.param2).pictureStatus)
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(emon.getContact(op.param2).displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": "klo mo culik.pm dulu yah :D",
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": clor},
   }
},
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "==Sekilas info==\nPengen cobain make bot line?gampang ko,ngga prlu ribet :v..skrg 50rb/bulan udah bisa mainin selfbot..mau tanya2 dlu boleh.buruan klik tulisan\n CHAT ME dibawah..\n by:☛ꓐꓳꓔ ꬴ൱⭙൨☚ ",
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": "TAP HERE TO CHAT ME",
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "md",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": clor},
   }
}
],
"type": "carousel"
}
}
]
}
                        sendTemplate(op.param1,dataa)
                        emon.leaveGroup(op.param1)

        if op.type == 13:
            if Mid in op.param3:
                if wait["autoJoin"] == True:
                   # if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                     #   emon.acceptGroupInvitation(op.param1)
                      #  ginfo = emon.getGroup(op.param1)
                        #emon.sendMessage(op.param1,":v \n " + str(ginfo.name))                      
                #    else:
                            emon.acceptGroupInvitation(op.param1)
                            group = emon.getGroup(op.param1)
                            emon.updateGroup(group)
                            #ginfo = emon.getGroup(op.param1)
                            #emon.sendMessage(op.param1,"v: \n " + str(ginfo.name))
                            clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                            clor = random.choice(clr)
                            dataa= {
                           "messages": [
                              {
                                "type": "flex",
                                "altText": "hai",
                                "contents":{
"contents":[
{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(emon.getGroup(op.param1).pictureStatus),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(emon.getGroup(op.param1).pictureStatus)
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "heíiii guys {}".format(group.name),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": "assallamuallaikum",
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": clor},
   }
},
{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(emon.getContact(op.param2).pictureStatus),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(emon.getContact(op.param2).pictureStatus)
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(emon.getContact(op.param2).displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": "makasi dah di jepit",
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": clor},
   }
}
],
"type": "carousel"
}
}
]
}
                            sendTemplate(op.param1,dataa)

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = emon.getGroup(op.param1)
                contact = emon.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                #emon.sendImageWithURL(op.param1, image)
                clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                clor = random.choice(clr)
                dataa= {
                           "messages": [
                              {
                                "type": "flex",
                                "altText": "baper",
                                "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(emon.getContact(op.param2).pictureStatus),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(emon.getContact(op.param2).pictureStatus)
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(emon.getContact(op.param2).displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": wait["leave"],
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": clor},
   }
}
}
]
}
                sendTemplate(op.param1,dataa)

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = emon.getGroup(op.param1)
                contact = emon.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                #emon.sendImageWithURL(op.param1, image)
                clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                clor = random.choice(clr)
                dataa= {
                           "messages": [
                              {
                                "type": "flex",
                                "altText": "welcome",
                                "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(emon.getContact(op.param2).pictureStatus),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(emon.getContact(op.param2).pictureStatus)
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(emon.getContact(op.param2).displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": wait["welcome"],
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": clor},
   }
}
}
]
}
                sendTemplate(op.param1,dataa)

        if op.type == 0:
            return

        if op.type == 5:
            if wait["autoAdd"] == True:
                emon.findAndAddContactsByMid(op.param1)
                cover = emon.getProfileCoverURL(op.param1)
                dataa = {
                           "messages": [
                              {
                                "type": "flex",
                                "altText": "salken ya",
                                "contents":{
"contents":[
{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(emon.getContact(op.param1).pictureStatus),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(emon.getContact(op.param1).pictureStatus)
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(emon.getContact(op.param1).displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": wait["message"],
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": "#FFF0F5"},
   }
},
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "==Sekilas info==\nPengen cobain make bot line?gampang ko,ngga prlu ribet :v..skrg 70rb/bulan udah bisa mainin selfbot..mau tanya2 dlu boleh.buruan klik tulisan\n CHAT ME dibawah..\n by:☛ꓐꓳꓔ ꬴ൱⭙൨☚ ",
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": "TAP HERE TO CHAT ME",
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "md",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": "#FFF0F5"},
   }
}
],
"type": "carousel"
}
}
]
}
                sendTemplate(op.param1,dataa)

        if op.type == 5:
        	if wait["autoBlock"] == True:
        		emon.blockContact(op.param1)
        		cl.sendMessage(op.param1,"Tapi Maaf Auto Block Saya Aktif........")

        if op.type == 55:
            try:
                if op.param1 in Setmain["readPoint"]:
                   if op.param2 in Setmain["readMember"][op.param1]:
                       pass
                   else:
                       Setmain["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
                
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = emon.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = emon.getContact(op.param2)
                        status = emon.getContact(op.param2)
                        clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#C0F785","#8BEFEF","#EAC6F4")
                        clor = random.choice(clr)
                     #   to = msg.to
                        dataa= {
                           "messages": [
                              {
                                "type": "flex",
                                "altText": "anda keciduk",
                                "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(emon.getContact(op.param2).pictureStatus),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(emon.getContact(op.param2).pictureStatus)
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(emon.getContact(op.param2).displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": wait["mention"],
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": clor},
   }
}
}
]
}
                        sendTemplate(op.param1,dataa)
                #        emon.postTemplate(op.param1,dataa);
                    
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = emon.getGroup(at)
                                Emon = emon.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Gambar Dihapus 」 "
                                #ret_ += " Nama Grup : {}".format(str(ginfo.name))
                               # ret_ += "\n❂➣ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n By Botemon™️"
                               # emon.sendMessage(at, str(ret_))
                                dataa= {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "keciduk",
                                        "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(emon.getContact(msg_dict[msg_id]["from"]).pictureStatus),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(emon.getContact(msg_dict[msg_id]["from"]).pictureStatus),
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(emon.getContact(msg_dict[msg_id]["from"]).displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": str(ret_),
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": "#FFF0F5"},
   }
}
}
]
}
                                sendTemplate(at, dataa)
                                emon.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = emon.getGroup(at)
                                Emon = emon.getContact(msg_dict[msg_id]["from"])
                                #ret_ =  "「 Pesan Dihapus 」\n"
                                #ret_ += "• Pengirim : {}".format(str(emon.displayName))
                                #ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                            #    ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ = "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                              #  flexHelp1(at, str(ret_))
                                dataa= {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "keciduk",
                                        "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(emon.getContact(msg_dict[msg_id]["from"]).pictureStatus),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(emon.getContact(msg_dict[msg_id]["from"]).pictureStatus),
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(emon.getContact(msg_dict[msg_id]["from"]).displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": str(ret_),
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": "#FFF0F5"},
   }
}
}
]
}
                                sendTemplate(at, dataa)
                #        emon.postTemplate(op.param1,dataa);
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = emon.getGroup(at)
                                Emon = emon.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」"
                                #ret_ += "• Pengirim : {}".format(str(Emon.displayName))
                                #ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                #ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                dataa= {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "keciduk",
                                        "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(emon.getContact(msg_dict1[msg_id]["from"]).pictureStatus),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(emon.getContact(msg_dict1[msg_id]["from"]).pictureStatus),
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(emon.getContact(msg_dict1[msg_id]["from"]).displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": str(ret_),
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": "#FFF0F5"},
   }
}
}
]
}
                                sendTemplate(at, dataa)
                                #emon.sendMessage(at, str(ret_))
                                emon.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message                    
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               emon.sendMessage(msg.to, str(data["answer"])) 
                   except Exception as error:
                       pass

               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           emon.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                           
                           
               if msg.to in translateid:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='id')
                           A = hasil.text
                           emon.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translateth:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='th')
                           A = hasil.text
                           emon.sendMessage(msg.to, A)
                   except Exception as error:
                       pass
                   
               if msg.to in translatetw:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='zh-tw')
                           A = hasil.text
                           emon.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translatear:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='ar')
                           A = hasil.text
                           emon.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                    


        if op.type == 25 or op.type == 26:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                          if msg._from not in Mid:
                            if msg.toType != 0 and msg.toType == 2:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                contact = emon.getContact(msg._from)
                                status = emon.getContact(msg._from)
                                for mention in mentionees:
                                  if Mid in mention["M"]:
                                    if wait["autoRespon"] == True:
                                      contact = emon.getProfile()
                                      mids = [contact.mid]
                                      status = emon.getContact(msg._from)
                                      to = msg.to
                                      clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                                      clor = random.choice(clr)
                                      dataa= {
                                         "messages": [
                                            {
                                              "type": "flex",
                                              "altText": "anda disebut",
                                              "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(emon.getContact(msg._from).pictureStatus),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(emon.getContact(msg._from).pictureStatus),
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xs",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(status.displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": wait["autoResponMessage"],
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/nurtin12",
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": clor},
   }
}
}
]
}
                                      sendTemplate(to, dataa)
                                      break

        if op.type == 26:
            try:
                #print("[ 26 ] RECEIVE MESSAGE")
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                to       = sender if not msg.toType and sender != Mid else receiver
                txt      = text.lower()
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != emon.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if wait["autoRead"] == True:
                            emon.sendChatChecked(to, msg_id)
                        if sender not in Mid:
                            if msg.toType != 0 and msg.toType == 2:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    bobb = "u805403f0153ed8e754ea53c0e7e04468"
                                    group = emon.getGroup(to)
                                    for mention in mentionees:
                                        if Mid in mention["M"]:
                                            if wait["autoRespon1"] == True:
                                                emon.sendMention(sender, wait["autoResponMessagepm"], [sender])
                                            break
                        if msg.toType == 0:
                          if wait["autoReply"] == True:
                            if sender in autoanswer:
                              emon.sendMessage(sender, wait["autoAnswerMessage"])
            except Exception as error:
                logError(error)

        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = emon.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           emonFooter(msg.to, wait["Respontag"])
                           emon.sendImageWithURL(msg.to,image)                           
                           sid = str(wait["AddstickerTag"]["sid"])
                           spkg = str(wait["AddstickerTag"]["spkg"])
                           emon.sendSticker(msg.to, spkg, sid)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           emonFooter(msg.to, "yang taq dapat gif php :v..")
                           emon.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           emonFooter(msg.to, "Jangan tag saya....")
                           emon.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    to = msg.to
                    flexHelp1( to,"「Cek ID Sticker」\n STKID : " + msg.contentMetadata["STKID"] + "\n STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 7:
                   if msg._from in Owner:
                       try:
                           if wait["tstiker"] == True:
                               wait["emontikel"][wait["memproses"]] = msg.contentMetadata
                               wait["memproses"] = {}
                               wait["tstiker"] = False
                               f=codecs.open("wait.json","w","utf-8")
                               json.dump(wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                               emonFooter(msg.to,"Key sticker tersimpan")
                       except Exception as e:
                           emonFooter(msg.to,"{}".format(str(e)))
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    emon.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = emon.getContact(msg.contentMetadata["mid"])
                        path = emon.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        emon.sendMessage(msg.to," Nama : " + msg.contentMetadata["displayName"] + "\n MID : " + msg.contentMetadata["mid"] + "\n Status : " + contact.statusMessage + "\n Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        emon.sendImageWithURL(msg.to, image)
                 if msg._from in Owner:
                     if wait["delFriend"] == True:
                         emon.deleteContact(msg.contentMetadata["mid"])
                         emonFooter(msg.to,"kontak dihapus")

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 1:
                    path = emon.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   #ret_ = "\n「 Sticker Info 」"
                   ret_  = "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = emon.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}

            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    emon.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    emon.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = emon.getContact(msg.contentMetadata["mid"])
                        path = emon.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        emon.sendMessage(msg.to," Nama : " + msg.contentMetadata["displayName"] + "\n MID : " + msg.contentMetadata["mid"] + "\n Status : " + contact.statusMessage + "\n Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        emon.sendImageWithURL(msg.to, image)

#===========ADD BOT============#
               if msg.contentType == 13:
                 if msg._from in Owner:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        emonFooter(msg.to,"sudah anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        emonFooter(msg.to,"anggota bot ditambahkan")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        emonFooter(msg.to,"anggota bot dihapus")
                    else:
                        wait["dellbots"] = True
                        emonFooter(msg.to,"bukan anggota BOT")
#===========ADD STAFF============#
                 if msg._from in Owner:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        emonFooter(msg.to,"sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        emonFooter(msg.to,"staff ditambahkan")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        emonFooter(msg.to,"staff dihapus")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        emonFooter(msg.to,"bukan staff")
#===========ADD ADMIN============#
                 if msg._from in Owner:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        emonFooter(msg.to,"sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        emonFooter(msg.to,"admin ditambahkan")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        emonFooter(msg.to,"admin dihapus")
                    else:
                        wait["delladmin"] = True
                        emon.sendMessage(msg.to,"bukan admin")
#===========ADD BLACKLIST============#
                 if msg._from in Owner:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        emonFooter(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        emonFooter(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        emonFooter(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        emonFooter(msg.to,"Contact itu tidak ada di blacklist")
#===========TALKBAN============#
                 if msg._from in Owner:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        emonFooter(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        emonFooter(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        emonFooter(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        emonFooter(msg.to,"Contact itu tidak ada di Talkban")
#===========UPDATE FOTO============#
               if msg.contentType == 1:
                 if msg._from in Owner:
                    if Setmain["Addimage"]["status"] == True:
                        path = emon.downloadObjectMsg(msg.id)
                        images[Setmain["Addimage"]["name"]] = str(path)
                        f = codecs.open("image.json","w","utf-8")
                        json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                        emon.sendMessage(msg.to, "sukses tambah gambar: {} ".format(str(Setmain["Addimage"]["name"])))
                        Setmain["Addimage"]["status"] = False                
                        Setmain["Addimage"]["name"] = ""
               if msg.contentType == 1:
                 if msg._from in Owner:
                    if Setmain["proPict"]["status"] == True:
                        path = emon.downloadObjectMsg(msg_id)
                        Setmain["pro_pict"][msg.to] = str(path)
                        backupData()
                        emon.sendMessage(msg.to, "pictureGroup di kunci \nsukses save pictureGroup ")
                        Setmain["proPict"]["status"] = False                
                        backupData()
               if msg.contentType == 2:
                 if msg._from in Owner:
                    if Setmain["Addvideo"]["status"] == True:
                        path = emon.downloadObjectMsg(msg.id)
                        videos[Setmain["Addvideo"]["name"]] = str(path)
                        f = codecs.open("video.json","w","utf-8")
                        json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                        emon.sendMessage(msg.to, "sukses tambah video: {} ".format(str(Setmain["Addvideo"]["name"])))
                        Setmain["Addvideo"]["status"] = False                
                        Setmain["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                 if msg._from in Owner:
                    if Setmain["AddSticker"]["status"] == True:
                        stickers[Setmain["AddSticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                        f = codecs.open("sticker.json","w","utf-8")
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        emon.sendMessage(msg.to, "sukses tambah sticker: {} ".format(str(Setmain["AddSticker"]["name"])))
                        Setmain["AddSticker"]["status"] = False                
                        Setmain["AddSticker"]["name"] = ""
               if msg.contentType == 7:
                 if msg._from in Owner:
                    if Setmain["AddstickerSider"]["status"] == True:
                        Setmain["AddstickerSider"]["sid"] = msg.contentMetadata['STKID']
                        Setmain["AddstickerSider"]["spkg"] = msg.contentMetadata['STKPKGID']
                        backupData()
                        emon.sendMessage(msg.to, "sukses tambah sticker sider ")
                        Setmain["AddstickerSider"]["status"] = False                
                        backupData()
               if msg.contentType == 7:
                 if msg._from in Owner:
                    if Setmain["AddstickerTag"]["status"] == True:
                        Setmain["AddstickerTag"]["sid"] = msg.contentMetadata['STKID']
                        Setmain["AddstickerTag"]["spkg"] = msg.contentMetadata['STKPKGID']
                        backupData()
                        emon.sendMessage(msg.to, "sukses tambah sticker tag ")
                        Setmain["AddstickerTag"]["status"] = False                
                        backupData()
               if msg.contentType == 3:
                 if msg._from in Owner:
                    if Setmain["Addaudio"]["status"] == True:
                        path = emon.downloadObjectMsg(msg.id)
                        audios[Setmain["Addaudio"]["name"]] = str(path)
                        f = codecs.open("audio.json","w","utf-8")
                        json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                        emon.sendMessage(msg.to, "sukses tambah mp3: {} ".format(str(Setmain["Addaudio"]["name"])))
                        Setmain["Addaudio"]["status"] = False                
                        Setmain["Addaudio"]["name"] = ""
                        
               if msg.toType == 2:
                 if msg._from in Owner:
                   if settings["groupPicture"] == True:
                     path = emon.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     emon.updateGroupPicture(msg.to, path)
                     emonFooter(msg.to, "foto group diganti")

               if msg.contentType == 1:
                   if msg._from in Owner:
                       if Mid in Setmain["EMONfoto"]:
                            path = emon.downloadObjectMsg(msg_id)
                            del Setmain["EMONfoto"][Mid]
                            emon.updateProfilePicture(path)
                            emonFooter(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in Owner:
                   if settings["changePicture"] == True:
                     path1 = ka.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ka.updateProfilePicture(path1)
                     ka.sendMessage(msg.to, "sukses..")

               if msg.contentType == 1:
                   if artha["changepicture"] == True:
                       path = zam.downloadObjectMsg(msg_id)
                       artha["changepicture"] = False
                       emon.updateProfilePicture(path)
                       emon.sendReplyMessage(msg.id,to, "Succes updated profile picture :D")
               if msg.contentType == 16:
                   if wait["likeOn"] == True:
                           url = msg.contentMetadata["postEndUrl"]
                           emon.sukaPost(url[25:58], url[66:], likeType=1002)
                           emon.comment(url[25:58], url[66:], "🅞🅟🅔🅝 🅞🅡🅓🅔🅡\n☛ 🅂🄴🄻🄵🄱🄾🅃\n☛ 🅂🄴🄻🄵🄱🄾🅃+🄰🄽🅃🄸🄹🅂\n☛ 🄿🅁🄾🅃🄴🄺 🅁🄾🄾🄼\n☛ Ⓣⓞⓚⓔⓝ ⓅⓡⓘⓜⓐⓡⓎ\nBy ☛ 🄴🄼🅾🄽ᴃᴏᴛ\nMau tanya2,pm aja⤵\nhttp://line.me/ti/p/nurtin12")
                           mons = "numpang ngelapak"
                           data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/nurtin12"}}]}
                           sendTemplate(msg.to, data)
                           #flexHelp(to, "➥Like Success ♪")

               elif msg.contentType == 2:
               	if msg._from in Owner:
               		if settings["changevp"] == True:
               			contact = emon.getProfile()
               		path = emon.downloadFileURL("https://obs.line-scdn.net/{}".format(contact.pictureStatus))
               		#pict = LineAPI/tmp/cpp.jpg
               		#path = cl.downloadFileURL(pict)
               		path1 = emon.downloadObjectMsg(msg_id)
               		settings["changevp"] = False
               		changeVideoAndPictureProfile(path, path1)
               		emonFooter(to, "Success change video profile")

               if msg.contentType == 2:
                   if msg._from in Owner:
                       if mid in Setmain["Dentvideo"]:
                            path = emon.downloadObjectMsg(msg_id,saveAs="tmp/vid.bin")
                            del Setmain["Dentvideo"][mid]
                            emon.updateProfileVideoPicture(path)
                            emon.sendMessage(msg.to,"sukses update video")
                            
               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        emon.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == ".help":
                            if msg._from in Owner:
                               helpMessage = help()
                               data = {"messages":[{"type":"text","text": helpMessage,"sentBy":{"label":"『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                               sendTemplate(msg.to, data)

                        elif cmd == ".help1":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               helpMessage1 = help1()
                               data = {"messages":[{"type":"text","text": helpMessage1,"sentBy":{"label":"『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                               sendTemplate(msg.to, data)

                        elif cmd == ".settings":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               helpMessage2 = helpbot()
                               data = {"messages":[{"type":"text","text": helpMessage2,"sentBy":{"label":"『🔴N & D 🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                               sendTemplate(msg.to, data)

                        elif cmd == ".media":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               helpMedia = help3()
                               data = {"messages":[{"type":"text","text": helpMedia,"sentBy":{"label":"『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                               sendTemplate(msg.to, data)

                        elif cmd == ".list meme":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               helpMessage3 = infomeme()
                               data = {"messages":[{"type":"text","text": helpMessage3,"sentBy":{"label":"『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                               sendTemplate(msg.to, data)
                               
                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                            	settings["changevp"] = True
                            	emonFooter(to, "「CHANGE VIDEO PROFILE」\nKirim videonya\nMblo")
                            
                        elif cmd == ".terjemahan":
                            if msg._from in Owner:
                               helpTranslate = translate()
                               data = {"messages":[{"type":"text","text": helpTranslate,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                               sendTemplate(msg.to, data)
                               #flexHelp1( to, helpTranslate)                              
                               
                        elif text.lower() == "order" or text.lower() == "list" or text.lower() == "pricelist" or text.lower() == "list harga" or text.lower() == "open order" or text.lower() == "sewa" or text.lower() == "daftar harga":
                          if msg._from not in Owner:
                                flexHelp2( to, "Bukalapak.com")
#======================================================================================
                        if cmd == "self on":
                            if msg._from in Owner:
                                wait["selfbot"] = True
                                emonFooter( to, "Bot telah aktif")

                        elif cmd == "self off":
                            if msg._from in Owner:
                                wait["selfbot"] = False
                                #sendTextTemplate(msg.to, "Bot Nonaktif")
                                emonFooter( to, "Bot dinonaktifkan")
#======================================================================================
                        if cmd == "cl":
                            if msg._from in Owner:
                               try:emon.kickoutFromGroup(to, ["uccd51ba9f22f686238f2949357c04c53"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has1 == "OK":sil1 = "✔"
                               else:sil1 = "❌"
                               emon.sendMessage(to, "{}".format(sil1))

                        if cmd == "unsend on":
                            if msg._from in Owner:
                                wait["unsend"] = True
                                emonFooter( to, "Deteksi Unsend Diaktifkan")
                                #emon.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")
                                
                        if cmd == "unsend off":
                            if msg._from in Owner:
                                wait["unsend"] = False
                                emonFooter( to, "Deteksi Unsend Dinonaktifkan")
                                #emon.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")                                

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                               # md = "╭──────────────╮\n"
                                if wait["unsend"] == True: md =" ⭕ Unsend\n"
                                else: md =" 🔴 Unsend\n"                                
                                if wait["sticker"] == True: md1 =" ⭕ Sticker\n"
                                else: md1 =" 🔴 Sticker\n"
                                if wait["contact"] == True: md2 =" ⭕ Contact\n"
                                else: md2 =" 🔴 Contact\n"
                                if wait["Mentionkick"] == True: md4 =" ⭕ Notag\n"
                                else: md4 =" 🔴 Notag\n"
                                if wait["detectMention"] == True: md5 =" ⭕ Respon\n"
                                else: md5 =" 🔴 Respon\n"
                                if wait["Mentiongift"] == True: md6 =" ⭕ Respongift\n"
                                else: md6 =" 🔴 Respongift\n"                                
                                if wait["autoJoin"] == True: md7 =" ⭕ Autojoin\n"
                                else: md7 =" 🔴 Autojoin\n"
                                if settings["autoJoinTicket"] == True: md8 =" ⭕ Jointicket\n"
                                else: md8 =" 🔴 Jointicket\n"                                
                                if wait["autoAdd"] == True: md9 =" ⭕ Autoadd\n"
                                else: md9 =" 🔴 Autoadd\n"
                                if msg.to in welcome: md10 =" ⭕ Welcome\n"
                                else: md10 =" 🔴 Welcome\n"
                                if wait["autoLeave"] == True: md11 =" ⭕ Autoleave\n"
                                else: md11 =" 🔴 Autoleave\n"
                                md12 =" Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                #data = {"messages":[{"type":"text","text": md,"sentBy":{"label":" 『🔴Emon🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                #sendTemplate(msg.to, data)
                                #flexHelp2( to, md)
                                clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                                clor = random.choice(clr)
                                data = {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "status",
                                        "contents": {
      "styles": {
        "body": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FFE4E1"
        },
        "footer": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(emon.getContact(sender).pictureStatus),
                "align": "start",
                "aspectRatio": "2:1",
                "margin": "xl",
                "size": "md",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://cdn1.iconfinder.com/data/icons/ui-5/502/switch-512.png",
                "align": "start",
                "margin": "xl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Crystal_Clear_action_exit.svg/1024px-Crystal_Clear_action_exit.svg.png",
                "align": "start",
                "margin": "xxl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "type": "box",
            "spacing": "xs",
            "flex": 2,
            "layout": "vertical",
            "contents": [
              {
                "text": "STATUS", #Hal 1
                "size": "sm",
                "color": "#6F4E37",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "flex": 2
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "??Nurtin ?? Dewi??", #"☛ꓐꓳꓔ ꬴ൱⭙൨☚ ",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md,
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md1,
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": md2,
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md4,
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md5,
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md6,
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": md7,
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md8,
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md9,
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md10,
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md11,
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md12,
                "weight": "bold",
                "size": "xxs",
                "wrap": True,
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ]
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://obs.line-scdn.net//0hlRsC2XChM31OOhlenbdMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                    "type": "icon",
                    "size": "md"
                    },
                    {
                    "text": "✭??Nurtin ?? Dewi??✭",
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/nurtin12",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "start",
                    "color": "#DC143C",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      }  
}
}
]
}
                                sendTemplate(to, data)

                        elif cmd == "status translate":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                             #   md = "╭──────────────\n││         S T A T U S \n│├─────────────\n"
                                if msg.to in translateen: md =" ⭕ English「ON」\n"
                                else: md =" 🔴 English「OFF」\n"
                                if msg.to in translateid: md1 =" ⭕ Indonesia「ON」\n"
                                else: md1 =" 🔴 Indonesia「OFF」\n"
                                if msg.to in translateth: md2 =" ⭕ Thailand「ON」\n"
                                else: md2 =" 🔴 Thailand「OFF」\n"
                                if msg.to in translatetw: md3 =" ⭕ Taiwan「ON」\n"
                                else: md3 =" 🔴 Taiwan「OFF」\n"
                                if msg.to in translatear: md4 =" ⭕ Arab「ON」\n"
                                else: md4 =" 🔴 Arab「OFF」\n"       
                                md5 ="Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                #data = {"messages":[{"type":"text","text": md,"sentBy":{"label":" 『🔴Emon🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                #sendTemplate(msg.to, data)
                                #flexHelp1( to, md)
                                clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                                clor = random.choice(clr)
                                data = {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "status",
                                        "contents": {
      "styles": {
        "body": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FFE4E1"
        },
        "footer": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(emon.getContact(sender).pictureStatus),
                "align": "start",
                "aspectRatio": "2:1",
                "margin": "xl",
                "size": "md",
                "flex": 0 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://cdn.iconscout.com/icon/free/png-256/settings-409-461608.png",
                "align": "start",
                "margin": "xl",
                "size": "full",
                "flex": 0 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Crystal_Clear_action_exit.svg/1024px-Crystal_Clear_action_exit.svg.png",
                "align": "start",
                "margin": "xxl",
                "size": "full",
                "flex": 0 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "type": "box",
            "spacing": "xs",
            "flex": 2,
            "layout": "vertical",
            "contents": [
              {
                "text": "STATUS", #Hal 1
                "size": "sm",
                "color": "#6F4E37",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "flex": 1
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "??Nurtin ?? Dewi??",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md,
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md1,
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": md2,
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md3,
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md4,
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": md5,
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ]
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://obs.line-scdn.net//0hlRsC2XChM31OOhlenbdMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                    "type": "icon",
                    "size": "md"
                    },
                    {
                    "text": "✭emon✭",
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/nurtin12",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "start",
                    "color": "#DC143C",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      }  
}
}
]
}
                                sendTemplate(to, data)
#========================================================
                        elif cmd == "pengembang" or text.lower() == 'pengembang': #
                            if msg._from in Owner:
                                emon.sendMessage(msg.to,"Contact Person") 
                                ma = ""
                                for i in creator:
                                    ma = emon.getContact(i)
                                    #flexHelp1( to, None, contentMetadata={'mid': i}, contentType=13)
                                    emon.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "informasi": #
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               sendMention(msg.to, sender, "「 SelfBOT 」\n")
                               emon.sendMessage(to, None, contentMetadata={'mid': mid}, contentType=13)
                               emon.sendMessage(msg.to, None, contentMetadata={'mid': Mid}, contentType=13)
#========================================================
                        elif cmd == "about":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                today = datetime.today()
                                future = datetime(2019,2,1)
                                hari = (str(future - today))
                                comma = hari.find(",")
                                hari = hari[:comma]
                                teman = emon.getAllContactIds()
                                gid = emon.getGroupIdsJoined()
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                anu = emon.getProfile()
                                veza = anu.displayName
                                name = anu.displayName
                            #    teks = " About"
                                teks1 = "\n• User: {}".format(str(veza))
                                teks2 = "\n• Waktu: {} wib".format(str(datetime.strftime(timeNow,'%H:%M:%S')))
                                teks3 = "\n• Group: {}".format(str(len(gid)))
                                teks4 = "\n• Teman: {}".format(str(len(teman)))
                                teks5 = "\n• Version: SelfBots"
                                teks6 = "\n• Tanggal: {}".format(str(datetime.strftime(timeNow,'%Y-%m-%d')))
                                teks7 = "\n• Runtime:\n• {}".format(str(bot))
                                #flexHelp1(to, str(teks))
                                clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                                clor = random.choice(clr)
                                data = {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "about",
                                        "contents": {
      "styles": {
        "body": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FFE4E1"
        },
        "footer": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(emon.getContact(sender).pictureStatus),
                "align": "start",
                "aspectRatio": "2:1",
                "margin": "xl",
                "size": "md",
                "flex": 0 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://cdn.iconscout.com/icon/free/png-256/settings-409-461608.png",
                "align": "start",
                "margin": "xl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Crystal_Clear_action_exit.svg/1024px-Crystal_Clear_action_exit.svg.png",
                "align": "start",
                "margin": "xxl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "type": "box",
            "spacing": "xs",
            "flex": 2,
            "layout": "vertical",
            "contents": [
              {
                "text": "STATUS", #Hal 1
                "size": "sm",
                "color": "#6F4E37",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "flex": 4
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "??Nurtin ?? Dewi??",
                "weight": "bold",
                "size": "xxs",
                "flex": 4,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": teks1,
                "weight": "bold",
                "size": "xxs",
                "flex": 4,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": teks5,
                "weight": "bold",
                "size": "xxs",
                "flex": 4,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": teks3,
                "weight": "bold",
                "size": "xxs",
                "flex": 4,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": teks4,
                "weight": "bold",
                "size": "xxs",
                "flex": 4,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": teks2,
                "weight": "bold",
                "size": "xxs",
                "flex": 4,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": teks6,
                "weight": "bold",
                "size": "xxs",
                "flex": 4,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": teks7,
                "weight": "bold",
                "wrap": True,
                "size": "xxs",
                "flex": 4,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ]
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://obs.line-scdn.net//0hlRsC2XChM31OOhlenbdMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                    "type": "icon",
                    "size": "md"
                    },
                    {
                    "text": "✭??Nurtin ?? Dewi??✭",
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/nurtin12",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "start",
                    "color": "#DC143C",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      }  
}
}
]
}
                                sendTemplate(to, data)
#========================================================
                        elif text.lower() == "mid":
                               mid = emon.getContact(msg._from).mid
                               data = {"messages":[{"type":"text","text": msg._from,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                               sendTemplate(msg.to, data)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = emon.getContact(key1)
                               data = {"messages":[{"type":"text","text": key1,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                               sendTemplate(msg.to, data)
#========================================================
                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = emon.getContact(key1)
                               flexHelp1(to, "☞ Nama : "+str(mi.displayName)+"\n☞ Mid : " +key1+"\n☞ Status : "+str(mi.statusMessage))
                               if "videoProfile='{" in str(emon.getContact(key1)):
                                   emon.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   emon.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
#========================================================
                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               try:
                                   emon.removeAllMessages(op.param2)
                                   emonFooter( to,"Delete msg done")
                               except:
                                   pass
#========================================================
                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = emon.getGroupIdsJoined()
                               for group in saya:
                                   flexHelp1(group,"[BC]\n"+pesan)

                        elif cmd.startswith("friendbc: "):
                          if msg._from in Owner:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            contacts = emon.getAllContactIds()
                            for contact in contacts:
                                flexHelp1(contact, "[ Broadcast ]\n{}".format(str(txt)))
                            emon.sendMessage(to, "Berhasil broadcast ke {} teman".format(str(len(contacts))))
#========================================================
                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               emonFooter( to, "key bot「 " + str(Setmain["keyCommand"]) + " 」")
                               #emon.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   emonFooter( to, "gagal ganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   emonFooter( to, "Setkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               Setmain["keyCommand"] = ""
                               emonFooter( to, "key kembali ke awal")
                               #emon.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")
#========================================================
                        elif cmd == "restart bot":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               mons = "Sistem di restart."
                               data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                               sendTemplate(msg.to, data)
                               Setmain["restartPoint"] = msg.to
                               restartBot()
    
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               #data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" Emon TEAM『🔴Emon🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"https://line.me/ti/p/~.-_-."}}]}
                               #sendTemplate(msg.to, data)
                               emonFooter(msg.to,bot)
#========================================================
                        elif cmd == "ginfo":
                          if msg._from in Owner:
                            try:
                                G = emon.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(emon.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                data = {"messages":[{"type":"text","text":"☆ Detail Group ☆\n ☞ Nama Group : {}".format(G.name)+ "\n ☞ ID Group : {}".format(G.id)+ "\n ☞ Pembuat : {}".format(G.creator.displayName)+ "\n ☞ Tgl buat : {}".format(str(timeCreated))+ "\n ☞ Member : {}".format(str(len(G.members)))+ "\n ☞ Pendingan : {}".format(gPending)+ "\n ☞ Group Qr : {}".format(gQr)+ "\n ☞ Group Ticket : {}".format(gTicket),"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"line.me/ti/p/5SrVh2uzuR"}}]}
                                sendTemplate(msg.to, data)
                                emon.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                emonFooter( to, str(e))
#========================================================
                        elif cmd.startswith("infogrup "):
                          if msg._from in Owner:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = emon.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = emon.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(emon.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "☞ BOT Grup Info\n"
                                ret_ += "\n☞ Name : {}".format(G.name)
                                ret_ += "\n☞ ID : {}".format(G.id)
                                ret_ += "\n☞ Creator : {}".format(gCreator)
                                ret_ += "\n☞ Created Time : {}".format(str(timeCreated))
                                ret_ += "\n☞ Member : {}".format(str(len(G.members)))
                                ret_ += "\n☞ Pending : {}".format(gPending)
                                ret_ += "\n☞ Qr : {}".format(gQr)
                                ret_ += "\n☞ Ticket : {}".format(gTicket)
                                ret_ += ""
                                data = {"messages":[{"type":"text","text": ret_,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)
                            except:
                                pass
#========================================================
                        elif cmd.startswith("infomem "):
                          if msg._from in Owner:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = emon.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = emon.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "☞ "+ str(no) + ". " + mem.displayName
                                flexhelp1(to,"☆ Name : [ " + str(G.name) + " ]\nList Member \n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("xinfomem "):
                          if msg._from in Owner:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = emon.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = emon.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "☞ "+ str(no) + ". " + mem.displayName
                                data = {"messages":[{"type":"text","text": ret_,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)
                            except: 
                                pass
#=====================TIDAK WORK===================================
                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = emon.getGroupIdsJoined()
                                for i in gid:
                                    h = emon.getGroup(i).name
                                    if h == ng:
                                        emonFooter(i, "Silahkan admin invite atau masukan kembali")
                                        emon.leaveGroup(i)
                                      #  kk.leaveGroup(i)
                                       # kc.leaveGroup(i)
                                        #ka.leaveGroup(i)
                                        #kb.leaveGroup(i)
                                        emonFooter(to,"?Berhasil keluar dari grup " +h)

                        elif cmd.startswith("leave: "): #x
                          if msg._from in Owner:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = emon.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = emon.getGroup(i)
                                if ginfo == group:
                                    emon.leaveGroup(i)
                                    emon.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))
#========================================================
                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               ma = ""
                               a = 0
                               gid = emon.getAllContactIds()
                               for i in gid:
                                   G = emon.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├ " + str(a) + ". " +G.displayName+ "\n"
                               flexHelp1(msg.to,"╭───「 My friend」\n"+ma+"╰───[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "xfriendlist":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               ma = ""
                               a = 0
                               gid = emon.getAllContactIds()
                               for i in gid:
                                   G = emon.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├ " + str(a) + ". " +G.displayName+ "\n"
                                   mons1 = "╰───[ Total「"+str(len(gid))+"」Friends ]"
                               data = {"messages":[{"type":"text","text": ma + mons1,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                               sendTemplate(msg.to, data)
#===================[]=====================================
                        elif cmd.startswith("cnamegc: "):
                            if msg.toType == 2:
                                sep = text.split(" ")
                                groupname = text.replace(sep[0] + " ","")
                                if len(groupname) <= 100:
                                    group = emon.getGroup(to)
                                    group.name = groupname
                                    emon.updateGroup(group)
                                    emonFooter(to, "Nama group menjadi : {}".format(groupname))

                        elif cmd == "absen member":
                          if msg._from in Owner:
                            group = emon.getGroup(to)
                            midMembers = [contact.mid for contact in group.members]
                            for data in midMembers:
                                emon.sendMessage(to, "{}".format(emon.getContact(data).displayName), contentMetadata={"MSG_SENDER_NAME":"{}".format(emon.getContact(data).displayName),"MSG_SENDER_ICON": "http://dl.profile.line-cdn.net/{}".format(emon.getContact(data).pictureStatus)})

                        elif cmd == "all mid":
                          if msg._from in Owner:
                            if msg.toType == 2:
                                group = emon.getGroup(to)
                                num = 0
                                ret_ = "╭───「 Mid member  {} 」".format(group.name)
                                for contact in group.members:
                                    num += 1
                                    ret_ += "\n├ {}.{}\n├{}".format(num, contact.displayName, contact.mid)
                                ret_ += "\n╰───「 Total {} Members 」".format(len(group.members))
                                emon.sendReplyMessage(msg_id, to, ret_)
                                
                        elif cmd.startswith("clone "):
                          if msg._from in Owner:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    emon.cloneProfile(ls)
                                    emon.sendContact(to, sender)
                                    emonFooter(to, "clone done !!!")

                        if cmd=='restore' and msg._from in Owner:
                            profile = emon.getProfile()
                            profile.displayName = wait['myProfile']['displayName']
                            profile.statusMessage = wait['myProfile']['statusMessage']
                            emon.updateProfile(profile)
                            if wait['myProfile']['pictureStatus']:
                                pict = emon.downloadFileURL('http://dl.profile.line-cdn.net/' + wait['myProfile']['pictureStatus'])
                                emon.updateProfilePicture(pict)
                            coverId = wait['myProfile']['coverId']
                            emon.updateProfileCoverById(coverId)
                            emonFooter(to, "restore done")

                        elif cmd == "backpp":
                          if msg._from in Owner:
                            try:
                                emonProfile = emon.getProfile()
                                wait["myProfile"]["displayName"] = str(emonProfile.displayName)
                                wait["myProfile"]["statusMessage"] = str(emonProfile.statusMessage)
                                wait["myProfile"]["pictureStatus"] = str(emonProfile.pictureStatus)
                                coverId = emon.getProfileDetail()["result"]["objectId"]
                                wait["myProfile"]["coverId"] = str(coverId)
                                emonFooter(to, "backup done")
                            except Exception as error:
                                logError(error)
                                emonFooter(to, "backup failed")
                        elif cmd.startswith("changebio: "):
                          if msg._from in Owner:
                            sep = text.split(" ")
                            bio = text.replace(sep[0] + " ","")
                            if len(bio) <= 500:
                                profile = emon.getProfile()
                                profile.statusMessage = bio
                                emon.updateProfile(profile)
                                emon.sendMessage(to, "Change bio : {}".format(bio))
#=======================================================
                        elif cmd == "memberpict":
                          kontak = emon.getGroup(to)
                          group = kontak.members
                          picall = []
                          for ids in group:
                            if len(picall) >= 400:
                              pass
                            else:
                              picall.append({
                               "imageUrl": "https://os.line.naver.jp/os/p/{}".format(ids.mid),
                               "action": {
                                  "type": "uri",
                                  "uri": "http://line.me/ti/p/NmTJyOoQLb"
                                  }
                                }
                              )
                          k = len(picall)//10
                          for aa in range(k+1):
                            data = {
                              "messages": [
                                 {
                                   "type": "template",
                                   "altText": "warga",
                                   "template": {
                                     "type": "image_carousel",
                                     "columns": picall[aa*10 : (aa+1)*10]
                                   }
                                 }
                               ]
                             }
                            sendTemplate(to, data)

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               ma = ""
                               a = 0
                               gid = emon.getGroupIdsJoined()
                               for i in gid:
                                   G = emon.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├ " + str(a) + ". " +G.name+ "\n"
                               flexHelp1(msg.to,"╭───「 My Group 」\n"+ma+"╰───[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "xgruplist":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               ma = ""
                               a = 0
                               gid = emon.getGroupIdsJoined()
                               for i in gid:
                                   G = emon.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "├ " + str(a) + ". " +G.name+ "\n"
                               emonFooter(msg.to,"╭───「 My Group 」\n"+ma+"╰───[ Total「"+str(len(gid))+"」Groups ]")
#========================================================
                        elif cmd.startswith("close "):
                          if msg._from in Owner:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = emon.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = emon.getGroup(group)
                                G.preventedJoinByTicket = True
                                emon.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = emon.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = 'Sukses Close Qr Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(emon.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "╭Nama : {}".format(G.name)
                                ret_ += "\n│Group Qr : {}".format(gQr)
                                ret_ += "\n│Pendingan : {}".format(gPending)
                                ret_ += "\n╰Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                emon.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass

                        elif cmd.startswith("open "):
                          if msg._from in Owner:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = emon.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = emon.getGroup(group)
                                G.preventedJoinByTicket = False
                                emon.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = emon.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = 'Sukses Open Qr Creator:  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(emon.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "╭Nama : {}".format(G.name)
                                ret_ += "\n│Qr : {}".format(gQr)
                                ret_ += "\n│Pendingan : {}".format(gPending)
                                ret_ += "\n╰Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                emon.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                if msg.toType == 2:
                                   X = emon.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   emon.updateGroup(X)
                                   #mons = "➥Url Opened"
                                   #data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Emon🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                   #sendTemplate(msg.to, data)
                                   emonFooter( to, "Url group opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                if msg.toType == 2:
                                   X = emon.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   emon.updateGroup(X)
                                   #mons = "➥Url Closed"
                                   #data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Emon🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                   #sendTemplate(msg.to, data)
                                   emonFooter( to, "Url group closed")
#========================================================
                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                if msg.toType == 2:
                                   x = emon.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      emon.updateGroup(x)
                                   gurl = emon.reissueGroupTicket(msg.to)
                                   emonFooter( to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
#========================================================
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                              ginvited = emon.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      emon.rejectGroupInvitation(gid)
                                  emonFooter( to, "Reject {} undangan grup".format(str(len(ginvited))))
                              else:
                                  emonFooter( to, "Tidak ada undangan")                                
#===========UPDATE FOTO============
                        elif cmd == "cpict grup":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                emonFooter( to,"Send pict to change")

                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                Setmain["EMONfoto"][Mid] = True
                                emonFooter( to,"Send pict to change")

                        elif cmd.startswith("myname: "):
                          if msg._from in Owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = emon.getProfile()
                                profile.displayName = string
                                emon.updateProfile(profile)
                                emonFooter( to,"Name change to " + string + "")
#=============[TAGALL]===========================================
                        elif cmd == "mention":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                group = emon.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Alin \n'
                                    emon.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    #emonFooter( to, "Jumlah anggota  {} ".format(str(len(nama))))          
#========================================================
                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +emon.getContact(m_id).displayName + "\n"
                                flexHelp1( to,"☞ BOT\n"+ma+"\nTotal「%s」BOT" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +emon.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +emon.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +emon.getContact(m_id).displayName + "\n"
                                flexHelp1( to,"☞ Admin BOT\n☞Creator BOT:\n"+ma+"\n☞Admin:\n"+mb+"\n☞Staff:\n"+mc+"\n☞Total「%s」" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +emon.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +emon.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +emon.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +emon.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +emon.getGroup(group).name + "\n"                                    
                                flexHelp1( to,"☞ BOT Protection\n\n☞ PROTECT URL :\n"+ma+"\n☞ PROTECT KICK :\n"+mb+"\n☞ PROTECT JOIN :\n"+md+"\n☞ PROTECT CANCEL:\n"+mc+"\n☞ PROTECT INVITE :\n"+me+"\nTotal「%s」Protect yang aktif" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))
#========================================================
                        elif cmd == "@bye":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                G = emon.getGroup(msg.to)
                                flexHelp2( to, "See You Next Time "+str(G.name))
                                emon.leaveGroup(msg.to)

                        elif cmd == "sp" or cmd == "speed":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               sendMention1(msg.to, sender, "「", "」")
                               start = time.time()
                               time.sleep(0.008)
                               elapsed_time = time.time() - start
                               emonFooter( to, "「%s」" % (elapsed_time))
#========================================================
                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['readPoint'][msg.to] = msg_id
                                 Setmain['readMember'][msg.to] = {}
                                 flexHelp1( to, "Lurking diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['readPoint'][msg.to]
                                 del Setmain['readMember'][msg.to]
                                 flexHelp1( to, "Lurking dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in Owner:
                            if msg.to in Setmain['readPoint']:
                                if Setmain['readMember'][msg.to] != {}:
                                    nad = []
                                    for x in Setmain['readMember'][msg.to]:
                                        nad.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(nad)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in nad:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(nad):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(emon.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        emon.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['readPoint'][msg.to]
                                        del Setmain['readMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['readPoint'][msg.to] = msg.id
                                    Setmain['readMember'][msg.to] = {}
                                else:
                                    flexHelp1( to, "User kosong...")
                            else:
                                flexHelp1( to, "Ketik lurking on dulu")
#========================================================
                        elif cmd == "s on":
                          if wait["selfbot"] == True:
                           if msg._from in Owner:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  #flexHelp1( to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  emonFooter(msg.to, "Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "s off":
                          if wait["selfbot"] == True:
                           if msg._from in Owner:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  #flexHelp1( to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  #flexHelp1( to, cctv['sidermem'][to])
                                  emonFooter(msg.to, "Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  emonFooter( to, cctv['sidermem'][to])
                              else:
                                  emonFooter( to, "Sudak tidak aktif")

#========================================================
                        elif cmd.startswith("youtube "):
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            url = requests.get("https://api-rtb.herokuapp.com/search-youtube=query".format(txt))
                            data = url.json()
                            if data["videos"] != []:
                                    ret_ = []
                                    for fn in data["videos"]:
                                            if len(ret_) >= 20:
                                                pass
                                            else:
                                                ret_.append({
                                                        "thumbnailImageUrl": "{}".format(fn["thumbnail"]),
                                                        "imageBackgroundColor": "#FFFFFF",
                                                        "title": "{}....".format(fn['title'][:36]),
                                                        "text": "Source : Youtube",
                                                        "actions": [
                                                            {
                                                                "type": "uri",
                                                                "label": "Click Me to download",
                                                                "uri": "line://app/1603968955-ORWb9RdY/?type=text&text={}".format(urllib.parse.quote("ytdl {}".format(fn["id"])))
                                                            }
                                                        ]
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                           "messages": [
                                              {
                                                "type": "template",
                                                "altText": "Youtube",
                                                "template": {
                                                    "type": "carousel",
                                                    "columns": ret_[aa*10 : (aa+1)*10]
                                                }
                                              }
                                           ]
                                        }
                                        sendTemplate(to, data)

                        elif cmd.startswith("ytdl "):
                          if msg._from in Owner:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            url = requests.get("https://rest.farzain.com/api/yt_download.php?id={}&apikey=ppqeuy".format(txt))
                            data = url.json()
                            def sendVid():
                                emon.sendVideoWithURL(to, data["urls"][1]["id"])
                            td = Thread(target=sendVid)
                            td.daemon = True
                            td.start()
#==========================[menu help]================================
                        if cmd == "help":
                            if msg._from in Owner:
                                clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                                clor = random.choice(clr)
                                data = {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "help",
                                        "contents": {
  "contents": [
    {
      "styles": {
        "body": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FFE4E1"
        },
        "footer": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(emon.getContact(sender).pictureStatus),
                "align": "start",
                "aspectRatio": "2:1",
                "margin": "xl",
                "size": "md",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://www.freeiconspng.com/uploads/camera-photos-pictures-icon-7.png",
                "align": "start",
                "margin": "xl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://cdn.pixabay.com/photo/2013/04/01/21/30/photo-99136_1280.png",
                "align": "start",
                "margin": "xxl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "type": "box",
            "spacing": "xs",
            "flex": 2,
            "layout": "vertical",
            "contents": [
              {
                "text": "SELFBOT", #Hal 1
                "size": "sm",
                "color": "#6F4E37",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "flex": 1
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• mention",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• @bye",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• sp/speed",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• refresh",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• restart bot",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• runtime",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• reject",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• hapus chat",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• cnamegc: (text)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• Backpp",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#F5DEB3"
              },
              {
                "type": "text",
                "text": "• myname: (text)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": "• changebio: (text)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ]
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://obs.line-scdn.net//0hlRsC2XChM31OOhlenbdMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                    "type": "icon",
                    "size": "md"
                    },
                    {
                    "text": "✭N&D✭",
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/NmTJyOoQLb",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "start",
                    "color": "#DC143C",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      }  
    },
    {
      "styles": {
        "body": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        },
        "footer": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FFE4E1"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(emon.getContact(sender).pictureStatus),
                "align": "start",
                "aspectRatio": "2:1",
                "margin": "xl",
                "size": "md",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://static1.squarespace.com/static/53e01567e4b092e63a26bdd6/t/54d1115ee4b07e05a0b5e906/1422987707650/mail+icon+round.png",
                "align": "start",
                "margin": "xl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRmydEmK9DBiMmgWs8fRYlK5mMoeHHd7cKhm0eH71Uhhn3O88ID",
                "align": "start",
                "margin": "xxl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "type": "box",
            "spacing": "xs",
            "flex": 2,
            "layout": "vertical",
            "contents": [
              {
                "text": "SELFBOT", #Hal 2
                "size": "sm",
                "color": "#6F4E37",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "flex": 1
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• updatefoto",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• cpict grup",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• open/close",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
                            {
                "type": "text",
                "text": "• url grup",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• ginfo",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": "• friendlist",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• gruplist",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• infogrup (number)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• infomem (number)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• memberpict",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• absen member",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ]
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://obs.line-scdn.net//0hlRsC2XChM31OOhlenbdMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                    "type": "icon",
                    "size": "md"
                    },
                    {
                    "text": "✭D & N ✭",
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/nurtin12",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "start",
                    "color": "#DC143C",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      }  
    },
    {
      "styles": {
        "body": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        },
        "footer": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(emon.getContact(sender).pictureStatus),
                "align": "start",
                "aspectRatio": "2:1",
                "margin": "xl",
                "size": "md",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgGUkJBQLqSmQyYazsTazQUzoQ5IV1qRNiGN06WS58vn6B-Z1CBA",
                "align": "start",
                "margin": "xl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaBDeHHKI6-mRC4YnPjI0hMrWWQGUkB6zUiuprtH5e8TOBcvFlnA",
                "align": "start",
                "margin": "xxl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "type": "box",
            "spacing": "xs",
            "flex": 2,
            "layout": "vertical",
            "contents": [
              {
                "text": "SELFBOT", #Hal 3
                "size": "sm",
                "color": "#6F4E37",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "flex": 1
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• creator",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• sbkick @",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• scall (jumlah)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": "• call (jumlah) @",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• tag (jumlah) @",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• Mid @",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• Info @",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• broadcast: (text)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": "• friendbc: (text)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ]
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://obs.line-scdn.net//0hlRsC2XChM31OOhlenbdMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                    "type": "icon",
                    "size": "md"
                    },
                    {
                    "text": "✭emon✭",
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/NmTJyOoQLb",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "start",
                    "color": "#DC143C",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      }  
    }
  ],
  "type": "carousel"
}
}
]
}
                                sendTemplate(to, data)
#=======================[menu settings]====================================
                        if cmd == "settings":
                            if msg._from in Owner:
                                clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                                clor = random.choice(clr)
                                data = {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "settings",
                                        "contents": {
  "contents": [
    {
      "styles": {
        "body": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FFE4E1"
        },
        "footer": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(emon.getContact(sender).pictureStatus),
                "align": "start",
                "aspectRatio": "2:1",
                "margin": "xl",
                "size": "md",
                "flex": 0 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://openclipart.org/image/2400px/svg_to_png/119749/power-off.png",
                "align": "start",
                "margin": "xl",
                "size": "full",
                "flex": 0 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://i.pinimg.com/originals/5e/ba/da/5ebada17a183f5778cf4982c5fb1e8e4.png",
                "align": "start",
                "margin": "xxl",
                "size": "full",
                "flex": 0 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "type": "box",
            "spacing": "xs",
            "flex": 2,
            "layout": "vertical",
            "contents": [
              {
                "text": "SETTINGS", #Hal 1
                "size": "sm",
                "color": "#6F4E37",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "flex": 1
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• s「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• unsend「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• respon「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": "• responpm「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• Welcome「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• autoread「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• autojoin「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• autoleave「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": "• autoadd「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• banlist/blc",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• clban",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ]
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://obs.line-scdn.net/{}".format(emon.getContact(sender).pictureStatus),
                    "type": "icon",
                    "size": "md"
                    },
                    {
                    "text": "✭emon✭",
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/NmTJyOoQLb",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "start",
                    "color": "#DC143C",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      }  
    },
    {
      "styles": {
        "body": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        },
        "footer": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(emon.getContact(sender).pictureStatus),
                "align": "start",
                "aspectRatio": "2:1",
                "margin": "xl",
                "size": "md",
                "flex": 0 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://cdn1.iconfinder.com/data/icons/ui-5/502/switch-512.png",
                "align": "start",
                "margin": "xl",
                "size": "full",
                "flex": 0 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://yapibilgisayar.com/wp-content/uploads/2017/05/service.png",
                "align": "start",
                "margin": "xxl",
                "size": "full",
                "flex": 0 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "type": "box",
            "spacing": "xs",
            "flex": 2,
            "layout": "vertical",
            "contents": [
              {
                "text": "SETTINGS", #Hal 2
                "size": "sm",
                "color": "#6F4E37",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "flex": 1
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• sticker「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": "• jointicket「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• notag 「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• contact「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• +admin「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• -admin「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• +talkban「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• -talkban「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• +talkban @",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• -talkban @",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ]
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://obs.line-scdn.net//0hlRsC2XChM31OOhlenbdMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                    "type": "icon",
                    "size": "md"
                    },
                    {
                    "text": "✭emon✭",
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/NmTJyOoQLb",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "start",
                    "color": "#DC143C",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      }  
    },
    {
      "styles": {
        "body": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        },
        "footer": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(emon.getContact(sender).pictureStatus),
                "align": "start",
                "aspectRatio": "2:1",
                "margin": "xl",
                "size": "md",
                "flex": 0 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://cdn1.iconfinder.com/data/icons/ui-5/502/switch-512.png",
                "align": "start",
                "margin": "xl",
                "size": "full",
                "flex": 0 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://yapibilgisayar.com/wp-content/uploads/2017/05/service.png",
                "align": "start",
                "margin": "xxl",
                "size": "full",
                "flex": 0 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "type": "box",
            "spacing": "xs",
            "flex": 2,
            "layout": "vertical",
            "contents": [
              {
                "text": "SETTINGS", #Hal 3
                "size": "sm",
                "color": "#6F4E37",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "flex": 1
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• +ban @/ -ban @",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": "• +ban「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• -ban  「On/Off」",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• talkbanlist",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• Set pesan: (text)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• Set welcome: (text)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• Set leave: (text)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• Set respon: (text)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• Set responpm: (text)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• Set sider: (text)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• contact admin",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ]
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://obs.line-scdn.net//0hlRsC2XChM31OOhlenbdMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                    "type": "icon",
                    "size": "md"
                    },
                    {
                    "text": "✭emon✭",
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/NmTJyOoQLb",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "start",
                    "color": "#DC143C",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      }  
    }
  ],
  "type": "carousel"
}
}
]
}
                                sendTemplate(to, data)

#=========================[menu hiburan]==================================
                        if cmd == "hiburan":
                            if msg._from in Owner:
                                clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                                clor = random.choice(clr)
                                data = {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "hiburan",
                                        "contents": {
  "contents": [
    {
      "styles": {
        "body": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FFE4E1"
        },
        "footer": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(emon.getContact(sender).pictureStatus),
                "align": "start",
                "aspectRatio": "2:1",
                "margin": "xl",
                "size": "md",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSnMaJwLCyfIFBSZGJmXeAXX4PUE3WpsgAskIh2Kt40SJpTGDQW",
                "align": "start",
                "margin": "xl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSnMaJwLCyfIFBSZGJmXeAXX4PUE3WpsgAskIh2Kt40SJpTGDQW",
                "align": "start",
                "margin": "xxl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "type": "box",
            "spacing": "xs",
            "flex": 2,
            "layout": "vertical",
            "contents": [
              {
                "text": "HIBURAN", #Hal 1
                "size": "sm",
                "color": "#6F4E37",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "flex": 2
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• +sticker「key」",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• -sticker「key」",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• Liststicker",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": "• listquran",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• murrotal (number)",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• al-qur'an (number)",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• get-quran: (number)",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• asmaulhusna (nomor)",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": "• jadwal sholat (kota)",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• xmusik (judul)",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• xlagu (judul)",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• ytdl (link)",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• ytmp4: (judul)",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• cuaca: (kota)",
                "weight": "bold",
                "size": "xxs",
                "flex": 2,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ]
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://obs.line-scdn.net//0hlRsC2XChM31OOhlenbdMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                    "type": "icon",
                    "size": "md"
                    },
                    {
                    "text": "✭emon✭",
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/NmTJyOoQLb",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "start",
                    "color": "#DC143C",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      }  
    },
    {
      "styles": {
        "body": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FFE4E1"
        },
        "footer": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSnMaJwLCyfIFBSZGJmXeAXX4PUE3WpsgAskIh2Kt40SJpTGDQW",
                "align": "start",
                "aspectRatio": "2:1",
                "margin": "xl",
                "size": "md",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSnMaJwLCyfIFBSZGJmXeAXX4PUE3WpsgAskIh2Kt40SJpTGDQW",
                "align": "start",
                "margin": "xl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSnMaJwLCyfIFBSZGJmXeAXX4PUE3WpsgAskIh2Kt40SJpTGDQW",
                "align": "start",
                "margin": "xxl",
                "size": "full",
                "flex": 1 #gambar jdi kecil
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "type": "separator",
            "color": "#DC143C"
          },
          {
            "type": "box",
            "spacing": "xs",
            "flex": 2,
            "layout": "vertical",
            "contents": [
              {
                "text": "HIBURAN", #Hal 2
                "size": "sm",
                "color": "#6F4E37",
                "wrap": True,
                "weight": "bold",
                "type": "text",
                "flex": 1
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• love|nama|nama",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• img: (nama)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": "• image (nama)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• foto: (nama)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• imagetext (text)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• meme@nama@text@text",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• date (hr-bl-th)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#FF0000"
              },
              {
                "type": "text",
                "text": "• get-zodiak (bintang)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• text (text)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• searchapp (nama)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• kode cctv/lihat: (number)",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• Topnews",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "text",
                "text": "• 1cak",
                "weight": "bold",
                "size": "xxs",
                "flex": 1,
                "align": "start"
              },
              {
                "type": "separator",
                "color": "#DC143C"
              }
            ]
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://obs.line-scdn.net//0hlRsC2XChM31OOhlenbdMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                    "type": "icon",
                    "size": "md"
                    },
                    {
                    "text": "✭emon✭",
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/NmTJyOoQLb",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "start",
                    "color": "#DC143C",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      }  
    }
  ],
  "type": "carousel"
}
}
]
}
                                sendTemplate(to, data)
#===========================================================
                        if cmd == "key":
                            if msg._from in Owner:
                                clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                                clor = random.choice(clr)
                                data = {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "help",
                                        "contents": {
  "contents": [
    {
      "styles": {
        "body": {
          "backgroundColor": clor,
          "separator": True,
          "separatorColor": "#FF0000"
        },
        "footer": {
          "backgroundColor": "#000000",
          "separator": True,
          "separatorColor": "#FF0000"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgGUkJBQLqSmQyYazsTazQUzoQ5IV1qRNiGN06WS58vn6B-Z1CBA",
                "align": "start",
                "action": {
                  "type": "uri",
                  "uri": "line://app/1643963120-oYbGLGry?type=text&text=help"
                },
                "size": "full",
                "margin": "xxl",
                "aspectMode": "cover",
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "text": "HELP",
                    "size": "sm",
                    "action": {
                      "type": "uri",
                      "uri": "line://app/1643963120-oYbGLGry?type=text&text=help"
                    },
                    "align": "center",
                    "color": "#6F4E37",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "flex": 1
                  }
                ]
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSnMaJwLCyfIFBSZGJmXeAXX4PUE3WpsgAskIh2Kt40SJpTGDQW",
                "align": "start",
                "action": {
                  "type": "uri",
                  "uri": "line://app/1643963120-oYbGLGry?type=text&text=hiburan"
                },
                "size": "full",
                "margin": "xxl",
                "aspectMode": "cover",
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "text": "HIBURAN",
                    "size": "sm",
                    "action": {
                      "type": "uri",
                      "uri": "line://app/1643963120-oYbGLGry?type=text&text=hiburan"
                    },
                    "align": "center",
                    "color": "#6F4E37",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "flex": 1
                  }
                ]
              },
              {
                "type": "separator", #garis bwah foto2
                "color": "#DC143C"
              }
            ],
            "type": "box",
            "spacing": "xs", #spasi garis kebawah sama tlisan selfbot
            "layout": "vertical" #(foto kebawah) horizontal (foto datar)
          },
          {
            "type": "separator", #garis kebawah
            "color": "#DC143C"
          },
          {
            "type": "box",
            "spacing": "xs",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://i.pinimg.com/originals/5e/ba/da/5ebada17a183f5778cf4982c5fb1e8e4.png",
                "action": {
                  "type": "uri",
                  "uri": "line://app/1643963120-oYbGLGry?type=text&text=settings"
                },
                "align": "start",
                "size": "full",
                "margin": "xxl",
                "aspectMode": "cover",
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "text": "SETTINGS",
                    "size": "sm",
                    "action": {
                      "type": "uri",
                      "uri": "line://app/1643963120-oYbGLGry?type=text&text=settings"
                    },
                    "align": "center",
                    "color": "#6F4E37",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "flex": 1
                  }
                ]
              },
              {
                "type": "separator",
                "color": "#DC143C"
              },
              {
                "type": "image",
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaBDeHHKI6-mRC4YnPjI0hMrWWQGUkB6zUiuprtH5e8TOBcvFlnA",
                "align": "start",
                "action": {
                  "type": "uri",
                  "uri": "line://app/1643963120-oYbGLGry?type=text&text=status"
                },
                "size": "full",
                "margin": "xxl",
                "aspectMode": "cover",
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "text": "STATUS",
                    "size": "sm",
                    "action": {
                      "type": "uri",
                      "uri": "line://app/1643963120-oYbGLGry?type=text&text=status"
                    },
                    "align": "center",
                    "color": "#6F4E37",
                    "wrap": True,
                    "weight": "bold",                      
                    "type": "text",
                    "flex": 1
                  }
                ]
              },
              {
                "type": "separator", #garis bwah foto2
                "color": "#DC143C"
              }
            ]
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"#tulisan selfbot disamping
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "url": "https://obs.line-scdn.net//0hlRsC2XChM31OOhlenbdMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh",
                    "type": "icon",
                    "size": "md"
                    },
                    {
                    "text": "✭emon✭",
                    "size": "sm",
                    "action": {
                      "uri": "http://line.me/ti/p/NmTJyOoQLb",
                      "type": "uri",
                      "label": "Add Creator"
                    },
                    "margin": "xl",
                    "align": "start",
                    "color": "#DC143C",
                    "weight": "bold",
                    "type": "text"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "layout": "horizontal"
          }
        ]
      }  
    }
  ],
  "type": "carousel"
}
}
]
}
                                sendTemplate(to, data)
#==========================================================
                        elif cmd == "me":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               contact = emon.getContact(msg._from)
                               cover = emon.getProfileCoverURL(msg._from)
                               LINKFOTO = "https://os.line.naver.jp/os/p/" + Mid
                               LINKVIDEO = "https://os.line.naver.jp/os/p/" + Mid + "/vp"
                               clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                               clor = random.choice(clr)
                               dataa= {
                                 "messages": [
                                    {
                                      "type": "flex",
                                      "altText": "profile",
                                      "contents":{
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://obs.line-scdn.net/{}".format(contact.picturePath),
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "uri": "https://obs.line-scdn.net/{}".format(contact.picturePath),
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical", #vertical
        "spacing": "xs",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(contact.displayName),
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "align": "center",
            "size": "md",
            "flex": 2
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "type": "text", 
            "text": "{}".format(contact.statusMessage),
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "align": "center",
            "size": "xs",
            "action": {
              "type": "uri",
              "uri": "line://app/1643963120-oYbGLGry?type=video&ocu={}&piu={}".format(LINKVIDEO,LINKFOTO)
            }
          }
        ]
      },
      "styles": {"body": {"backgroundColor": clor},
       }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": cover,
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover",
        "action": {
          "type": "uri",
          "uri": cover,
        }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "spacing": "xs",
        "contents": [
          {
            "type": "text",
            "text": "{}".format(contact.displayName),
            "wrap": True,
            "weight": "bold",
            "color": "#FF0000",
            "align": "center",
            "size": "md",
            "flex": 2
          },
          {
            "type": "separator",
            "color": "#000000"
          },
          {
            "type": "text", 
            "text": "ꓐꓳꓔ ꬴ൱⭙൨",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "align": "center",
            "size": "xs",
            "action": {
              "type": "uri",
              "uri": "line://app/1643963120-oYbGLGry?type=video&ocu={}&piu={}".format(LINKVIDEO,LINKFOTO)
            }
          }
        ]
      },
      "styles": {"body": {"backgroundColor": clor},
       }
    }
  ],
  "type": "carousel"
}
}
]
}
                               sendTemplate(to, dataa)
                #        emon.postTemplate(op.param1,dataa);

                        elif cmd == ".me":
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               contact = emon.getContact(msg._from)
                               LINKFOTO = "https://os.line.naver.jp/os/p/" + Mid
                               LINKVIDEO = "https://os.line.naver.jp/os/p/" + Mid + "/vp"
                               clr = ("#FFF0F5","#B5ECEE","#E4EB85","#B0ABF9","#EAC6F4","#8BEFEF","#C0F785")
                               clor = random.choice(clr)
                               dataa= {
                                 "messages": [
                                    {
                                      "type": "flex",
                                      "altText": "profile",
                                      "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(contact.picturePath),
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "https://obs.line-scdn.net/{}".format(contact.picturePath),
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "xxl",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(contact.displayName),
        "wrap": True,
        "weight": "bold",
        "color": "#FF0000",
        "align": "center",
        "size": "md",
        "flex": 2
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text", 
        "text": "{}".format(contact.statusMessage),
        "color": "#FF0000",
        "wrap": True,
        "weight": "bold",
        "align": "center",
        "size": "xs",
        "action": {
          "type": "uri",
          "uri": "line://app/1643963120-oYbGLGry?type=video&ocu={}&piu={}".format(LINKVIDEO,LINKFOTO)
        }
      }
    ]
  },
  "styles": {"body": {"backgroundColor": clor},
   }
}
}
]
}
                               sendTemplate(to, dataa)
#=========[Sticker]=====================================================================#
                        #elif cmd == "bodo" or text.lower() == 'bodo amat':
                          #if wait["selfbot"] == True:
                           # if msg._from in Owner:
                            #    templatesendSticker(to, "https://stickershop.line-scdn.net/stickershop/v1/sticker/18125796/IOS/sticker_animation@2x.png", "line://shop/detail/1495172")

                        elif cmd == "haha" or text.lower() == 'wkwk':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                templatesendSticker(to, "https://2.bp.blogspot.com/-i6_y7ZczxN8/WQRkLQTPjPI/AAAAAAAHRjM/QqB_sVvFdCsz8PvzO5wQXacG5MNlh1SXgCLcB/s1600/AW419418_06.gif", "line://shop/detail/1495172")
#========================================================
                        elif cmd == "mee":
                          if wait["selfbot"] == True:
                             if msg._from in Owner:
                                contact = emon.getProfile()
                                mids = [contact.mid]
                                status = emon.getContact(sender)
                                data = {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "Emon",
                                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "flex": 2,
            "text": "{}".format(status.displayName),
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "gravity": "center",
            "color": "#657383"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "text",
            "text": "Status Profile:",
            "size": "xs",
            "weight": "bold",
            "wrap": True,
            "color": "#657383"
          },
          {
            "type": "text",
            "text": "{}".format(status.statusMessage),
            "size": "xs",
            "color": "#657383",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "https://obs.line-scdn.net//0hlRsCjKPDM31OOhlr7StMKnJ_PRA5FDU1Ng4uTm86Ph1rXXcoJVt1HGg4ZBpgAnEjcFh6SWo_P0lh"
    },
    "footer": {
      "backgroundColor": "#00BFFF"
    }
  },
  "hero": {
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(emon.getContact(sender).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "Me",
        "size": "xs",
        "wrap": True,
        "weight": "bold",
        "color": "#E5E4E2",
        "action": {
          "type": "uri",
          "uri": "line://app/1643963120-oYbGLGry?type=profile"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      }
    ]
  }
}
}
]
}
                                sendTemplate(to, data)
#=======[HIBURAN]===============================================================
                        elif cmd.startswith("mule "):
                          if msg._from in Owner:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split("-")
                            search = str(count[0])
                            r = requests.get("https://www.smule.com/"+search+"/performances/json")
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                ret_ = "?? [ Record Smule ] ??\n"
                                for aa in data["list"]:
                                    no += 1
                                    ret_ += "\n" + str(no) + ". " + str(aa["title"])
                                ret_ += "\n\nSelanjutnya ketik:smule {}-nomor\nuntuk melihat detailnya. ".format(str(search))
                                emon.sendMessage(msg.to,ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["list"][num - 1]
                                    smule = str(b["web_url"])
                                    c = "?? Judul Oc: "+str(b["title"])
                                    c += "\n?? Pembuat: "+str(b["owner"]["handle"])
                                    c += "\n?? Total like: "+str(b["stats"]["total_loves"])+" like"
                                    c += "\n?? Total comment: "+str(b["stats"]["total_comments"])
                                    c += "\n?? Status VIP: "+str(b["owner"]["is_vip"])
                                    c += "\n?? Status Oc: "+str(b["message"])
                                    c += "\n?? Created Oc: {}".format(b["created_at"][:10])
                                    c += "\n?? Didengarkan: {}".format(b["stats"]["total_listens"])+" orang"
                                    hasil = "?? [ Detail Record ] ??\n\n"+str(c)
                                    dl = str(b["cover_url"])
                                    emon.sendImageWithURL(msg.to,dl)
                                    emon.sendMentionv10(msg.to, hasil, {'AGENT_NAME': ' URL Smule','AGENT_LINK': 'https://www.smule.com/{}'.format(str(b['owner']['handle'])),'AGENT_ICON': 'https://png.icons8.com/color/50/000000/speaker.png' })
                                    with requests.session() as s:
                                        s.headers['user-agent'] = 'Mozilla/5.0'
                                        r = s.get("https://sing.salon/smule-downloader/?url=https://www.smule.com{}".format(urllib.parse.quote(smule)))
                                        data = BeautifulSoup(r.content, 'html5lib')
                                        get = data.select("a[href*=https://www.smule.com/redir?]")[0]
                                        title = data.findAll('h2')[0].text
                                        imag = data.select("img[src*=https://www.smule.com/redir?]")[0]
                                        if 'Smule.m4a' in get['download']:
                                            emon.sendMessage(msg.to,"Type: Audio\n\nPlease wait for audio...")
                                            emon.sendAudioWithURL(msg.to, get['href'])
                                            emon.sendAudioWithURL(msg.to,e)
                                        else:
                                            emon.sendMessage(msg.to,"Type: Video\n\nPlease wait for video...")
                                            emon.sendVideoWithURL(msg.to, get['href'])
                                            emon.sendAudioWithURL(msg.to,e)
                                except Exception as e:
                                    emon.sendMessage(to,"?JANGAN LUPA LIKE N FOLLOWNYA YA GUYZ?\n\n"+str(c))
                                     
                        elif cmd.startswith("mp3 "):
                          if msg._from in Owner:
                                anunya = text.replace("mp3 ","")
                                r = requests.get("https://dzin.me/api/smule/download/?apikey=beta&url={}".format(str(anunya)))
                                music = data["list"][first - 1]
                                a = "🔰 Detail Record:\n"
                                a += "\n• Pembuat Oc: " + str(music['owner']['handle'])
                                a += "\n• Judul: " + str(music["title"])
                                a += "\n• Bio Lagu: " + str(music["message"])
                                a += "\n• Dibuat: " + str(music["created_at"][:10])
                                a += "\n• Didengarkan: " + str(music["stats"]["total_listens"])+" orang"
                                a += "\n• Disukai: " + str(music["stats"]["total_loves"])+" orang"
                                a += "\n• Comment : " + str(music["stats"]["total_comments"])+" komen"
                                a += "\n\n🔰 Waiting For Audio..."
                                image = music['cover_url']
                                emon.sendImageWithURL(to,image)
                                emon.sendMessage(to,a)
                                headers = {}
                                headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                gege = requests.get("https://dzin.me/api/smule/download/?apikey=beta&url={}".format(str(anunya)))
                                soup = BeautifulSoup(gege.content, "html5lib")
                                links = soup.findAll("ul", {"clientass":"sm2-playlist-bd"})
                                for link in links:
                                    URL = link.a['href']
                                emon.sendAudioWithURL(to,URL)

                        elif cmd.startswith("love"):
                          if msg._from in Owner:
                            sep = text.split("|")
                            you = sep[1]
                            lop = sep[2]
                            per = random.randint(1,100)
                            emon.sendReplyMessage(msg_id, to, "Kecocokan {} dan {} adalah {}% :)".format(you, lop, per), contentMetadata={"MSG_SENDER_NAME":"I am Love Percenter","MSG_SENDER_ICON": "http://universeofthoughts.com/wp-content/uploads/2016/01/firstlove-flowers.jpg"})
                            if per >= 80:
                                emon.sendMessage(to, "Cocok Sekaliiiiii ^_^",contentMetadata={"MSG_SENDER_NAME":"I am Love Percenter","MSG_SENDER_ICON": "http://universeofthoughts.com/wp-content/uploads/2016/01/firstlove-flowers.jpg"})
                            if per >= 50 <= 80:
                                    emon.sendMessage(to, "hmm lumayan jodoh :) <3",contentMetadata={"MSG_SENDER_NAME":"I am Love Percenter","MSG_SENDER_ICON": "http://universeofthoughts.com/wp-content/uploads/2016/01/firstlove-flowers.jpg"})
                            if per <= 50:
                                emon.sendMessage(to, "Maaf {} kek nya ngga jodoh haha".format(you),contentMetadata={"MSG_SENDER_NAME":"I am Love Percenter","MSG_SENDER_ICON": "http://universeofthoughts.com/wp-content/uploads/2016/01/firstlove-flowers.jpg"})

                        elif cmd.startswith("img: "):
                          if msg._from in Owner:
                                query = msg.text.replace("img: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        emon.sendImageWithURL(msg.to, str(food["url"]))        

                        elif cmd.startswith("image "):
                          if msg._from in Owner:
                            try:
                                search = cmd.replace("image ","")
                                r = requests.get("https://xeonwz.herokuapp.com/images/google.api?q={}".format(search))
                                data = r.text
                                data = json.loads(data)
                                if data["content"] != []:
                                    items = data["content"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    emon.sendImageWithURL(to, str(path))
                            except Exception as error:
                                 logError(error)
                                 var= traceback.print_tb(error.__traceback__)
                                 emon.sendMessage(to,str(var))

                        elif cmd.startswith("date "):
                          if msg._from in Owner:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            flexHelp1(msg.to,"「 Date Info 」\n"+"╭────────────────\n├❖ Date : "+lahir+"\n├❖ Age : "+usia+"\n├❖ Ultah : "+ultah+"\n├❖ Zodiak : "+zodiak+"\n╰────────────────")

                        elif cmd.startswith("get-zodiak "):
                          if msg._from in Owner:
                            sep = msg.text.split(" ")
                            query = text.replace(sep[0] + " ","")
                            r = requests.post("https://aztro.herokuapp.com/?sign={}&day=today".format(urllib.parse.quote(query)))
                            data = r.text
                            data = json.loads(data)
                            data1 = data["description"]
                            data2 = data["color"]
                            translator = Translator()
                            hasil = translator.translate(data1, dest='id')
                            hasil1 = translator.translate(data2, dest='id')
                            A = hasil.text
                            B = hasil1.text
                            ret_ = "「 Ramalan zodiak {} hari ini 」\n".format(str(query))
                            ret_ += str(A)
                            ret_ += "\n======================\n• Tanggal : " +str(data["current_date"])
                            ret_ += "\n• Rasi bintang : "+query
                            ret_ += " ("+str(data["date_range"]+")")
                            ret_ += "\n• Pasangan Zodiak : " +str(data["compatibility"])
                            ret_ += "\n• Angka keberuntungan : " +str(data["lucky_number"])
                            ret_ += "\n• Waktu keberuntungan : " +str(data["lucky_time"])
                            ret_ += "\n• Warna kesukaan : " +str(B)
                            flexHelp1(msg.to, str(ret_))

                        elif cmd.startswith("text"):
                            txt = removeCmd("text", text)
                            zal = zalgo.zalgo().zalgofy('{}'.format(txt))
                            emon.sendMessage(to, zal)

                        elif cmd.startswith("foto: "):
                            if msg._from in Owner:
                                query = removeCmd("foto:", text)
                                cond = query.split(" ")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []                                	
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1643963120-oYbGLGry?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                          "messages": [
                                            {
                                              "type": "template",
                                              "altText": "image",
                                              "template": {
                                                  "type": "image_carousel",
                                                  "columns": ret_[aa*10 : (aa+1)*10]
                                              }
                                            }
                                          ]
                                        }
                                        sendTemplate(to, data)

                        elif cmd.startswith("searchapp "):
                            if msg._from in Owner:
                                query = removeCmd("searchapp", text)
                                cond = query.split(" ")
                                search = str(cond[0])
                                result = requests.get("http://api.farzain.com/playstore.php?id={}&apikey=KJaOT94NCD1bP1veQoJ7uXc9M".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data != []:
                                    ret_ = []
                                    for music in data:
                                        if 'http://' in music["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(music["icon"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Download",
                                                        "uri": "{}".format(str(music["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                          "messages": [
                                            {
                                              "type": "template",
                                              "altText": "Searching App",
                                              "template": {
                                                  "type": "image_carousel",
                                                  "columns": ret_[aa*10 : (aa+1)*10]
                                              }
                                            }
                                          ]
                                        }
                                        sendTemplate(to, data)
#=======scrip smule====
                        elif msg.text.lower().startswith("song: "):
                          if msg._from in Owner:
                            separate = text.split(" ")
                            channel = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0"
                                r = web.get("http://api.fckveza.com/downloadsmule={}".format(urllib.parse.quote(channel)))
                                data = r.text
                                data = json.loads(data)
                                for design in data["result"]:
                                    image = design["image"]
                                    url = design["url"]
                                data = {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "Smule",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#0000FF"
    },
    "header": {
      "backgroundColor": "#0000FF"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": image,
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "\n🎶MP3🎶\nSMULE",
            "size": "xl",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "align": "center"            
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Song smule\n ᴋᴇᴛɪᴋ sᴏɴɢ:☞ ʟɪɴᴋ sᴍᴜʟᴇ ☜" ,
                "size": "xs",
                "margin": "none",
                "color": "#00FF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#FF0000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴄʀᴇᴀᴛᴏʀ",
                  "uri": "http://line.me/ti/p/NmTJyOoQLb"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#800080",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴅᴏᴡɴʟᴏᴅ ᴍᴘ3",
                  "uri": url
              }
          }]
      }]
  },
  "header": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "D&N",
                "size": "xl",
                "weight": "bold",
                "align": "center",            
                "color": "#FFD700",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
]
}
                                sendTemplate(to, data)
                                emon.sendAudioWithURL(msg.to, url)

                        elif cmd.startswith("sing "): #profile smule
                          if msg._from in Owner:
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] +" ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api.fckveza.com/record={}".format(urllib.parse.quote(links)))
                                ssa = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                time.sleep(2)
                                data = {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "smule",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#FFF0F5"
    },
    "footer": {
      "backgroundColor": "#FFE4E1"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://w1.smule.com/assets/nation/apps/fb_app_icon_sing-987ed8826cef57c25cd8a3f828c8d43a.png",
            "type": "image",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#800080"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "❂➣ ID Smule : "+smule+"\n❂➣ Link:\n"+links ,
                "size": "xs",
                "margin": "none",
                "color": "#00FF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#FF0000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴄʀᴇᴀᴛᴏʀ",
                  "uri": "http://line.me/ti/p/NmTJyOoQLb"
              }
          }, {
              "flex": 2,
              "type": "button",
              "style": "primary",
              "color": "#800080",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴛᴏ sɪɴɢ",
                  "uri": links
              }
          }]
      }]
  }
}
}
]
}
                                sendTemplate(to, data)
                            #    client.postTemplate(to, data)
                            except Exception as e:
                                pass
#=================================
                        elif cmd.startswith("xmusik "):
                           if msg._from in Owner: 
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                hasil = "\nVocalis : "+str(d)
                                hasil += "\nJudul : "+str(c)
                                data = {
                                   "messages": [
                                      {
                                        "type": "flex",
                                        "altText": "xmusik",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#0000FF"
    },
    "header": {
      "backgroundColor": "#0000FF"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": g,
            "type": "image",
            "size": "full",
            "aspectRatio": "20:13",
            "aspectMode": "cover"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FF0000"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": hasil,
                "size": "xs",
                "margin": "none",
                "color": "#00FF00",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#FF0000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴄʀᴇᴀᴛᴏʀ",
                  "uri": "http://line.me/ti/p/NmTJyOoQLb"
              }
          }, {
              "flex": 3,
              "type": "button",
              "style": "primary",
              "color": "#800080",
              "margin": "sm",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴅᴏᴡɴʟᴏᴅ ᴍᴘ3",
                  "uri": e
              }
          }]
      }]
  }
}
}
]
}
                                sendTemplate(to, data)
                                emon.sendAudioWithURL(to,e)
                            except Exception as error:
                                flexHelp1(to, "maaf terjadi kesalahan" + str(error))
                                logError(error)
#=================================
                        elif cmd.startswith("idsmule "): #x tdk di tmukan
                          if msg._from in Owner: 
                                sep = text.split(" ")
                                nama = text.replace(sep[0] + " ","")    
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0'
                                    r = s.get("https://www.smule.com/{}".format(urllib.parse.quote(nama)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    try:
                                        for anu in soup.findAll('script', attrs={'type':'text/javascript'})[1]:
                                            a = anu.replace('DataStore.Pages.Profile =','')
                                            b = a.replace(';','')
                                            get = json.loads(b)
                                            pict = get['user']['pic_url']
                                            ret_ = "Account ID: "+str(get['user']['account_id'])
                                            ret_ += "\nᴜsᴇʀ ɴᴀᴍᴇ: "+str(get['user']['handle'])
                                            ret_ += "\nƒσℓℓσωєrs: "+str(get['user']['followers'])
                                            ret_ += "\nƒσℓℓσω: "+str(get['user']['followees'])
                                            ret_ += "\nρєrƒσrмαทcєs: "+str(get['user']['num_performances'])
                                            ret_ += "\nᴠɪᴘ sᴛᴀᴛᴜs: "+str(get['user']['is_vip'])
                                            ret_ += "\nDescription:\n❂➢ "+str(get['user']['blurb'])
                                        data = {
                                           "messages": [
                                              {
                                                "type": "flex",
                                                "altText": "smule",
                                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "รtศtนร รɱนɭε ℘гσʄıɭε :",
            "size": "xl",
            "weight": "bold",
            "wrap": True,
            "color": "#FFFF00"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "type": "text",
            "text": ret_,
            "size": "sm",
            "weight": "bold",
            "color": "#00FF00",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#0000FF"
    },
    "header": {
      "backgroundColor": "#0000FF"
    }
  },  
  "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [{
          "type": "box",
          "layout": "horizontal",
          "contents": [{
              "type": "button",
              "flex": 2,
              "style": "primary",
              "color": "#FF0000",
              "height": "sm",
              "action": {
                  "type": "uri",
                  "label": "ᴄʀᴇᴀᴛᴏʀ",
                  "uri": "http://line.me/ti/p/NmTJyOoQLb"
              }
          }]
      }]
  },
  "hero": {
    "aspectMode": "cover",
    "aspectRatio": "20:13",
    "type": "image",
    "url": pict,
    "size": "full",
    "align": "center",
  },
  "header": {
    "type": "box",   
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "D&N",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFFFFF",
        "align": "center"
      }
    ]
  }
}
}
]
}
                                        sendTemplate(to, data)
                                        #client.postTemplate(to, data)
                                    except:
                                        flexHelp1(msg.to, "User tidak ditemukan!")
#===========Hiburan============#
                        elif cmd.startswith("kode cctv"):
                          if msg._from in Owner:
                            ret_ = "📜Daftar Kode Wilayah:\n\n"
                            ret_ += "248 = Alternatif - Cibubur\n119 = Ancol - bandara\n238 = Asia afrika - Bandung\n169 = Asia afrika - Hang lekir"
                            ret_ += "\n276 = Asia afrika - Sudirman\n295 = Bandengan - kota\n294 = Bandengan - Selatan\n255 = Boulevard Barat raya"
                            ret_ += "\n102 = Buncit raya\n272 = Bundaran - HI\n93 = Cideng barat\n289 = Cikini raya\n242 = Ciledug raya - Cipulir"
                            ret_ += "\n175 = Ciloto - Puncak\n142 = Daan mogot - Grogol\n143 = Daan mogot - Pesing\n338 = Dewi sartika - Cawang"
                            ret_ += "\n124 = DI Panjaitan - By pass\n123 = DI Panjaitan - Cawang\n13 = Dr Satrio - Casablanca\n105 = Dr Satrio - Karet"
                            ret_ += "\n245 = Dukuh atas - MRT Jakarta\n334 = Fachrudin raya\n252 = Fatmawati - Blok A\n253 = Fatmawati - Cipete raya"
                            ret_ += "\n203 = Flyover Daan mogot\n336 = Flyover Jati baru\n172 = Flyover Senen - Kramat\n77 = Gunung sahari"
                            ret_ += "\n137 = Hasyim Ashari\n273 = Jalan MH Thamrin\n327 = Jalan RS Fatmawati\n292 = Jl. Otista 3\n333 = Jl. Panjang - Kebon jeruk"
                            ret_ += "\n226 = JORR - Bintaro\n227 = JORR - Fatmawati\n173 = Kramat raya - Senen\n117 = Kyai Caringin - Cideng\n126 = Letjen Suprapto - Senen"
                            ret_ += "\n204 = Mangga besar\n319 = Margaguna raya\n326 = Margonda raya\n310 = Mas Mansyur - Karet\n309 = Mas Mansyur - Tn. Abang"
                            ret_ += "\n64 = Matraman\n140 = Matraman - Salemba\n284 = Metro Pdk. Indah\n191 = MT Haryono - Pancoran\n160 = Pancoran barat"
                            ret_ += "\n331 = Pejompongan - Slipi\n332 = Pejompongan - Sudirman\n312 = Perempatan pramuka\n171 = Permata hijau - Panjang\n99 = Petojo Harmoni"
                            ret_ += "\n223 = Pramuka - Matraman\n222 = Pramuka raya\n314 = Pramuka raya - jl. Tambak\n313 = Pramuka - Salemba raya\n130 = Puncak raya KM84"
                            ret_ += "\n318 = Radio dalam raya\n328 = RS Fatmawati - TB\n274 = Senayan city\n132 = Slipi - Palmerah\n133 = Slipi - Tomang"
                            ret_ += "\n162 = S Parman - Grogol\n324 = Sudirman - Blok M\n18 = Sudirman - Dukuh atas\n325 = Sudirman - Semanggi\n112 = Sudirman - Setiabudi"
                            ret_ += "\n246 = Sudirman - Thamrin\n320 = Sultan agung - Sudirman\n100 = Suryo pranoto\n220 = Tanjung duren\n301 = Tol kebon jeruk"
                            ret_ += "\n41 = Tomang/Simpang\n159 = Tugu Pancoran\n145 = Warung jati - Pejaten\n205 = Yos Sudarso - Cawang\n206 = Yos Sudarso - Tj. Priuk"
                            ret_ += "\n\nUntuk melihat cctv!\nKetik {}lihat: (no kode)".format(str(Setmain["keyCommand"]))                          
                            data = {"messages":[{"type":"text","text": ret_,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                            sendTemplate(msg.to, data)
#=====================================
                        elif cmd.startswith("lihat: "):
                          if msg._from in Owner:
                            sep = msg.text.split(" ")
                            cct = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
                                r = s.get("http://lewatmana.com/cam/{}/bundaran-hi/".format(str(urllib.parse.quote(cct))))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                try:
                                    ret_ = "📜Info cctv:\n\n• Area: "
                                    ret_ += soup.select("[class~=cam-viewer-title]")[0].text
                                    ret_ += "\n\n📜 Untuk hasil lain ketik {}: no ♪".format(str(Setmain["keyCommand"]))
                                    vid = soup.find('source')['src']
                                    flexHelp1(to, ret_)
                                    emon.sendVideoWithURL(to, vid)
                                except:
                                	flexHelp1(to, "Data cctv tidak ditemukan!")
#==========[AL-QUR`AN]==============================================
                        elif cmd.startswith("murrotal"): #mp3
                          if msg._from in Owner:
                            try:
                                sep = text.split(" ")
                                txt = int(text.replace(sep[0] + " ",""))
                                if 0 < txt < 115:
                                    if txt not in [2,3,4,5,6,7,9,10,11,12,16,17,18,20,21,23,26,37]:
                                        if len(str(txt)) == 1:
                                            audionya = "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-00" + str(txt) + "-muslimcentral.com.mp3"
                                            emon.sendAudioWithURL(to, audionya)
                                        elif len(str(txt)) == 2:
                                            audionya =  "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-0" + str(txt) + "-muslimcentral.com.mp3"
                                            emon.sendAudioWithURL(to, audionya)
                                        else:
                                            audionya =  "https://audio5.qurancentral.com/mishary-rashid-alafasy/mishary-rashid-alafasy-" + str(txt) + "-muslimcentral.com.mp3"
                                            emon.sendAudioWithURL(to, audionya)
                                    else:
                                        flexHelp1(to, "sorri surah is too long")
                                else:
                                    emon.sendMessage(to, "Holy Qur'an Only have 114 surah :)")
                            except Exception as error:
                                flexHelp1(to, "error\n"+str(error))
                          #      logError(error)
#=====================================
                        elif cmd.startswith("al-qur'an"): #ayat
                          if msg._from in Owner:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            web = requests.get("http://api.alquran.cloud/surah/{}".format(txt))
                            data = web.json()
                            result = "~[~{}~]~".format(data["data"]["englishName"])
                            quran = data["data"]
                            result += "\n~ Surah ke {} ~".format(quran["number"])
                            result += "\n~ Nama Surah ~ {} ~".format(quran["name"])
                            result += "\n~ {} Ayat ~".format(quran["numberOfAyahs"])
                            result += "\n~ {} ~".format(quran["name"])
                    #        result += "\n~ Ayat Sajadah = {} ~".format(quran["ayahs"][0]["sajda"])
                            result += "\n==============================\n"
                            no = 0
                            for ayat in data["data"]["ayahs"]:
                                no += 1
                                result += "\n{}. {}".format(no,ayat['text'])
                            k = len(result)//10000
                            for aa in range(k+1):
                                mons = '{}'.format(result[aa*10000 : (aa+1)*10000])
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)
#=====================================
                        elif cmd == "listquran":
                          if msg._from in Owner:
                              ret_ = "List Al-Quran:"
                              ret_ += "\n╭────────╮"
                              ret_ += "\n├❖ 1. Al-Faatiha"
                              ret_ += "\n├❖ 2. Al-Baqara"
                              ret_ += "\n├❖ 3. Aal-i-Imraan"
                              ret_ += "\n├❖ 4. An-Nisaa"
                              ret_ += "\n├❖ 5. Al-Maaida"
                              ret_ += "\n├❖ 6. Al-An'aam"
                              ret_ += "\n├❖ 7. Al-A'raaf"
                              ret_ += "\n├❖ 8. Al-Anfaal"
                              ret_ += "\n├❖ 9. At-Tawba"
                              ret_ += "\n├❖ 10. Yunus"
                              ret_ += "\n├❖ 11. Hud"
                              ret_ += "\n├❖ 12. Yusuf"
                              ret_ += "\n├❖ 13. Ar-Ra'd"
                              ret_ += "\n├❖ 14. Ibrahim"
                              ret_ += "\n├❖ 15. Al-Hijr"
                              ret_ += "\n├❖ 16. An-Nahl"
                              ret_ += "\n├❖ 17. Al-Israa"
                              ret_ += "\n├❖ 18. Al-Kahf"
                              ret_ += "\n├❖ 19. Maryam"
                              ret_ += "\n├❖ 20. Taa-Haa"
                              ret_ += "\n├❖ 21. Al-Anbiyaa"
                              ret_ += "\n├❖ 22. Al-Hajj"
                              ret_ += "\n├❖ 23. Al-Muminoon"
                              ret_ += "\n├❖ 24. An-Noor"
                              ret_ += "\n├❖ 25. Al-Furqaan"
                              ret_ += "\n├❖ 26. Ash-Shu'araa"
                              ret_ += "\n├❖ 27. An-Naml"
                              ret_ += "\n├❖ 28. Al-Qasas"
                              ret_ += "\n├❖ 29. Al-Ankaboot"
                              ret_ += "\n├❖ 30. Ar-Room"
                              ret_ += "\n├❖ 31. Luqman"
                              ret_ += "\n├❖ 32. As-Sajda"
                              ret_ += "\n├❖ 33. Al-Ahzaab"
                              ret_ += "\n├❖ 34. Saba"
                              ret_ += "\n├❖ 35. Faatir"
                              ret_ += "\n├❖ 36. Yaseen"
                              ret_ += "\n├❖ 37. As-Saaffaat"
                              ret_ += "\n├❖ 38. Saad"
                              ret_ += "\n├❖ 39. Az-Zumar"
                              ret_ += "\n├❖ 40. Ghafir"
                              ret_ += "\n├❖ 41. Fussilat"
                              ret_ += "\n├❖ 42. Ash-Shura"
                              ret_ += "\n├❖ 43. Az-Zukhruf"
                              ret_ += "\n├❖ 44. Ad-Dukhaan"
                              ret_ += "\n├❖ 45. Al-Jaathiya"
                              ret_ += "\n├❖ 46. Al-Ahqaf"
                              ret_ += "\n├❖ 47. Muhammad"
                              ret_ += "\n├❖ 48. Al-Fath"
                              ret_ += "\n├❖ 49. Al-Hujuraat"
                              ret_ += "\n├❖ 50. Qaaf"
                              ret_ += "\n├❖ 51. Adh-Dhaariyat"
                              ret_ += "\n├❖ 52. At-Tur"
                              ret_ += "\n├❖ 53. An-Najm"
                              ret_ += "\n├❖ 54. Al-Qamar"
                              ret_ += "\n├❖ 55. Ar-Rahmaan"
                              ret_ += "\n├❖ 56. Al-Waaqia"
                              ret_ += "\n├❖ 57. Al-Hadid"
                              ret_ += "\n├❖ 58. Al-Mujaadila"
                              ret_ += "\n├❖ 59. Al-Hashr"
                              ret_ += "\n├❖ 60. Al-Mumtahana"
                              ret_ += "\n├❖ 61. As-Saff"
                              ret_ += "\n├❖ 62. Al-Jumu'a"
                              ret_ += "\n├❖ 63. Al-Munaafiqoon"
                              ret_ += "\n├❖ 64. At-Taghaabun"
                              ret_ += "\n├❖ 65. At-Talaaq"
                              ret_ += "\n├❖ 66. At-Tahrim"
                              ret_ += "\n├❖ 67. Al-Mulk"
                              ret_ += "\n├❖ 68. Al-Qalam"
                              ret_ += "\n├❖ 69. Al-Haaqqa"
                              ret_ += "\n├❖ 70. Al-Ma'aarij"
                              ret_ += "\n├❖ 71. Nooh"
                              ret_ += "\n├❖ 72. Al-Jinn"
                              ret_ += "\n├❖ 73. Al-Muzzammil"
                              ret_ += "\n├❖ 74. Al-Muddaththir"
                              ret_ += "\n├❖ 75. Al-Qiyaama"
                              ret_ += "\n├❖ 76. Al-Insaan"
                              ret_ += "\n├❖ 77. Al-Mursalaat"
                              ret_ += "\n├❖ 78. An-Naba"
                              ret_ += "\n├❖ 79. An-Naazi'aat"
                              ret_ += "\n├❖ 80. Abasa"
                              ret_ += "\n├❖ 81. At-Takwir"
                              ret_ += "\n├❖ 82. Al-Infitaar"
                              ret_ += "\n├❖ 83. Al-Mutaffifin"
                              ret_ += "\n├❖ 84. Al-Inshiqaaq"
                              ret_ += "\n├❖ 85. Al-Burooj"
                              ret_ += "\n├❖ 86. At-Taariq"
                              ret_ += "\n├❖ 87. Al-A'laa"
                              ret_ += "\n├❖ 88. Al-Ghaashiya"
                              ret_ += "\n├❖ 89. Al-Fajr"
                              ret_ += "\n├❖ 90. Al-Balad"
                              ret_ += "\n├❖ 91. Ash-Shams"
                              ret_ += "\n├❖ 92. Al-Lail"
                              ret_ += "\n├❖ 93. Ad-Dhuhaa"
                              ret_ += "\n├❖ 94. Ash-Sharh"
                              ret_ += "\n├❖ 95. At-Tin"
                              ret_ += "\n├❖ 96. Al-Alaq"
                              ret_ += "\n├❖ 97. Al-Qadr"
                              ret_ += "\n├❖ 98. Al-Bayyina"
                              ret_ += "\n├❖ 99. Az-Zalzala"
                              ret_ += "\n├❖ 100. Al-Aadiyaat"
                              ret_ += "\n├❖ 101. Al-Qaari'a"
                              ret_ += "\n├❖ 102. At-Takaathur"
                              ret_ += "\n├❖ 103. Al-Asr"
                              ret_ += "\n├❖ 104. Al-Humaza"
                              ret_ += "\n├❖ 105. Al-Fil"
                              ret_ += "\n├❖ 106. Quraish"
                              ret_ += "\n├❖ 107. Al-Maa'un"
                              ret_ += "\n├❖ 108. Al-Kawthar"
                              ret_ += "\n├❖ 109. Al-Kaafiroon"
                              ret_ += "\n├❖ 110. An-Nasr"
                              ret_ += "\n├❖ 111. Al-Masad"
                              ret_ += "\n├❖ 112. Al-Ikhlaas"
                              ret_ += "\n├❖ 113. Al-Falaq"
                              ret_ += "\n├❖ 114. An-Naas"
                              ret_ += "\n╰✦ ʙʏ : ✰ emon-вσт ✰" 
                              ret_ += "\nMp3 ketik:\n murrotal (no)".format(str(Setmain["keyCommand"]))
                              ret_ += "\nAyat ketik: \n Al-qur'an (no)".format(str(Setmain["keyCommand"]))
                              #flexHelp1(to, str(ret_))
                              data = {"messages":[{"type":"text","text": ret_,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                              sendTemplate(msg.to, data)
#=====================================
                        elif cmd.startswith("get-quran:"):
                            if msg._from in Owner:      
                                try:
                                    sep = msg.text.split(" ")
                                    search = msg.text.replace(sep[0] + " ","")
                                    with requests.session() as web:
                                        r = requests.get("http://api.alquran.cloud/surah/{}/ar.alafasy".format(str(search)))
                                        data = r.text
                                        data = json.loads(data)
                                        no = 0
                                        ret_ = "Quran Surah {}/{}\nSurah Ke-{}".format(str(data["data"]["englishName"]),str(data["data"]["name"]),str(data["data"]["number"]))
                                        for quran in data["data"]["ayahs"]:
                                            no += 1
                                            ret_ += "\n{}. {}".format(str(no),quran["text"])
                                        flexHelp1( to, str(ret_))
                                except Exception as error:
                                     pass
#=====================================xxx
                        elif cmd.startswith("mtoh "):
                          if msg._from in Owner:      
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            url = requests.get("http://api.aladhan.com/v1/gToH?date={}".format(txt))
                            data = url.json()
                            result = "~ Hijriah ~ = {}".format(str(data["data"]["hijri"]["date"]))
                            result += "\n~ Masehi ~ = {}".format(str(data["data"]["gregorian"]["date"]))
                            emon.sendMessage(to, result)

                        elif cmd.startswith(".leaveall"):
                           if msg._from in Owner:
                           	gid = emon.getGroupIdsJoined()
                           	for i in gid:
                           		emon.leaveGroup(i)

                        elif cmd.startswith("asmaulhusna"):
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            url = requests.get("http://api.aladhan.com/asmaAlHusna/{}".format(txt))
                            data = url.json()
                            result = "~ Asma Allah ke {} = ~ {} ~".format(txt,data["data"][0]["name"])
                            flexHelp1(to, result)
#=====================================
                        elif cmd == "ayat sajadah":
                          if msg._from in Owner:
                            url = requests.get("http://api.alquran.cloud/sajda/quran-uthmani")
                            data = url.json()
                            result = "~[Ayat Sajadah]~"
                            for ayat in data["data"]["ayahs"]:
                                ayatnya = ayat["text"]
                                result += "\n{}".format(ayatnya)
                                result += "\n Surah {}".format(ayat["surah"]["englishName"])
                            result += "\n ~~~~~~ Juz {} ~~~~~~".format(ayat["juz"])
                            emon.sendMessage(to, result)
#=====================================
                        elif cmd.startswith("jadwal sholat "):
                            sep = text.split(" ")
                            txt = text.replace(sep[0]+ " ","")
                            url = requests.get("https://time.siswadi.com/pray/{}".format(txt))
                            data = url.json()
                            ret_ = "Jadwal {} ".format(txt)
                            ret_ += "\n Date : {}".format(data["time"]["date"])
                            ret_ += "\n Subuh : {}".format(data["data"]["Fajr"])
                            ret_ += "\n Dzuhur : {}".format(data["data"]["Dhuhr"])
                            ret_ += "\n Ashar : {}".format(data["data"]["Asr"])
                            ret_ += "\n Magrib : {}".format(data["data"]["Maghrib"])
                            ret_ += "\n Isha : {}".format(data["data"]["Isha"])
                            ret_ += "\n 1/3 Malam : {}".format(data["data"]["SepertigaMalam"])
                            ret_ += "\n Tengah Malam : {}".format(data["data"]["TengahMalam"])
                            ret_ += "\n 2/3 Malam : {}".format(data["data"]["DuapertigaMalam"])
                            ret_ += "\n  jangan lupa sholat teman :)"
                            flexHelp1(to, str(ret_))
#========================================================
                        elif cmd.startswith("xlagu "):
                            if msg._from in Owner:      
                                def sdc():
                                    kitsunesplit = rynSplitText(msg.text.lower()).split("|")
                                    r = requests.get('https://soundcloud.com/search?q={}'.format(rynSplitText(msg.text.lower())))
                                    soup = BeautifulSoup(r.text,'html5lib')
                                    data = soup.find_all(class_='soundTitle__titleContainer')
                                    data = soup.select('li > h2 > a')
                                    if len(kitsunesplit) == 1:
                                        a = 'Soundcloud';no=0
                                        for b in data:
                                            no+=1
                                            a+= '\n{}. {}'.format(no,b.text)
                                        flexHelp1(to,a)
                                    if len(kitsunesplit) == 2:
                                        a = data[int(kitsunesplit[1])-1];b = list(a)[0]
                                        kk = random.randint(0,999)
                                        flexHelp1(to,' Soundcloud \nJudul: {}\nStatus: Waiting... For Upload'.format(a.text))
                                        hh=subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output {}.mp3 {}'.format(kk,'https://soundcloud.com{}'.format(a.get('href'))))
                                        try:emon.sendAudio(to,'{}.mp3'.format(kk))
                                        except Exception as e:emon.sendMessage(to,' ? ERROR ?\nJudul: {}\nStatus: {}\nImportant: Try again'.format(a.text,e))
                                        os.remove('{}.mp3'.format(kk))
                                ryn = Thread(target=sdc)
                                ryn.daemon = True
                                ryn.start()
                                ryn.join()
#============================================================
                        elif cmd.startswith("smule "): #x
                                if '/' in text:
                                    sep = text.split(" ")
                                    x = len(sep)
                                    smule = sep[x - 1]
                                else:
                                    smule == text.split(" ")[1]               
                                with requests.session() as s:
                                    s.headers['user-agent'] = random.choice(settings["userAgent"])
                                    r = s.get("http://www.singsmule.net//p/{}.html".format(str(smule)))
                                    data = BeautifulSoup(r.content, 'html5lib')
                                    note = data.findAll('div', attrs={'class':'col-md-4'})[3].text
                                    x = data.title.string
                                    title = x.replace('| SingSmule.Net','')
                                    tumb = data.select("img.img-thumbnail")[0]
                                    pict = tumb['src']
                                    if 'Not Available' in note:
                                        aud = data.select('a[href*=https://y-ash.smule.com/]')[0]
                                        m4a = aud['href']
                                        emon.sendMessage(msg.to,"Title :\n"+title)
                                        emon.sendImageWithURL(msg.to, pict)
                                        emon.sendMessage(msg.to,"Type : Audio\nWait for media uploading..!")
                                        emon.sendAudioWithURL(msg.to, m4a)
                                    else:
                                        vid = data.select('a[href*=https://y-ash.smule.com/]')[1]
                                        mp4 = vid['href']
                                        emon.sendMessage(msg.to,"Title :\n"+title)
                                        emon.sendImageWithURL(msg.to, pict)
                                        emon.sendMessage(msg.to,"Type : Video\nWait for media uploading..!")
                                        emon.sendVideoWithURL(msg.to, mp4)
#=====================================
                        elif cmd.startswith(".smule "):
                          if msg._from in Owner:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split("|")
                            search = str(cond[0])
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("https://smule.com/{}/performances/json".format(str(search)))
                                data = r.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    no = 0
                                    ret_ = "Record Smule:"
                                    for smule in data["list"]:
                                        no += 1
                                        ret_ += "\n" + str(no)+"Pembuat Oc "+str(smule['owner']['handle'])
                                        ret_ += "\n     Judul: "+str(smule["title"])
                                    ret_ += "\n\nTotal: {} Record Smule".format(str(len(data["list"])))
                                    ret_ += "\n\nKetik:\n{}.smule {},nomer".format(str(Setmain["keyCommand"]),str(search))
                                    contact = emon.getProfile()
                                    mids = [contact.mid]
                                    name = "YourSmule"
                                    url = 'https://line.me/ti/p/~khent_'
                                    iconlink = 'https://downloadsmulesing.files.wordpress.com/2016/07/smule-free.png'
                                    sendMentionV10(msg.to, str(ret_), str(name), str(url), str(iconlink))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["list"]):
                                        smule = data["list"][num - 1]
                                        r = web.get("https://dzin.me/api/smule/download/?apikey=beta&url={}".format(str(smule["key"])))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["list"][first - 1]:
                                            ret_ = "Oc Smule\n"
                                            ret_ += "\n Pembuat Oc: " + str(smule['owner']['handle'])
                                            ret_ += "\n Judul: " + str(smule["title"])
                                            ret_ += "\n Bio Lagu: " + str(smule["message"])
                                            ret_ += "\n Dibuat: " + str(smule["created_at"][:10])
                                            ret_ += "\n Didengarkan: " + str(smule["stats"]["total_listens"])+" orang"
                                            ret_ += "\n Disukai: " + str(smule["stats"]["total_loves"])+" orang"
                                            ret_ += "\n Comment : " + str(smule["stats"]["total_comments"])+" komen"
                                            ret_ += "\n\n Waiting For Recording..."
                                            image = smule['cover_url']
                                            emon.sendImageWithURL(to,image)
                                            emon.sendMessage(to, str(ret_), {'AGENT_LINK': 'https://line.me/ti/p/~khent_', 'AGENT_ICON': "https://cdn4.iconfinder.com/data/icons/various-icons-2/476/Spotify.png", 'AGENT_NAME': "Music on Spotify"})
                                            emon.sendAudioWithURL(to, str(smule["list"]["mp3"][0]))
#=====================================
                        elif cmd.startswith("smuleid "):
                                sep = text.split(" ")
                                nama = text.replace(sep[0] + " ","")    
                                with requests.session() as s:
                                    s.headers['user-agent'] = 'Mozilla/5.0'
                                    r = s.get("https://www.smule.com/{}".format(urllib.parse.quote(nama)))
                                    soup = BeautifulSoup(r.content, 'html5lib')
                                    try:
                                        ret_ = 'Smule profile'
                                        for anu in soup.findAll('script', attrs={'type':'text/javascript'})[1]:
                                            a = anu.replace('DataStore.Pages.Profile =','')
                                            b = a.replace(';','')
                                            get = json.loads(b)
                                            pict = get['user']['pic_url']
                                            ret_ += "\nAccount ID: "+str(get['user']['account_id'])
                                            ret_ += "\nUsername: "+str(get['user']['handle'])
                                            ret_ += "\nFollowers: "+str(get['user']['followers'])
                                            ret_ += "\nFollowees: "+str(get['user']['followees'])
                                            ret_ += "\nPerformances: "+str(get['user']['num_performances'])
                                            ret_ += "\nVIP Status: "+str(get['user']['is_vip'])
                                            ret_ += "\nVerified: "+str(get['user']['is_verified'])
                                            ret_ += "\nURL: https://www.smule.com/"+str(get['user']['handle'])
                                            ret_ += "\nDescription:\n"+str(get['user']['blurb'])
                                        #flexHelp1(msg.to, ret_)
                                        data = {"messages":[{"type":"text","text": ret_,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                        sendTemplate(msg.to, data)
                                        emon.sendImageWithURL(msg.to, pict)
                                    except:
                                        flexHelp1(msg.to, "User tidak ditemukan!")

                        elif cmd.startswith("1smule "): 
                          if msg._from in Owner:
                                 sep = text.split(" ")
                                 x = len(sep)
                                 smule = sep[x - 1]
                                 with requests.session() as s:
                                      s.headers['user-agent'] = 'Mozilla/5.0'
                                      r = s.get("https://www.smuledownloader.download/{}".format(str(smule)))
                                      data = BeautifulSoup(r.content, 'html5lib')
                                      ret = data.select("div#videodl > p")[0].text
                                      for title in data.findAll('div', attrs={'class':'container ptb'}):
                                          ret_ = title.find('h1').text
                                          if 'No Video File' in ret:
                                              mp3 = data.select("a[href*=7737506]")[0]
                                              yyk = mp3['href']
                                              aud = yyk.replace("https://adf.ly/7737506/","")
                                              audio = aud.replace("\n","")
                                              flexHelp1( to, "Type: Audio\nTitle :\n"+ret_+"\n\n🌎Wait uploading media..!")
                                              emon.sendAudioWithURL(msg.to, audio)
                                          else:
                                              mp4 = data.select("a[href*=7737506]")[1]
                                              yoyok = mp4['href']
                                              video = yoyok.replace("https://adf.ly/7737506/","")
                                              flexHelp1( to, "Type: Video\nTitle :\n"+ret_+"\n\🌎Wait uploading media..!")
                                              emon.sendVideoWithURL(msg.to,video)
#=======================================================
                        elif cmd.startswith("profilesmule: "): #x
                          if msg._from in Owner:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                emon.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                emonFooter( to, "ID Smule : "+smule+"\nLink : "+links)
                                emon.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass                                
#=============================================================
                        elif cmd.startswith("get-anime: "):
                          if msg._from in Owner:
                            kata = removeCmd("get-anime:", text)
                            with _session as web:
                                try:
                                    r = web.get("http://ariapi.herokuapp.com/api/anime/search?q={}".format(urllib.parse.quote(kata)))
                                    data = r.text
                                    data = json.loads(data)
                                    anu = data["result"]["anime"][0]
                                    title = anu['title']
                                    link = anu['link']
                                    ret_ = "[Anime]"
                                    ret_ += "\n\nTitle : {}\nLink : {}".format(str(title), str(link))
                                    data = {"messages":[{"type":"text","text": ret_,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                    sendTemplate(msg.to, data)
                                except:
                                    mons = "data tidak di temukan"
                                    data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                    sendTemplate(msg.to, data)
#=============================================================
                        elif cmd.startswith("siarantv "): #expried
                            sep = text.split(" ")
                            kotanya = text.replace(sep[0] + " ", "")
                            result = requests.get("http://rest.farzain.com/api/acaratv.php?id=" + kotanya + "&apikey=tkj-api12&type=separate")
                            try:
                                data = result.text
                                data = json.loads(data)
                                ret_ = "[ JADWAL SIARAN ]\n"
                                for anu in data:
                                    ret_ += "\n" + str(anu["acara"]) + "(" + str(anu["jam"]) + ")"
                                flexHelp1( to, str(ret_))
                            except Exception as error:
                                flexHelp1( to, "error\n"+str(error))
                                logError(error)
#========================================================
                        elif cmd.startswith("topnews"):
                              if msg._from in Owner: 
                                  dpk=requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                                  data=dpk.text
                                  data=json.loads(data)
                                  hasil = "Top News\n\n"
                                  hasil += "(1) " + str(data["articles"][0]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][0]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][0]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][0]["url"])
                                  hasil += "\n\n(2) " + str(data["articles"][1]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][1]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][1]["author"])   
                                  hasil += "\n     Link : " + str(data["articles"][1]["url"])
                                  hasil += "\n\n(3) " + str(data["articles"][2]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][2]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][2]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][2]["url"])
                                  hasil += "\n\n(4) " + str(data["articles"][3]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][3]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][3]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][3]["url"])
                                  hasil += "\n\n(5) " + str(data["articles"][4]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][4]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][4]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][4]["url"])
                                  hasil += "\n\n(6) " + str(data["articles"][5]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][5]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][5]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][5]["url"])
                                  path = data["articles"][3]["urlToImage"]
                                  data = {"messages":[{"type":"text","text": hasil,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                  sendTemplate(msg.to, data)
                                  emon.sendImageWithURL(msg.to, str(path))
#========================================================
                        elif cmd.startswith("1cak"):
                          if msg._from in Owner:
                              r=requests.get("https://api-1cak.herokuapp.com/random")
                              data=r.text
                              data=json.loads(data)
                              print(data)
                              hasil = "Result :\n"
                              hasil += "\nID : " +str(data["id"])
                              hasil += "\nTitle : " + str(data["title"])
                              hasil += "\nUrl : " + str(data["url"]) 
                              hasil += "\nVotes : " + str(data["votes"])
                              #flexHelp1( to, str(hasil))
                              data = {"messages":[{"type":"text","text": hasil,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                              sendTemplate(msg.to, data)
#========================================================
                        elif cmd.startswith("imagetext "):
                            text_ = removeCmd("imagetext", text)
                            web = _session
                            web.headers["User-Agent"] = random.choice(settings["userAgent"])
                            font = random.choice(["arial","comic"])
                            r = web.get("http://api.img4me.com/?text=%s&font=%s&fcolor=FFFFFF&size=35&bcolor=000000&type=jpg" %(urllib.parse.quote(text_),font))
                            data = str(r.text)
                            if "Error" not in data:
                                path = data
                                emon.sendImageWithURL(to,path)
                            else:
                                flexHelp1( to,"[RESULT] %s" %(data.replace("Error: ")))
#========================================================
                        elif cmd.startswith("get-image: "):
                          if msg._from in Owner:
                            start = time.time()
                            search = removeCmd("get-image:", text)
                            url = "https://xeonwz.herokuapp.com/images/google.api?q=" + urllib.parse.quote(search)
                            with _session as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["status"] == True:
                                    items = data["content"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    emon.sendImageWithURL(to, str(path))
                                    elapsed_time = time.time() - start
                                    emon.sendMessage(to,"[Image Result]\nGot image in %s seconds" %(elapsed_time))
#========================================================
                        elif cmd.startswith("img food: "):
                          if msg._from in Owner:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        emon.sendImageWithURL(msg.to, str(food["url"]))
#===========================================================
                        elif cmd.startswith("get-film:"):
                            proses = msg.text.split(":")
                            get = msg.text.replace(proses[0] + ":","")
                            getfilm = get.split()
                            title = getfilm[0]
                            tahun = getfilm[1]
                            r = requests.get('http://www.omdbapi.com/?t='+title+'&y='+tahun+'&plot=full&apikey=4bdd1d70')
                            start = time.time()
                            data=r.text
                            data=json.loads(data)
                            hasil = "Informasi \n" +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                            hasil += "\n\n " +str(data["Plot"])
                            hasil += "\n\nDirector : " +str(data["Director"])
                            hasil += "\nActors   : " +str(data["Actors"])
                            hasil += "\nRelease : " +str(data["Released"])
                            hasil += "\nGenre    : " +str(data["Genre"])
                            hasil += "\nRuntime   : " +str(data["Runtime"])
                            path = data["Poster"]
                            emon.sendImageWithURL(msg.to, str(path))
                            flexHelp1(msg.to,hasil)
#========================================================
                        elif cmd.startswith("cuaca: "):
                          if msg._from in Owner:
                              separate = msg.text.split(" ")
                              location = msg.text.replace(separate[0] + " ","")
                              r = requests.get("http://api.farzain.com/cuaca.php?id={}&apikey=tkj-api12".format(location))
                              data = r.text
                              data = json.loads(data)
                              hasil = data["respon"]
                              tz = pytz.timezone("Asia/Jakarta")
                              timeNow = datetime.now(tz=tz)
                              ret_ = "╭───[cuaca]───╮"
                              ret_ += "\n├❖ Location : " + location
                             # ret_ += "\n├❖ Cuaca : " + str(hasil["cuaca"])
                              #ret_ += "\n├❖ Deskripsi : " + str(hasil["deskripsi"])
                              ret_ += "\n├❖ Suhu : " + str(hasil["suhu"])
                              ret_ += "\n├❖ Kelembapan : " + str(hasil["kelembapan"])
                              ret_ += "\n├❖ Udara : " + str(hasil["udara"])
                              ret_ += "\n├❖ Angin : " + str(hasil["angin"])
                              ret_ += "\n├──[ Time ]"
                              ret_ += "\n├❖ ️Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                              ret_ += "\n├❖ Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB "
                              ret_ += "\n╰─✦ ʙʏ : ✰ emon- вσт ✰"
                              flexHelp1( to, str(ret_)) 
                              emon.sendImageWitURL(msg.to, str(data["peta_gambar"]))                   
#========================================================
                        elif cmd.startswith("meme"):
                          if msg._from in Owner:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            emon.sendImageWithURL(msg.to, image)
#========================================================
                        elif cmd.startswith("ytmp4: "):
                          if msg._from in Owner:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n☛ Author : ' + str(vid.author)
                                    durasi = '\n☛ Duration : ' + str(vid.duration)
                                    suka = '\n☛ Likes : ' + str(vid.likes)
                                    rating = '\n☛ Rating : ' + str(vid.rating)
                                    deskripsi = '\n☛ Deskripsi : ' + str(vid.description)
                                emon.sendVideoWithURL(msg.to, me)
                                #flexHelp1( to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                flexHelp1( to,str(e))
#==========================================================
                        elif cmd.startswith("profileig: "):
                          if msg._from in Owner:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                emon.sendMessage( to, detail + user + user1 + followers + following + post + link + details)
                                emon.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                emon.sendMessage( to, str(njer))
                                
#===========[SPAM]=============================================
                        elif cmd.startswith('scall '):
                          if msg._from in Owner:
                            if msg.toType == 2:
                                sep = text.split(" ")
                                strnum = text.replace(sep[0] + " ","")
                                num = int(strnum)
                                emon.sendMessage(to, "^_^")
                                for var in range(0,num):
                                   group = emon.getGroup(to)
                                   members = [mem.mid for mem in group.members]
                                   emon.acquireGroupCallRoute(to)
                                 #  emon.inviteIntoGroupCall(to, contactIds=members)

                        elif cmd.startswith('call '):
                          if msg._from in Owner:
                            sep = text.split(" ")
                            num = int(sep[1])
                            try:                           
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        for var in range(0,num):
                                            group = emon.getGroup(to)
                                            members = [ls]
                                            kunkun = emon.getContact("uccd51ba9f22f686238f2949357c04c53").displayName
                                            emon.acquireGroupCallRoute(to)
                                            emon.inviteIntoGroupCall(to, contactIds=members)
                                        emon.sendMention(to, "^_^ @!", [ls])
                            except Exception as error:
                                emon.sendMessage(to, str(error))

                        elif cmd.startswith('tag '):
                          if msg._from in Owner:
                            sep = text.split(" ")
                            num = int(sep[1])                           
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    for var in range(0,num):
                                        emon.sendMention(to, "@!", [ls])


#===========[TRANSLATE]===================================================================# 
                        elif msg.text.lower().startswith("tr-af "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='af')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sq "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sq')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-am "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='am')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ar "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ar')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hy "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hy')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-az "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='az')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-eu "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='eu')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-be "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='be')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bn "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bn')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bs "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bs')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bg "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bg')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ca "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ca')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ceb "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ceb')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ny "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ny')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zh-cn "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zh-cn')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zh-tw "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zh-tw')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-co "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='co')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hr "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hr')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-cs "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='cs')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-da "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='da')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-nl "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='nl')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-en "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='en')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-et "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='et')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fi "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fi')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fr "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fr')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fy "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fy')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-yo "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='yo')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zu "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zu')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fil "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fil')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-he "):
                          if wait["selfbot"] == True:
                           if msg._from in Owner:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='he')
                            A = hasil.text
                            emon.sendMessage(msg.to, A)
#===========[SETTING]=======================================
                        elif 'Simi ' in msg.text:
                              spl = msg.text.replace('Simi ','')
                              if spl == 'on':
                                  if msg.to in simisimi:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       simisimi.append(msg.to)
                                       ginfo = emon.getGroup(msg.to)
                                       msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                  flexHelp1( to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in simisimi:
                                         simisimi.remove(msg.to)
                                         ginfo = emon.getGroup(msg.to)
                                         msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Simi-simi Sudah Tidak Aktif"
                                    flexHelp1( to, "「Dinonaktifkan」\n" + msgs) 
#========================================================
                        elif 'Autotrans th-' in msg.text:
                              spl = msg.text.replace('Autotrans th-','')
                              if spl == 'on':
                                  if msg.to in translateth:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateth.append(msg.to)
                                       ginfo = emon.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  emon.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateth:
                                         translateth.remove(msg.to)
                                         ginfo = emon.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    emon.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                    
                                    
                        elif 'Autotrans en-' in msg.text:
                              spl = msg.text.replace('Autotrans en-','')
                              if spl == 'on':
                                  if msg.to in translateen:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateen.append(msg.to)
                                       ginfo = emon.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  emon.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateen:
                                         translateen.remove(msg.to)
                                         ginfo = emon.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    emon.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
#=========== [ Add Sticker ] ==================================
                        elif cmd.startswith("+sticker "):
                          if msg._from in Owner:
                                proses = text.split(" ")
                                nama = text.replace(proses[0] + " ","")
                                try:
                                    if nama in wait["emontikel"]:
                                        flexHelp1(msg.to,"Nama tersebut sudah ada")
                                    else:
                                        wait["memproses"] = nama
                                        wait["tstiker"] = True
                                        f=codecs.open("wait.json","w","utf-8")
                                        json.dump(wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        flexHelp1(msg.to,"Kirim stikernya")
                                except Exception as e:
                                    emon.sendMessage(msg.to,"{}".format(str(e)))
                                    
                        elif cmd.startswith("-sticker "):
                          if msg._from in Owner:
                                proses = text.split(" ")
                                nama = text.replace(proses[0] + " ","")
                                try:
                                    if nama not in wait["emontikel"]:
                                        emon.sendText(msg.to,"Nama tersebut tidak ada")
                                    else:
                                        del wait["emontikel"][nama]
                                        f=codecs.open("wait.json","w","utf-8")
                                        json.dump(wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        flexHelp1(msg.to,"Stiker terhapus")
                                except Exception as e:
                                    emon.sendMessage(msg.to,"{}".format(str(e)))

                        elif cmd.startswith("liststicker"):
                          if msg._from in Owner:
                                if wait["emontikel"] == {}:
                                    flexHelp1(msg.to,"Stiker belum ada")
                                else:
                                    no = 0
                                    hasil = "List\n"
                                    for a in wait["emontikel"]:
                                        no += 1
                                        hasil += "\n" +str(no)+". " +str(a)
                                    hasil += "\n\nTotal %i Stiker" % len(wait["emontikel"])
                                    flexHelp1(msg.to, hasil)
                        elif text.lower() in wait["emontikel"]:
                          #  if msg._from in Owner:
                                    #emon.sendMessage(to,text=None,contentMetadata=wait["kimliststiker"][text.lower()], contentType=7)
                                    query = wait["emontikel"][text.lower()]["STKID"]
                                    spkg = wait["emontikel"][text.lower()]["STKPKGID"]
                                    sticker = requests.get('https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/IOS/sticker_animation@2x.png').text
                                    if sticker == "404 Not Found":
                                       data = {
                                          "messages": [{
                                              "type": "template",
                                              "altText": "{} mengirim stiker".format(emon.getContact(msg._from).displayName),
                                              "baseSize": {
                                                  "height": 1040, 
                                                  "width": 1040 
                                              }, 
                                              "template": {
                                                  "type": "image_carousel",
                                                  "imageAspectRatio": "square",
                                                  "imageSize": "cover",
                                                  "columns": [{
                                                      "imageUrl": 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png',
                                                      "action": {
                                                          "type": "uri",
                                                          "uri": "line://shop/detail/{}".format(spkg),
                                                          "area": {
                                                              "x": 520,
                                                              "y": 0,
                                                              "width": 520,
                                                              "height": 1040
                                                          }
                                                      }
                                                  }]
                                              }
                                          }]
                                       }
                                       sendTemplate(to, data)
                                    else:
                                       data = {
                                          "messages": [{
                                              "type": "template",
                                              "altText": "{} mengirim stiker".format(emon.getContact(msg._from).displayName),
                                              "baseSize": {
                                                  "height": 1040, 
                                                  "width": 1040 
                                              }, 
                                              "template": {
                                                  "type": "image_carousel",
                                                  "imageAspectRatio": "square",
                                                  "imageSize": "cover",
                                                  "columns": [{
                                                      "imageUrl": 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/IOS/sticker_animation@2x.png',
                                                      "action": {
                                                          "type": "uri",
                                                          "uri": "line://shop/detail/{}".format(spkg),
                                                          "area": {
                                                              "x": 520,
                                                              "y": 0,
                                                              "width": 520,
                                                              "height": 1040
                                                          }
                                                      }
                                                  }]
                                              }
                                          }]
                                       }
                                       sendTemplate(to, data)
#=========== [ Add Video ] ============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in Owner:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = emon.getGroup(msg.to)
                                       msgs = "di Group : " +str(ginfo.name)
                                  emonFooter(msg.to, "Sambutan on\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = emon.getGroup(msg.to)
                                         msgs = "di Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    emonFooter(msg.to, "Sambutan off\n" + msgs)       
#===========KICKOUT============#                  
                        elif ("sbkick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           emon.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#==========================================================
                        elif cmd == "+admin on" or text.lower() == '+admin on':
                            if msg._from in Owner:
                                wait["addadmin"] = True
                                emonFooter( to,"Silahkan Kirim kontaknya...")

                        elif cmd == "+admin off" or text.lower() == '+admin off':
                            if msg._from in Owner:
                                wait["addadmin"] = False
                                emonFooter( to,"Add admin dinonaktifkan")

                        elif cmd == "-admin on" or text.lower() == '-admin on':
                            if msg._from in Owner:
                                wait["delladmin"] = True
                                emonFooter( to,"Silahkan Kirim kontaknya...")

                        elif cmd == "-admin off" or text.lower() == '-admin off':
                            if msg._from in Owner:
                                wait["delladmin"] = False
                                emonFooter( to,"Delladmin dinonaktifkan.")
#==========================================================
                        elif cmd == "+staff on" or text.lower() == '+staff on':
                            if msg._from in Owner:
                                wait["addstaff"] = True
                                emonFooter( to,"Silahkan Kirim kontaknya...")

                        elif cmd == "+staff off" or text.lower() == '+staff off':
                            if msg._from in Owner:
                                wait["addstaff"] = False
                                emonFooter( to,"Add staff dinonaktifkan")

                        elif cmd == "-staff on" or text.lower() == '-staff on':
                            if msg._from in Owner:
                                wait["dellstaff"] = True
                                emonFooter( to,"Silahkan Kirim kontaknya...")

                        elif cmd == "-staff off" or text.lower() == '-staff off':
                            if msg._from in Owner:
                                wait["dellstaff"] = False
                                emonFooter( to,"Dell staff dinonaktifkan")
#==========================================================
                        elif cmd == "+bot on" or text.lower() == '+bot on':
                            if msg._from in Owner:
                                wait["addbots"] = True
                                emonFooter( to,"Silahkan Kirim kontaknya...")

                        elif cmd == "+bot off" or text.lower() == '+bot off':
                            if msg._from in Owner:
                                wait["addbots"] = False
                                emonFooter( to,"Add bot dinonaktifkan")

                        elif cmd == "-bot on" or text.lower() == '-bot on':
                            if msg._from in Owner:
                                wait["dellbots"] = True
                                emonFooter( to,"Silahkan Kirim kontaknya...")

                        elif cmd == "-bot off" or text.lower() == '-bot off':
                            if msg._from in Owner:
                                wait["dellbots"] = False
                                emonFooter( to,"Silahkan Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in Owner:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                mons = "Berhasil di Refresh..."
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)
                                #flexHelp1( to,"➥Berhasil di Refresh...")
#===========================================================
                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in Owner:
                                ma = ""
                                for i in admin:
                                    ma = emon.getContact(i)
                                    emon.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in Owner:
                                ma = ""
                                for i in staff:
                                    ma = emon.getContact(i)
                                    emon.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in Owner:
                                ma = ""
                                for i in Bots:
                                    ma = emon.getContact(i)
                                    emon.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["Mentionkick"] = True
                                emonFooter( to,"Notag berhasil diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["Mentionkick"] = False
                                emonFooter( to,"Notag berhasil dinonaktifkan")
#===========COMMAND ON OFF============#
                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["contact"] = True
                                emonFooter( to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["contact"] = False
                                emonFooter( to,"Deteksi contact dinonaktifkan")
#===========COMMAND ON OFF============#
                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["autoRespon"] = True
                                mons = "Auto respon diaktifkan"
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)
                               # flexHelp1( to,"➥Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["autoRespon"] = False
                                mons = "Auto respon dinonaktifkan"
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)
                                #flexHelp1( to,"➥Auto respon dinonaktifkan")

                        elif cmd == "responpm on" or text.lower() == 'responpm on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["autoRespon1"] = True
                                mons = "Auto respon diaktifkan"
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)
                               # flexHelp1( to,"➥Auto respon diaktifkan")

                        elif cmd == "responpm off" or text.lower() == 'responpm off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["autoRespon1"] = False
                                mons = "Auto respon dinonaktifkan"
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)
                                #flexHelp1( to,"➥Auto respon dinonaktifkan")
#===========COMMAND ON OFF============#
                        elif cmd == "autoread on":
                          if msg._from in Owner:
                            if wait["autoRead"] == True:
                                emonFooter(to, "Auto read telah aktif")
                            else:
                                wait["autoRead"] = True
                                emonFooter(to, "Berhasil mengaktifkan auto read")
                        elif cmd == "autoread off":
                          if msg._from in Owner:
                            if wait["autoRead"] == False:
                                emonFooter(to, "Auto read telah nonaktif")
                            else:
                                wait["autoRead"] = False
                                emonFooter(to, "Berhasil menonaktifkan auto read")
                                
                        elif cmd == "autoblock on" or text.lower() == 'block on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["autoBlock"] = True
                                emon.sendMessage(msg.to,"「 Status autoblock 」\n telah diaktifkan")
                                
                        elif cmd == "autoblock off" or text.lower() == 'block off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["autoBlock"] = False
                                emon.sendMessage(msg.to,"「 Status autoblock 」\n telah dinonaktifkan")
                                
                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["autoJoin"] = True
                                emonFooter( to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["autoJoin"] = False
                                emonFooter( to,"Autojoin dinonaktifkan")
#===========COMMAND ON OFF============#
                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["autoLeave"] = True
                                emonFooter( to,"Auto Leave Diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["autoLeave"] = False
                                emonFooter( to,"Auto Leave dinonaktifkan")
#===========COMMAND ON OFF============#
                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["autoAdd"] = True
                                emonFooter( to,"Auto Add Diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["autoAdd"] = False
                                emonFooter( to,"Auto Add dinonaktifkan")
#===========COMMAND ON OFF============#
                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["sticker"] = True
                                emonFooter( to,"Detect Sticker Diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["sticker"] = False
                                emonFooter( to,"Detect Sticker dinonaktifkan")
#===========COMMAND ON OFF============#
                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                settings["autoJoinTicket"] = True
                                emonFooter( to,"Join Ticket Diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                settings["autoJoinTicket"] = False
                                emonFooter( to,"Join Ticket dinonaktifkan")
#===========COMMAND ON OFF============#
                        elif cmd == "auto like" or text.lower() == 'auto like':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               wait["likeOn"] = True
                               emonFooter( to, " Shere Post")                

                        elif cmd == "auto like off" or text.lower() == 'auto like off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               wait["likeOn"] = False
                               emonFooter( to, " autolike dinonaktifkan")                
#===========COMMAND BLACKLIST============#
                        elif ("+talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           emonFooter(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("-talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           emonFooter(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass
#===========COMMAND BLACKLIST============#
                        elif cmd == "+talkban on" or text.lower() == '+talkban on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["Talkwblacklist"] = True
                                #emon.sendMessage(msg.to,"Kirim kontaknya...")
                                mons = "Kirim kontaknya..."
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)

                        elif cmd == "+talkban off" or text.lower() == '+talkban off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["Talkwblacklist"] = False
                        #        emon.sendMessage(msg.to,"Talkban contact dinonaktifkan")
                                mons = "Talkban contact dinonaktifkan..."
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)

                        elif cmd == "-talkban on" or text.lower() == '-talkban on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["Talkdblacklist"] = True
                            #    emon.sendMessage(msg.to,"Kirim kontaknya...")
                                mons = "kirim kontaknya"
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)

                        elif cmd == "-talkban off" or text.lower() == '-talkban off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["Talkdblacklist"] = False
                              #  emon.sendMessage(msg.to,"Untalkban contact dinonaktifkan")
                                mons = "Untalkban contact dinonaktifkan..."
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)
#==========================================================
                        elif ("+ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           emonFooter(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("-ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           emonFooter(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass
#=======================================================
                        elif cmd == "+ban on" or text.lower() == '+ban on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["wblacklist"] = True
                            #    emon.sendMessage(msg.to,"Kirim kontaknya...")
                                mons = "kirim kontak nya"
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)

                        elif cmd == "+ban off" or text.lower() == '+ban off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["wblacklist"] = False
                            #    emon.sendMessage(msg.to,"Ban contact dinonaktifkan")
                                mons = "Ban contak dinonaktifkan..."
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)


                        elif cmd == "-ban on" or text.lower() == '-ban on':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["dblacklist"] = True
                              #  emon.sendMessage(msg.to,"Kirim kontaknya...")
                                mons = "Kirim kontaknya"
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)

                        elif cmd == "-ban off" or text.lower() == '-ban off':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                                wait["dblacklist"] = False
                              #  emon.sendMessage(msg.to,"Unban contatc dinonaktifkan")
                                mons = "Unban contak dinonaktifkan..."
                                data = {"messages":[{"type":"text","text": mons,"sentBy":{"label":" 『🔴Nurtin💓Dewi🔴』","iconUrl":'http://dl.profile.line-cdn.net/{}'.format(emon.getContact(msg._from).pictureStatus),"linkUrl":"http://line.me/ti/p/NmTJyOoQLb"}}]}
                                sendTemplate(msg.to, data)
#=======================================================
                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                              if wait["blacklist"] == {}:
                                emonFooter( to, "Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +emon.getContact(m_id).displayName + "\n"
                                emonFooter( to," Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                              if wait["Talkblacklist"] == {}:
                                emon.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +emon.getContact(m_id).displayName + "\n"
                                emon.sendMessage(msg.to," Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                              if wait["blacklist"] == {}:
                                    emon.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = emon.getContact(i)
                                        emon.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clban" or text.lower() == 'clban':
                          if wait["selfbot"] == True:
                            if msg._from in Owner:
                              wait["blacklist"] = {}
                              ragets = emon.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              emonFooter(to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif cmd == "setsticker sider":
                          if msg._from in Owner:
                              Setmain["AddstickerSider"]["status"] = True
                              flexHelp1( to, "kirim stickernya ") 

                        elif cmd == "setsticker tag":
                          if msg._from in Owner:
                              Setmain["AddstickerTag"]["status"] = True
                              flexHelp1( to, "kirim stickernya ") 

                        elif 'Set pesan: ' in msg.text:
                           if msg._from in Owner:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  emonFooter( to, "Gagal mengganti Pesan Message")
                              else:
                                  wait["message"] = spl
                                  emonFooter( to, "「Pesan Msg」\nPesan Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in Owner:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  emonFooter( to, "Gagal mengganti Welcome Message")
                              else:
                                  wait["welcome"] = spl
                                  emonFooter( to, "Welcome Message diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           if msg._from in Owner:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  emonFooter( to, "Gagal mengganti Leave Message")
                              else:
                                  wait["leave"] = spl
                                  emonFooter( to, "Leave Message diganti jadi :\n\n「{}」".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           if msg._from in Owner:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  emonFooter( to, "Gagal mengganti Respon Message")
                              else:
                                  wait["autoResponMessage"] = spl
                                  emonFooter( to, "「Respon Msg」\nRespon Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set responpm: ' in msg.text:
                           if msg._from in Owner:
                              spl = msg.text.replace('Set responpm: ','')
                              if spl in [""," ","\n",None]:
                                  emonFooter( to, "Gagal mengganti Respon pm")
                              else:
                                  wait["autoResponMessagepm"] = spl
                                  emonFooter( to, "「Respon Msg」\nRespon Message pm diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in Owner:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  emon.sendMessage(msg.to, "Gagal mengganti Sider Message")
                              else:
                                  wait["mention"] = spl
                                  emonFooter( to, "「Sider Msg」\nSider Message diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in Owner:
                               emonFooter( to, "Pesan Message :\n「 " + str(wait["message"]) + " 」")
                               emonFooter( to, "Welcome Message : \n「 " + str(wait["welcome"]) + " 」")
                               emonFooter( to, "Leave Message :\n「 " + str(wait["leave"]) + " 」")                                 
                               emonFooter( to, "Respon Message :\n「 " + str(wait["Respontag"]) + " 」")
                               emonFooter( to, "Sider Message :\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = emon.findGroupByTicket(ticket_id)
                                     emon.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     emonFooter( to, "➥OTW MASUK KE GROUP : %s" % str(group.name))
                                     #group1 = emon.findGroupByTicket(ticket_id)
                                     #emon.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     #flexHelp1( to,"➥OTW MASUK KE GROUP : %s" % str(group.name))

    except Exception as error:
        print (error)

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "     ☆ Selfbot ☆" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "├⚫ " + key + "About\n" + \
                  "├⚫ " + key + "Me\n" + \
                  "├⚫ " + key + "Sbkick @\n" + \
                  "├⚫ " + key + "Sp \n" + \
                  "├⚫ " + key + "Sider「On\Off」\n" + \
                  "├⚫ " + key + "Mention\n" + \
                  "├⚫ " + key + "Hapus chat\n" + \
                  "├⚫ " + key + "Myurl\n" + \
                  "├⚫ " + key + "Mid\n" + \
                  "├⚫ " + key + "Mid @ \n" + \
                  "├⚫ " + key + "Info @\n" + \
                  "├⚫ " + key + "Broadcast:「Text」\n" + \
                  "├⚫ " + key + "@bye\n" + \
                  "├⚫ " + key + "Refresh\n" + \
                  "├⚫ " + key + "Reject\n" + \
                  "├⚫ " + key + "Restart bot\n" + \
                  "├⚫ " + key + "Runtime\n" + \
                  "├⚫ " + key + "Myname:「Text」\n" + \
                  "├⚫ " + key + "Cek/Set pesan:\n" + \
                  "├⚫ " + key + "Cek/Set welcome:\n" + \
                  "├⚫ " + key + "Cek/Set leave:\n" + \
                  "├⚫ " + key + "Cek/Set respon:\n" + \
                  "├⚫ " + key + "Cek/Set sider:\n" + \
                  "╰──────────╯"
    return helpMessage

def help1():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "     ☆ Selfbot ☆" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "├ ⚫" + key + "Gruplist\n" + \
                  "├ ⚫" + key + "Friendlist\n" + \
                  "├ ⚫" + key + "Infogrup「nmr」\n" + \
                  "├ ⚫" + key + "Infomem「nmr」\n" + \
                  "├ ⚫" + key + "Url grup\n" + \
                  "├ ⚫" + key + "Ginfo\n" + \
                  "├ ⚫" + key + "Open\n" + \
                  "├ ⚫" + key + "Close\n" + \
                  "├ ⚫" + key + "Cpict grup\n" + \
                  "├ ⚫" + key + "Admin「On/Off」\n" + \
                  "├ ⚫" + key + "Delladmin「On/Off」\n" + \
                  "├ ⚫" + key + "Staff「On/Off」\n" + \
                  "├ ⚫" + key + "Dellstaff「On/Off」\n" + \
                  "├ ⚫" + key + "Bot:on\n" + \
                  "├ ⚫" + key + "Bot:delete\n" + \
                  "├ ⚫" + key + "Listadmin\n" + \
                  "├ ⚫" + key + "Listbot\n" + \
                  "├ ⚫" + key + "Contact admin/staff/bot\n" + \
                  "├ ⚫" + key + "Cpict my\n" + \
                  "├ ⚫" + key + "Mykey\n" + \
                  "├ ⚫" + key + "Setkey「New Key」\n" + \
                  "├ ⚫" + key + "Resetkey\n" + \
                  "├ ⚫" + key + "mytoken\n" + \
                  "╰────────────"
    return helpMessage1

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "     ☆ Settings ☆" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "├⚫ " + key + "Respon「On/Off」\n" + \
                  "├ ⚫" + key + "Autojoin「on/off」\n" + \
                  "├ ⚫" + key + "Autoleave「on/off」\n" + \
                  "├ ⚫" + key + "Autoadd「on/off」\n" + \
                  "├ ⚫" + key + "Welcome「On/Off」\n" + \
                  "├ ⚫" + key + "Unsend「On/Off」\n" + \
                  "├ ⚫" + key + "Delfriend「On/Off」\n" + \
                  "├ ⚫" + key + "Contact「On/Off」\n" + \
                  "├ ⚫" + key + "Sticker「on/off」\n" + \
                  "├ ⚫" + key + "Jointicket「on/off」\n" + \
                  "├ ⚫" + key + "Notag「on/off」\n" + \
                  "├ ⚫" + key + "Talkban @\n" + \
                  "├ ⚫" + key + "Untalkban @\n" + \
                  "├ ⚫" + key + "Talkbanlist\n" + \
                  "├ ⚫" + key + "Talkban「On/Off」\n" + \
                  "├ ⚫" + key + "Untalkban「On/Off」\n" + \
                  "├ ⚫" + key + "Ban「on/off」\n" + \
                  "├ ⚫" + key + "Unban「on/off」\n" + \
                  "├ ⚫" + key + "Ban @\n" + \
                  "├ ⚫" + key + "Unban @\n" + \
                  "├ ⚫" + key + "Banlist / Blc\n" + \
                  "├ ⚫" + key + "Clban \n" + \
                  "╰────────────"
    return helpMessage2

def help3():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMedia = "     ☆ Hiburan ☆" + "\n" + \
                  "╭──────────╮" + "\n" + \
                  "├ ⚫" + key + "+sticker「key」\n" + \
                  "├ ⚫" + key + "-sticker「key」\n" + \
                  "├ ⚫" + key + "Liststicker\n" + \
                  "├ ⚫" + key + "Kode cctv\n" + \
                  "├ ⚫" + key + "Lihat「nmr」\n" + \
                  "├ ⚫" + key + "Listquran\n" + \
                  "├ ⚫" + key + "Murrotal 「nmr」\n" + \
                  "├ ⚫" + key + "Al-qur'an 「nmr」\n" + \
                  "├ ⚫" + key + "Get-quran: 「nmr」\n" + \
                  "├ ⚫" + key + "Asmaulhusna 「nmr」\n" + \
                  "├ ⚫" + key + "Ayat sajadah\n" + \
                  "├ ⚫" + key + "Jadwal sholat「kota」\n" + \
                  "├ ⚫" + key + "Date「H-B-TH」\n" + \
                  "├ ⚫" + key + "Get-zodiak「zodiak」\n" + \
                  "├ ⚫" + key + "Cuaca「kota」\n" + \
                  "├ ⚫" + key + "Youtube「judul」\n" + \
                  "├ ⚫" + key + "Ytmp4:「judul」\n" + \
                  "├ ⚫" + key + "Soundcloud「judul」\n" + \
                  "├ ⚫" + key + "Searchlyric「judul」\n" + \
                  "├ ⚫" + key + ".Smule「idsmule」\n" + \
                  "├ ⚫" + key + "Smuleid「idsmule」\n" + \
                  "├ ⚫" + key + "Profileig:「nama」\n" + \
                  "├ ⚫" + key + "Get-anime: 「Keyword」\n" + \
                  "├ ⚫" + key + "Siarantv「Keyword」\n" + \
                  "├ ⚫" + key + "topnews\n" + \
                  "├ ⚫" + key + "1cak\n" + \
                  "├ ⚫" + key + "imagetext「Keyword」\n" + \
                  "├ ⚫" + key + "Get-image:「Keyword」\n" + \
                  "├ ⚫" + key + "Image「Keyword」\n" + \
                  "├ ⚫" + key + "Img:「Keyword」\n" + \
                  "├ ⚫" + key + "Image food:「Keyword」\n" + \
                  "├ ⚫" + key + "List meme\n" + \
                  "├ ⚫" + key + "Meme@Nama@Teks1@Teks2\n" + \
                  "├ ⚫" + key + "Get-film: 「judul」\n" + \
                  "├ ⚫" + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "├ ⚫" + key + "Spam:「Mid korban」「Jumlah」\n" + \
                  "├ ⚫" + key + "Love|「nama」|「nama」\n" + \
                  "╰────────────"
    return helpMedia

def infomeme():
    helpMessage3 = """
╭━━━━━━━━━━━━━━
┃🛑 Buzz
┃🛑 Spongebob
┃🛑 Patrick
┃🛑 Doge
┃🛑 Joker
┃🛑 Xzibit
┃🛑 You_tried
┃🛑 cb
┃🛑 blb
┃🛑 wonka
┃🛑 keanu
┃🛑 cryingfloor
┃🛑 disastergirl
┃🛑 facepalm
┃🛑 fwp
┃🛑 grumpycat
┃🛑 captain
┃🛑 mmm
┃🛑 rollsafe
┃🛑 sad-obama
┃🛑 sad-clinton
┃🛑 aag
┃🛑 sarcasticbear
┃🛑 sk
┃🛑 sparta
┃🛑 sad
├────────────
┃          Contoh   
┃❂ meme@sad@text1@text2
╰━━━━━━━━━━━━━━
"""
    return helpMessage3

def translate():
    helpTranslate =     "╔══〘 T R A N S L A T E 〙" + "\n" + \
                       "╠➥ af : afrikaans" + "\n" + \
                       "╠➥ sq : albanian" + "\n" + \
                       "╠➥ am : amharic" + "\n" + \
                       "╠➥ ar : arabic" + "\n" + \
                       "╠➥ hy : armenian" + "\n" + \
                       "╠➥ az : azerbaijani" + "\n" + \
                       "╠➥ eu : basque" + "\n" + \
                       "╠➥ be : belarusian" + "\n" + \
                       "╠➥ bn : bengali" + "\n" + \
                       "╠➥ bs : bosnian" + "\n" + \
                       "╠➥ bg : bulgarian" + "\n" + \
                       "╠➥ ca : catalan" + "\n" + \
                       "╠➥ ceb : cebuano" + "\n" + \
                       "╠➥ ny : chichewa" + "\n" + \
                       "╠➥ zh-cn : chinese (simplified)" + "\n" + \
                       "╠➥ zh-tw : chinese (traditional)" + "\n" + \
                       "╠➥ co : corsican" + "\n" + \
                       "╠➥ hr : croatian" + "\n" + \
                       "╠➥ cs : czech" + "\n" + \
                       "╠➥ da : danish" + "\n" + \
                       "╠➥ nl : dutch" + "\n" + \
                       "╠➥ en : english" + "\n" + \
                       "╠➥ eo : esperanto" + "\n" + \
                       "╠➥ et : estonian" + "\n" + \
                       "╠➥ tl : filipino" + "\n" + \
                       "╠➥ fi : finnish" + "\n" + \
                       "╠➥ fr : french" + "\n" + \
                       "╠➥ fy : frisian" + "\n" + \
                       "╠➥ gl : galician" + "\n" + \
                       "╠➥ ka : georgian" + "\n" + \
                       "╠➥ de : german" + "\n" + \
                       "╠➥ el : greek" + "\n" + \
                       "╠➥ gu : gujarati" + "\n" + \
                       "╠➥ ht : haitian creole" + "\n" + \
                       "╠➥ ha : hausa" + "\n" + \
                       "╠➥ haw : hawaiian" + "\n" + \
                       "╠➥ iw : hebrew" + "\n" + \
                       "╠➥ hi : hindi" + "\n" + \
                       "╠➥ hmn : hmong" + "\n" + \
                       "╠➥ hu : hungarian" + "\n" + \
                       "╠➥ is : icelandic" + "\n" + \
                       "╠➥ ig : igbo" + "\n" + \
                       "╠➥ id : indonesian" + "\n" + \
                       "╠➥ ga : irish" + "\n" + \
                       "╠➥ it : italian" + "\n" + \
                       "╠➥ ja : japanese" + "\n" + \
                       "╠➥ jw : javanese" + "\n" + \
                       "╠➥ kn : kannada" + "\n" + \
                       "╠➥ kk : kazakh" + "\n" + \
                       "╠➥ km : khmer" + "\n" + \
                       "╠➥ ko : korean" + "\n" + \
                       "╠➥ ku : kurdish (kurmanji)" + "\n" + \
                       "╠➥ ky : kyrgyz" + "\n" + \
                       "╠➥ lo : lao" + "\n" + \
                       "╠➥ la : latin" + "\n" + \
                       "╠➥ lv : latvian" + "\n" + \
                       "╠➥ lt : lithuanian" + "\n" + \
                       "╠➥ lb : luxembourgish" + "\n" + \
                       "╠➥ mk : macedonian" + "\n" + \
                       "╠➥ mg : malagasy" + "\n" + \
                       "╠➥ ms : malay" + "\n" + \
                       "╠➥ ml : malayalam" + "\n" + \
                       "╠➥ mt : maltese" + "\n" + \
                       "╠➥ mi : maori" + "\n" + \
                       "╠➥ mr : marathi" + "\n" + \
                       "╠➥ mn : mongolian" + "\n" + \
                       "╠➥ my : myanmar (burmese)" + "\n" + \
                       "╠➥ ne : nepali" + "\n" + \
                       "╠➥ no : norwegian" + "\n" + \
                       "╠➥ ps : pashto" + "\n" + \
                       "╠➥ fa : persian" + "\n" + \
                       "╠➥ pl : polish" + "\n" + \
                       "╠➥ pt : portuguese" + "\n" + \
                       "╠➥ pa : punjabi" + "\n" + \
                       "╠➥ ro : romanian" + "\n" + \
                       "╠➥ ru : russian" + "\n" + \
                       "╠➥ sm : samoan" + "\n" + \
                       "╠➥ gd : scots gaelic" + "\n" + \
                       "╠➥ sr : serbian" + "\n" + \
                       "╠➥ st : sesotho" + "\n" + \
                       "╠➥ sn : shona" + "\n" + \
                       "╠➥ sd : sindhi" + "\n" + \
                       "╠➥ si : sinhala" + "\n" + \
                       "╠➥ sk : slovak" + "\n" + \
                       "╠➥ sl : slovenian" + "\n" + \
                       "╠➥ so : somali" + "\n" + \
                       "╠➥ es : spanish" + "\n" + \
                       "╠➥ su : sundanese" + "\n" + \
                       "╠➥ sw : swahili" + "\n" + \
                       "╠➥ sv : swedish" + "\n" + \
                       "╠➥ tg : tajik" + "\n" + \
                       "╠➥ ta : tamil" + "\n" + \
                       "╠➥ te : telugu" + "\n" + \
                       "╠➥ th : thai" + "\n" + \
                       "╠➥ tr : turkish" + "\n" + \
                       "╠➥ uk : ukrainian" + "\n" + \
                       "╠➥ ur : urdu" + "\n" + \
                       "╠➥ uz : uzbek" + "\n" + \
                       "╠➥ vi : vietnamese" + "\n" + \
                       "╠➥ cy : welsh" + "\n" + \
                       "╠➥ xh : xhosa" + "\n" + \
                       "╠➥ yi : yiddish" + "\n" + \
                       "╠➥ yo : yoruba" + "\n" + \
                       "╠➥ zu : zulu" + "\n" + \
                       "╠➥ fil : Filipino" + "\n" + \
                       "╠➥ he : Hebrew" + "\n" + \
                       "╚══〘 Jangan Typo 〙" + "\n" + "\n" + \
                       "Contoh : tr-en santai"
    return helpTranslate

while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass

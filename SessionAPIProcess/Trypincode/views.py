from django.shortcuts import render,redirect
from .models import Trypincode
# Create your views here.
from urllib.request import urlopen
import json
import requests


def home(request):

    return render(request,"index.html")


def getpin(request):
    authcode = Trypincode.objects.values() #"If authcode is invalid, get a new one "
    for code in authcode:
        pincode = (code['authcode'])
    html = urlopen("https://secure.logmeinrescue.com/API/requestPINCode.aspx?authcode=%s" % pincode).read()#target html read(html type is bytes)
    str = html.decode()

    data = json.dumps(str)
    return redirect("https://secure.logmeinrescue.com/API/requestPINCode.aspx?authcode=%s" % pincode)


def UserinfoPullDataBase():
    userInfo = Trypincode.objects.values()

    for email in userInfo:
        email = (email['email'])
    for pwd in userInfo:
        pwd = (pwd['pwd'])
    return email,pwd


def generateAuthCode(request):
    userInfo = Trypincode.objects.values()
    email,pwd = UserinfoPullDataBase()
    html = urlopen("https://secure.logmeinrescue.com/API/requestAuthCode.aspx?email=%s&pwd=%s" % (email,pwd)).read()
    str = html.decode()

    print(str)
    authCode = str[13:]
    changeAuthcode = Trypincode.objects.get(id=1)
    changeAuthcode.authcode = authCode
    changeAuthcode.save() #change value database
    print(authCode)
    return redirect("https://secure.logmeinrescue.com/API/requestAuthCode.aspx?email=%s&pwd=%s" % (email,pwd))


def loginProcess(login):
    userInfo = Trypincode.objects.values()

    email,pwd = UserinfoPullDataBase()
    # for email in userInfo:
    #     email = (email['email'])
    # for pwd in userInfo:
    #     pwd = (pwd['pwd'])
    login_data = dict(login=email, password=pwd)
    session = requests.session()
    r = session.post("https://secure.logmeinrescue.com/API/login.aspx?email=%s&pwd=%s" % (email, pwd), data=login_data)
    print(r.text)
    if login == 0:
        return email,pwd
    elif login == 1:
        return session


def login(request):
    email,pwd = loginProcess(login=0)

    return redirect("https://secure.logmeinrescue.com/API/login.aspx?email=%s&pwd=%s" % (email,pwd))


def getAccount(request):
    html = urlopen("https://secure.logmeinrescue.com/API/getAccount.aspx").read()
    print(html)
    return redirect("https://secure.logmeinrescue.com/API/getAccount.aspx")

def listSession(request):

    techInfo = Trypincode.objects.values()
    for channel in techInfo:
        channel = (channel['channel'])
    for node in techInfo:
        node = (node['techID'])

    session = loginProcess(login=1)
    html=session.get("https://secure.logmeinrescue.com/API/getSession_v3.aspx?node=%s&noderef=%s" % (node,channel))
    print(html.text)

    # technicianID = r2.text[269:277]
    # print(technicianID)
    # sessionNum =r2.text[243:252]
    # print(sessionNum)

    return redirect("https://secure.logmeinrescue.com/API/getSession_v3.aspx?node=%s&noderef=%s" % (node,channel))


def getTechInfo():
    techInfo = Trypincode.objects.values()
    for channel in techInfo:
        channel = (channel['channel'])
    for node in techInfo:
        node = (node['techID'])

    session = loginProcess(login=1)
    html=session.get("https://secure.logmeinrescue.com/API/getSession_v3.aspx?node=%s&noderef=%s" % (node,channel))
    #html = urlopen("https://secure.logmeinrescue.com/API/getSession_v3.aspx?node=%s&noderef=%s" % (node,channel)).read()
    print(html.text)

    technicianID =html.text[269:277]
    #print(technicianID)
    #print(type(html.text))
    #print(type(str.text))
    #print(str)
    sessionNum = html.text[243:252]
    #print(sessionNum)
    return technicianID,sessionNum


def createSession(request):
    authcode = Trypincode.objects.values()  # "If authcode is invalid, get a new one "
    for code in authcode:
         authcode= (code['authcode'])
    session =loginProcess(login=1)
    node,sessionNum = getTechInfo()
    print(node)
    print(session)
    html=session.get("https://secure.logmeinrescue.com/API/startSession.aspx?session=%s&node=%s&authcode=%s" % (sessionNum,node,authcode))
    print(html.text)

    #return redirect("https://secure.logmeinrescue.com/API/startSession.aspx?session=788105637&node=22993387&authcode=b43c10w491rump6nbqqpfzxgcfotksmwpcmserbx383woemu8oobw79pgi2s62rssydfjnceovugwiyb8m01cvdl85ayw0ezrqe67yqzrmwj8q7hz1fvgp00lh2vqsi6")
    return redirect("https://secure.logmeinrescue.com/API/startSession.aspx?session=%s&node=%s&authcode=%s" % (sessionNum,node,authcode))





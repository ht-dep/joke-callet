import itchat,time,os,time
from itchat.content import INCOME_MSG,TEXT,RECORDING,VOICE,PICTURE
import queue,threading
UserList=[]
robot=''
master_id=''
MyQ=queue.Queue(maxsize=100)

def get_reply(msg,user):
    itchat.send_msg(msg=msg, toUserName="@c97ce30365082f1f5ea4042057f7c893")
def replyPic(msg,user):
    msg.download(msg.fileName)
    itchat.send('@%s@%s' % (
        'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
                user)
    if os.path.exists(msg['FileName']):
        os.remove(msg['FileName'])

@itchat.msg_register([TEXT,VOICE,PICTURE],isFriendChat=True)
def simple_reply(msg):
    print(msg['FromUserName'])
    print(msg['ToUserName'])
    if msg['Type'] in ["Recording",PICTURE]:
        print("接收到好友的语音或图片")
        # print(msg)
        # print(msg["MediaId"])
        # replyPic(msg,msg["FromUserName"])
        # itchat.send_msg('我现在 还听不见。领养我以后，就自动解锁呐。<a href="http://r.msxiaobing.com/link?url=https%3a%2f%2fwww.msxiaobing.com%2fv2%2fpartnerapi%3fpartner%3dwechat%26openid%3doxh_Kvi2tXDRMdmPzr2aRhyHtyTM%26time%3d636286220128313274%26signed_request%3d57f4ef51a96c853b9dfeac3eaeab3053&ftid=7b968f28ffa75445948ad3d10dd4bf4d&feid=7b968f28ffa75445948ad3d10dd4bf4d&spid=mK-hiJouuzRGiRUJuU2sDdEqFkpfysH0Ral88WkA">点击链接</a>',msg['ToUserName'])
    else:
    # print(msg)
        if msg['FromUserName']==master_id:
            print("主人发送的消息")
        else:
            print("接收到好友消息：")
            print(msg["Text"])

            itchat.send_msg(msg=msg["Text"], toUserName=robot)
            UserList.append(msg['FromUserName'])
            # UserList.append(msg['ToUserName'])


@itchat.msg_register(INCOME_MSG,isMpChat=True)
def simple_reply(msg):
    time.sleep(1)
    # print(msg['Type'])
    # print(msg)
    if msg['Type'] in ['Recording',PICTURE]:
        print("消息类型为："+msg['Type'])
        print("其他类型 删除回复")
        if msg['FromUserName'] == robot:
            print("小冰回复")
            # print(msg['Text'])
            print(len(UserList))
            if len(UserList):
                user = UserList.pop(0)
                print("回复好友：" + user)
                replyPic(msg, user)

    print(msg['FromUserName'])
    if msg['FromUserName']==robot:
        print("小冰回复")
        print(msg['Text'])
        print(len(UserList))
        if len(UserList):
            user=UserList.pop(0)
            print("回复好友："+user)
            itchat.send_msg(msg=msg['Text'],toUserName=user)

itchat.auto_login(hotReload=True)
mps=itchat.get_mps()
master=itchat.get_friends()[0]
master_id=master['UserName']

for m in mps:
    if "小冰"== m["NickName"]:
        robot=m["UserName"]

itchat.run()

# coding=utf8
import requests
import itchat
from itchat.content import *
import time,random,threading
from test_list_face import get_videos_list, get_faces_list

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

msglist = ["首先声明，视频是我本人，转发视频，我诅咒你小鸡鸡永远硬不起来，能做到吗？能做到我再送你一个我的自拍。妹妹今晚做哥哥的小情人！",
           "毕竟第一次，哥哥再来个8块的红包奖励一下撒，收到就开始视频，玩30分钟可以了吧，绝不墨迹，泥鳅钻洞马上奉上，高潮带喷水，让哥哥你不撸自射，没任何后续费用，你还可以进群，群里还有我的两个好姐妹，每天都可以陪你玩，毕竟第一次，拿出你的诚意，这样以后我们才能相处下去哦，不发包妹妹就不理你了，缘分已尽，还是删了",
           "哥哥10块钱不舍肯定看不到你想看的呀",
           "哥哥下面硬了吗？要不要妹妹帮你弄出来？妹妹功夫很厉害的哦，想不想现场看我表演？哥哥再发个10块的红包，单独视频，20分钟，听你指挥，然后拉你进群，以后每天可以在群里找我玩，不方便视频的话，妹妹给你发10部我的自拍和10部精彩爱爱录像，视频完再送哥哥两部人兽的和一部泥鳅钻洞洞带高潮喷水的。",
           "哥哥发个6.66呀，六六大顺！我拍好看刺激的给你",
           "哥哥2017发大财，祝哥哥身体健康，哥哥的下面年年吃香好哥哥，今天是你和柠檬认识的第一天，哥哥随意赏妹妹个红包呗，妹妹一个人在外面打工不容易，土豪哥哥随意哦，妹妹也不介意哦，嘻嘻！拍视频只为赚点零花钱，紅包走一走，激情马上有，哥哥的双手下面来回走，妹妹舔死你哦。",
           "我去群里玩了哦。哥哥想进群红包20元。群里还有我的姐妹们哦",
           "哥哥最后最后给我8块钱吧 妹妹也是想多吃点好吃的一个人在外不容易 等下妹妹给你看我操的直播好不好。",
           "好了我也不想墨迹，口罩衣服已经脱光光，要玩最后发个8块的红包，立马开视频，制服道具都有，毕竟第一次，骗！子！死！可以了吧，那个女的用下面把泥鳅都夹死了，不发红包我就不回你消息了。我去群里陪其他哥哥了，想玩的，一会我把群二维码发你，扫码自动进群，每晚我跟闺蜜一次同性视频直播，保证你没看过，还有收集的各种精品视频，每天更新不少于300部"]
videos = get_videos_list()
faces = get_faces_list()


def get_response(msg):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return None


def action(user):

    itchat.send_msg('下面开始模拟最新微信骗局', user)
    time.sleep(1)
    itchat.send_msg('5秒后开始', user)
    time.sleep(5)


    i = 0
    for msg in msglist:
        print(i)
        itchat.send_msg(msg, user)
        if i == 0:
            itchat.send_video(videos[0], user)
        elif i == 1:
            itchat.send_video(videos[1], user)
        elif i == 3:
            itchat.send_video(videos[2], user)
        elif i == 5:
            itchat.send_video(videos[3], user)
        elif i == 7:
            itchat.send_video(videos[4], user)
        time.sleep(60)
        i = i + 1


# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
@itchat.msg_register(TEXT, isFriendChat=True)
def text_reply(msg):
    print("文本消息")
    print(msg['Text'])
    if "能" in msg['Text']:
        pass  # video[0]
    if "test" in msg['Text']:
        print("start")
        t2 = threading.Thread(target=action, args=(msg['FromUserName'],))
        t2.start()
        # action(msg['FromUserName'])

@itchat.msg_register(FRIENDS)
def add_Friend(msg):
    print("添加好友")
    # print(msg)
    print(msg['RecommendInfo'])
    itchat.add_friend(**msg['Text'])
    itchat.send_msg("大家好，我是squirrel")
    time.sleep(5)
    # itchat.add_friend(msg["Friends"])
    t1 = threading.Thread(target=action, args=(msg['RecommendInfo']['UserName'],))
    t1.start()
    # action(msg['RecommendInfo']['UserName'])


@itchat.msg_register(PICTURE, isFriendChat=True)
def picture_reply(msg):
    print("接收到图片:")
    # print(videos)
    # itchat.send_video(videos[0], msg['FromUserName'])
    # action(msg['FromUserName'])
    # print(faces)
    face=random.choice(faces)
    print(face)
    itchat.send('@img@{}'.format(face), msg["FromUserName"])
    # itchat.send_image(PICTURE,face, msg['FromUserName'])
    # print("视频地址：{}".format(get_videos_list()[0]))
    # itchat.send_video(get_videos_list()[0], msg['FromUserName'])


# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
# itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.auto_login(hotReload=True)
itchat.run()

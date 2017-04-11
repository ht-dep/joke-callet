'''
撩妹机器人
1、每天早上定时发爱心
2、
'''

# coding=utf8
import requests
import itchat, datetime
from itchat.content import *
import time, random, threading

friends = {}
KEYS = ['241b5a1059b04c898d00d197522a917c', 'ca6acaabfd7a40edb0b42a7bea233dc7', '85c0d048714b43e6bed1b0c966c20cbe']
apiUrl = 'http://www.tuling123.com/openapi/api'
data = {
    'key': random.choice(KEYS),
    'info': "笑话",
    'userid': 'wechat-robot',
}
a = ['''
尼沙·卡巴尼说，
“当我爱你的时候，一种新的语言萌芽，
新的城市，新的国家出现。”''',
     '''
     我爱你，虽然我嘴笨不太会说甜言蜜语，
     但我却愿意为你，学说一万句情话。
     我一直想从你的窗子里看月亮。
     ——张爱玲《倾城之恋》''',
     '''
     我可能会忘记今天发生的世界大事，
     但是我永远不会忘记，
     在这向海的阳台上，
     你用矿泉水为我洗头。
     ——《甜言蜜语》''',
     '''
     如果我爱你，而你也正巧爱我。
     你头发乱了的时候，我会笑笑，替你拨一拨，
     然后，手还留恋地在你发上多待几秒。
     但是，如果我爱你，而你不巧地不爱我。
     你头发乱了，我只会轻轻地告诉你，
     你头发乱了喔。
     ——村上春树''',
     '''
     如果说去旅行去冒险，
     是为了遇见不曾见过的美妙景色，
     经历不曾想过的充实人生，
     那么与你的相遇相守，
     就是我能想到的最美丽的冒险。
     ——《飞屋环游记》''',
     '''
     他说你任何为人称道的美丽，
     不及他第一次遇见你。
     ——《南山南》''',
     '''
     “我很孤独用英文怎么说？”
     “I love you.”
     ——《算死草》''',
     '''
     谁说现在是冬天呢？
     当你在我身旁时，
     我感到百花齐放，鸟唱蝉鸣。
     ——夏洛蒂•勃朗特''',
     '''
     我喜欢你的皱纹，
     每一条都爱。
     ——《本杰明巴顿奇事》''',
     '''
     请把你的心给我，与我为伍，
     这个世界太残酷了，我有些害怕。
     ——王尔德''',
     '''
     从你叫什么名字开始，
     后来，有了一切。
     ——梵高''',
     '''
     如果你说你在下午四点来，
     从三点钟开始，我就开始感觉很快乐，
     时间越临近，我就越来越感到快乐。
     ——《小王子》''',
     '''
     现在的爱情和以前不一样了。
     现在我爱上你，
     可能是因为你有房有车；
     那时我爱上你，
     可能只是因为那天下午阳光很好，
     而你恰巧穿了一件白衬衫。
     ——吴秀波''',
     '''
     你是我温暖的手套，
     冰冷的啤酒，
     带着太阳光气息的衬衫，
     日复一日的梦想。
     ——廖一梅《恋爱的犀牛》''',
     '''
     爱是一场战争，
     我不怕受伤只怕你不快乐。
     ——饶雪漫''',
     '''
     你的名字，
     是我读过，
     最短的情诗。
     ——新海诚《你的名字》''',
     '''
     你在人群中对我微微一笑，
     因为这个微笑，
     我已经等了好久。
     ——席慕蓉《初老》''',
     '''
     愿有岁月可回首，
     且以深情共白头。
     ——《岁晚》''',
     '''
     醒来觉得，
     甚是爱你。
     ——朱生豪''',
     '''
     我把我整个灵魂都给你，
     连同它的怪癖，
     耍小脾气，忽明忽暗，
     一千八百种坏毛病。
     它真讨厌，只有一点好，爱你。
     ——王小波《爱你就像爱生命》''',
     '''
     你可以怀疑星星是火焰，
     怀疑太阳会移动，
     怀疑真理是谎言，
     但绝对不要怀疑我的爱。
     ——莎士比亚''',
     '''
     当我决定与你共度下半生时，
     我希望我的下半生赶快开始。
     ——《当哈利遇上莎莉》''',
     '''
     我希望有个如你一般的人，
     如山间清爽的风，如古城温暖的光。
     从清晨到夜晚，由山野到书房。
     只要最后是你，就好。
     ——《从你的全世界路过》''',
     '''
     从来不偷东西的你，却爱偷笑，
     于是从来不偷东西的我，
     便学会了偷看。
     ——北川理惠《三行情书》''',
     '''
     我不能把爱情推迟到下一个世纪，我不能。
     尽管呼喊在喉咙里被窒息，
     尽管灰蒙蒙的山峦，灰蒙蒙的山峦下，
     仇恨劈啪作响，在爆发，在燃烧。
     ——拉莫斯·罗萨''',
     '''
     我只想从你这得到一个王冠，
     你却给了我一个王国。
     ——珍妮特·温特森《写在身体上》''',
     '''
     我遇见那么多人，
     可为什么偏偏是你，
     看起来最应该是过客的你，
     却在我心里占据这么重要的位子。
     ——《one day》''',
     '''
     从前的日色变得慢，车，马，邮件都慢，一生只够爱一个人。
     ——《从前慢》''',
     ]
word_faces = ["✪ω✪", '✷(ꇐ‿ꇐ)✷', "｡◕‿◕｡", "(๑￫ܫ￩)", "(-人-) [拜佛] ", "(*/ω＼*)",
              " ( *^-^)ρ(^0^* )", "(●'◡'●)ﾉ♥", "( ◔ ڼ ◔ )", "( ´◔ ‸◔`)", "(・ω< )★", "(♥◠‿◠)ﾉ",
              '（*＾-＾*）', "(｡◕ˇ∀ˇ◕）", "✪ω✪", "~Ⴚ(●ტ●)Ⴢ~", "(๑◕ܫ￩๑)b",
              "v( ^-^(ё_ёゝ", "(✿◡‿◡)", "o(￣▽￣)ｄ",
              "٩(๑´0`๑)۶",
              "( ´◔ ‸◔`) ", "๑乛◡乛๑ ", "♥(｡￫v￩｡)♥",
              "(•‾̑⌣‾̑•)✧˖°", " (｀◕‸◕´+) ",
              "(oﾟωﾟo)", " (*′∇`*)", "(￣y▽￣)~*", "------\(˙<>˙)/------",
              "（＾∀＾）", "(•̀ᴗ•́)و ̑̑ "
              ]
girls = ["O_o-小燕~", "雯", "喵小姐", "瑾江", "像鱼摆摆一样"]

def sendXiaohua():
    try:
        r = requests.post(apiUrl, data=data).json()
        msg= r['text']
        # print(msg)
    except:
        # print("失败笑话")
        return "今日没笑话"

    tests = ["squirrel"]
    for i in girls:
        # print(i)
        # print(friends[i])
        if i in friends.keys():
            # print(i)
            itchat.send_msg(msg, friends[i])
    time.sleep(60)
    for i in girls:
        # print(i)
        # print(friends[i])
        if i in friends.keys():
            # print(i)
            itchat.send_msg(" 嘿嘿   ", friends[i])
def doWakeup():
    for i in girls:
        if i in friends.keys():
            itchat.send_msg("起床啦  起床啦    {}".format(random.choice(word_faces)), friends[i])

def doNight():
    for i in girls:
        if i in friends.keys():
            itchat.send_msg("晚安     {}".format(random.choice(word_faces)), friends[i])
def action():
    flag = True
    while flag:
        current_time = datetime.datetime.now().strftime("%H:%M")
        print("当前时间：{}".format(current_time))
        # todo 获取朋友列表
        # todo 给指定朋友发爱心
        if current_time == "07:33":
            doLove()
        if current_time == "08:00":
            doWakeup()
        if current_time == "08:10":
            sendXiaohua()
        if current_time == "22:10":
            doLove()
        if current_time == "22:30":
            doWakeup()
        time.sleep(60)


def get_friends():
    list_friend = itchat.get_friends(update=True)
    for j in list_friend:
        friends[j['NickName']] = j['UserName']
    # print(friends)


def doLove():
    # print("****")
    msg = random.choice(a)
    tests = ["squirrel"]
    for i in girls:
        # print(i)
        # print(friends[i])
        if i in friends.keys():
            # print(i)
            itchat.send_msg(msg, friends[i])
    # time.sleep(60 * 10)


# 这里是我们在“1. 实现微信消息的获取”中已经用到过的同样的注册方法
@itchat.msg_register(TEXT, isFriendChat=True)
def text_reply(msg):
    print("文本消息")
    # print(msg['Text'])





@itchat.msg_register(FRIENDS)
def add_Friend(msg):
    print("添加好友")
    # print(msg)
    # print(msg['RecommendInfo'])
    itchat.add_friend(**msg['Text'])
    # itchat.send_msg("大家好，我是squirrel")
    # time.sleep(5)


@itchat.msg_register(PICTURE, isFriendChat=True)
def picture_reply(msg):
    print("接收到图片:")


t1 = threading.Thread(target=action)
t1.start()
itchat.auto_login(hotReload=True)
get_friends()
itchat.run()

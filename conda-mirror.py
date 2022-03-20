import os
import json
def ClearChannel():
    os.system("conda config --remove-key channels")

def SetChannel(channelList):
    for i in channelList:
        os.system("conda config --add channels " + i)

def DetechDelay(ip, count):
    delay = os.popen("ping " + ip + " -c " + str(count) + " | grep ^rtt | cut -d \" \" -f 4 | cut -d \"/\" -f 2", "r")
    return float(delay.read())

def ReadConfig(filename):
    f = open(filename, "r")
    obj = json.loads(f.read())
    f.close()
    return obj

def DelayLED(time):
    if(time < 10.0):
        coloredTime = "[●○○]"
    elif(time < 20.0):
        coloredTime = "[●●○]"
    else:
        coloredTime = "[●●●]"
    return coloredTime

AllMirrors = ReadConfig("config.json")

index = 0
shortestDelay = 100000.0
shortestDelayIndex = 0
os.system("clear")
for i in AllMirrors:
    index = index + 1
    delay = DetechDelay(i["detect"], 1)
    print(str(index) + " " + i["name"] + ": " + str(delay) + "ms " + DelayLED(delay))
    if(delay < shortestDelay):
        shortestDelay = delay
        shortestDelayIndex = index

sel = input("请选择镜像（默认为" + str(shortestDelayIndex) + "）：")
if(sel == ""):
    print("默认选择最快的镜像。")
    sel = str(shortestDelayIndex)
if(int(sel) <= index):
    print("清除原有的镜像。")
    ClearChannel()
    print("设置新镜像。")
    SetChannel(AllMirrors[int(sel)]["mirrors"])

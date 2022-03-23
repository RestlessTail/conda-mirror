import os
import json

class Mirror():
    AllMirrors = []
    def ClearChannel(self):
        os.system("conda config --remove-key channels")
    def CleanIndex(self):
        os.system("conda clean -i")
    def SetChannel(self, channelList):
        for i in reversed(channelList):
            os.system("conda config --add channels " + i)
    def DetechDelay(self, ip, count):
        delay = os.popen("ping " + ip + " -c " + str(count) + " -W 5 | grep ^rtt | cut -d \" \" -f 4 | cut -d \"/\" -f 2", "r")
        time = delay.read()
        if(time == ""):
            return -1.0
        else:
            return float(time)
    def ReadConfig(self, filename):
        f = open(filename, "r")
        self.AllMirrors = json.loads(f.read())
        f.close()
    def DelayLED(self, time):
        if(time < 0.0):
            coloredTime = "[———]"
        elif(time < 10.0):
            coloredTime = "[●○○]"
        elif(time < 20.0):
            coloredTime = "[●●○]"
        else:
            coloredTime = "[●●●]"
        return coloredTime

def Run():
    index = 0
    shortestDelay = 10.0
    shortestDelayIndex = 0

    m = Mirror()
    m.ReadConfig("config.json")

    for i in m.AllMirrors:
        print("尝试连接" + i["detect"] + "……")
        delay = m.DetechDelay(i["detect"], 1)
        if(delay < 0.0):
            print("\r" + str(index) + " " + i["name"] + ": 无法连接 " + m.DelayLED(delay))
            continue
        print("\r" + str(index) + " " + i["name"] + ": " + str(delay) + "ms " + m.DelayLED(delay))
        if(delay < shortestDelay):
            shortestDelay = delay
            shortestDelayIndex = index
        index = index + 1

    sel = input("请选择镜像（默认为" + str(shortestDelayIndex) + "）：")
    if(sel == ""):
        print("默认选择最快的镜像。")
        sel = shortestDelayIndex
    if(sel <= index):
        print("清除原有的镜像。")
        m.ClearChannel()
        print("设置新镜像。")
        m.SetChannel(m.AllMirrors[sel]["mirrors"])
        print("刷新索引。")
        m.CleanIndex()

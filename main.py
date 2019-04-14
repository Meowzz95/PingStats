import subprocess
import os
import platform
import sys

SYSTEM_MAC_PLATFORM="Darwin"

IP="192.168.0.1"
STR_TIME="time="
STR_MS="ms"

FAST_UPPER_F=10.0
SLOW_THRESHOLD_F=50.0
SUPER_SLOW_THRESHOLD_F=250.0

PRINT_RECENT_COUNT=3
__PRINT_RECENT_COUNT__=-PRINT_RECENT_COUNT


fastCounter=0
okCounter=0
slowCounter=0
superSlowCounter=0
failureCounter=0
total=0

fastRecords=[]
okRecords=[]
slowRecords=[]
sslowRecords=[]
failureRecords=[]


def print_status():
    print("--------------------")
    print("Fast  %s %.2f%% %s"%(fastCounter,fastCounter/total*100,fastRecords[__PRINT_RECENT_COUNT__:]))
    print("Ok    %s %.2f%% %s"%(okCounter,okCounter/total*100,okRecords[__PRINT_RECENT_COUNT__:]))
    print("Slow  %s %.2f%% %s"%(slowCounter,slowCounter/total*100,slowRecords[__PRINT_RECENT_COUNT__:]))
    print("SSlow %s %.2f%% %s"%(superSlowCounter,superSlowCounter/total*100,sslowRecords[__PRINT_RECENT_COUNT__:]))
    print("Fail  %s %.2f%% %s"%(failureCounter,failureCounter/total*100,failureRecords[__PRINT_RECENT_COUNT__:]))
    print("--------------------")

if __name__ == '__main__':
    if len(sys.argv)<3:
        print("Invalid param(s)")
        exit()
    IP = sys.argv[1]
    notificationFlag = int(sys.argv[2])

    proc=subprocess.Popen(["ping", IP],stdout=subprocess.PIPE)
    for line in proc.stdout:
        lineStr = line.decode('UTF8').strip()
        if "56 data" in lineStr:
            continue
        if "time=" in lineStr:
            strTimeIndex=lineStr.find(STR_TIME)
            strMsIndex=lineStr.find(STR_MS)
            timeStr=lineStr[strTimeIndex+len(STR_TIME):strMsIndex-1]
            timeF=float(timeStr)
            if timeF<FAST_UPPER_F:
                fastCounter+=1
                fastRecords.append(timeF)
            elif timeF<=SLOW_THRESHOLD_F:
                okCounter+=1
                okRecords.append(timeF)
            if timeF>SLOW_THRESHOLD_F:
                slowCounter+=1
                slowRecords.append(timeF)
            elif timeF>SUPER_SLOW_THRESHOLD_F:
                superSlowCounter+=1
                sslowRecords.append(timeF)

            if platform.system()==SYSTEM_MAC_PLATFORM and notificationFlag:
                #handle notification
                if timeF>SLOW_THRESHOLD_F:
                    os.system("osascript -e 'display notification \"%sms to %s \" with title \"slow connection detected \"'"%(timeF,IP))
        else:
            failureCounter+=1
            #failure record error msg
            failureRecords.append(lineStr)
        total+=1
        print()
        print(lineStr)
        print_status()

#coding:utf-8
#! /usr/bin/python
# code for linux
import sys
import socket
def decodeIpHeader(packet):
        mapRet = {}
        mapRet["版本 号"] = (int(ord(packet[0])) & 0xF0)>>4
        mapRet["首部长度"] = (int(ord(packet[0])) & 0x0F)<<4
        mapRet["服务类型"] = hex(int(ord(packet[1])))
        mapRet["总长 度"] = (int(ord(packet[2])<<8))+(int(ord(packet[3])))
        mapRet["标   识"] = (int(ord(packet[4])<<8))+(int(ord(packet[5])))
        mapRet["标   志"] = int(ord(packet[6]) & 0xE0)>>5
        mapRet["段 偏移"] = int(ord(packet[6]) & 0x1F)<<8 + int(ord(packet[7]))
        mapRet["生存 期"] = int(ord(packet[8]))
        mapRet["协   议"] = int(ord(packet[9]))
        mapRet["首部校验和"] = int(ord(packet[10])<<8)+int(ord(packet[11]))
        mapRet["源   IP"] = "%d.%d.%d.%d" % (int(ord(packet[12])),int(ord(packet[13])),int(ord(packet[14])), int(ord(packet[15])))
        mapRet["目的 IP"] = "%d.%d.%d.%d" % (int(ord(packet[16])),int(ord(packet[17])),int(ord(packet[18])), int(ord(packet[19])))
        return mapRet 
        
keylist=["版本 号","首部长度","服务类型","总长 度","标   识","标   志","段 偏移","生存 期","协   议","首部校验和","源   IP","目的 IP"]
proto = socket.getprotobyname('tcp') # only tcp
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, proto)
while True:
    try:
        s=raw_input("请输入你想要的抓包数>")
        if s=="exit":
            print "已经退出了！"
            sys.exit(0)
        else:
            n=int(s)
    except ValueError:
        print "你输入的不是整数！请输入一个整数！"
        continue
    for i in range(n):
        print "这是第本次抓包的第%d个数据包！"%(i+1)
        packet = sock.recvfrom(65535)[0]
        if len(packet) == 0:
            sock.close()
        else:
            mapIpTmp = decodeIpHeader(packet)
            for k in range(len(keylist)):
                print keylist[k],"\t : \t",mapIpTmp[keylist[k]]
        print ""
        print ""
    print "本轮抓包结束，结束请输入exit！"
    print ""
    print ""

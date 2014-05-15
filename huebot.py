# HueBot huehue when you hue. Additionally, it huehuehuahue when you huehuehue.
# Triggers when "hue" is found in a message. Maybe I will change that to it being the only chars in a comment.

# Ask /u/SolarLiner anything!

import praw, sys
import datetime

reddit=praw.Reddit('User-Agent: HueBot/1.0')
HasLog=False

# Blacklist:
disallowed=[
    "anime", 
    "asianamerican", 
    "askhistorians", 
    "askscience", 
    "aww", 
    "chicagosuburbs", 
    "cosplay", 
    "cumberbitches", 
    "d3gf", 
    "deer", 
    "depression", 
    "drinkingdollars", 
    "forwardsfromgrandma", 
    "grindsmygears", 
    "indianfetish", 
    "misc", 
    "mixedbreeds", 
    "news", 
    "omaha", 
    "petstacking", 
    "programmingcirclejerk", 
    "raerthdev", 
    "science", 
    "seiko", 
    "suicidewatch", 
    "talesfromtechsupport", 
    "unitedkingdom",
	"bmw", 
    "politics"
  ]
debug=True # True means that bot will only look for comments in /r/testing_ground

try:
	log=open("log.txt", 'a')
	HasLog=True
except:
	print("Failed to open log, log not saved for this session")
	
# === Functions ===
def logWrite(msg):
	stamp=time.strftime("%d %b %Y %H:%M:%S", time.localtime())
	print(msg)
	if HasLog:
		log.write(stamp+": "+msg+"\n")
		log.flush()
		
def Start():
	logWrite("Starting bot, loading processed comments")

	for line in fDone:
		aDone.append(line)
		
def TERMINATE(code):
	logWrite("=== TERMINATED ===")
	sys.exit(code)

def Stop():
	logWrite("Stopping bot")
	fDone.close()
	TERMINATE(0)


	
def connect():
	while true:
		try:
			logWrite("Attempting to connect ...")
			reddit.login('HueBot', 'HueHueHuaHueHueHuaHueHueHua')
			logWrite("Connected.")
			break
		except:
			logWrite("Failed to connect.")
			time.sleep(5)

def generateMessage(level):
	logWrite("Level" + str(level) + " message to respond")

	if(level==0): # comment said "hue"
		return "huehue"
	elif(level==1): # comment said "huehuehue" or "huehuahue"
		return "huehuahuehue"
	elif(level==2): # comment said "huehuahuehuehua" ONLY
		return "WIN"

def AddProcComment(ID):
	aDone.append(ID)
	fDone.write

def processQueue():
	logWrite("==== PROCESSING QUEUE ====")
	
	try:
		for comment in praw.helpers.coment_stream(reddit, 'testing_ground', limit=2500):
			if comment.id not in aDone:
				cDone=False
				level=0
				AddProcComment(comment.id)
				Words = comment.body.lower().split()
				for word in Words:
					if "hue" in word:
						level=0
						cDone=True
					elif "huehuahue" or "huehuehue" or "huehuehua" in word:
						level=1
						cDone=True
					elif "huehuahuehuehua" in word:
						level=2
						cDone=True
					
					if cDone==True:
						break
				
				while cDone==True:
					try:
						comment.reply(generateMessage(level))
						logWrite("Replied to ID "+str(comment.id))
						cDone=False
					except praw.errors.RateLimitExceeded:
						logWrite("Rate limit exceeded. Trying again in 1 minute ...")
						time.sleep(65)
	except praw.errors.RedirectException:
		logWrite("Unexcpected redirection. Attempting to reload ...")
		time.sleep(3)
		
# running part

try:
	fDone=open("ProcID.log", 'r+')
	aDone = []
except:
	logWrite("Error while loading parsed comments. Shutting down.")
	TERMINATE(-1)


Start()
connect()

while True:
	try:
		processQueue()
		
	except KeyboardInterrupt:
		Stop()
		
	except requests.exceptions.ConnectionError:
		logWrite("Connection to server lost!")
		connect()
		
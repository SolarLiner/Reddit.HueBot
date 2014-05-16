# HueBot huehue when you hue. Additionally, it huehuehuahue when you huehuehue.
# Triggers when "hue" is found in a message. Maybe I will change that to it being the only chars in a comment.

# Ask /u/SolarLiner anything!

import praw, sys
from datetime import date, time

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
	#stamp=time.strftime("%d %b %Y %H:%M:%S UTC", time.now())
	stamp = "Message"
	full="["+stamp+"] "+msg
	print(full)
	if HasLog==True:
		log.write(full+"\n")
		log.flush()
		
def Start():
	logWrite("Starting bot, loading processed comments")

	IDs=open("ProcID.log", 'r')
	for line in IDs:
		aDone.append(line)
	IDs.close()
		
def TERMINATE(code):
	logWrite("=== TERMINATED ===")
	sys.exit(code)

def Stop():
	logWrite("Stopping bot")
	fDone.close()
	log.close()
	HasLog=False
	TERMINATE(0)


	
def connect():
	while True:
		try:
			logWrite("Attempting to connect ...")
			reddit.login('Huehue_Bot', 'HueHueHuaHueHueHuaHueHueHua')
			logWrite("Connected.")
			break
		except:
			logWrite("Failed to connect.")

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
	fDone.write(ID+'\n')

def processQueue():
	logWrite("==== PROCESSING QUEUE ====")
	
	try:
		for comment in praw.helpers.comment_stream(reddit, 'bottesting', limit=1000):
			if comment.id not in aDone:
				cDone=False
				level=0
				Words = comment.body.lower().split()
				for word in Words:
					if "hue" in word:
						level=0
						cDone=True
					elif "huehuahue" in word:
						level=1
						cDone=True
					elif "huehuehue" in word:
						level=1
						cDone=True
					elif "huehuehua" in word:
						level=1
						cDone=True
					elif "huehuahuehuehua" in word:
						level=2
						cDone=True
					
					if cDone==True:
						logWrite("Found comment ID "+comment.id)
						break
				
				while cDone==True:
					try:
						comment.reply(generateMessage(level))
						logWrite("Replied to ID "+str(comment.id))
						cDone=False
						AddProcComment(comment.id)
					except praw.errors.RateLimitExceeded:
						logWrite("Rate limit exceeded. Closing ...")
						Stop()
					except praw.errors.APIException:
						logWrite("Content too old. Moving on.")
						cDone=False
						AddProcComment(comment.id)
	except praw.errors.RedirectException:
		logWrite("Unexcpected redirection. Attempting to reload ...")
		
# running part

try:
	fDone=open("ProcID.log", 'a')
	aDone = []
except:
	logWrite("Error while loading parsed comments. Shutting down.")
	TERMINATE(-1)


Start()
logWrite("Hello !")
connect()

while True:
	try:
		processQueue()
		
	except KeyboardInterrupt:
		Stop()
		
	except requests.exceptions.ConnectionError:
		logWrite("Connection to server lost!")
		connect()
		
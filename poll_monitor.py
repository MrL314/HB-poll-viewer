







############### INSERT TOKENS HERE ############################

API_KEY             = ""
       # looks like   "aSAFl8S5Dms90Nda56SAFDJhs"  (this is gibberish :p)
API_KEY_SECRET      = ""
       # looks like   "kaslfhsdui34fphaHGAlSHAlaAkifdashA26D02nDaWGSsja5g"  (this is gibberish :p)

ACCESS_TOKEN        = ""
       # looks like   "0123456789-Abc6DeGhIj2kLmn1OPQ7Rs2TuV1WxyZ123adb8s"  (this is gibberish :p)
ACCESS_TOKEN_SECRET = ""
       # looks like   "afkgs23q0fSa09fdsgsE21kLaFbnSh23FBkj90fsd099D"  (this is gibberish :p)


############## PRESET STUFF #######################

TWEET_ID = 1536891506124267520


########################### BOT CODE ##############

import tweepy, time



CLIENT = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_KEY_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET, wait_on_rate_limit=True)




import math
import matplotlib
import numpy as np
import matplotlib.pyplot as plt



I_CNT = [0, 0]
K_CNT = [0, 0]

X = np.linspace(1, 2, 2)


plt.ion()
fig, ax = plt.subplots()
ax.axis([1, 2, 0, 100])
data_I, = ax.plot(X, np.array(I_CNT), color='#c296ca')
data_K, = ax.plot(X, np.array(K_CNT), color="blue")

ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
ax.tick_params(axis='y', which='major', left=True, right=True, labelright=False)

from matplotlib.ticker import (AutoMinorLocator, MultipleLocator) # for grid ticks
ax.yaxis.set_major_locator(MultipleLocator(2000))
ax.yaxis.set_minor_locator(AutoMinorLocator(2))

ax.grid(which='major', axis='y', color='gray', linestyle='--', linewidth=0.5)
ax.grid(which='minor', axis='y', color='gray', linestyle=':', linewidth=0.5)

fig.set_size_inches((7.55, 4.8))


I_MAX = 0
K_MAX = 0

try:
	with open("VOTE_DATA.csv", 'r') as f:
		for line in f:
			sp = line.replace("\n", "").split(",")
			I_CNT.append(int(sp[0]))
			K_CNT.append(int(sp[1]))
except:
	pass


while True:
	POLL_OPTIONS = CLIENT.get_tweet(TWEET_ID, user_auth=True, expansions="attachments.poll_ids", poll_fields="options").includes['polls'][0].options

	# IRIS
	IRIS_COUNT = POLL_OPTIONS[0]['votes']
	
	# KAIRO
	KAIRO_COUNT = POLL_OPTIONS[1]['votes']


	TOTAL_COUNT = IRIS_COUNT + KAIRO_COUNT

	IRIS_P = round(1000 * IRIS_COUNT / TOTAL_COUNT)/10
	KAIRO_P = round(1000 * KAIRO_COUNT / TOTAL_COUNT)/10

	print("Iris :", str(IRIS_COUNT).rjust(5), "votes (" + str(IRIS_P) + "%)")
	print("Kairo:", str(KAIRO_COUNT).rjust(5), "votes (" + str(KAIRO_P) + "%)")


	I_CNT.append(IRIS_COUNT)
	K_CNT.append(KAIRO_COUNT)

	if IRIS_COUNT > I_MAX:  I_MAX = IRIS_COUNT
	if KAIRO_COUNT > K_MAX: K_MAX = KAIRO_COUNT

	m_cnt = max(IRIS_COUNT, KAIRO_COUNT)
	T = time.perf_counter()

	L = len(I_CNT)-2
	if L > 2:
		X = np.linspace(1, L, L)
		ax.axis([1, L, 0, m_cnt*1.1])
		data_I.set_xdata(X)
		data_I.set_ydata(np.array(I_CNT[2:]))
		data_K.set_xdata(X)
		data_K.set_ydata(np.array(K_CNT[2:]))
		while time.perf_counter() - T < 10:
			
			
				


			fig.canvas.draw()

			fig.canvas.flush_events()

			time.sleep(0.1)



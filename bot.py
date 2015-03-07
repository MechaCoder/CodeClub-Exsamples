#for teepy to work you will need to be working on python 2 and if you have tux the optain tweepy though pip or on windows you will need download the rep form git hub.
import tweepy

TwitterData = {
	'consumK':'gvaMThnctIoHdBr8mIGr9FG9o',
	'consumS':'x9WT4pIWjWpAS1MJKoJI1NHMJH4ae2ohMAJpuHYG0NWuU3pPyv',
	'AccessT':'67029535-ZMdtRQEmf4Laqv667RLHx2rmDcj22S2DkMDU0Js3p',
	'AccessS':'KIKxcHarxdI2Y7bArbnZb2EAA3BFUbVaMeUfGAgTG1l6l'
}

auth = tweepy.OAuthHandler(TwitterData['consumK'], TwitterData['consumS'])
auth.set_access_token(TwitterData['AccessT'], TwitterData['AccessS'])

api = tweepy.API(auth)
data = api.me()
api.update_status(status="[enter a string here to ipload to twitter")


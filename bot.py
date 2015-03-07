#for teepy to work you will need to be working on python 2 and if you have tux the optain tweepy though pip or on windows you will need download the rep form git hub.
import tweepy

TwitterData = { #this is a data dictory consiting of a key and value which helps a lot when working with object.
	'consumK':'gvaMThnctIoHdBr8mIGr9FG9o',
	'consumS':'x9WT4pIWjWpAS1MJKoJI1NHMJH4ae2ohMAJpuHYG0NWuU3pPyv',
	'AccessT':'67029535-ZMdtRQEmf4Laqv667RLHx2rmDcj22S2DkMDU0Js3p',
	'AccessS':'KIKxcHarxdI2Y7bArbnZb2EAA3BFUbVaMeUfGAgTG1l6l'
}

auth = tweepy.OAuthHandler(TwitterData['consumK'], TwitterData['consumS'])
auth.set_access_token(TwitterData['AccessT'], TwitterData['AccessS'])
api = tweepy.API(auth) #api is now the data call oubject which will get the dat for you
''' twitter use a sercure API that Requires a speail handshake,
the handshake is not done with hands it is done with keys as 
you can see in the data dictory "TwitterData" so what i am doing 
here is conductioning the handshake with twitter, I have done 
is placed the data at the top which means i am not reapting my self in code
and if the keys change then i only need change the keys in one place ^_^ '''
data = api.me()
''' unlike with Parse the data is not given use JSON but useing a class of wich you can interact
with the fuctions and varibales of the class an exsample being below '''

#i call the api object use the class 'update_status' and change the status varable 'status to a string of my choice ^_^'
api.update_status(status="[enter a string here to upload to twitter]")
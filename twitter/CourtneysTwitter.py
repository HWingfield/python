import twitter, datetime, urllib2

user = 792015036235603968
file = open("twittercredentials.txt")
creds = file.read().split('\n')

filename = open("C:\Users\Harrison\AppData\Local\Google\Chrome\User Data\Default\Current Session")
mywebsites = filename.read()

previouswebsite = mywebsites.rfind("http")
previouswebsite2 = mywebsites[previouswebsite:-50]
print(str(previouswebsite2))

api = twitter.Api(creds[0],creds[1],creds[2], creds[3])

##timestamp = datetime.datetime.utcnow()
#
response = api.PostUpdate ("Last website visited " + str(previouswebsite2))
#
#print("Status updated to: " + response.text)


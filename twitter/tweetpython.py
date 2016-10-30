import twitter, datetime, sqlite3, urllib, urllib2

TwitterUser = 238760074

Creds_Text_File = open("TwitterCredentials.txt")
CredsContent = Creds_Text_File.read()
CredsList = CredsContent.split('\n')
Creds_Text_File.close()

Chrome_History_Text_File = open("C:\Users\Harrison\AppData\Local\Google\Chrome\User Data\Default\Current Session")
Chrome_History_Contents = Chrome_History_Text_File.read()

SearchChromeHistory = Chrome_History_Contents.rfind("http")

endIndex = Chrome_History_Contents.find(chr(0),SearchChromeHistory)
LastURL = Chrome_History_Contents[SearchChromeHistory:endIndex]

response = urllib2.urlopen(LastURL)
html = response.read()
startIndex = html.find("<title>")
endIndex = html.find("</title>")

HtmlTitle = html[startIndex+7:endIndex]

TweetingAPI = twitter.Api(CredsList[0],CredsList[1],CredsList[2],CredsList[3])
Time = datetime.datetime.utcnow()

print(HtmlTitle)
Tweet = TweetingAPI.PostUpdate("Went to " + str(HtmlTitle))

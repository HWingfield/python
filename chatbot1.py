#*******
#opens text file and reads it
text_file = open("stop-words.txt")
content_of_file = text_file.read()

#*******
#gives a list of stopwords
stopwords = content_of_file.split('\n')
text_file .close()


#*********
#Greeting
print("Welcome to RupertBot")
response = raw_input("Comment vous appelez-vous?(That's french for what's yo name bruv) ")
UserInputList = response.split(" ")
filteredList = []
for UserInputWord in UserInputList:
    if (UserInputWord not in stopwords):
        filteredList.append(UserInputWord)
        
for filteredUserWord in filteredList:
    if(filteredUserWord == "rupert"):
        print("yay")

##******
##How are you?
print("Hello " + response)
response = raw_input("Hows you fam? ")

howareyou = "good" or "fine" or "swell" or "smashing" or "great" or "top" or "lavely" or "lovely gubly"
seshmeht = "sesh"

if (response == howareyou):
    print("lavely, I'm also " + response)
    
if (response == seshmeht):
    print("ayyy you ruddy legend meht")
    
elif (response not in howareyou):
    print("Why are you " + response + "?") 

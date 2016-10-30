#--------------------------------------------------------------------
#opens text file and reads it
text_file = open("stop-words.txt")
content_of_file = text_file.read()


#--------------------------------------------------------------------
#opens text file and reads it
text_file2 = open("nounwords.txt")
content_of_file2 = text_file2.read()
#--------------------------------------------------------------------
#gives a list of stopwords
stopWordsList = content_of_file.split('\n')
text_file.close()
nounList = content_of_file2.split('\n')
text_file2.close()



howareyou = ["good", "fine", "swell", "smashing", "great", "top", "lavely", "lovely gubly"]
seshmeht = "sesh"


nonstopwords = []
filteredList = []

#--------------------------------------------------------------------
#Greeting
print("Welcome to RupertBot")
response = raw_input("Comment vous appelez-vous? ")
UserInputList = response.split(" ")

for UserInputWord in UserInputList:
    if (UserInputWord not in stopWordsList):
        nonstopwords.append(UserInputWord)
        

#--------------------------------------------------------------------
#how are you
        
nonstopwords = []
UserInputList = []

print("Hello " + UserInputWord)
response = raw_input("Hows you fam? ")
UserInputList = response.split(" ")

for UserInputWord in UserInputList:
    if (UserInputWord not in stopWordsList):
        nonstopwords.append(UserInputWord)

for everyFilteredWord in nonstopwords:
    if (everyFilteredWord in howareyou):
        print("safe! I'm glad you're " + everyFilteredWord + "!" + '\n')
        response = raw_input ("ur sure tho right meht?")
    elif (everyFilteredWord == seshmeht):
        print("ayyy you ruddy legend meht")
    elif (everyFilteredWord not in howareyou or seshmeht):
        print("U sayin' wut famalam")
 
#--------------------------------------------------------------------
#Activities?
response = raw_input("Anyway gov, wat u been up to fam? ")
UserInputList = response.split(" ")

for UserInputWord in UserInputList:
    if (UserInputWord in nounList):
        nonstopwords.append(UserInputWord)
print("Ye, I also love " + UserInputWord + "s tbh")
print("Anyway gov, I'd love to stay and chat about " + UserInputWord + " but don't you have other projects to Mark?")
print("K bye, gimme a first plz")


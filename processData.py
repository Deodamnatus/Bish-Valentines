from bs4 import BeautifulSoup

# html file is pulled from whipplehill directory search (scroll to bottom to load all, copied from id="directory-items-container")
path='/home/jeremy/Documents/Programming/Web-Dev/Bish-Valentines/'

gradeSortDict={21:'Freshman', 20:'Sophomore', 19:'Junior', 18:'Senior'}

noEmailList=[]
 # Dict format: {email: {matches:{match1email:percentmatch}}, name:name, picture:pictureurl, grade:grade} SHOULD BE DICT WITH EMAIL KEYS

soup9 = BeautifulSoup(open(path + '9Scrape.html'), "html.parser")
soup10 = BeautifulSoup(open(path + '10Scrape.html'), "html.parser")
soup11 = BeautifulSoup(open(path + '11Scrape.html'), "html.parser")
soup12 = BeautifulSoup(open(path + '12Scrape.html'), "html.parser")

elementList9 = soup9.find_all('tr')
elementList10 = soup10.find_all('tr')
elementList11 = soup11.find_all('tr')
elementList12 = soup12.find_all('tr')
elementList = elementList9 + elementList10 + elementList11 + elementList12
print('Got list of ',len(elementList),'elements . . .')

def convertStringToDict(stringDict):
    replaceDict={}

    # Adding each email scraped to replaceDict
    for tr in elementList:
        nameList=str(tr.find('td', attrs={'width': ''}).find('div', attrs={'class': ''}).find('h3').text).split("'")
        name=nameList[0]
        if tr.find('td', attrs={'width': ''}).find('div', attrs={'class': ''}).find('p').find('a') == None:
            email='No Email'
            noEmailList.append(name)
        else:
            email=str(tr.find('td', attrs={'width': ''}).find('div', attrs={'class': ''}).find('p').find('a').text)
            replaceDict[email]="'" + email.lower().replace('.','~|') + "'"
            print(email.lower().replace('.','~|'))

    # missing emails populated through this list
    emailPatchList=[]
    # Adding emails that weren't scraped but still answered survey
    for email in emailPatchList:
        replaceDict[email]="'" + email.lower().replace('.','~|') + "'"


    # Adding genders to replaceDict
    genderList=['Male','Female','Either','Who even knows anymore','gay af','nonbinary','Nonbinary','Child','Trans-octopus','Gender is fake' ]
    for gender in genderList:
        replaceDict[gender]="'"+gender+"'"

    # Adding static keys to replaceDict & = --> : & fix empty gender
    replaceDict["'gender:,'"]="'gender':'',"    # replace empty gender values with ''
    replaceDict['ranking']="'ranking'"
    replaceDict['percentage']="'percentage'"
    replaceDict['email']="'email'"
    replaceDict['name']="'name'"
    replaceDict['gender']="'gender'"
    replaceDict['=']=':'

    # Run replaceDict against stringDict
    for key in list(replaceDict.keys()):
        print('replacing ', key, ' with ', replaceDict[key])
        stringDict=stringDict.replace(str(key),str(replaceDict[key]))

    # Push ouput to file, formatted for copy paste into script
    outputFile = open(path+"completedDict.txt","w")
    # Will do newline after every '{' so python can regonize format
    splitStringDict=stringDict.replace('{','{\n')
    outputFile.write(splitStringDict)
    outputFile.close()

def convertValidDictToPushFormat(stringDict):
    userDict={} # final data structure

    keyErrored=[] # list of users who don't have entires, yet are in other users' matchlist (any users in here were not processed by the googlescript)
    emailList=[] # list of every email from those who submitted the form

    # Generate list of emails who submitted results from old data structure
    for user in stringDict:
        emailList.append(user['email'])
        userDict[user['email']]={}

    # Generating userDict[useremail][matches]
    for user in stringDict:
        for i in range(0,5):
            print('adding: ',user['ranking'][i]['email'], ' : ',  user['ranking'][i]['percentage'])

        userDict[user['email']]['matches']={
        user['ranking'][0]['email']:user['ranking'][0]['percentage'],
        user['ranking'][1]['email']:user['ranking'][1]['percentage'],
        user['ranking'][2]['email']:user['ranking'][2]['percentage'],
        user['ranking'][3]['email']:user['ranking'][3]['percentage'],
        user['ranking'][4]['email']:user['ranking'][4]['percentage'],
        }

        # Add gender of matches to their profile
        for match in user['ranking']:
            print('adding: ',match['email'],' : ', match['gender'])
            # if KeyError, that means data incomplete
            try:
                userDict[match['email']]['gender']=match['gender']
            except KeyError:
                keyErrored.append(match['email'])

    print('Keyerrored: ',keyErrored)
    # Push converted dict to newDitStructure.txt NOTE THIS IS NOT THE STURCTURE TO PASTE INTO FIFREBASE UPLOAD
    outputFile = open(path+"newDictStructure.txt","w")
    outputFile.write(str(userDict).replace('{','{\n'))
    outputFile.close()


    # add scraped data to new data structure
    for tr in elementList:
        #finding image
        if tr.find('td', attrs={'width': '12%'}).find('div') == None:
            imglink='https://www.chcs.org/media/Profile_avatar_placeholder_large-1-200x200.png'
        else:
            imglink='https://bbk12e1-cdn.myschoolcdn.com' + str(tr.find('td', attrs={'width': '12%'}).find('div').img['src'])

        #finding name
        nameList=str(tr.find('td', attrs={'width': ''}).find('div', attrs={'class': ''}).find('h3').text).split("'")
        name=nameList[0]
        grade=gradeSortDict[int(nameList[1])]

        #finding email
        if tr.find('td', attrs={'width': ''}).find('div', attrs={'class': ''}).find('p').find('a') == None:
            email='No Email'
            noEmailList.append(name)
        else:
            email=str(tr.find('td', attrs={'width': ''}).find('div', attrs={'class': ''}).find('p').find('a').text).lower().replace('.', '~|')

        #add data to dict element
        if email in emailList:
            userDict[email]['name']=name
            userDict[email]['picture']=imglink
            userDict[email]['grade']=grade
    print('\n\nNo Email: ',noEmailList) # list of users whos email visibility is turned off in whipplehill
    print('Writing dict output to file: fullyProcessedDict.txt . . .')
    outputFile = open(path+"fullyProcessedDict.txt","w")
    outputFile.write(str(userDict).replace('}', '}\n'))
    outputFile.close()

stringDict = ''

#convertStringToDict(stringDict)
convertValidDictToPushFormat(stringDict)

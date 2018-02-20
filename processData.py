from bs4 import BeautifulSoup

nameOfDataFile=input("Name of file you'd like to output to\n:") + '.txt'

# html file is pulled from whipplehill directory search (scroll to bottom to load all, copied from id="directory-items-container")
soup9 = BeautifulSoup(open(path + '9Scrape.html'), "html.parser")
soup10 = BeautifulSoup(open(path + '10Scrape.html'), "html.parser")
soup11 = BeautifulSoup(open(path + '11Scrape.html'), "html.parser")
soup12 = BeautifulSoup(open(path + '12Scrape.html'), "html.parser")

elementList9 = soup9.find_all('tr')
elementList10 = soup10.find_all('tr')
elementList11 = soup11.find_all('tr')
elementList12 = soup12.find_all('tr')
elementList = elementList9 + elementList10 + elementList11 + elementList12

print('Got list of ',len(elementList),' students . . .\n')

def convertValidDictToPushFormat(stringDict):
    # add scraped data to data structure
    global userDict
    gradeSortDict={21:'Freshman', 20:'Sophomore', 19:'Junior', 18:'Senior'} # dict to get grade string from 20YY
    missingInfo={'email': [], 'picture': []}
    for tr in elementList:
        #finding name
        nameList=str(tr.find('td', attrs={'width': ''}).find('div', attrs={'class': ''}).find('h3').text).split("'")
        name=nameList[0]
        grade=gradeSortDict[int(nameList[1])]

        #finding image
        if tr.find('td', attrs={'width': '12%'}).find('div') == None:
            imglink='https://www.chcs.org/media/Profile_avatar_placeholder_large-1-200x200.png'
            missingInfo['picture'].append(name)
        else:
            imglink='https://bbk12e1-cdn.myschoolcdn.com' + str(tr.find('td', attrs={'width': '12%'}).find('div').img['src'])

        #finding email
        if tr.find('td', attrs={'width': ''}).find('div', attrs={'class': ''}).find('p').find('a') == None:
            email='No Email'
            missingInfo['email'].append(name)
        else:
            email=str(tr.find('td', attrs={'width': ''}).find('div', attrs={'class': ''}).find('p').find('a').text).lower().replace('.', '~|')

        #add data to dict element
        if email in list(userDict.keys()):
            userDict[email]['name']=name
            userDict[email]['picture']=imglink
            userDict[email]['grade']=grade

    print('\nNo Email: ', missingInfo['email']) # list of users whos email visibility is turned off in whipplehill
    for user in missingInfo['email']:
        print(user)
    print('\nNo Picture: ', missingInfo['picture']) # list of users whos picture visibility is turned off in whipplehill
    for user in missingInfo['picture']:
        print(user)

    print('\nWriting dict output to file: ' + nameOfDataFile + '.txt . . .')
    outputFile = open(nameOfDataFile+'.txt',"w")
    outputFile.write()
    outputFile.close()

userDict= #PASTE GOOGLE DOC HERE ex: userDict={someEmail:{...}...}

convertValidDictToPushFormat(userDict)

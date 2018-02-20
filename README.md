# Bish-Valentines
Files for processing data for Bishop's Valentines and files to firebase website hosting
# Description of files

9Scrape.html  - Data pulled from WhippleHill search for 9th graders

10Scrape.html  - Data pulled from WhippleHill search for 10th graders

11Scrape.html  - Data pulled from WhippleHill search for 11th graders

12Scrape.html  - Data pulled from WhippleHill search for 12th graders

processData.py  - Script to process data ouputted by matching algorithm and reformat to be uploaded to firebase

database.rules.json  - Firebase rules file. Turn on writing when pushing data GENERATED WHEN INTIALIZING FIREBASE

firebase.json  - Used by Firebase to push files GENERATED WHEN INTIALIZING FIREBASE

public  - Contains website files (replace firebase scripts in html with your project scripts)

# Instructions
Initialize firebase project in directory of downloaded files.
Note: processData.py requires BeautifulSoup library installed in order to scrape html
1. Aquire googlescript data. This is not in any useable format, so we need to process it with processData.py
2. Download html queries to files. Do a WhippleHill search for each grade level and scroll to the bottom to load all students. View souce and copy inner html of element with id="directory-items-container" then paste into corresponding html file
3. Get list of unique gender responses and set genderList equal to it. emailPatchList will be populated later.
4. Put data through processData.py. Set stringDict to a string of googlescript data. Run convertStringToDict(stringDict). Some students have email visibility turned off in whipplehill, so search completedDict.txt for @bishops.com and add each address to emailPatchList. Put data through processData.py. Set stringDict to a string of googlescript data. Run convertStringToDict(stringDict).
Now we have a valid data structure we can import into python. However, if we pushed this to firebase, it woulnd't process lists correctly and would be inefficient.
5. Put new data through processData.py again. Set stringDict to the contents of completedDict.txt. Python will recognize this as a valid structure (list of nested dictoinaries). Run convertValidDictToPushFormat(stringDict). If you recieve a syntax error, check that the data structure is formatted propperly. If you see Keyerrored: [] your data is complete and you can move onto the next step. If not, your data from googlescript is incomplete.
6. Make sure in firebase rules, write is set to true. Add the following lines to index.html below the other script tags, replacing '$data' with the data structure returned into "fullyProcessedDict.txt", and paste the path of the page into your browser:
```
<script>
firebase.database().ref().set( $data
);
</script>
```
7. Your data should be uploaded to firebase. SET WRITE TO FALSE AND READ TO TRUE. Deploy the firebase website.

# Note about GoogleScript Code and Questions
Sahil Malhotra has not documented how he ran the GoogleScript code Kevin Chen wrote and gave him. Therefore not included in this repository. Please get in contact with him in order to get the matching algorithm and instructions on how to run it.

Any questions regarding the python script or website files can be addressed to Jeremy Gleeson or you can open an issue on the respository.

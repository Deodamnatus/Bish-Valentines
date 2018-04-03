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

Initialize firebase project in directory of downloaded files. Instructions on how to do this can be found here: https://firebase.google.com/docs/web/setup
Hosting and Realtime Database should be enabled when you initialize the project.

Note: processData.py requires python3 and the BeautifulSoup library installed in order to scrape html.
To install the newest version of python3: https://www.python.org/downloads/
To install libraries in python: https://packaging.python.org/tutorials/installing-packages/

1. Copy the GoogleScript file to your google drive: https://script.google.com/d/1-1gyYickzpFOlmM7Uq293q5mz-dJKtoCFGUOhxA7_O4V5oWoEQSzoxcb/edit?usp=sharing
2. Update answers to current year's answers, spreadsheet ID, and google doc output link
3. Run GoogleScript. Output in the google doc should look like a bunch of nested dictionaries.
4. Download html queries to files. Do a WhippleHill search for each grade level and scroll to the bottom to load all students. View source and copy inner html of element with id="directory-items-container" then paste into corresponding html file
5. Put data through processData.py by copying google document contents to the value of userDict and running the script
6. Replace the firebase scripts in index.html and results.html with those from your new firebase project (found by clicking "Add Firebase to your web app" on the project overview page)
6. Make sure in firebase rules, write is set to true. Add the following lines to index.html below the other script tags, replacing '$data' with the data structure returned into the processData.py output file, and paste the path of the page into your browser (something like /home/yourname/Documents/Bish-Valentines/public/index.html):
```
<script>
firebase.database().ref().set( $data
);
</script>
```
7. Your data should be uploaded to firebase. Remove the above code from your index.html page and make sure to set read to true and write to false for the whole database before moving to the next step.
8. Deploy the web files to firebase.

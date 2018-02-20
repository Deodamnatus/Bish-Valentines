const mainContainer=document.getElementById('mainContainer');
const titleBox=document.getElementById('titleBox');
const database=firebase.database();

String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.split(search).join(replacement);
};

function checkEmail(email) {
  firebase.database().ref(email).once('value').then(function(snapshot){
    if (snapshot.val() !== null) {
      fetchResults();
    } else {
      alert('Invalid Email');
      window.location.href = 'index.html';
    }
  });
}



function createMatchElement(name, gender, grade, pic, match){
  var newDiv=document.createElement("div");
  var newImg=document.createElement("img");
  var newDivProfileBox=document.createElement("div");
  var newUl=document.createElement("ul");
  var newLiName=document.createElement("li");
  var newLiGender=document.createElement("li");
  var newLiGrade=document.createElement("li");
  var newLiMatch=document.createElement("li");
  var newTextName=document.createTextNode(name);
  var newTextGender=document.createTextNode(gender);
  var newTextGrade=document.createTextNode(grade);
  var newTextMatch=document.createTextNode(match+'% Match');
  newDiv.classList.add("wrap-input100");
  newDiv.classList.add("m-b-16");
  newDivProfileBox.classList.add('profileBox');
  newImg.src=pic;
  newLiName.appendChild(newTextName);
  newLiGender.appendChild(newTextGender);
  newLiGrade.appendChild(newTextGrade);
  newLiMatch.appendChild(newTextMatch);
  newUl.appendChild(newLiName);
  newUl.appendChild(newLiGender);
  newUl.appendChild(newLiGrade);
  newUl.appendChild(newLiMatch);
  newDivProfileBox.appendChild(newUl);
  newDiv.appendChild(newImg);
  newDiv.appendChild(newDivProfileBox);
  mainContainer.append(newDiv);
}

function fetchResults() {
  database.ref(window.email).once('value').then( function(snapshot) {
    if (snapshot.val().name){
      titleBox.innerHTML='Top 5 Matches For ' + snapshot.val().name.split(' ')[0];
    }
    snapshot.child('matches').forEach(function(childSnapshot) {
      database.ref(childSnapshot.key).once('value').then( function(matchSnapshot) {
        if (matchSnapshot.val().name){
          name=matchSnapshot.val().name;
        } else {
          name=childSnapshot.key.toString().replaceAll('~|','.') // if error fetching name set it to email
        }

        if (matchSnapshot.val().grade){
          grade=matchSnapshot.val().grade;
        } else {
          grade=''
        }

        if (matchSnapshot.val().picture){
          picture=matchSnapshot.val().picture;
        } else {
          picture='https://www.chcs.org/media/Profile_avatar_placeholder_large-1-200x200.png'
        }

        gender=matchSnapshot.val().gender;
        match=childSnapshot.val();
        createMatchElement(name, gender, grade, picture, match);
      });
    });
  });
}

var url = document.location.href;
window.email = url.split('?')[1].split('=')[1];
checkEmail(window.email);

const txtEmail=document.getElementById("email");
const btnSubmit=document.getElementById("submitBtn");

String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.split(search).join(replacement);
};

function checkEmail(email) {
  firebase.database().ref(email).once('value').then(function(snapshot){
    if (snapshot.val() !== null) {
      var url = 'results.html?email=' + email;
      document.location.href = url;
    } else {
      alert('Invalid Email');
      window.location.href = 'index.html';
    }
  });
}

btnSubmit.addEventListener('click', e =>{
  var email=txtEmail.value.toString().toLowerCase().replaceAll('.', '~|');
  checkEmail(email);
});

txtEmail.addEventListener("keyup", function(event) {
    event.preventDefault();
    // if enter pressed
    if (event.keyCode === 13) {
        btnSubmit.click();
    }
});

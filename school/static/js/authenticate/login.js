
// show and hide password
var togglePassword = document.querySelector('#togglePassword');
var password = document.querySelector('#password');
var type;
// add event listener as clicked on icon to hide password

togglePassword.addEventListener('click', function (e) {


  if (password.getAttribute('type') === 'password') {
    type = 'text';
  }
  else {
    type = 'password';
  }

  password.setAttribute('type', type);

  // toggle the eye slash icon
  this.classList.toggle('fa-eye-slash');
});

// remember me

const rmCheck = document.getElementById("rememberMe"),
  emailInput = document.getElementById("email");

if (localStorage.checkbox && localStorage.checkbox !== "") {
  rmCheck.setAttribute("checked", "checked");
  emailInput.value = localStorage.username;
} else {
  rmCheck.removeAttribute("checked");
  emailInput.value = "";
}


// function lsRememberMe() {
//   if (rmCheck.checked && emailInput.value !== "") {
//     localStorage.username = emailInput.value;
//     localStorage.checkbox = rmCheck.value;
//   } else {
//     localStorage.username = "";
//     localStorage.checkbox = "";
//   }
// }
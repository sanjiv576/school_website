var general_panel = document.querySelector('#fill-general-details');
var register_panel = document.querySelector('#fill-signup-details');

function openRegisterPanel() {
    general_panel.style.left = '-430px';
    register_panel.style.left = '50px';
}


function openGeneralPanel() {
    general_panel.style.left = '50px';
    register_panel.style.left = '350px';
}


var modal = document.getElementById('login-form');
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = 'flex';
    }
}


// register validation

// checks the validation of repeating every form field of Search Flight
function checkFormValidation(formVal, whichForm, msg){
    if(formVal === ''){
        setError(whichForm, msg);

    } 
    else {

        setSuccess(whichForm);
        
    }
}
// const form = document.getElementById('register');
// const firstName = document.getElementById('firstName');
// const middleName = document.getElementById('middleName');
// const lastName = document.getElementById('lastName');
// const contact = document.getElementById('contact');
// const role = document.getElementById('role');
// const username = document.getElementById('username');
// const password = document.getElementById('password');
// const confirmPassword = document.getElementById('confirmPassword');

function checkValidation(){
    

    const form = document.getElementById('register');
    const firstName = document.getElementById('firstName');
    const middleName = document.getElementById('middleName');
    const lastName = document.getElementById('lastName');
    const contact = document.getElementById('contact');
    const role = document.getElementById('role');
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirmPassword');


    var firstNameVal = firstName.value;
    var middleNameVal = middleName.value;
    var lastNameVal = lastName.value;
    var contactVal = contact.value;
    var roleVal = role.value;
    var usernameVal = username.value;
    var passwordVal = password.value;
    var confirmPassVal = confirmPassword.value;

    var firstNameMsg = "invalid";
    checkFormValidation(firstNameVal, firstName, firstNameMsg);

    

}
// form.addEventListener('submit', e => {
//     e.preventDefault();

//     validateInputs();
// });

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

const validateInputs = () => {
    var usernameValue = username.value.trim();
    var emailValue = email.value.trim();
    var passwordValue = password.value.trim();
    var confirmPassVal = confirmPassword.value.trim();

    if(usernameValue === '') {
        setError(username, 'Username is required');
    } else {
        setSuccess(username);
    }

    if(emailValue === '') {
        setError(email, 'Email is required');
    } else if (!isValidEmail(emailValue)) {
        setError(email, 'Provide a valid email address');
    } else {
        setSuccess(email);
    }

    if(passwordValue === '') {
        setError(password, 'Password is required');
    } else if (passwordValue.length < 6 ) {
        setError(password, 'Password must be at least 6 character.')
    } else {
        setSuccess(password);
    }

    if(confirmPassVal === '') {
        setError(confirmPassword, 'Please confirm your password');
    } else if (confirmPassVal !== passwordValue) {
        setError(confirmPassword, "Passwords doesn't match");
    } else {
        setSuccess(confirmPassword);
        
    }


    if(usernameValue !== '' && emailValue !== '' && confirmPassVal === passwordValue && passwordValue !== '' && password2Value !== '' && password2Value.length > 6){
        
        alert("successfully inserted");
        form.submit();

    }




};

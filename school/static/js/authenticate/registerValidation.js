
// function to display error message

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
}

// function to success message which is empty 
const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

// pop sweet alert message 

function popAlert(msg){
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: msg,
        
      })
}

// checks the validation of repeating every form field
function checkFormValidation(formVal, fieldName, fieldLabel){
    if(formVal === ''){
        erro_msg = " * " + fieldLabel + " is required, which cannot be empty."
        popAlert(erro_msg);
        setError(fieldName,erro_msg);

    } 
    else {

        setSuccess(fieldName);
        
    }
}

// if all fields are empty show error in all fields
function emptyFields(item, indx){
    setError(item,erro_msg);
}


var erro_msg = '';
function verifyDetails(){
    // alert("Hello boss");
    // e.preventDefault();
    const form = document.getElementById('register');
    const firstName = document.getElementById('firstName');
    const middleName = document.getElementById('middleName');
    const lastName = document.getElementById('lastName');
    const contact = document.getElementById('contact');
    const role = document.getElementById('role');
    const username = document.getElementById('username');
    const password = document.getElementById('password');
    const password2 = document.getElementById('confirmPassword');


    var firstNameVal = firstName.value.trim();
    var middleNameVal = middleName.value.trim();
    var lastNameVal = lastName.value.trim();
    var roleVal = role.value.trim();
    var usernameVal = username.value.trim();
    var contactVal = contact.value.trim();
    var passwordVal = password.value.trim();
    var password2Val = password2.value.trim();


    if(firstNameVal === ''){
        erro_msg = "* First Name is required, which cannot be empty."
        popAlert(erro_msg);
        setError(firstName,erro_msg);
    }
    else {
        setError(firstName);
    }

    if(lastNameVal === ''){
        erro_msg = " * Last Name is required, which cannot be empty."
        popAlert(erro_msg);
        setError(lastName,erro_msg);
    }
    else {
        setError(lastName);
    }


    if(contactVal === ''){
        erro_msg = " * Contact is required, which cannot be empty."
        popAlert(erro_msg);
        setError(contact,erro_msg);
    }
    else {
        setError(contact);
    }


    if(roleVal === '' || roleVal == "Choose role"){
        erro_msg = " * Role is required, which cannot be empty."
        popAlert(erro_msg);
        setError(role,erro_msg);
    }

    else {
        setError(role);
    }

    if(firstNameVal === '' && lastNameVal === '' && contactVal === '' &&  roleVal === 'Choose role' && usernameVal === '' && passwordVal === '' && password2Val === ''){
        
        erro_msg = "* fields are required, cannot be empty."
        
        const all_fields = ["firstName", 'lastName', 'contact', 'role', 'username', 'password', 'password2'];

        // all_fields.forEach(emptyFields);
        for(let i = 0; i < all_fields.length; i++){
            
            popAlert(all_fields[i],erro_msg);
        }
        popAlert(erro_msg);


        
    }


    // if(passwordVal == ''){
    //     erro_msg = " * Password is required, which cannot be empty."
    //     popAlert(erro_msg);
    //     setError(password, erro_msg);
    // }
    // else {
    //     setSuccess(password);
    // }

    // if(usernameVal === ''){
    //     erro_msg = " * Username is required, which cannot be empty."
    //     // popAlert(erro_msg);
    //     setError(username,erro_msg);
    // }

    // else {
    //     setError(username);
    // }


    // checkFormValidation(firstNameVal, firstName, 'First Name');
    // checkFormValidation(lastNameVal, lastName, 'Last Name');
    // checkFormValidation(contactVal, contact, 'Contact');
    // checkFormValidation(roleVal, role, 'Role');
    // checkFormValidation(usernameVal, username, 'Username');
    // checkFormValidation(passwordVal, password, 'Password');
    // checkFormValidation(password2Val, password2, 'Confirm Password');
    


    

}

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
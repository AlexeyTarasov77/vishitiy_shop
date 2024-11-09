document.addEventListener('DOMContentLoaded', function() {
    const userNameInput = document.getElementById('id_username');
    const passwordOne = document.getElementById('id_password1');
    const passwordTwo = document.getElementById('id_password2');
    const password = document.getElementById('id_password');
   
    if (userNameInput) {
        userNameInput.addEventListener('input', function() {
            const maxLength = 25;
            if (userNameInput.value.length > maxLength) {
                userNameInput.value = userNameInput.value.slice(0, maxLength);
            }
        });
    }

    if (passwordOne) {
        passwordOne.addEventListener('input', function() {
            const maxLength = 30;
            if (passwordOne.value.length > maxLength) {
                passwordOne.value = passwordOne.value.slice(0, maxLength);
            }
        });
    }

    if (passwordTwo) {
        passwordTwo.addEventListener('input', function() {
            const maxLength = 30;
            if (passwordTwo.value.length > maxLength) {
                passwordTwo.value = passwordTwo.value.slice(0, maxLength);
            }
        });
    }

    if (password) {
        password.addEventListener('input', function() {
            const maxLength = 30;
            if (password.value.length > maxLength) {
                password.value = password.value.slice(0, maxLength);
            }
        });
    }
});

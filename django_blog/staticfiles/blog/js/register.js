// blog/static/blog/js/register.js

document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.querySelector('form');
    
    if (registerForm) {
        registerForm.addEventListener('submit', function(e) {
            const username = document.querySelector('#id_username');
            const email = document.querySelector('#id_email');
            const password1 = document.querySelector('#id_password1');
            const password2 = document.querySelector('#id_password2');
            
            if (!username.value.trim()) {
                e.preventDefault();
                alert('Please enter a username');
                username.focus();
            } else if (!email.value.trim()) {
                e.preventDefault();
                alert('Please enter an email address');
                email.focus();
            } else if (!password1.value.trim()) {
                e.preventDefault();
                alert('Please enter a password');
                password1.focus();
            } else if (password1.value !== password2.value) {
                e.preventDefault();
                alert('Passwords do not match');
                password2.focus();
            }
        });
    }

    console.log('Register script loaded successfully');
});
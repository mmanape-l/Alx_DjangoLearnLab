// blog/static/blog/js/login.js

document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.querySelector('form');
    
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            const username = document.querySelector('#id_username');
            const password = document.querySelector('#id_password');
            
            if (!username.value.trim()) {
                e.preventDefault();
                alert('Please enter a username');
                username.focus();
            } else if (!password.value.trim()) {
                e.preventDefault();
                alert('Please enter a password');
                password.focus();
            }
        });
    }

    console.log('Login script loaded successfully');
});
function emailValidation() {
const form = document.getElementById('form');

form.addEventListener('submit', function(e) {
    if (form.email.value !== form.email_confirm.value) {
    e.preventDefault();

      // Remove any existing alert to avoid duplicates
    const oldAlert = document.querySelector('.alert');
    if (oldAlert) {
        oldAlert.remove();
    }

      // Create error message
    const element = document.createElement('p');
    element.textContent = "Email addresses do not match";
    element.classList.add("alert");

      // Insert after confirm email field
    form.email_confirm.insertAdjacentElement('afterend', element);

      // Remove after 3 seconds
    setTimeout(function() {
        if (element.parentNode) {
        element.remove();
        }
    }, 3000);
    }
});
}

window.onload = emailValidation;
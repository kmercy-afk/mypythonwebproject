document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default submission for demo

    const email = document.getElementById('email').value;
    const confirmEmail = document.getElementById('confirm-email').value;
    const errorDiv = document.getElementById('error-message');

    if (email !== confirmEmail) {
        errorDiv.style.display = 'block';
        // Form background remains white, no change
    } else {
        errorDiv.style.display = 'none';
        // Proceed with form submission logic here if needed
        alert('Form submitted successfully!');
    }
});

// Optional: Real-time validation on confirmation email input
document.getElementById('confirm-email').addEventListener('input', function() {
    const email = document.getElementById('email').value;
    const confirmEmail = this.value;
    const errorDiv = document.getElementById('error-message');

    if (confirmEmail && email !== confirmEmail) {
        errorDiv.style.display = 'block';
    } else {
        errorDiv.style.display = 'none';
    }
});
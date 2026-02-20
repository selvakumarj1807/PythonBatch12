const form = document.getElementById("registerForm");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    let name = document.getElementById("name");
    let email = document.getElementById("email");
    let password = document.getElementById("password");
    let confirmPassword = document.getElementById("confirmPassword");

    let valid = true;

    clearErrors();

    // Name validation
    if (name.value.trim() === "") {
        showError(name, "Name is required");
        valid = false;
    }

    // Email validation
    if (email.value.trim() === "") {
        showError(email, "Email is required");
        valid = false;
    } else if (!validateEmail(email.value)) {
        showError(email, "Invalid email format");
        valid = false;
    }

    // Password validation
    if (password.value.length < 6) {
        showError(password, "Password must be at least 6 characters");
        valid = false;
    }

    // Confirm password validation
    if (confirmPassword.value !== password.value) {
        showError(confirmPassword, "Passwords do not match");
        valid = false;
    }

    if (valid) {
        alert("Registration Successful!");
        form.reset();
    }
});

function showError(input, message) {
    const error = input.nextElementSibling;
    error.innerText = message;
}

function clearErrors() {
    const errors = document.querySelectorAll(".error");
    errors.forEach(error => error.innerText = "");
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}
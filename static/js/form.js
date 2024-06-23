document.addEventListener('DOMContentLoaded', function () {
    const showHidePw = document.querySelectorAll('.showHidePw');
    const pwFields = document.querySelectorAll('.password');

    showHidePw.forEach(eyeIcon => {
        eyeIcon.addEventListener("click", () => {
            pwFields.forEach(pwField => {
                if (pwField.type === "password") {
                    pwField.type = "text";
                    eyeIcon.style.color = "#4070f4"
                } else {
                    pwField.type = "password";
                    eyeIcon.style.color = "#999"
                }
            });
        });
    });
});

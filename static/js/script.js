document.addEventListener("DOMContentLoaded", () => {

    // Add a small fade-in effect when the page loads

    document.body.classList.add("page-loaded");


    // Automatically hide alerts after a few seconds

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach((alert) => {

        setTimeout(() => {

            alert.style.opacity = "0";

            alert.style.transform = "translateY(-10px)";

            alert.style.transition = "0.5s";

            setTimeout(() => {
                alert.remove();
            }, 500);

        }, 4000);

    });


    // Prevent accidental double submission

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", () => {

            const button = form.querySelector(
                ".submit-btn"
            );

            if (button) {

                button.innerText = "Sending...";

                button.disabled = true;

            }

        });

    }

});

// script.js

document.addEventListener("DOMContentLoaded", function () {
    // Code to run after the DOM is fully loaded

    // Example: Highlight the active page link in the navigation
    let currentPage = window.location.pathname.split("/").pop();
    let navLinks = document.querySelectorAll(".nav-link");

    navLinks.forEach(link => {
        if (link.getAttribute("href").endsWith(currentPage)) {
            link.classList.add("active");
        }
    });

    // Example: Confirm before logging out
    let logoutButton = document.getElementById("logoutButton");

    if (logoutButton) {
        logoutButton.addEventListener("click", function (event) {
            event.preventDefault();

            let confirmLogout = confirm("Are you sure you want to logout?");

            if (confirmLogout) {
                // Redirect to logout route or perform logout action
                window.location.href = this.getAttribute("href");
            }
        });
    }
});

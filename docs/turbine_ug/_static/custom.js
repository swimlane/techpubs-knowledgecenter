document.addEventListener("DOMContentLoaded", function() {
    const toggleSections = document.querySelectorAll(".toggle");
    toggleSections.forEach(section => {
        section.classList.add("toggle-open");
    });

    const toggleButtons = document.querySelectorAll(".toggle-button");
    toggleButtons.forEach(button => {
        button.setAttribute("aria-expanded", "true");
        const target = document.getElementById(button.getAttribute("aria-controls"));
        if (target) {
            target.style.display = "";
        }
    });
});

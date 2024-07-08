document.addEventListener("DOMContentLoaded", function() {
    var modalLow = document.getElementById("feedback-modal-low");
    var modalHigh = document.getElementById("feedback-modal-high");
    var closeButtons = document.querySelectorAll(".close");

    var starButtons = document.querySelectorAll(".feedback-star");

    starButtons.forEach(function(star) {
        star.addEventListener("click", function() {
            // Remove active class from all stars
            starButtons.forEach(function(s) {
                s.classList.remove("active");
            });
            // Add active class to the clicked star
            star.classList.add("active");

            var rating = parseInt(star.id.replace("star", ""));
            if (rating <= 3) {
                modalLow.style.display = "block";
                modalHigh.style.display = "none";
            } else {
                modalHigh.style.display = "block";
                modalLow.style.display = "none";
            }
        });
    });

    closeButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var targetModal = document.getElementById(button.getAttribute("data-target"));
            targetModal.style.display = "none";
        });
    });

    window.onclick = function(event) {
        if (event.target == modalLow) {
            modalLow.style.display = "none";
        }
        if (event.target == modalHigh) {
            modalHigh.style.display = "none";
        }
    };
});

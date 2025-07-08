// Find the button by its ID
const redirectButton = document.getElementById('redirectButton');

// Add an event listener that waits for a click
redirectButton.addEventListener('click', function() {
    console.log("Redirecting..."); // A message for you in the browser's console
    window.location.href = "https://www.google.com"; // The destination URL
});

const expandableimage = document.getElementById('portfolio-item');

expandableimage.addEventListener('click', function() {
    expandableimage.classList.toggle('expanded');
});
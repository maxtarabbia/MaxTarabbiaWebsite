
// Find the button by its ID
const artstationButton = document.getElementById('artstationButton');

// Add an event listener that waits for a click
artstationButton.addEventListener('click', function() {
    console.log("Redirecting..."); // A message for you in the browser's console
    window.location.href = "https://www.artstation.com/teamwinftw/albums/2404062"; // The destination URL
});

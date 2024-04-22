// Continuously run getData function and update progress bar every 3 seconds
setInterval(() => {
  getData((updatedValue) => {
    // Update progress bar with the latest value
    updateProgressBar(updatedValue);
  });
}, 3000); // Interval in milliseconds (3 seconds)

// Function to read the contents of the progress.txt file
function getData(callback) {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", "progress.txt");
  xhr.onload = () => {
    const progressValue = parseInt(xhr.response);
    if (typeof callback === "function") {
      callback(progressValue);
    }
  };
  xhr.send();
}

// Function to update the progress bar based on the value of the variable
function updateProgressBar(value) {
  const progressBar = document.getElementById("my-progress-bar");
  progressBar.style.width = value + "%";
  progressBar.textContent = value + "%";
}

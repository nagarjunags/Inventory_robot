// Function to toggle between dark and light themes
// Function to toggle between dark and light themes
function toggleTheme() {
  const body = document.body;
  const container = document.querySelector(".container"); // Select the .container div
  body.classList.toggle("dark-theme");
  container.classList.toggle("dark-theme");

  // Get the theme button
  const themeButton = document.getElementById("theme-btn");

  // Check the current text of the button and toggle it
  if (themeButton.innerHTML == "Dark Theme") {
    themeButton.innerHTML = "Light Theme";
  } else {
    themeButton.innerHTML = "Dark Theme";
  }
}

// Add event listener to the theme button
document.getElementById("theme-btn").addEventListener("click", toggleTheme);

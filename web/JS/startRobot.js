document.getElementById("run-script-btn").addEventListener("click", () => {
  // Make a GET request to localhost:3001 when the button is clicked
  fetch("http://localhost:3001/run-script", {
    method: "GET",
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      console.log("Response from server:", data);
      // Handle response data if needed
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});

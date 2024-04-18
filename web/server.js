const express = require("express");
const { exec } = require("child_process");

const app = express();
const port = 3001;

// Define the route handler for the root route ("/")
app.get("/", (req, res) => {
  // Execute the command each time the root route is accessed
  exec("pwd", (error, stdout, stderr) => {
    if (error) {
      console.error("Error executing Bash script:", error);
      res.status(500).send("Error executing Bash script");
      return;
    }
    console.log("Bash script executed successfully:", stdout);
    res.send("Bash script executed successfully");
  });
});

// Add route for running the script
app.get("/run-script", (req, res) => {
  exec("pwd", (error, stdout, stderr) => {
    if (error) {
      console.error("Error executing Bash script:", error);
      res.status(500).send("Error executing Bash script");
      return;
    }
    console.log("Bash script executed successfully:", stdout);
    res.send("Bash script executed successfully");
  });
});

// Start the server and listen on the specified port
const server = app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});

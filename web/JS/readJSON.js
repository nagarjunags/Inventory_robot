// Function to read the contents of the JSON file
function readJSONFile(filePath, callback) {
  fetch(filePath)
    .then((response) => response.json())
    .then((data) => {
      // Call the callback function with the data
      callback(data);
    })
    .catch((error) => {
      console.error("Error reading JSON file:", error);
    });
}

// Function to update the dashboard with warehouse data and display total changes
function updateDashboard(data) {
  // Update the warehouse table with the data
  const table = document.getElementById("warehouse-table");
  // Clear existing table content
  table.innerHTML = "";

  let totalItems = 0; // Variable to store the total number of items

  // Iterate through the data and populate the table
  data.forEach((row) => {
    const newRow = table.insertRow();
    newRow.dataset.rack = row.rackNumber; // Add data attribute for easier identification
    newRow.insertCell().textContent = row.rackNumber;
    newRow.insertCell().textContent = row.itemPresent ? "Yes" : "No";
    // Increment totalItems if item is present
    if (row.itemPresent) {
      totalItems++;
    }
  });

  // Update the total items display
  const totalItemsDisplay = document.getElementById("total-changes");
  const previousTotalItems =
    parseInt(totalItemsDisplay.dataset.previousItems) || 0; // Get previous total items
  const itemsAdded = totalItems - previousTotalItems; // Calculate items added
  totalItemsDisplay.textContent = `Total Items Added: ${itemsAdded}, Total Items Removed: 0`;
  totalItemsDisplay.dataset.previousItems = totalItems; // Update previous total items
}

// Function to identify changes between current and previous data
function identifyChanges(previousData, currentData) {
  let totalItemsAdded = 0; // Variable to store the total number of items added
  let totalItemsRemoved = 0; // Variable to store the total number of items removed

  // Compare current data with previous data to identify changes
  currentData.forEach((currentRow) => {
    const previousRow = previousData.find(
      (row) => row.rackNumber === currentRow.rackNumber
    );
    if (!previousRow) {
      // If corresponding row not found in previous data, it's a new row
      totalItemsAdded++;
    } else if (previousRow.itemPresent !== currentRow.itemPresent) {
      // If item presence has changed, count as an addition or removal
      if (currentRow.itemPresent) {
        totalItemsAdded++;
      } else {
        totalItemsRemoved++;
      }
    }
  });

  // Display the total items added and removed
  const totalChangesDisplay = document.getElementById("total-changes");
  totalChangesDisplay.textContent = `Total Items Added: ${totalItemsAdded}, Total Items Removed: ${totalItemsRemoved}`;
}

// Variable to store the previous data
let previousData = null;

// Function to fetch new data and update the dashboard
function fetchDataAndUpdate() {
  const jsonFilePath = "data/data.json"; // Replace 'data.json' with the path to your JSON file
  readJSONFile(jsonFilePath, function (data) {
    // Check if there is previous data
    if (previousData !== null) {
      // Identify changes between current and previous data
      identifyChanges(previousData, data);
    }
    // Update the dashboard with the new data
    updateDashboard(data);
    // Store current data as previous data for next comparison
    previousData = data;
  });
}

// Initial fetch and update
fetchDataAndUpdate();

// Add event listener to the button (optional)

// Add event listener to the light theme button

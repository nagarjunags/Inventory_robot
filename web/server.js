const express = require('express');
const { exec } = require('child_process');

const app = express();
const port = 3000;

app.get('/run-script', (req, res) => {
    // Replace 'your-bash-script.sh' with the path to your Bash script
    exec('sh your-bash-script.sh', (error, stdout, stderr) => {
        if (error) {
            console.error('Error executing Bash script:', error);
            res.status(500).send('Error executing Bash script');
            return;
        }
        console.log('Bash script executed successfully:', stdout);
        res.send(stdout);
    });
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});

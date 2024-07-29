const express = require('express');
const cors = require('cors');
const { spawn } = require('child_process');

const app = express();
app.use(cors({
  origin: 'http://localhost:3000'
}));
app.use(express.json());

app.use(express.static('public'));

app.post('/api/process-text', (req, res) => {
  const { text } = req.body;

  console.log(`Processing text: ${text}`);

  // Create a Python subprocess
  const pythonProcess = spawn('python', ['script.py', text]);
  pythonProcess.stdout.on('data', (data) => {
    // Handle the output from the Python script
    console.log(`Python script output:\n${data}`);
    res.header('Access-Control-Allow-Origin', 'http://localhost:3000'); // Add this header
    res.send(data.toString()); // Send the output back to the frontend
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python script error:\n${data}`);
    res.status(500).send('Error processing text');
  });
});

app.listen(4000, () => {
  console.log('Server listening on port 4000');
});

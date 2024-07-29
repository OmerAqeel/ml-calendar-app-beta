const express = require('express');
const cors = require('cors');
const { spawn } = require('child_process');

const app = express();
app.use(cors({
  origin: 'http://localhost:3000'
}));
app.use(express.json());

app.use(express.static('public'));

app.post('/api/process-text', async (req, res) => {
  const { text } = req.body;

  console.log(`Processing text: ${text}`);

  try {
    // Set header
    res.header('Access-Control-Allow-Origin', 'http://localhost:3000');

    // Create a Python subprocess
    const pythonProcess = spawn('python3', ['script.py', text]);

    const data = await new Promise((resolve, reject) => {
      pythonProcess.stdout.on('data', (data) => {
        resolve(data.toString());
        // printing the result from the python script
        console.log(`Python script result: ${data}`);
      });
      pythonProcess.stderr.on('data', (data) => {
        reject(new   
 Error(`Python script error: ${data}`));
      });
    });

    // Send data only after successfully receiving it
    res.send(data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error processing text');
  }
});

app.listen(4000, () => {
  console.log('Server listening on port 4000');
});

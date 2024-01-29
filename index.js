const express = require("express");
const { spawn } = require("child_process");

const app = express();
const port = 3000;

app.get("/", (req, res) => {
  // Handle your request parameters here
  const username = req.query.username;
  const password = req.query.password;
  const chatID = req.query.chatID;
  const message = req.query.message;

  // Call the Python script as a child process
  const pythonProcess = spawn("python3", [
    "your_script.py",
    username,
    password,
    chatID,
    message,
  ]);

  pythonProcess.stdout.on("data", (data) => {
    console.log(`Python script output: ${data}`);
    res.send(`Python script output: ${data}`);
  });

  pythonProcess.stderr.on("data", (data) => {
    console.error(`Error in Python script: ${data}`);
    res.status(500).send(`Error in Python script: ${data}`);
  });
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

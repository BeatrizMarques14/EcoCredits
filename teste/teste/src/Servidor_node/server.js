const express = require('express');
const { spawn } = require('child_process');
const fs = require('fs'); // file system
const app = express();
const port = 5000;
const publicPath = process.cwd()+"/public";

app.get('/run-script', (req, res) => {
  
  const python = spawn('python3', ['\matching.py']); // caminho  para o script matching.py

  let scriptOutput = "";

  python.stdout.on('data', (data) => {
    console.log('Pipe data from python script ...');
    scriptOutput += data.toString();
  });

  python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    res.send(scriptOutput);
  });
});
app.get(
  "*",
  (req, res, next) => sendPublicFiles(req, res, next),
  (req, res) => sendIndexHTML(req, res)
);

app.listen(port, () => console.log(`App listening on port ${port}`));

function sendPublicFiles(req, res, next) {
  const path = `${publicPath}${req.originalUrl}`;
  console.log(path);
  if (!fs.existsSync(path)) return next();
  res.status(200).sendFile(path);

}

function sendIndexHTML(req, res) {
  res.sendFile(`${publicPath}/index.html`);
}
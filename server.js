const express = require('express');
const { spawn } = require("child_process")
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

app.get('/', (req, res) => {
  var process = spawn('python3', ['./python/pcInformation.py']);
  process.stdout.on('data', function(data) {
    var data = data.toString().replace(/break/gi, "<br>")
    res.send(`<h1>${data}</h1>`)
})});

io.on('connection', (socket) => {
    socket.on('chat message', (msg) => {
      io.emit('chat message', msg);
    });
});

server.listen(3000, () => {
  console.log('listening on 3000');
});
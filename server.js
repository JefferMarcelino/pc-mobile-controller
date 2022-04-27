const express = require('express')
const { spawn } = require('child_process');
const app = express()
const port = 3001

app.get('/create-folder', (req, res) => {
    var process = spawn('python3', ['./python/create-folder.py']);
    console.log("Folder created")
})

app.get('/list-folders', (req, res) => {
    var process = spawn('python3', ['./python/list-folders.py']);
    process.stdout.on('data', function(data) {
        var data = data.toString()
        //res.send(`<p>${data.toString()}</p>`)
        res.send(data.replace(/-/g, "<br>"));
    } )
})

app.listen(port, () => console.log(`Example app listening on port 
${port}!`))
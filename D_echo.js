const http = require("http");
const fs = require('fs');
const hostname = "0.0.0.0";
const port = 3000;
const server = http.createServer((req, res) => {
  req.on("data", function(chunk) {

    fs.appendFile('measure.txt', chunk + '\n', (err) => {
    if (err) throw err;
    console.log("doing");
});
  });

  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  res.end("Hello World\n");
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://localhost:${port}/`);
});

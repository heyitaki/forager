const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(express.static(__dirname + "/public"));
app.use(bodyParser.urlencoded({extended: true}));

app.listen(3000, function() {
  console.log('Listening on port 3000');
})

app.post('/query', (req, res) => {
  console.log(req.body);
})

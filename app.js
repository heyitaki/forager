const express = require('express');
const bodyParser = require('body-parser');
const MongoClient = require('mongodb').MongoClient;
const pug = require('pug');
const app = express();

const compilePug = pug.compileFile('views/search-results.pug');

app.set('view engine', 'pug');
app.set('views', path.join(__dirname, "views"))

app.use('/static', express.static(path.join(__dirname, "public"));
app.use(bodyParser.urlencoded({extended: true}));

MongoClient.connect('mongodb://forage:forage@ds031741.mlab.com:31741/forage', (err, database) => {
  if (err) return console.log(err)
  db = database
  app.listen(3000, function() {
    console.log('Listening on port 3000');
  })
})

app.post('/query', (req, res) => {
  res.redirect( compilePug({name:'Michael'}));
})

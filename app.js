const express = require('express');
const url = require('url');
const querystring = require('querystring');
const bodyParser = require('body-parser');
const path = require('path');
const MongoClient = require('mongodb').MongoClient;
const pug = require('pug');
const app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "public")));
app.set('view engine', 'pug');

MongoClient.connect('mongodb://forage:forage@ds031741.mlab.com:31741/forage', (err, database) => {
  if (err) return console.log(err)
  db = database
  app.listen(3000, function() {
    console.log('Listening on port 3000');
  })
})

app.get('/', (req, res) => {
  var searchItem = req.query;
  if(Object.keys(searchItem).length === 0) {
    res.render('index');
  } else {
    res.render('searchResults', {search: searchItem.search});
  }
})

app.post('/query', (req, res) => {
  res.redirect(url.format({
    pathname: '/',
    query: {
      search: req.body.searchQuery
    }
  }))
})

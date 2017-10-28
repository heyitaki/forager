const express = require('express');
const url = require('url');
const querystring = require('querystring');
const bodyParser = require('body-parser');
const path = require('path');
const MongoClient = require('mongodb').MongoClient;
const pug = require('pug');
const PythonShell = require('python-shell');
const app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "public")));
app.set('view engine', 'pug');

MongoClient.connect('mongodb://root:root@cluster0-shard-00-00-inppe.mongodb.net:27017,cluster0-shard-00-01-inppe.mongodb.net:27017,cluster0-shard-00-02-inppe.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin', (err, database) => {
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
  } else if(searchItem.isSearch) {
    var options = {
      mode: 'json',
      args: [searchItem.search],
      scriptPath: './mongodb',
    }
    PythonShell.run('search.py', options, function (err, results) {
        if (err) throw err;
        console.log(results[0]);
        res.render('searchResults', {search: searchItem.search, results: results[0]});
    });
  }
})

app.post('/query', (req, res) => {
  res.redirect(url.format({
    pathname: '/',
    query: {
      search: req.body.searchQuery,
      isSearch: true
    }
  }))
})

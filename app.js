const express = require('express');
const url = require('url');
const querystring = require('querystring');
const bodyParser = require('body-parser');
const path = require('path');
const MongoClient = require('mongodb').MongoClient;
const pug = require('pug');
const PythonShell = require('python-shell');
const app = express();
const PORT = process.env.PORT || 5003;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "public")));
app.set('view engine', 'pug');

// MongoClient.connect('mongodb://root:root@cluster0-shard-00-00-inppe.mongodb.net:27017,cluster0-shard-00-01-inppe.mongodb.net:27017,cluster0-shard-00-02-inppe.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin', (err, database) => {
//   if (err) return console.log(err);
//   db = database;
  
// });

app.listen(PORT, function() {
  console.log(`Listening on port ${ PORT }`);
});

app.get('/', (req, res) => {
  res.render('index');
});

app.get('/query', (req, res) => {
  res.status(303).send('303: Use /search');
});

app.post('/query', (req, res) => {
  res.redirect(url.format({
    pathname: '/search/' + req.body.searchQuery,
  }));
});

app.get('/search/:id', (req, res) => {
  var options = {
    mode: 'json',
    args: [req.params.id],
    scriptPath: './elasticsearch',
  };

  PythonShell.run('search_by_query.py', options, function (err, results) {
      if (err) throw err;
      res.render('search', {query: req.params.id, results: results[0]});
  });
});

app.get('/question/:id', (req, res) => {
  var options = {
    mode: 'json',
    args: [req.params.id],
    scriptPath: './elasticsearch',
  };

  PythonShell.run('search_by_id.py', options, function (err, results) {
      if (err) throw err; 
      res.render('question', {question: results[0], require: require});
  });
});

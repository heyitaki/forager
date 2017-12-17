## FORAGER

### Development Instructions
#### Starting node.js
1. Navigate to the root dir and exec 'npm run dev' ['npm start' for node]

#### Starting Elasticsearch
1. Open search.py and set local=True [+ upload.py if uploading data]
2. Navigate to ./elasticsearch and run bin\elasticsearch.bat [cmd on Windows]

### Usage Instructions
Simply navigate to https://www.4ager.org.

### Next steps
- Integration with HKN site
- ~~Transition to Elasticsearch~~
- ~~Conduct more user ideas to accrue feedback on new features & formatting~~
- Further data acquisition through Amazon Turk or some other contracting platform [in progress, manual]
- ~~Custom domain (www.4ager.org) should point to the heroku URL above.~~
- Rewrite Python backend with Nodejs in order to remove dependency on Python buildpack & decrease app size
- Decouple ES & GCS uploads, write bulk upload for huge time optimization

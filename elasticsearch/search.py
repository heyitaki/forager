from elasticsearch import Elasticsearch
from google.cloud import storage
import os, re, json, certifi

def search(query):
  es = start_bonsai()
  res = es.search(index='exam', doc_type='question', body={'query': {'multi_match': {'query': query, 'fields': ['q_txt', 's_txt', 'teacher', 'term', 'school', 'course', 'exam_type', 'redundancy', 'extra']}}})
  # print "%d documents found" % res['hits']['total']
  return json.dumps(res['hits']['hits'])

def search_by_id(qid):
  es = start_bonsai()
  res = es.get(index='exam', doc_type='question', id=qid)
  q_img, s_img = res['_source']['q_img'], res['_source']['s_img']
  save_img_from_gcs(q_img, './public/img/question.PNG')
  save_img_from_gcs(s_img, './public/img/solution.PNG')
  return json.dumps(res)

def save_img_from_gcs(blob_name, dst_filename):
  storage_client = storage.Client.from_service_account_json('forager-download.json')
  bucket = storage_client.get_bucket('forager-qa-images')
  blob = bucket.get_blob(blob_name)
  blob.download_to_filename(dst_filename)
  # print 'Successfully downloaded %s to %s' % (blob_name, dst_filename)

##### HELPERS #####
def start_elastic():
  return Elasticsearch([{'host': 'localhost', 'port': 9200}])

def start_bonsai():
  bonsai = os.environ['BONSAI_URL']
  auth = re.search('https\:\/\/(.*)\@', bonsai).group(1).split(':')
  host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')
  es_header = [{
    'host': host, 
    'port': 443, 
    'use_ssl': True, 
    'verify_certs': True,
    'http_auth': (auth[0],auth[1]),
    'ca_certs': certifi.where()
  }]
  return Elasticsearch(es_header)
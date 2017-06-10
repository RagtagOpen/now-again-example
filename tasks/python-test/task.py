import os
import json
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

print 'hey there!'

input = {'message':'yo'}

if 'INPUT' in os.environ:
  input = json.loads(os.environ['INPUT'])

print 'EOF: ' + json.dumps({'message': input['message'] })

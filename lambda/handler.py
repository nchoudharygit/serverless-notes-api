import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NotesTable')

def lambda_handler(event, context):
    method = event['httpMethod']
    path   = event['path']

    if method == 'POST' and path == '/notes':
        return create_note(event)
    elif method == 'GET' and path == '/notes':
        return list_notes()
    elif method == 'GET' and '/notes/' in path:
        note_id = event['pathParameters']['id']
        return get_note(note_id)
    elif method == 'DELETE' and '/notes/' in path:
        note_id = event['pathParameters']['id']
        return delete_note(note_id)
    else:
        return response(404, {'error': 'Route not found'})

def create_note(event):
    body    = json.loads(event['body'])
    note_id = str(uuid.uuid4())
    item    = {
        'noteId':    note_id,
        'title':     body.get('title', ''),
        'content':   body.get('content', ''),
        'createdAt': datetime.utcnow().isoformat()
    }
    table.put_item(Item=item)
    return response(201, {'message': 'Note created', 'noteId': note_id})

def list_notes():
    result = table.scan()
    return response(200, {'notes': result['Items']})

def get_note(note_id):
    result = table.get_item(Key={'noteId': note_id})
    if 'Item' not in result:
        return response(404, {'error': 'Note not found'})
    return response(200, result['Item'])

def delete_note(note_id):
    table.delete_item(Key={'noteId': note_id})
    return response(200, {'message': 'Note deleted'})

def response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body)
    }
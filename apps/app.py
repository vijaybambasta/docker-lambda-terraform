import logging
import base64
#import boto3
import os
import json
import io
import cgi
from cgi import parse_header, parse_multipart
from io import BytesIO
from requests_toolbelt.multipart import decoder


def handler(event, context):
    response = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Headers":"Content-Type,X-Amz-Date,Authorization,X-Amz-Security-Token",
            "Access-Control-Allow-Credentials": True,
            "Content-Type": "application/json"
            },
        "body": ""
    }
    #fp = io.BytesIO(event['body'].encode('utf-8']

   

    
    content_type_header = event['headers']['Content-Type']

    #body = event["body"].encode()

    #response = ''
    #for part in decoder.MultipartDecoder(body, content_type_header).parts:
    #    response += part.text + "\n"
      


    #myBody = event['body']
    #img = base64.decode(myBody)



    #content_length = event
    #rfile = event['queryStringParameters']['file']
    #_, parameters = cgi.parse_header(event['headers']['content-type'])[1]


    #size = fp.getbuffer().nbytes
    #img = base64.decode(fp.read())



    #myEvent = event['body']
    #resultStart = myEvent.find("Content-Type: image/png")
    #resultEnd = myEvent.find("dl")
    #data = myEvent[resultStart:resultEnd]
    


    #s3 = boto3.client('s3')
    #s3.put_object(Bucket="photoholic.com" , key='mydata', Body=fp.read()
    

    #c_type, c_data = parse_header(event['headers']['Content-Type'])
    #assert c_type == 'multipart/form-data'
    


    #form_data = parse_multipart(BytesIO(event['body'].decode('base64')), c_data)
    #post_data = base64.b64decode(event['body'].encode['utf-8'])
    #headers, data = post_data.decode('utf-8').split('\r\n', 1)




    #event['body']['file']


   


    #uploaded_file = fp.read()
    #uploaded_file.seek(0, os.SEEK_END)
    #file_size = uploaded_file.tell()




    #pdict = cgi.parse_header(event['headers']['Content-Type'])[1]
    #if 'boundary' in pdict:
    #    pdict['boundary'] = pdict['boundary'].encode('utf-8')
    #pdict['CONTENT-LENGTH'] = len(event['body'])
    #form_data = cgi.parse_multipart(fp, pdict)

    #file_content = base64.b64decode(event['body'])

    body_response = {
            "content_length": "size"
            }

    response['body'] = json.dumps(body_response)


    return response

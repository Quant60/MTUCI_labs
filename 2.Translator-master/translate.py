import os, requests, uuid, json
subscription_key = 'b9300248783547b1ad5a3379b83b8e89'
location = 'global'

def get_translation(text_input, language_output):
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to=' + language_output
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text_input
    }]
    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()
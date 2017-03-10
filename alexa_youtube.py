from flask import Flask
from flask_ask import Ask, statement
import requests
import json

app = Flask(__name__)
ask = Ask(app, '/')

# Google API Key that has YouTube Search enabled
googApiKey = 'aaaabbbbcccc'

# IP address and port of the TV. /apps/YouTube should stay the same
chromecastUrl = 'http://12.34.56.78:56789/apps/YouTube' 

# Port to run the app on
flaskPort = 5001


@ask.intent('PlayYoutube')
def runQuery(Query):
	
	response = requests.get('https://www.googleapis.com/youtube/v3/search?key=' + googApiKey + \
    '&part=snippet&maxResults=1&type=video&alt=json&q=' + Query)
	
	results = json.loads(response.text)
	
	for r in results['items']:
		videoId = r['id']['videoId']
	
	data = {'Origin:':'', 'v': str(videoId)}
	requests.post(chromecastUrl, data=data)

	return statement('Playing video') \
	.simple_card(title='Youtube', content='Played video')
	
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=flaskPort)


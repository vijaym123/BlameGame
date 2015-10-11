import csv
import sys
import nltk
import json
import requests

def alchemy_calls_left(api_key):
    # Typical response from Alchemy:
    #{
    #    "status": "OK",
    #    "consumedDailyTransactions": "1020",
    #    "dailyTransactionLimit": "1000"
    #}
    # This URL tells us how many calls we have left in a day
    URL = "http://access.alchemyapi.com/calls/info/GetAPIKeyInfo?apikey={}&outputMode=json".format(api_key)
    # call AlchemyAPI, ask for JSON response
    response = requests.get(URL)
    calls_left = json.loads(response.content)
    # convert the text number fields to integers
    calls_left['consumedDailyTransactions'] = int(calls_left['consumedDailyTransactions'])
    calls_left['dailyTransactionLimit'] = int(calls_left['dailyTransactionLimit'])
    # add a convenience boolean
    return calls_left['consumedDailyTransactions'] < calls_left['dailyTransactionLimit']

BasePath = '/Users/vijaysm/Projects/BlameGame'

sys.path.append(BasePath+'/BootstrapTools/alchemyapi_python')
from alchemyapi import AlchemyAPI 

reader = csv.DictReader(open(BasePath+'/metadata_merged_final.csv','r'))

officialData=[]
for row in reader:
    if row['Email.Type']=='1':
        officialData.append(row['Filename'])

alchemyapi = AlchemyAPI()

for f in officialData[21:]:
    newsletter = open(BasePath+"/NewsLetters/"+f+".txt","r").read()
    count = 0
    csvfile = open(BasePath+"/TrainingData/Newsletters-Parsed/"+f+'.csv', 'wb')
    csvwriter = csv.writer(csvfile)
    call_left_none = False
    for sentence in nltk.tokenize.PunktSentenceTokenizer().sentences_from_text(newsletter):
        if not alchemy_calls_left(alchemyapi.apikey):
            call_left_none = True
            break
        statement = sentence.replace("\n","").replace("\t","").replace("&rsquo;",'\'')
        response = alchemyapi.sentiment('text', statement)
        if 'docSentiment' in response:
            csvwriter.writerow([ statement, str(response['docSentiment']['type']), str(response['docSentiment']['score'] if 'score' in response['docSentiment'] else None) ])
        else:
            csvwriter.writerow([ statement, str(None), str(None)])
        count += 1
    if call_left_none:
        print count, f
        break

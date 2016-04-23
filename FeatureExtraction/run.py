import os, glob
import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json 
path = 'K:\Old\E_DRIVE\ACADEMICS IV\BTP\April\FE\Pydownloaded'

##### Import user defiined  Functions ###
from clrAvg import ImgAnalyze
from FeatureVector import getFeatureVector

print("PROCESSING ...")
counter=0;          ## Number of Files processed
rowNumber=0;        ## A1 == (row==0 && column ==0)
dd = []
for infile in glob.glob( os.path.join(path, '*.*') ):
    #####  FEATURE EXTRACTION AND DATA RETRIEVAL    #####

    base=os.path.basename(infile);
     ## Get Feature Vector ##
    fv= getFeatureVector(base);

    #FV
#    for i in range(0,8) :
#       print str(fv[i])
    dd.append(fv)




data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["avgBrightness", "LA", "LB", "LC", "anti-blurr", "exposure&colourfullness", "saturation", "hue", "ROT1", "ROT2", "ROT3", "size", "aspectRatio", "WTH1", "WTH2", "WTH3", "WTS1", "WTS2", "WTS3", "WTV1", "WTV2", "WTV3", "hue (2)", "saturation (2)", "value"],
                    "Values": dd
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/31e47406fe864aed854c1689c721f759/services/6d1b98fad43a4ee7b263ad4796902af0/execute?api-version=2.0&details=true'
api_key = 'abc123' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers) 

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    i = len(result)-7
    ans = []
    while (result[i+1]!=':') :
        j = i-1
        while (result[j]!='"') :
            j= j-1
        s = result[j+1:i]
        ans.append(s)
        i = j-4
    i = len(ans)-1
    while i!=-1 :
        print (ans[i])
        i = i -1
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))                 
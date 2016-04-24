import os, glob
import urllib
import json
from operator import itemgetter
path = 'K:\Old\E_DRIVE\ACADEMICS IV\BTP\April\FE\dp'
from interactivegetFeatures import getFeatureVector


print("PROCESSING ...")
counter=0;          ## Number of Files processed
rowNumber=0;        ## A1 == (row==0 && column ==0)
names = []
dd = []
count = 0
for infile in glob.glob( os.path.join(path, '*.*') ):
    if(count==2) :
        break;
    count = count + 1
    #####  FEATURE EXTRACTION AND DATA RETRIEVAL    #####  
    base=os.path.basename(infile);
    names.append(base[:-4])
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
                    "ColumnNames": ["rAvg", "gAvg", "bAvg", "avgBrightness", "LA", "LB", "LC", "anti-blurr", "exposure&colourfullness", "saturation", "hue", "ROT1", "ROT2", "ROT3", "size", "aspectRatio", "WTH1", "WTH2", "WTH3", "WTS1", "WTS2", "WTS3", "WTV1", "WTV2", "WTV3", "DOFH", "DOFS", "DOFV", "Simplicity1", "Simplicity2", "colourfullness"],
                    "Values": dd
					},        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/46e95f4217c34016a4b7299df71d2414/services/a5a3f35fbbdc4ca8b93321b658ccaded/execute?api-version=2.0&details=true'
api_key = '3ZXuMpBRnEy/p2u0ADuQ+b7S/efO8773mUkXPH+NfFyNvo3jt/MiVRt5N++T4ZYUdj2Xwt/tZWnAnMJtTbsIrw==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers) 

try:
    response = urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)
    result = str(response.read())
    
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
    pairs = []
    for n in names :
        print (str(n)+" -> "+str(ans[i]))
        pairs.append((str(n),float(ans[i])))
        i = i -1
    pairs = sorted(pairs, key=itemgetter(1))
except urllib.request.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    #print(json.loads(error.read()))                 

import urllib2
# If you are using Python 3+, import urllib instead of urllib2


import json 
'''
path = 'K:\Old\E_DRIVE\ACADEMICS IV\BTP\April\FE\Pydownloaded'

##### Import user defiined  Functions ###
from clrAvg import ImgAnalyze
from fv1 import getFeatureVector

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
'''

data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["rAvg", "gAvg", "bAvg", "avgBrightness", "LA", "LB", "LC", "anti-blurr", "exposure&colourfullness", "saturation", "hue", "ROT1", "ROT2", "ROT3", "size", "aspectRatio", "WTH1", "WTH2", "WTH3", "WTS1", "WTS2", "WTS3", "WTV1", "WTV2", "WTV3", "DOFH", "DOFS", "DOFV", "Simplicity1", "Simplicity2", "colourfullness"],
                    "Values": [ [ "121.2073136","121.2073136","121.2073136","121.2073136","121.2073136","121.2073136","121.2073136","859.0793606","121.2073136","121.2073136","121.2073136","131.9672549","131.9672549","131.9672549","1127","0.674591382","-8401.5","-2863.75","27131.625","-8401.5","-2863.75","27131.625","-8401.5","-2863.75","27131.625","0.112811375","0.112811375","0.112811375","0.398565165","0.384615385","18.87151986"],["148.0638482","120.0089527","109.6503695","125.9077235","125.2255338","127.216488","127.5071627","280.8046256","109.6503695","120.0089527","148.0638482","154.825707","114.7194969","97.23574677","764","0.682819383","4185","17448.5","12839.25","5458","23794","16994","6979.5","22703.75","17800.875","0.389041686","0.330585576","0.259529188","8.547008547","0.136986301","39.74896919"],["127.0881035","146.7887918","164.60613","146.1610084","143.8868373","142.9294626","144.4261213","1099.554342","164.60613","146.7887918","127.0881035","97.76823075","110.9850498","116.0287223","952","0.740402194","-40325","-4433.5","-81877.75","-38116","-6816","-66721.5","-29855.5","-4017.75","-41555.375","-0.058175904","-0.023442651","0.00444148","2.985074627","0.5","34.10074276"],["67.8774832","59.51468957","54.78926799","60.72714692","60.95144406","61.47646681","61.58897589","250.7113621","70.70736812","75.39774095","47.15372835","69.9693801","38.45997809","140.4438517","1099","0.75","-17245.5","-11069.75","-11596.875","7108","6358","4009","-1606.5","-3712.25","-3377.875","0.3495826","0.305079298","3.077258922","4.854368932","0.032051282","6.281786445"]]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/46e95f4217c34016a4b7299df71d2414/services/a5a3f35fbbdc4ca8b93321b658ccaded/execute?api-version=2.0&details=true'
api_key = '3ZXuMpBRnEy/p2u0ADuQ+b7S/efO8773mUkXPH+NfFyNvo3jt/MiVRt5N++T4ZYUdj2Xwt/tZWnAnMJtTbsIrw==' # Replace this with the API key for the web service
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

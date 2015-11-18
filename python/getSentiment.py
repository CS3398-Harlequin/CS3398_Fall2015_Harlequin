#any string you input returns 0.00 value for sentiment
#whereas testing on their website gives positive/negative values


import http.client, urllib.parse, json, string, sys

def getSentiment(text, ID):
    usr = 'venusinfurs'
    pwd = '1a2MMbrRuN98Id1HtGf3'   
    service='/WS_Nops_Val/Service.aspx'
    params = urllib.parse.urlencode({'User': '%s' % usr, 'Pass': '%s' %pwd, 'ID': '%s' %ID, 'Text': '%s' % text, 'Detail': 'Global', 'OutFormat':'JSON', 'Normalized': 'No', 'Theme': 'Gen'})
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    server="svc8.bitext.com"    
    
    #conn = httplib.HTTPConnection("%s" % server)
    conn = http.client.HTTPConnection("%s" % server)
    conn.request("POST", "%s" % service, params, headers)
    response = conn.getresponse()
    data = response.read()
    conn.close() 
    return data
    
    
analysis_string = getSentiment('Happy happy love peace', 123)

print((analysis_string).decode(sys.stdout.encoding))
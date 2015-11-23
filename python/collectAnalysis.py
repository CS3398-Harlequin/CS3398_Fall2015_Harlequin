from getSheetValue import getSheetValue
#using B for bitext. (A for Semantria)
from getSentimentA import getSentiment
from time import sleep

def collectAnalysis(workbook, start, end, output_list):
    f = open('sentiment_output.txt', 'a')
    for cellrow in range(start, end):
        sleep(1)
        if (cellrow % ((end-start)/5) == 0): print ("=====Progress: " + str(int(((cellrow-start)/(end-start))*100)) + "%=====")
        #try:
        senText = getSheetValue(workbook, 'results', 4, cellrow)
        if "NAGW" in senText: continue        #skip that spam
        senText = senText.replace('\r\n', '')
        
        senValue = getSentiment(senText, cellrow+100)
        if senValue == 0.0: continue        #ignore neutral sentiment
        if(senValue == None): continue

        senText = senText.replace("\n", "")
        senText = senText.replace("\r\n", "")
        senText = senText.encode("utf-8")
        senText = str(senText)
        
        output_list.append([senText[2:],senValue])
        
        f.write(senText[2:] + '\t' + str(senValue) + '\n')
        print(senText[2:80] + '\t' + str(senValue))
        
        #except Exception as e: 
        #    print(e)
        #    print("Error for cell row " + str(cellrow)) 
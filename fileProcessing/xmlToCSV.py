#Python code to illustrate parsing of XML files 
# importing the required modules 
import csv 
import requests 
import xml.etree.ElementTree as ET 

def parseXML(xmlfile): 
  
    # create element tree object 
    tree = ET.parse(xmlfile) 
  
    # get root element 
    root = tree.getroot() 
  
    # create empty list for news items 
    newsitems = [] 
  
    # iterate news items 
    for item in root.findall('./channel/item'): 
  
        # empty news dictionary 
        news = {} 
  
        # iterate child elements of item 
        titleFlag = 0
        linkFlag = 0
        temp = []
        for child in item: 
            # if child.tag == '{http://search.yahoo.com/mrss/}content':
            # temp = []
            if (child.tag == 'title'):
                titleFlag = 1
                temp.append(child.text)
                # print(child.text)
            #    temp.append(child.text)
            if (child.tag == 'link'):
                linkFlag = 1
                temp.append(child.text)
                # print(child.text)
            if (titleFlag == 1 and linkFlag == 1):
                news['term'] = temp[0]
                news['link'] = temp[1]

        # append news dictionary to news items list 
        newsitems.append(news) 
    return newsitems 
  
  
def savetoCSV(newsitems, filename): 
  
    # specifying the fields for csv file 
    fields = ['term', 'link'] 
  
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
  
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
  
        # writing headers (field names) 
        writer.writeheader() 
  
        # writing data rows 
        writer.writerows(newsitems) 
  
      
def main(): 
  
    # parse xml file 
    newsitems = parseXML('loyslunarlexicon.wordpress.2018-11-29.xml') 
  
    # store news items in a csv file 
    savetoCSV(newsitems, 'posts.csv') 
      
      
if __name__ == "__main__": 
  
    # calling main function 
    main() 

import csv 
  
 
def savetoCSV(data, filename): 
  
    # specifying the fields for csv file 
    fields = ['Term', 'Poem', 'Part of Speech', 'Definition', 'Tags'] 
  
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
  
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
  
        # writing headers (field names) 
        writer.writeheader() 
  
        # writing data rows 
        writer.writerows(data) 
  
      
def main(): 
    # load rss from web to update existing xml file 
    # loadRSS() 
  
    # parse xml file 
    newsitems = parseXML('loyslunarlexicon.wordpress.2018-11-29.xml') 
  
    # store news items in a csv file 
    savetoCSV(newsitems, 'posts.csv') 
      
      
if __name__ == "__main__": 
  
    # calling main function 
    main() 
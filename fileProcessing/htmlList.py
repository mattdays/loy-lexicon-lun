
import csv, sys

data = []

def formatData(term, link):
    data.append([term, link])

def csvParse(name):
    with open(name) as file:
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        try:
            for row in reader:
                formatData(row['term'], row['link'])
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(name, reader.line_num, e))

# def csvParse(name):
#     with open(name) as file:
#         reader = csv.DictReader(file, delimiter=",", quotechar='"')
#         try:
#             for row in reader:
#                 print(row)
                
#         except csv.Error as e:
#             sys.exit('file {}, line {}: {}'.format(name, reader.line_num, e))

  
def savetoCSV(filename): 

    # specifying the fields for csv file 


    # writing to csv file 
    with open(filename, 'w') as file:
        file.write('<ul id="myUL">\n') 
        for row in data:
            output =  (('<li><a href="{}">{}</a></li>\n').format(row[1], row[0]))
            file.write(output)
        file.write('</ul>') 

        # creating a csv dict writer object 
        # writer = csv.DictWriter(csvfile, fieldnames = fields) 

        # writing headers (field names) 
        # writer.writeheader() 

        # writing data rows 
        # writer.writerows(newsitems)
        #  

def sortData():
    from operator import itemgetter
    data.sort(key=itemgetter(0))
    # x.sort(key=itemgetter(1))

      
def main(): 
    # load rss from web to update existing xml file 
    # loadRSS() 
  
    # parse xml file 
    csvParse('posts.csv') 
    print(data)
  
    # store news items in a csv file 
    savetoCSV('list2.txt') 
      
      
if __name__ == "__main__": 
  
    # calling main function 
    main() 
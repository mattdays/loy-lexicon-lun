
import csv, sys

data = []
data2 = []

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

def formatData2(term, poem, occur, speech, definition, tags):
    # data = []
    data2.append([term, poem, occur, speech, definition, tags])

def tsvParse(name):
    with open(name) as f:
        reader2 = csv.DictReader(f, delimiter="\t", quotechar='"')
        try:
            for row in reader2:
                formatData2(row["Term"], row["Poem"], row["Number of Occurrences"], row["Part of Speech"], row["Definition"], row["Tags"])
        except csv.Error as e:
            sys.exit('f {}, line {}: {}'.format(name, reader2.line_num, e))
  
def savetoCSV(filename): 

    # specifying the fields for csv file 


    # writing to csv file 
    with open(filename, 'w') as file:
        file.write('<ul id="myUL">\n') 
        for row in data2:
            for entry in data:
                if (row[0] == entry[0]):
                    output =  (('<li><a href="{}">{}</a></li>\n').format(entry[1], row[0]))
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
    tsvParse('definitions.tsv') 
    # print(data2)
  
    # store news items in a csv file 
    savetoCSV('list3.txt') 
      
      
if __name__ == "__main__": 
  
    # calling main function 
    main() 
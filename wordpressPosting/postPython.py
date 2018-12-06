import csv, sys, time

data = []
wordFreq = {}
totalWords = set()
# spreadsheetWords = set()
# nonSpreadsheetWords = set()

def testPost(term, poem, numOccur, partSpeech, definition, tags):
# def testPost(term, poem, numOccur, context, partSpeech, officialDef, tags, etymology, webster1907Def, oedDef, loyUsage, categories):    
    from wordpress_xmlrpc import Client
    from wordpress_xmlrpc.methods import posts
    # , taxonomies

    client = Client('http://EXAMPLESITE.com/xmlrpc.php', 'EXAMPLE', ('EXAMPE_PASSWORD')) #, blog_id=0,transport=None)
    # postList = client.call(posts.GetPosts())
    # print(postList) # == [WordPressPost, WordPressPost, ...]

    from wordpress_xmlrpc import WordPressPost, WordPressTerm


    # tagList = client.call(taxonomies.GetTerms('post_tag'))

    # print("Taglist:", tagList)
    # print()
    # print("TSV Tags:", tags)

    for item in tags:
        # if (item not in tagList):
        tag = WordPressTerm()
        tag.taxonomy = 'post_tag'
        tag.name = ('%a', item)
            # tag.id = client.call(taxonomies.NewTerm(tag))
        # else:
        #     pass

    if(term.lower() in wordFreq):
        numOccur = wordFreq[term.lower()][0]
        # print (numOccur)
    # print(term, poem, numOccur, partSpeech, definition,tags)
    if (not partSpeech):
        pass
    else:
        partSpeech = '(' + partSpeech + ')'

    post = WordPressPost()
    post.title = ('{}'.format(term))
    post.content = (
                    ('<strong><span style="color: #993300;">Appears in: </span> </strong>{}<br>'.format(poem)) + 
                    '<br>' +
                    (' <span style="color: #993300;"><strong>Frequency: </strong></span>{}<br>'.format(numOccur)) +
                    '<br>' +
                    (' <strong><span style="color: #993300;">Definition: </span> </strong> <br>{} {}<br>'.format(partSpeech, definition))
                    # .format(poem, numOccur, partSpeech, definition)
                    ) 

    # post.content = (('<h3>Poem:</h3> %a <h3>Number of Occurrences:</h3> %a',
    #     # ' [expand title="Etymology" rel="entry-highlander" tag="h3" trigclass="noarrow"]%a[/expand]',
    #     ' [expand title="Definition" rel="entry-highlander" tag="h3" trigclass="noarrow"]%a[/expand]')
    #     # ' [expand title="Webster(1907)" rel="entry-highlander" tag="h3" trigclass="noarrow"]%a[/expand]',
    #     # ' [expand title="Oxford English Dictionary" rel="entry-highlander" tag="h3" trigclass="noarrow"]%a[/expand]',
    #     # ' [expand title="Loy Usage" rel="entry-highlander" tag="h3" trigclass="noarrow"]%a[/expand]',
    #      %(poem, numOccur, definition))
    # # [expand title="Merriam-Webster Dictionary (1907)" rel="entry-highlander" tag="h3" trigclass="noarrow"]%a[/expand] [expand title="Proposed Definition" rel="entry-highlander" tag="h3" trigclass="noarrow"]%a[/expand] &nbsp;' %(a,b,c,d)
    #                 # )

    post.terms_names = {
                    'post_tag': tags,#['Lexicon'],
                    'category': ['Lexicon']
                }

    post.id = client.call(posts.NewPost(post))

    post.post_status = 'publish'
    client.call(posts.EditPost(post.id, post))

def formatData(term, poem, occur, speech, definition, tags):
    # data = []
    data.append([term, poem, occur, speech, definition, tags])
    totalWords.add(term.lower())

def formatWordFreq(term, occur, relFreq):
    # data = []
    wordFreq[term] = [occur, relFreq]
    # print (term, wordFreq[term])

def formatWordSet(term):
    capitalized = term.capitalize()
    if(term not in totalWords):
        totalWords.add(term)
        data.append([capitalized, '', '', '', '', []])
        # print(capitalized)
        


def testPrinter(table):
    # testTag = ['TestTag']
    # print (len(table))

    for row in table:
        # print(row[5])
        # time.sleep(1)
        testPost(row[0],row[1],row[2],row[3],row[4],row[5])
    # testPost(table[0][0], table[0][1], table[0][2], table[0][3], table[0][4], table[0][5])
    
    # print(table[2000][0], table[2000][1], table[2000][2], table[2000][3], table[2000][4], table[2000][5])
    # print(table[60][0], table[60][1], table[60][2], table[60][3], table[60][4], table[60][5])
    # testPost(table[60][0], table[60][1], table[60][2], table[60][3], table[60][4], table[60][5])

    # print(table[5])

def tsvParse(name):
    with open(name) as file:
        reader = csv.DictReader(file, delimiter="\t", quotechar='"')
        try:
            for row in reader:
                # testPost(row["Term"], row["Poem"], row["Number of Occurrences"], row["Context"], row["Part of Speech"], row["Official Definition"], row["Tags"])
                # print("test")
                tags = row["Tags"]
                if (not tags):
                    tags = []
                else:
                    tags = tags.replace(" ", "")
                    tags = tags.split(';')
                
                # tags = tags.append('lunar baedecker')
                # testPost(row["Term"], row["Poem"], row["Number of Occurrences"], row["Part of Speech"], row["Definition"], tags)
                
                # print(tags)
                # print(row["Term"], row["Poem"], row["Number of Occurrences"], row["Context"], row["Part of Speech"], row["Official Definition"], row["Tags"])
                formatData(row["Term"], row["Poem"], row["Number of Occurrences"], row["Part of Speech"], row["Definition"], tags)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(name, reader.line_num, e))

def parseWordFrequency(filename):
    with open(filename) as file:
        reader = csv.DictReader(file, delimiter="\t", quotechar='"')
        try:
            for row in reader:
                # print(row["Term"], row["RawFrequency"], row["RelativeFrequency"])

                formatWordFreq(row["Term"], row["RawFrequency"], row["RelativeFrequency"])
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

def parseNonSpreadsheet(filename):
    with open(filename) as file:
        reader = csv.DictReader(file, delimiter="\t", quotechar='"')
        try:
            for row in reader:
                # print(row["Term"])
                formatWordSet(row["Term"])
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))


def main():
    tsvParse("definitions.tsv")
    # testPost()
    parseWordFrequency("wordFrequency.tsv")

    parseNonSpreadsheet("totalWordFreq.tsv")

    # print(data[250])
    # print(len(data))
    testPrinter(data)


if __name__ == "__main__":
    main()
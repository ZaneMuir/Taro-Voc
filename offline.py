#!/usr/bin/env python3
import re
from DictionaryServices import DCSCopyTextDefinition



def system_dictionary(word):
    entry = {'name':'',
        'pronunciation':'',
        'definitions':[],
        'definitions-with-attr':{}}
    wordrange = (0, len(word))
    dictresult = DCSCopyTextDefinition(None, word, wordrange)

    if not dictresult:
        return entry
    else:
        tuned_result = re.sub(r'(ORIGIN|PHRASES .*?)$','',dictresult)
        entry['name'] = re.findall(r'^(.*?) \|', tuned_result)[0]
        entry['pronunciation'] = re.findall(r'(\|.*?\|)', tuned_result)[0]

        #print(tuned_result)

        attr = re.findall(r'▶(.*?) ', tuned_result)
        attr_def = re.findall(r'▶(.*?) ▶', tuned_result)
        attr_def.extend(re.findall(r'▶('+attr[-1]+'.*?)$', tuned_result))

        #entry['definitions'] = re.findall(r'\d (.*?\.)', tuned_result)
        #print(attr_def)
        for item in range(len(attr_def)):
            temp = []
            temp.extend(re.findall(r'\d (.*?)\.',attr_def[item]))
            temp.extend(re.findall(r'^'+attr[item]+r' (.*?)\.',attr_def[item]))
            
            entry['definitions-with-attr'][attr[item]] = temp
            entry['definitions'].extend(temp)

        return entry

if __name__ == '__main__':
    print(system_dictionary('drink'))

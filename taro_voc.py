import requests
import os, json, re, time
import multiprocessing as mp
from bcolors import bcolors

config_file_addr = os.path.join(os.getenv('HOME'), '.voc/config.json')

def default_modification(x):
    new = []
    for i in x:
        new.append(re.sub(r'(<.*?>|</.*?>)', '', i))
    return new


class TaroVoc(object):
    """docstring for TaroVoc."""
    def __init__(self, config_file_addr):
        super(TaroVoc, self).__init__()
        with open(config_file_addr, 'r') as config_file:
            self.config = json.loads(config_file.read())
        self.set_dictionary(self.config['default-dictionary'])
        return

    def set_dictionary(self, dict_name):
        #with open(os.path.join(os.getenv('HOME'), '.voc/template/%s.json'%dict_name), 'r') as dict_config_file:
        with open('template/%s.json'%dict_name, 'r') as dict_config_file:
            self.dictionary = json.loads(dict_config_file.read())
        return

    def check_single_word(self, word, showResult=True, color=True, modification=default_modification):
        # grab dictionary data
        data_url = self.dictionary['target-url']%word
        data_object = requests.get(data_url)
        data = data_object.text

        # analyze data
        entry = {'name':'',
            'pronunciation':'',
            'definitions':[]}
        entry['name'] = re.findall(self.dictionary['name'],data)[0]
        entry['pronunciation'] = re.findall(self.dictionary['pronunciation'],data)[0]
        for item in self.dictionary['definitions']:
            entry['definitions'].extend(re.findall(item,data))

        entry['definitions'] = modification(entry['definitions'])
        #print(entry)

        # return and print results
        if showResult:
            print(bcolors.BOLD + bcolors.BRIGHT_GREEN + entry['name'] + bcolors.ENDC)
            print(bcolors.BRIGHT_CYAN + entry['pronunciation'] + bcolors.ENDC)
            for i in range(len(entry['definitions'])):
                print(bcolors.BRIGHT_RED + str(i+1) + bcolors.ENDC + '. %s'%entry['definitions'][i])

        return entry

    def saveEntry(self, entry):
        #check file
        output_addr = os.path.join(self.config['output-dir'],'%s.txt'%time.strftime(self.config['filename-format']))
        if not os.path.isfile(output_addr):
            with open(output_addr, 'w') as output_file:
                output_file.write('')
        #add entry
        with open(output_addr, 'a') as output_file:
            output_file.write(entry['name']+'\t')
            output_file.write('/'.join(entry['definitions'])+'\t')
            output_file.write(entry['pronunciation'])
            output_file.write('\n')

    def check_file(self, file_addr):
        # read file and set a Queue
        process_n=self.config['process_n']
        self.word_tocheck = mp.Queue()
        self.mp_lock = mp.Lock()
        with open(file_addr, 'r') as word_file:
            for i in re.split(r'\n',word_file.read()):
                self.word_tocheck.put(i)

        # single mission
        def mission():
            while not self.word_tocheck.empty():
                # get a word from Queue
                self.mp_lock.acquire()
                word = self.word_tocheck.get()
                self.mp_lock.release()

                #check and store
                if word == '':
                    continue
                entry = self.check_single_word(word, showResult=False)
                self.saveEntry(entry)
                print(entry['name'])

        worker = []
        for i in range(process_n):
            p = mp.Process(target = mission)
            worker.append(p)
            p.start()

        for i in range(process_n):
            worker[i].join()

        print('finished')

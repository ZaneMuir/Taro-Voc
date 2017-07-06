#!usr/bin/env python3

__version__ = "Taro-Voc v0.1.2"
__doc__ = """Taro-Voc v0.1
Usage:
    voc WORD
    voc -f FILE
    voc -l LANG WORD
    voc install TEMPLATE

Options:
    -f FILE, check every words in a txt file, with one word in each line.
    -l LANG, using another language template
    --new , single new file

"""

from docopt import docopt
from taro_voc import TaroVoc

#default_config_file_addr = os.path.join(os.getenv('HOME'), '.voc/config.json')
default_config_file_addr = 'config.json'


if __name__ == '__main__':
    arguments = docopt(__doc__, version=__version__)
    voc_handler = TaroVoc(default_config_file_addr)
    print(arguments)
    if arguments['-l']:
        voc_handler.set_dictionary(arguments['-l'])

    if arguments['install']:
        pass #TODO install templates
    elif arguments['-f']:
        voc_handler.check_file(arguments['-f'])
    else:
        entry = voc_handler.check_single_word(arguments['WORD'])
        voc_handler.saveEntry(entry)

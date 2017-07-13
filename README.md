# voc_python
a python script to look up a new word from web dictionaries like [Merriam-Webster's](http://merriam-webster.com/).

and store the data with the formate designed for import of [ProVoc](http://www.arizona-software.ch/provoc/)

![provoc_icon](http://www.arizona-software.ch/provoc/images/provoc-icon.jpg)

---
Usage:
```
Taro-Voc v0.3
Usage:
    voc WORD
    voc -f FILE [--new]
    voc install TEMPLATE

Options:
    -f FILE, check every words in a txt file, with one word in each line.
    -l LANG, using another language template
    --new , with a new output file (with -f mode)

```

---

#### Change Log

##### v0.3
- support for **MacOS Dictionary.app** (```-l mac``` and as default when offline)
- display definitions with groups of its part-of-speech (ie. noun, pronoun, adjective, determiner, verb, adverb, preposition, conjunction, and interjection.) #TODO


##### v0.2.1
- support for Chinese-English dictionaries: **youdao dictionary** (```-l youdao```) and **bing dictionary** (```-l bing```)
- auto-installation of templates file
- using ```--new``` to output into a new single file

##### v0.2
- color print with [TaroColor](https://github.com/ZaneMuir/Taro-Color)
- multiprocessing with file mode
- using multiple dictionary templates (with manual installation)
- support for **Merriam-Webster's Medical Dictionary** (```-l mmed```)

##### v0.1
- first commit
- support for **Merriam-Webster's Dictionary** (as default)

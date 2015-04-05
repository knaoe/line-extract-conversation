# -*- coding: utf-8 -*-

__author__ = 'Kenichi'

import re


class LineUtil():
    talks_raw = []
    talks = []

    pDate = re.compile("\d{4}/\d{1,2}/\d{1,2}")

    def __init__(self, file_path):
        f = open(file_path, mode='r')
        self.talks_raw = f.readlines()
        f.close()
        print("open %s." % file_path)

    def extract_conversations(self):
        print("parsing...%d" % len(self.talks_raw))
        self.talks_raw = self.talks_raw[2:]  # ignore first 2 lines.
        for t in self.talks_raw:
            if t == '' or t == '\r\n':
                continue
            date = self.pDate.match(t)
            if date and date.start() == 0:
                continue
            if '\t' in t:
                _t = t.split('\t')
                sentence = "%s\t%s" % (_t[1], _t[2])
                self.talks.append(sentence)
            else:
                self.talks[-1] += t

    def save(self, filename='line_talks_only_conversation.txt'):
        f = open(filename, mode='w')
        f.writelines(self.talks)
        f.close()
        print("output %s." % filename)




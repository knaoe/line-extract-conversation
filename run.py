# -*- coding: utf-8 -*-

__author__ = 'Kenichi'

from line_util import LineUtil

if __name__ == "__main__":
    line_util = LineUtil('line_talks.txt')
    line_util.extract_conversations()
    line_util.save()

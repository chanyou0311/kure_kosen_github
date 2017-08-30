#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
import datetime

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

username = 'tebasakioisii'
print(u'こんにちは%s様。現在時刻は%sです。' % (username, datetime.datetime.now()))


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from txt2ipa.ipaconvert import ipa, broad
from txt2ipa.transliteration import tam2lat

with open("data/local/dict/lexicon.txt","w") as f1:
	with open("InputToIPA.txt") as f:
		for word in f.readlines():
			print >> f1,(word.strip() + " " + ipa(tam2lat(word.strip())))

# text = 'வணக்கம் தமிழகம்'


# t1 = tam2lat(text)
# t2 = " " + t1 + " "
# t2 = ipa(t2)
# t3 = broad(t2)
# print "after tam2lat", t1
# print "after ipa", t2
# print "after broad", t3


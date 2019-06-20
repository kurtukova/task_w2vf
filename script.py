#!/usr/bin/python3
# coding: utf8

import argparse
import spacy
import io
import sys
import os
from collections import defaultdict

# parse arguments --in and --out
parser = argparse.ArgumentParser()
parser.add_argument('-in', '--in', dest="inputfile", default='corpus.txt', help="Input file with corpus")
parser.add_argument('-out', '--out', dest="outputfile", default='dep.contexts', help="Output file with vectors")
namespace = parser.parse_args(sys.argv[1:])
inputfile=namespace.inputfile
outputfile=namespace.outputfile

if os.path.exists(outputfile):
    print ('Output file ' + outputfile + ' already exist.')
    sys.exit()
    
nlp = spacy.load("en_core_web_sm") # load language
nlp.max_length=10000000
bad_deps = ['ROOT','punct']



with open(inputfile, 'r') as infile:
    with open(outputfile, 'a') as outfile:
        for line in infile:
            doc = nlp(line)
            for sent in doc.sents:
                for word in sent:
                    head_context=""
                    child_context=""
                    full_context=""
                    w_source = word.head.text.lower()
                    w_target= word.text.lower()
                    w_dep = word.dep_
                    w_child_num = len(list(word.children))
                    if w_dep not in bad_deps:
                        head_context = w_source+"/"+w_dep+"-1"
                    if w_child_num > 0:
                        for child in word.children:
                            source = child.head.text.lower()
                            target= child.text.lower()
                            dep = child.dep_
                            #If we see a prep then merge it
                            if dep == 'prep':
                                for c2 in child.children:
                                    if (c2.dep_ == 'pobj'):
                                        if child_context=="":
                                            child_context = c2.text.lower()+"/"+"prep_"+child.text.lower()
                                        else:
                                            child_context = child_context+"_"+c2.text.lower()+"/"+"prep_"+child.text.lower()
                            else:
                                if not dep in bad_deps:
                                    if child_context=="":
                                        child_context = target+"/"+dep
                                    else:
                                            child_context = child_context+"_"+target+"/"+dep
                    if child_context=="" and head_context!="":
                        full_context = w_target+" "+head_context+"\n"
                    elif child_context!="" and head_context=="":
                        full_context = w_target+" "+child_context+"\n"
                    elif child_context!="" and head_context!="":
                        full_context = w_target+" "+child_context+"_"+head_context+"\n"
                    else:
                        continue
                    if word.is_alpha:
                         outfile.write(full_context)
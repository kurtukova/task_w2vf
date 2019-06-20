#!/bin/sh

echo -n "script"
python3 script.py --in corpus.txt --out dep.contexts

echo -n "count and filter"
./yoavgo-word2vecf-0d8e19d2f2c6/count_and_filter -train dep.contexts -cvocab cv -wvocab wv -min-count 1

echo -n "word2vecf"
./yoavgo-word2vecf-0d8e19d2f2c6/word2vecf -train dep.contexts -wvocab wv -cvocab cv -output dim200vecs -size 200 -negative 15 -threads 10 -dumpcv dim200context-vecs

echo -n "vecs2nps"
python ./yoavgo-word2vecf-0d8e19d2f2c6/scripts/vecs2nps.py dim200vecs vecs
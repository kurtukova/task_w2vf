FROM ubuntu

USER root

# install soft for make word2vec
RUN apt-get update && apt-get install -y \
    gcc \
    wget \
    unzip \
    make \
	nano \
	mc

# copy all to container
COPY . /root/

#compile wod2vec
RUN cd /root ; \
    wget https://bitbucket.org/yoavgo/word2vecf/get/0d8e19d2f2c6.zip ; \
    unzip 0d8e19d2f2c6.zip ; \
    cd yoavgo-word2vecf-0d8e19d2f2c6; \
    make ; \
    cp word2vec /usr/bin/ ; \
    cp word2vecf /usr/bin/
	
# install python3 and tools
RUN apt-get install -y python3 python3-pip
	
# install python2 and tools	
RUN apt-get install -y python python-pip
    
# install spacy and argparse
RUN pip3 install -U spacy ; \
    pip3 install -U argparse ; \
    python3 -m spacy download en
	
# install numpy
RUN pip install numpy

RUN /bin/bash -c 'chmod +x /root/script.py'
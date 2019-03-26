FROM pklehre/niso2019-lab3

ADD genetic.py /bin

RUN apt-get update
RUN apt-get -y install python-numpy
RUN apt-get -y install python-sexpdata
RUN apt-get -y install python-sklearn
RUN apt-get -y install python-pyparsing
RUN apt-get -y install python-argparse



CMD ["-username", "txs799", "-submission", "python /bin/genetic.py"]
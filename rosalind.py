#!/usr/bin/env python

def ReadFASTA(filename):
    '''Extract Sequence name and FASTA sequence from text file
    Input   : filename
    Output  : Dict with sequence Name as key and fasta sequence as value
    '''
    with open(filename) as file:
        FASTA = dict()
        lines = file.readlines()
        for line in lines:
            if line.startswith('>'):
                seqname = line.rstrip().lstrip('>')
                FASTA[seqname] = ''
            else:
                FASTA[seqname] += line.rstrip()
        return FASTA


def hello():
    print('Hello')

import os
os.environ['PATH']
import sys
sys.path.insert(0, './bin')
import canmatrix.convert


def convert_dbc(event, handler):
    command = './bin/canconvert ./eddy/test.dbc ./eddy/test.xlsx'
    canmatrix.convert.convert('./eddy/test.dbc', '/tmp/test.xlsx')
    files = [f for f in os.listdir('/tmp')]
    for f in files:
        print f
#!/usr/bin/env python
"""
This script demonstrates the usage of logparser to parse your own log data.
To get started, please first install the logparser via ``.
To get better parsing results, you are suggested to tune the hyper-parameters
`st` and `depth`.
"""
import sys
sys.path.append('../../')
from logparser.Spell import LogParser

#input_dir = '../data/test_log/' # The input directory of log file
#output_dir = 'result/'  # The output directory of parsing results
#log_file = 'unknow.log'  # The input log file name
#log_format = '<Date> <Time> <Level>:<Content>' # Define log format to split message fields
input_dir  = '../../data/TrainTicket/' # The input directory of log file
output_dir = 'demo_result/'  # The output directory of parsing results
log_file   = 'F0101raw_log2021-08-14_10-22-51.log'  # The input log file name
log_format = '<Date> <Time> <Context> <Thread> <Level> <Component> -<Content>'  # Train Ticket log format

# Regular expression list for optional preprocessing (default: [])
#regex = [
#    r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)' # IP
#]
regex = []
tau        = 0.5

parser = LogParser(indir=input_dir, outdir=output_dir, log_format=log_format, tau=tau, rex=regex)
parser.parse(log_file)









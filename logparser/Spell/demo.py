#!/usr/bin/env python

import sys
sys.path.append('../../')
from logparser.Spell import LogParser

input_dir  = '../../data/TrainTicket/' # The input directory of log file
output_dir = 'demo_result/'  # The output directory of parsing results
log_file   = 'normal0726data-raw_log_small.log'  # The input log file name
log_format = '<Date> <Time> <Context> <Thread> <Level> <Component> -<Content>'  # Train Ticket log format
tau        = 0.7  # Message type threshold (default: 0.5)
regex      = [
    r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)', # IP
    r'([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})' , # UUID
    r'\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{2} \d{2} \d{2} [A-Z]{3} \d{4}\b' ,# date
    r'\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{2} \d{2}:\d{2}:\d{2} [A-Z]{3} \d{4}\b' , #another date

    r'\[\s*(?:\w+\s*,\s*)*\w*\s*\]', # list of places
    r'\[\s*(?:\d+\s*,\s*)*\d*\s*\]', # list of distances
    r"'([^']+)'", #station
    r'(startStationId|terminalStationId)=([^&\n]+)',
    r'\[(\D*?)(\d+)(\D*?)\]',
    r'(\d+)\s*ms',
    r'(\d+)\s*seconds',
    r'port(?:s)?\s+(\d+)',
    r'TrainType\s+\w+',
    r'startingPlaceId\s+\w+',
    r'PlaceId\s+\w+',
    r'startingStationId\s+\w+',
    r'stationsId\s+\w+',
    r'(noSeat|businessSeat|firstClassSeat|secondClassSeat|hardSeat|softSeat|hardBed|softBed|highSoftBed)\s+\d+',
    r'(?<=[^A-Za-z0-9])(\-?\+?\d+)(?=[^A-Za-z0-9])|[0-9]+$', # Numbers
    r'USER TOKEN\s+(\S+)'

]  # Regular expression list for optional preprocessing (default: [])

sys.setrecursionlimit(2000)
parser = LogParser(indir=input_dir, outdir=output_dir, log_format=log_format, tau=tau, rex=regex)
parser.parse(log_file)

#!/usr/bin/env python
""" Convert PDF to CSV
"""

import os
import csv
import tabula
import log_app
from log_app import logging

class PdfApp(log_app.LogApp):
    """ Convert PDF to CSV """
    def __init__(self, args):
        super(PdfApp, self).__init__(args=args)
        #log_app.LogApp.__init__(self, args=args)
        script_name = os.path.splitext(os.path.basename(__file__))[0]
        self.get_config('{}.conf'.format(script_name))

        #self.in_pdf = args.pdf
        out_name = os.path.splitext(os.path.basename(args.pdf))[0]
        self.out_csv = '{}.csv'.format(out_name)

    def convert(self, out_path='.'):
        """ Do conversion """
        tabula.convert_into(self.args.pdf, 'KES-comma.csv', pages="all")
        with open('KES-comma.csv') as tabula_csv, \
             open(out_path + '/' + self.out_csv, 'w') as final_csv:
            reader = csv.reader(tabula_csv)
            writer = csv.writer(final_csv, delimiter='^')
            writer.writerows(reader)

if __name__ == '__main__':
    log_app.PARSER.add_argument('--pdf', type=str, required=True, help='input pdf file')
    ARGS = log_app.PARSER.parse_args()
    APP = PdfApp(args=ARGS)
    logging.info('Start parsing pdf file:%s', ARGS.pdf)
    APP.convert()

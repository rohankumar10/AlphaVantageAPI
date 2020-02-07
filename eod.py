from alpha_vantage.timeseries import TimeSeries
import csv


ts = TimeSeries(key='API KEY', output_format='csv', indexing_type=datetime)
data_csvreader, meta_data = ts.get_daily(symbol='AAPL', outputsize='full')

with open('AAPL.csv', 'w') as write_csvfile:
    writer = csv.writer(write_csvfile, dialect='excel')
    for row in data_csvreader:
        writer.writerow(row)

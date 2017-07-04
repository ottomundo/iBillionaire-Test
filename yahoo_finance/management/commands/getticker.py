from django.core.management.base import BaseCommand, CommandError
from yahoo_finance.models import Company, Stock
import pycurl, json, re

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('ticker', type=str)

    def handle(self, *args, **options):
        self.stdout.write(options['ticker'])
        def on_receive(data):
            data = data.decode('utf-8')
            #if 'yfs_mktmcb' in data:
                #raw = re.findall(r'yfs_mktmcb\((.*?)\)\;', data)
                #test = json.loads(raw[0])
                #print('---',test,'---')
            if 'yfs_u1f' in data:
                raw = re.findall(r'yfs_u1f\((.*?)\)\;', data)
                json_ = json.loads(raw[0].replace(':{', ':{"').replace('",','","').replace(':"','":"'))
                prices = json_[options['ticker']]
                stock = Stock.create(options['ticker'], prices)
                print(stock)

        ticker = options['ticker']
        url = 'https://streamerapi.finance.yahoo.com/streamer/1.0?s=' + ticker + '&k=j10,c63,p43,l84,t53,v53&callback=parent.yfs_u1f&mktmcb=parent.yfs_mktmcb&gencallback=parent.yfs_gencb&mu=1&lang=en-US&region=US&localize=0'
        try:
            conn = pycurl.Curl()
            conn.setopt(pycurl.URL, url)
            conn.setopt(pycurl.WRITEFUNCTION, on_receive)
            conn.perform()
        except KeyboardInterrupt:
            raise
        except:
            pass

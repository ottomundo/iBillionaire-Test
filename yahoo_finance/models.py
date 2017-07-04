from django.db import models
import datetime
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=6)

    def __str__(self):
        return self.ticker

    @classmethod
    def create(cls, name, ticker):
        company = cls(name=name, ticker=ticker)
        company.save()
        return company

class Stock(models.Model):
    ticker = models.ForeignKey(Company, related_name='stocks')
    price = models.CharField(max_length=200)
    change = models.CharField(max_length=200)
    change_perc = models.CharField(max_length=200)
    market_cap = models.CharField(max_length=200)
    volume = models.CharField(max_length=200)
    last_update = models.CharField(max_length=200)

    def __str__(self):
        return self.ticker.ticker

    @classmethod
    def create(cls, ticker, json):
        updated = datetime.datetime.now()
        company = Company.objects.filter(ticker=ticker)
        if len(company) > 0:
            company = company[0]
        else:
            company = Company.create(ticker, ticker)
        stock = cls(ticker=company, price=json['l84'],
                    change=json['c63'], change_perc=json['p43'],
                    market_cap=json['j10'], volume=json['v53'], last_update=updated)
        stock.save()
        return stock

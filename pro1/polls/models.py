from django.db import models

# Create your models here.
class ExchangeRate(models.Model):
    type = models.CharField(max_length=10, default='exchange_rate')
    rate = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f'{self.date} {self.cur_unit} : {self.deal_bas_r}'

class OilPrice(models.Model):
    oil_type = models.CharField(max_length=100)
    date = models.DateField()
    avg_price = models.DecimalField(max_digits=10, decimal_places=2) 
    
    def __str__(self):
        return f'{self.date} {self.oil_type} : {self.avg_price}'

class GoldPrice(models.Model):
    type = models.CharField(max_length=100, default='Gold') 
    date = models.DateField()  
    closing_price = models.DecimalField(max_digits=10, decimal_places=2)  
    
    def __str__(self):
        return f'{self.date} {self.type} : {self.closing_price}'
    
class Kospi(models.Model):
    type = models.CharField(max_length=100, default="KOSPI")
    date = models.DateField() 
    closing_price = models.DecimalField(max_digits=10, decimal_places=2) 
    
    def __str__(self):
        return f'{self.date} {self.type} {self.closing_price}'
    
class WTIOilPrice(models.Model):
    type = models.CharField(max_length=100, default='WTI_Oil') 
    date = models.DateField()  
    closing_price = models.DecimalField(max_digits=10, decimal_places=2)  
    
    def __str__(self):
        return f'{self.date} {self.type} : {self.closing_price}'

class NasdaqIndex(models.Model):
    type = models.CharField(max_length=100, default='Nasdaq')
    date = models.DateField()
    # index로 설정되어있었는데 index는 예약어라서 변경 >> index_price
    index_price = models.FloatField()
    def __str__(self):
        return f'{self.date} {self.type} : {self.index}'
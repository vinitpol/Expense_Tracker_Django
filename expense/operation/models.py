from django.db import models

# Create your models here.

class ExpenceModel (models.Model):
    payment_choise = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Online', 'Online'),   
        ('UPI', 'UPI'),
    ]
    payment_status = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('Pending', 'Pending'),
    ]
    sr = models.AutoField(primary_key=True, verbose_name="Sr.")
    spender = models.CharField(max_length=100)
    amount = models.IntegerField()
    payment_mode = models.CharField(max_length=100,choices=payment_choise)
    payment_status = models.CharField(max_length=100,choices=payment_status)
    date = models.DateField()
    class Meta:
        ordering = ['sr']



def __str__(self):
    return f"{self.spender} - {self.amount}"




from django.db import models

# Create your models here.
SUB = ['Physics', 'Chemistry', 'Mathematics']
ALL_SUB = sorted([(item, item) for item in SUB])
QN= ['1','2','3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
ALL_QN = sorted([(item, item) for item in QN])

QA = ['A', 'B', 'C', 'D', 'NA']
ALL_QA = sorted([(item, item) for item in QA])

RESULT = ['✅', '❌', '🚫']
ALL_RESULT = sorted([(item, item) for item in RESULT])

class MCQ(models.Model):
    EXC = models.CharField(max_length=50)
    SUB= models.TextField(choices=ALL_SUB, blank=True, null=True)
    QN = models.TextField(choices=ALL_QN, blank=True, null=True)
    QA = models.TextField(choices=ALL_QA, blank=True, null=True)
    RESULT = models.TextField(choices=ALL_RESULT, null=True)
    def __str__(self):
        return self.EXC + '  ' + self.SUB + '  ' +self.QN + '  '


QNN= ['21','22','23', '24', '25', '26', '27', '28', '29', '30']
ALL_QNN = sorted([(item, item) for item in QNN])

class NUMERICAL(models.Model):
    EXC = models.CharField(max_length=50)
    SUB= models.TextField(choices=ALL_SUB, blank=True, null=True)
    QNN = models.TextField(choices=ALL_QNN, blank=True, null=True)
    QA = models.FloatField()
    RESULT = models.TextField(choices=ALL_RESULT, null=True)

    def __str__(self):
        return self.EXC + '  ' + self.SUB + '  ' +self.QNN + '  '

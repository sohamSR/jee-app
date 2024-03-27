from django.forms import ModelForm
from .models import MCQ, NUMERICAL

class MCQFORM(ModelForm):
    class Meta:
            model = MCQ
            fields = ['EXC', 'SUB', 'QN', 'QA']

class NUMERICALFORM(ModelForm):
    class Meta:
            model = NUMERICAL
            fields = ['EXC', 'SUB', 'QA', 'QNN']
    
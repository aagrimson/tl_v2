#from django.forms import forms, ModelForm
from django import forms

from .models import Test, WaveDate



class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

class WaveDateForm(forms.ModelForm):
	class Meta:
		model = WaveDate
		exclude = ['test_no']

class ProductForm(forms.Form):
	super_category = forms.IntegerField(label='Super Category')
	category = forms.IntegerField(label='Category')
	sub_category = forms.IntegerField(label='Sub Category')
   	segment = forms.IntegerField(label='Segment')


class StoreForm(forms.Form):
	store_list = forms.FileField()
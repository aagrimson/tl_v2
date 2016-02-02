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


SUPER_CATEGORY_CHOICES = (
	(1, 'CONSUMER HEALTH CARE'),
	(2, 'BEAUTY CARE'),
	(3, 'GENERAL MERCHANDISE'),
	(4, 'EDIBLES'),
	(5, 'GREETING CARDS'),
	(6, 'PHOTO'),
	(7, 'PERSONAL CARE'),
)



class ProductForm(forms.Form):
	super_category = forms.MultipleChoiceField(label='Super Category', choices=SUPER_CATEGORY_CHOICES)
	category = forms.IntegerField(label='Category')
	sub_category = forms.IntegerField(label='Sub Category')
   	segment = forms.IntegerField(label='Segment')


class StoreForm(forms.Form):
	store_list = forms.FileField()
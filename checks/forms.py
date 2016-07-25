#from django.forms import ModelForm
from django import forms

class FormSearchCheck(forms.Form):
	MONTHS = (
		("1", "Enero"),
		("2", "Febrero"),
		("3", "Marzo"),
		("4", "Abril"),
		("5", "Mayo"),
		("6", "Junio"),
		("7", "Julio"),
		("8", "Agosto"),
		("9", "Setiembre"),
		("10", "Octubre"),
		("11", "Noviembre"),
		("12", "Diciembre"),
		)
	YEARS = (
		("2016", "2016"),
		("2015", "2015"),
		)
	ci = forms.CharField(label='Cedula', error_messages={'required': 'Debe ingresar su cedula'})
	month = forms.ChoiceField(choices=MONTHS)
	year = forms.ChoiceField(choices=YEARS)
	# fecha = forms.CharField(label='Mes', error_messages={'required': 'Debe ingresar un mes'})
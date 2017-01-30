# coding=utf-8

#from django.forms import ModelForm
from django import forms
from datetime import datetime
# from django.core.exceptions import ValidationError

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

	YEARS = tuple((str(n), str(n)) for n in range(datetime.now().year, 2013, -1))

	# YEARS = (
	# 	("2017", "2017"),
	# 	("2016", "2016"),
	# 	("2015", "2015"),
	# 	)

	VALUES = (
		('1', 'Nro. Cedula'),
		('2', 'Nro. Ficha'),
		)
	ci = forms.CharField(label='Cedula', error_messages={'required': 'Debe ingresar un valor'})
	month = forms.ChoiceField(choices=MONTHS)
	year = forms.ChoiceField(choices=YEARS)
	options = forms.ChoiceField(choices=VALUES, widget=forms.RadioSelect, error_messages={'required': 'Debe seleccionar una opción'})
	
	# def clean_ci(self):
	# 	cd = self.cleaned_data
	# 	ci = cd.get('ci')
	# 	if ci == '':
	# 		raise forms.ValidationError("Deber ingresar numero de cedula")
	# 	return ci
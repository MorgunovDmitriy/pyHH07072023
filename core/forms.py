from django import forms
from .models import Vacancy, Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name_company',
            'founding_date',
            'address_company'
        ]

class CompanyEditForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name_company',
            'founding_date',
            'address_company'
        ]

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'title',
            'salary',
            'description',
            'email',
            'contacts'
        ]

class VacancyEditForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'title',
            'salary',
            'description',
            'email',
            'contacts'
        ]
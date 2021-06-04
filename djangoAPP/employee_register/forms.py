from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('nome_completo', 'telefone', 'emp_code', 'posição')
        labels = {
            'nome_completo': 'Nome Completo',
            'emp_code': 'Código Emp',
            'posição': 'Cargo',
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['posição'].empty_label = "Select"
        self.fields['emp_code'].required = False

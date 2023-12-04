from django import forms


class CalcForm(forms.Form):
    first_number = forms.IntegerField(label="Первое число", min_value=-100, max_value=100,
                                      widget=forms.NumberInput(attrs={"class": "form-control"}))
    second_number = forms.IntegerField(label="Второе число", min_value=-100, max_value=100,
                                       widget=forms.NumberInput(attrs={"class": "form-control"}))

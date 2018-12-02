from django import forms


class SearchForm (forms.Form):
    busca = forms.CharField(required=True)


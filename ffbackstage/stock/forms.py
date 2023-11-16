from django import forms
from .models import *


class ProductFilterForm(forms.Form):
    search_field = forms.CharField(label='',
                                   required=False,
                                   widget=forms.TextInput(attrs={
                                       'class': 'search_field',
                                       'type': 'search',
                                       'placeholder': 'наименование, код, артикул'
                                   }))

    brand = forms.ModelMultipleChoiceField(
        queryset=Brands.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
        # widget=forms.CheckboxSelectMultiple(attrs={'class': 'brand_checkbox',})
    )
    tag = forms.ModelMultipleChoiceField(
        queryset=TagsProducts.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    supplied = forms.MultipleChoiceField(
        choices=((True, 'yes'),
                 (False, 'no')),
        label="supplied",
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    active = forms.MultipleChoiceField(
        choices=((True, 'yes'),
                 (False, 'no')),
        label="active",
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    promo = forms.MultipleChoiceField(
        choices=((True, 'yes'),
                 (False, 'no')),
        label="promo",
        required=False,
        widget=forms.CheckboxSelectMultiple
    )


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Products
        exclude = ['author']

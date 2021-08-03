from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('product_name', 'url' )

class CategoryForm(ModelForm):
    class Meta:
        model = Product
        fields = ('category',)

# class FilteredForm(ModelForm):
#     class Meta:
#         model = OrderForm
#         fields = ('product_name', 'url', 'email' )
    # def __init__(self, user=None, **kwargs):
    #     super(FilteredForm, self).__init__(**kwargs)
    #     if user:
    #         self.fields['email'].queryset = Order.objects.filter(user=user)


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('name', 'email', )


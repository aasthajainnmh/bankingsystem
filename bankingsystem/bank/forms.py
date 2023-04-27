from django import forms
from .models import customerList

class SenderForm(forms.Form):
    customer_names = customerList.objects.values_list('name', flat=True)
    sender_choices = [(name, name) for name in customer_names]
    currentbalance = customerList.objects.values_list('currentbalance', flat=True)
    sender_name = forms.ChoiceField(
        label='Choose Sender',
        choices=sender_choices,
        initial=sender_choices[0][0],  
        widget=forms.Select(attrs={'class': 'form-control'})  )

class ReceiverForm(forms.Form):
    customer_names = customerList.objects.values_list('name', flat=True)
    receiver_choices = [(name, name) for name in customer_names]
    receiver_name = forms.ChoiceField(label='Choose Receiver', choices=receiver_choices,initial=receiver_choices[0][0],
                                      widget=forms.Select(attrs={'class':'form-control'}))
    currentbalance = customerList.objects.values_list('currentbalance', flat=True)
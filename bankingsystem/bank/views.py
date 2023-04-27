from django.shortcuts import render
from .models import customerList
from .forms import SenderForm,ReceiverForm
def mainpage(request):
    return render(request,'mainpage.html')

def customerlist(request):
    customers = customerList.objects.all()
    return render(request, 'customerlist.html', {'customers': customers})

def transfer(request):
    names=customerList.objects.values_list('name',flat=True)
    sender_form = SenderForm(prefix='sender')
    receiver_form = ReceiverForm(prefix='receiver')
    return render(request, 'transfer.html', {'sender_form': sender_form,'receiver_form':receiver_form})

def send_money(request):
    sender_form = SenderForm(request.POST)
    receiver_form = ReceiverForm(request.POST)
    if request.method == 'POST':
        # Retrieve form data
        

        if sender_form.is_valid() and receiver_form.is_valid():
            # sender_form.currentbalance -= sender_form.cleaned_data['currentbalance']
            # receiver_form.currentbalance += receiver_form.cleaned_data['currentbalance']
            # sender_form.save()
            # receiver_form.save()

            # Show success message
            success_message = 'Money sent successfully!'
            return render(request, 'successmessage.html', {'message': success_message})

    # Render the template
    return render(request, 'transfer.html', {'sender_form': sender_form, 'receiver_form': receiver_form})
    
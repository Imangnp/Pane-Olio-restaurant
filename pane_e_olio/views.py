from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate




# class loginForm(forms.Form):
#     email = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)


# class SignUpForm(forms.Form):
#     email = forms.CharField()
#     phone_number = forms.CharField(widget=forms.NumberInput)
#     password1 = forms.CharField(widget=forms.NumberInput)
#     password2 = forms.CharField(widget=forms.NumberInput)


# def home(request):
  
#     form = loginForm()

#     if request.method == 'POST':
#         form = loginForm(request.POST)
#         print('LOGGING IN')
#         if form.is_valid():
#             # process the form data
#             username = request.POST.get('email')
#             password = request.POST.get('password')
#             user = authenticate(username=username, password=password)
#             if user:
#                 print('success')
#             else:
#                 print('fail')
                
#     print('IN HOME')

#     return render(request, 'index.html', {'form': form})

def home(request):
    # Render the "index.html" template
    return render(request, 'index.html')


def aboutus(request):

    # Render the "about-us.html" template
    return render(request, 'about-us.html')


def reserve(request):
    # Render the "reserve.html" template
    return render(request, 'reserve.html')
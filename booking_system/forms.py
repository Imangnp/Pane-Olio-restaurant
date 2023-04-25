from django import forms
from .models import Reservation
from datetime import datetime, timedelta, time, date


TIME_CHOICES = [
    ('12:00', '12:00 PM'),
    ('12:30', '12:30 PM'),
    ('13:00', '01:00 PM'),
    ('13:30', '01:30 PM'),
    ('14:00', '02:00 PM'),
    ('14:30', '02:30 PM'),
    ('15:00', '03:00 PM'),
    ('15:30', '03:30 PM'),
    ('16:00', '04:00 PM'),
    ('16:30', '04:30 PM'),
    ('17:00', '05:00 PM'),
    ('17:30', '05:30 PM'),
    ('18:00', '06:00 PM'),
    ('18:30', '06:30 PM'),
    ('19:00', '07:00 PM'),
    ('19:30', '07:30 PM'),
    ('20:00', '08:00 PM'),
    ('20:30', '08:30 PM'),
    ('21:00', '09:00 PM'),
]



PEOPLE_CHOICES = [    
    ('1', '1 person'),
    ('2', '2 people'), 
    ('3', '3 people'),
    ('4', '4 people'), 
    ('5', '5 people'),
    ('6', '6 people'),
    ('7', '7 people'),
    ('8', '8 people'),
    ('9', '9 people'),
    ('10', '10 people'),
]


class DateInput(forms.DateInput):
    '''
    This class method is nesessary to assist with providing
    the widgets of the date field in the booking form with a
    calendar view for the User
    '''
    input_type = 'date'


class ReservationForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Name',
                'class': 'form-control',
                'required': True
            }
        )
    )
    
    phone = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Phone',
                'class': 'form-control',
                'required': True
            }
        )
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control',
                'required': True
            }
        )
    )

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'min': str(date.today()),
                # 'id': 'input',
                # 'placeholder': 'Date',
                'class': 'form-control',
                'required': True,
            }
        )
    )

    people = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-select col-md-6',
                'required': True
            }
        ),
        choices=PEOPLE_CHOICES
    )

    time = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'type': 'time',
                'class': 'form-select col-md-6',
                'required': True,
                'min': datetime.now().strftime('%H:%M'),
                'data-min':'now',
            }
        ),
        choices=TIME_CHOICES
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Special request',
                'class': 'form-control col-md-12',
                'rows': 1
            }
        ),
        required=False
    )

    # def clean_date(self):
    #     date = self.cleaned_data['date']
    #     if date < datetime.date.today():
    #         raise forms.ValidationError("The date cannot be in the past!")
    #     return date
    

    class Meta:
        model = Reservation
        fields = ('name', 'phone', 'email', 'date', 'people', 'time', 'message')

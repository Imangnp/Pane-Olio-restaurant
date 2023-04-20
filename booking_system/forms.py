from django import forms
from .models import Reservation
from datetime import datetime, time

TIME_CHOICES = (
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
)

PEOPLE_CHOICES = [    ('1', '1 person'),
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
                'placeholder' :'Email',
                'class': 'form-control',
                         'required': True
            }
        )
    )

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder': 'Date',
                'class': 'form-control',
                'id': 'input',
                'required': True,
                'min': datetime.today().strftime('%Y-%m-%d')
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
                'class': 'form-select col-md-6',
                'required': True,
                'min': datetime.now().strftime('%H:%M')
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


    class Meta:
        model = Reservation
        fields = '__all__'


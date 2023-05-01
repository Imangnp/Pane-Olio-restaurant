import datetime
from django import forms
from .models import Reservation
from datetime import date
from django.utils import timezone



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


TIME_CHOICES = [
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
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
]


class ReservationForm(forms.ModelForm):
    """
    A form for creating a reservation.
    Displays fields for the user to enter their name, phone number, email, desired date and time,
    and number of people in their party. The date and time fields are restricted to valid future
    choices.
    """

    class Meta:
        model = Reservation
        fields = ('name', 'phone', 'email', 'date', 'people', 'time', 'message')


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
                # 'min': datetime.now().strftime('%H:%M'),
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


# Define a function to get the future time choices based on the current time


# class ReservationForm(forms.ModelForm):
#     """
#     A form for creating a reservation.

#     Displays fields for the user to enter their name, phone number, email, desired date and time,
#     and number of people in their party. The date and time fields are restricted to valid future
#     choices.

#     """

#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#         now = datetime.datetime.now().time()
#         valid_times = [datetime.time(hour=h, minute=m) for h in range(10, 22) for m in (0, 30)]
#         future_times = [t for t in valid_times if t >= now]
#         self.fields['time'].choices = [(t.strftime('%H:%M'), t.strftime('%H:%M')) for t in future_times]

#     def clean_date(self):
#         """
#         Get the selected date from the form data.
#         """
#         date = self.cleaned_data['date']
#         return date

#     def clean_time(self):
#         """
#         Get the selected time from the form data.
#         """
#         time = self.cleaned_data['time']
#         return time

#     def clean(self):
#         """
#         Validate the form data.
#         """
#         cleaned_data = super().clean()
#         date = cleaned_data.get('date')
#         time = cleaned_data.get('time')

#         # Get the current date and time.
#         now = timezone.now()

#         # If the selected date is in the past, raise a validation error.
#         if date < now.date():
#             raise forms.ValidationError("Invalid date - cannot book a table in the past.")

#         # If the selected date is today, filter the valid times to remove passed times.
#         if date == now.date():
#             valid_times = [datetime.time(now.hour, m) for m in range(0, 60, 30) if now.minute <= m]
#         else:
#             valid_times = [datetime.time(hour=h, minute=m) for h in range(10, 22) for m in (0, 30)]

#         # If the selected time is not valid, raise a validation error.
#         if time not in valid_times:
#             raise forms.ValidationError("Invalid time - please choose a valid time.")

#         return cleaned_data

#     class Meta:
#         model = Reservation
#         fields = ('name', 'phone', 'email', 'date', 'people', 'time', 'message')


#     name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Your Name',
#                 'class': 'form-control',
#                 'required': True
#             }
#         )
#     )

#     phone = forms.IntegerField(
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Phone',
#                 'class': 'form-control',
#                 'required': True
#             }
#         )
#     )
    
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 'placeholder': 'Email',
#                 'class': 'form-control',
#                 'required': True
#             }
#         )
#     )

#     date = forms.DateField(
#         widget=forms.DateInput(
#             attrs={
#                 'type': 'date',
#                 'min': str(date.today()),
#                 # 'id': 'input',
#                 # 'placeholder': 'Date',
#                 'class': 'form-control',
#                 'required': True,
#             }
#         )
#     )

#     people = forms.ChoiceField(
#         widget=forms.Select(
#             attrs={
#                 'class': 'form-select col-md-6',
#                 'required': True
#             }
#         ),
#         choices=PEOPLE_CHOICES
#     )

#     # time = forms.TimeField(
#     #     widget=forms.TimeInput(
#     #         attrs={
#     #             'type': 'time',
#     #             'class': 'form-select col-md-6',
#     #             'required': True,
#     #             'min': datetime.now().strftime('%H:%M'),
#     #             'data-min': 'now',
#     #         }
#     #     ),
#     #     choices=TIME_CHOICES
#     # )
#     time = forms.TypedChoiceField(
#         coerce=lambda x: datetime.strptime(x, '%H:%M').time(),
#         choices=(),
#         widget=forms.Select(
#             attrs={
#                 'class': 'form-select col-md-6',
#                 'required': True
#             }
#         )
#     )

#     # time = forms.ChoiceField(choices=(), widget=forms.Select(attrs={
#     #     'class': 'form-control',
#     #     'style': 'width: 50%'
#     # }))

#     message = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 'placeholder': 'Special request',
#                 'class': 'form-control col-md-12',
#                 'rows': 1
#             }
#         ),
#         required=False
#     )

    
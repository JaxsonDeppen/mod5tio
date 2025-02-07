from django import forms
from .models import Review

Sessions1 = (
    ('swimming', 'Swimming'),
    ('biking', 'biking'),
    ('racing', 'Racing'),
    ('meeting', 'Meeting'),
)

class ReviewForm(forms.ModelForm):
    sessions = forms.MultipleChoiceField(
        choices=Sessions1,
        widget=forms.CheckboxSelectMultiple(),
        label="Event Options"
    )
    
    class Meta:
        model = Review
        fields = ('user_name','email','number','sessions','allergies',)
        allergies1 = [
            ('Dairy', 'Dairy'),
            ('Peanuts', 'Peanuts'),
            ('air', 'air'),
        ]
        
        allergies = forms.MultipleChoiceField( 
            choices=allergies1,
            widget=forms.CheckboxSelectMultiple()
        )
        
        labels = {
            "user_name": "User Name",
            "email": "Email",
            "number" : "Phone Number",
            "allergies" : "allergies"
        }
    
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!"
            },
            "email" : {
                "required": "You must enter in an email address",
            },
            "feedback": {
                "required": "Please give us some feedback"
            }
        }



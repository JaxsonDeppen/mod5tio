from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         "required": "Your name must not be empty!",
#         "max_length": "Please enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
 
    class Meta:
        
       
        model = Review
        fields = ('user_name','email','number','sessions','allergies',)
        allergies1 = [
        ('Dairy', 'Dairy'),
        ('Peanuts', 'Peanuts'),
        ('air', 'air'),
        ]
        Sessions1= {
            ('swimming', 'Swimming'),
            ('biking', 'biking'),
            ('racing', 'Racing'),
            ('meeting', 'Meeting'),
        }
        sessions = forms.ChoiceField(
            choices=Sessions1,
            widget=forms.ChoiceField()
        )
        allergies = forms.MultipleChoiceField( 
            choices=allergies1,
            widget=forms.CheckboxSelectMultiple()
        )
       
        labels = {
            "user_name": "User Name",
            "email": "Email",
            "number" : "Phone Number",
            "sessions" : "Event options",
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
       
        

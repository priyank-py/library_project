from django import forms
from .models import Author
class AuthorForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ('name', 'about', 'dob', 'language', 'country', 'image')
    
    def clean_about(self):
        content = self.cleaned_data.get('about')
        if len(content) > 140:
            raise forms.ValidationError("That's too long for intro.")
        return content

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        
        about = data.get('about')
        print(about)
        if about == '':
            about = None        
        photo = data.get('image')
        if about is None and photo is None:
            raise forms.ValidationError('about or photo must be there.')
        
        super().clean(*args, **kwargs)

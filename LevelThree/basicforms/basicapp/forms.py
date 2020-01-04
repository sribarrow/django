from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Validation Error: Name needs to start with z.")

class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Confirm Email')
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,
                                 # widget=forms.HiddenInput,
                                 # validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        clean_all_data = super().clean()
        email = clean_all_data['email']
        vmail = clean_all_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Emails do not match. Retry...")
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #
    #     if len(botcatcher) > 0 :
    #         raise forms.ValidationError("Got your bot!")
    #
    #     return botcatcher

from xml.dom import ValidationErr
from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    confirm_email = forms.EmailField(label = "Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget = forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("Gotcha BOT!!")
    #     return botcatcher

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        confirm_email = all_clean_data['confirm_email']

        if email!=confirm_email:
            raise forms.ValidationErr("Email does not match.")
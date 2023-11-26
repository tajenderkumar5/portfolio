from django import forms


class contactForm(forms.Form):
    name = forms.CharField()
    userEmail = forms.EmailField()
    sub = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('userEmail')
        print(email)
        if email.endswith(".edu"):
            raise forms.ValidationError(
                "this is not vaild email .please do not use .edu")
        return email

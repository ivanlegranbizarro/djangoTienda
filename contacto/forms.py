from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True)
    email = forms.EmailField(label='Email', required=True)
    mensaje = forms.CharField(
        label='Mensaje', required=True, widget=forms.Textarea)

    def send_mail(self):
        # send email using the self.cleaned_data dictionary
        pass

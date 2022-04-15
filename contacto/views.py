from django.conf import settings
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.views import generic
from .forms import ContactoForm


class ContactoView(generic.FormView):
    template_name = 'contacto/contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('contacto:success')

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        mensaje = form.cleaned_data['mensaje']

        email = EmailMessage("Mensaje desde App Django",
                             "El usuario con nombre {}, desde la dirección {}, escribe lo siguiente:\n\n {}".format(nombre, email, mensaje), settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], reply_to=[email])
        email.send()
        return super().form_valid(form)


class SuccessView(generic.TemplateView):
    template_name = 'contacto/success.html'

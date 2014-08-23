# Create your views here.


import logging

from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from .forms import ContactForm1
from .forms import ContactForm2


logger = logging.getLogger(__name__)


class ContactWizard(SessionWizardView):
    template_name = 'demo/wizard.html'

    def done(self, form_list, **kwargs):
        for form in form_list:
            logger.debug(u'{}: {}'.format(form.__class__.__name__, form.cleaned_data))
        return HttpResponseRedirect(reverse('done'))


contact_wizard = ContactWizard.as_view([ContactForm1, ContactForm2])
done = TemplateView.as_view(template_name='demo/done.html')

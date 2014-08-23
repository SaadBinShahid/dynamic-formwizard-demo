# Create your views here.


from collections import OrderedDict
import logging

from django.contrib.formtools.wizard.views import SessionWizardView
from django.contrib.formtools.wizard.views import WizardView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from .forms import ContactForm1
from .forms import ContactForm2


logger = logging.getLogger(__name__)


class ContactWizard(SessionWizardView):
    template_name = 'demo/wizard.html'
    initial_dict = {}
    instance_dict = {}
    condition_dict = {}

    @classmethod
    def as_view(cls, *args, **kwargs):
        return super(WizardView, cls).as_view(*args, **kwargs)

    @property
    def form_list(self):
        return OrderedDict([
            ('contact1', ContactForm1),
            ('contact2', ContactForm2)
        ])

    def done(self, form_list, **kwargs):
        for form in form_list:
            logger.debug(u'{}: {}'.format(form.__class__.__name__, form.cleaned_data))
        return HttpResponseRedirect(reverse('done'))


contact_wizard = ContactWizard.as_view()
done = TemplateView.as_view(template_name='demo/done.html')

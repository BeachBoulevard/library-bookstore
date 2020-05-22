import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class BookRenewalForm(forms.Form):
  renew_date = forms.DateField(help_text="1 to 4 weeks")

  def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        # confirm relation with past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # ensure range with max of 3 weeks
        if data > datetime.date.today() + datetime.timedelta(weeks=3):
            raise ValidationError(_('Invalid date - renewal more than 3 weeks ahead'))

        return data
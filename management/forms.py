from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class BookRenewalForm(forms.Form):
  renewal_date = forms.DateField(help_text="1 to 3 weeks")

  def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        # compare with current for past
        if data < datetime.date.today():
            raise ValidationError(_('Past date, kindly revise you entry'))

        # ensure range with max of 3 weeks
        if data > datetime.date.today() + datetime.timedelta(weeks=3):
            raise ValidationError(_('The entry is past the stipulated three weeks, kindly revise'))

        return data
from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailusers.forms import UserEditForm, UserCreationForm


# class CustomUserEditForm(UserEditForm):
#     moniker = forms.CharField(required=True, label=_("Moniker"))
#
#
# class CustomUserCreationForm(UserCreationForm):
#     moniker = forms.CharField(required=True, label=_("Moniker"))

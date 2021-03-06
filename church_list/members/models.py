from datetime import datetime
from typing import Optional

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Member(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    phone = models.CharField(_('Phone'), max_length=255, blank=True)
    mobile_phone = models.CharField(_('Mobile phone'), max_length=255, blank=True)
    address = models.CharField(_('Address'), max_length=255)
    baptize_date = models.DateField(_('Baptize date'), blank=True, null=True)
    birth_date = models.DateField(_('Birth date'), blank=True, null=True)
    note = models.TextField(_('Note'), blank=True)

    def __str__(self) -> str:
        return self.name

    def first_name(self) -> str:
        name_parts = self.name.split(' ')
        if name_parts:
            return name_parts[0]
        return ''

    def last_name(self) -> str:
        name_parts = self.name.split(' ')
        if name_parts:
            return name_parts[-1]
        return ''

    def full_name(self) -> str:
        return f'{self.first_name()} {self.last_name()}'.strip()

    def years_old(self, year: Optional[int] = None) -> Optional[int]:
        if year is None:
            year = datetime.today().year

        if not self.birth_date:
            return None

        return year - self.birth_date.year

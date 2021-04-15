from datetime import datetime
from typing import List

from django.utils.translation import ugettext_lazy as _

from church_list.members.models import Member


month_to_name = {
    1: _('January'),
    2: _('February'),
    3: _('March'),
    4: _('April'),
    5: _('May'),
    6: _('June'),
    7: _('July'),
    8: _('August'),
    9: _('September'),
    10: _('October'),
    11: _('November'),
    12: _('December'),
}


def get_members_by_birth_month(month: int) -> List[Member]:
    return list(Member.objects.filter(birth_date__month=month).order_by('birth_date__day'))


def print_birthdays(year: int = None):
    if year is None:
        year = datetime.today().year

    for month in range(1, 13):
        print(f'Birthdays for {month_to_name[month]}')
        for member in get_members_by_birth_month(month):
            print(f'{member.first_name()} {member.last_name()}, {member.birth_date.strftime("%d.%m.%Y")} - {year - member.birth_date.year} years')
        print()

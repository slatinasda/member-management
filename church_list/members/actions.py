from calendar import Calendar
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


def group_birthday_members_by_weeks(
    members: List[Member],
    month_weeks: List[List[int]],
    remove_empty_weeks: bool = True,
) -> List[List[Member]]:
    if not members:
        return []

    members_by_weeks = []
    for week in month_weeks:
        members_by_weeks.append([])

        for member in members:
            if member.birth_date.day in week:
                members_by_weeks[-1].append(member)

        if remove_empty_weeks:
            if len(members_by_weeks[-1]) == 0:
                members_by_weeks.pop()

    return members_by_weeks


def print_birthdays(year: int = None):
    if year is None:
        year = datetime.today().year

    # Make Sunday the first day of the week (Saturday becomes the 7th day).
    # If a member has a birthday on Sunday, we want to move it to the next week.
    # We're doing this only for indentation and compartmentalization purposes.
    cal = Calendar(firstweekday=6)

    for month in range(1, 13):
        month_weeks: List[List[int]] = cal.monthdayscalendar(year, month)
        members = get_members_by_birth_month(month)

        print(f'Birthdays for {month_to_name[month]}')
        for week_ind, week in enumerate(group_birthday_members_by_weeks(members, month_weeks)):
            for member in week:
                member_info = f'{member.full_name()}, {member.birth_date.strftime("%d.%m.%Y")} - {member.years_old(year)} years'
                if week_ind % 2 == 0:
                    print(f'    {member_info}')
                else:
                    print(member_info)
        print()

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List
import csv

from django.core.management.base import BaseCommand

from church_list.members.models import Member


@dataclass
class MemberRow:
    """Represents a row from the CSV file"""
    id: str
    name: str
    phone: float
    mobile_phone: float
    address: str
    baptize_date: str
    birth_date: str
    note: str


def read_members_csv(csv_file: str) -> List[MemberRow]:
    with open(csv_file, 'r', newline='') as members_csv:
        memebrs_reader = csv.reader(members_csv, delimiter=',')
        all_members = [
            MemberRow(
                id=row[0],
                name=row[1],
                phone=row[2],
                mobile_phone=row[3],
                address=row[4],
                baptize_date=row[5],
                birth_date=row[6],
                note=row[7],
            )
            for row in memebrs_reader
        ]
    # Skip the first row, because it contains column names
    all_members = all_members[1:]
    # Filter out empty member names
    all_members = [member for member in all_members if member.name != '']

    return all_members


def map_to_db_member(csv_member: MemberRow, date_format: str = '%d/%m/%Y') -> Member:
    baptize_date = datetime.strptime(csv_member.baptize_date, date_format) if csv_member.baptize_date else None
    birth_date = datetime.strptime(csv_member.birth_date, date_format) if csv_member.birth_date else None

    return Member(
        name=csv_member.name,
        phone=csv_member.phone,
        mobile_phone=csv_member.mobile_phone,
        address=csv_member.address,
        baptize_date=baptize_date,
        birth_date=birth_date,
        note=csv_member.note,
    )


class Command(BaseCommand):
    help = """Import members from CSV file with the following columns:
        id, name, phone, mobile_phone, address, baptize_date, birth_date, note
    """

    def add_arguments(self, parser):
        parser.add_argument('csv_path', help='Absolute path to CSV file, or relative path from project root')

    def handle(self, csv_path: str, *args, **kwargs):
        file_path = Path(csv_path).absolute()
        if not file_path.is_file():
            print(f'Cannot find file at "{csv_path}"')
            exit(1)

        members = read_members_csv(csv_path)
        for member in members:
            db_member = map_to_db_member(member)
            print(f'Saving member.name="{db_member.name}"')
            db_member.save()



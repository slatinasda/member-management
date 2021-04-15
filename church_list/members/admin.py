from django.contrib import admin

from church_list.members.models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'baptize_date', 'address',)
    list_filter = ('birth_date', 'baptize_date')
    search_fields = ('name', 'address',)

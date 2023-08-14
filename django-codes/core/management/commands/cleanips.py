from django.core.management.base import BaseCommand, CommandParser
from accounts.models import BlockedIps


class Command(BaseCommand):
    help = "Used to delete non-superusers"
    requires_migrations_checks = True
    stealth_options = ("stdin",)

    def handle(self, *args, **options):
        ips = BlockedIps.objects.all()
        ips.delete()
from django.core.management.base import BaseCommand

from valuenetwork.valueaccounting.process_faircoin_requests import create_address_for_agent
from valuenetwork.valueaccounting.faircoin_utils import is_mine as is_address_in_wallet
from valuenetwork.valueaccounting.models import EconomicAgent


class Command(BaseCommand):

    help = "Reassign wallet addresses to new FairCoin accounts after changing to a test Electrum wallet."

    def handle(self, *args, **options):
        reassigned = 0
        found = 0
        total = 0
        models = EconomicAgent.objects.all()

        for agent in models:
            total += 1
            fcr = agent.faircoin_resource()
            if fcr is None:
                continue
            if fcr.digital_currency_address:
                found += 1
                if not is_address_in_wallet(fcr.digital_currency_address):
                    reassigned += 1
                    fcr.digital_currency_address = create_address_for_agent(agent)
                    fcr.save()

        print "Finished %d wallet reassignments of %d wallets & %d total agents" % (reassigned, found, total)

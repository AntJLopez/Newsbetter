from newsletter.models import Newsletter
from pprint import pprint


def run():
    newsletters = Newsletter.objects.all()
    for newsletter in newsletters:
        pprint(newsletter)
        for section in newsletter.sections():
            pprint(section)

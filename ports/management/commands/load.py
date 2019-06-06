from django.core.management.base import BaseCommand, CommandError

from parsing_scripts import load_initial_data


class Command(BaseCommand):

    help = "Populates the database with Initial data from portindex.json file"

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='?', type=str, default='portindex.json')

    def handle(self, *args, **options):
        try:
            ports = load_initial_data.open_portindex_json(options['path'])
            load_initial_data.load_categories_table(ports)
            load_initial_data.load_ports_and_maintainers_table(ports)
        except FileNotFoundError:
            raise CommandError('"{}" not found. Make sure "{}" is a valid JSON file and is in the root of the project'.format(
                options['path'], options['path']
            ))

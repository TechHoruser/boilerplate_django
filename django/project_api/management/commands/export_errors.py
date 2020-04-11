import inspect
from django.core.management.base import BaseCommand
from project_api.errors import Errors
from django.conf import settings


class Command(BaseCommand):
    help = "Export the errors to md file"

    def handle(self, *args, **options):
        errors = {
            error[0]: error[1]
            for error in inspect.getmembers(
                Errors, lambda a: not (inspect.isroutine(a))
            )
            if not error[0].startswith("__")
        }

        lines = [
            "%s | %s | %s" % (error, value["code"], value["message"])
            for error, value in sorted(errors.items(), key=lambda item: item[1]["code"])
        ]

        with open(settings.BASE_DIR + "/../doc/errors.md", "w") as f:
            f.write("Error | Code | Message\n")
            f.write("--- | :---: | ---:\n")
            for line in lines:
                f.write("%s\n" % line)

        print(self.style.SUCCESS("Successfully exported errors"))

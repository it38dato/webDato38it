from django.core.management.base import BaseCommand
from max_bot.client import MaxClient
from max_bot.handlers import handle_update


class Command(BaseCommand):
    help = "Запускает MAX-бота через Long Polling"
    def handle(self, *args, **options):
        client = MaxClient()
        marker = None
        self.stdout.write(
            self.style.SUCCESS("MAX bot started")
        )
        while True:
            try:
                result = client.get_updates(
                    timeout=30,
                    marker=marker,
                )
                self.stdout.write(
                    f"MAX response: {result}"
                )
                marker = result.get("marker", marker)
                updates = result.get("updates", [])
                for update in updates:
                    self.stdout.write(
                        f"Received update: {update}"
                    )
                    handle_update(update)
            except KeyboardInterrupt:
                self.stdout.write(
                    self.style.WARNING("MAX bot stopped")
                )
                break
            except Exception as error:
                self.stdout.write(
                    self.style.ERROR(
                        f"MAX bot error: {error}"
                    )
                )



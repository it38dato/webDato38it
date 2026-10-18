import time

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

                marker = result.get("marker", marker)
                updates = result.get("updates", [])

                for update in updates:
                    try:
                        handle_update(update)
                    except Exception as error:
                        self.stderr.write(
                            self.style.ERROR(
                                f"Update processing error: {error}"
                            )
                        )

            except KeyboardInterrupt:
                self.stdout.write(
                    self.style.WARNING("MAX bot stopped")
                )
                break

            except Exception as error:
                self.stderr.write(
                    self.style.ERROR(
                        f"MAX bot polling error: {error}"
                    )
                )
                time.sleep(5)
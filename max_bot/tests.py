from unittest.mock import patch
from django.test import SimpleTestCase
from max_bot.handlers import handle_update


class MaxBotTests(SimpleTestCase):

    @patch("max_bot.handlers.handle_start")
    def test_start_command_calls_handle_start(
        self,
        mock_handle_start,
    ):
        update = {
            "update_type": "message_created",
            "message": {
                "body": {"text": "/start"},
                "sender": {"user_id": 12345},
            },
        }

        handle_update(update)

        mock_handle_start.assert_called_once_with(12345)

    @patch("max_bot.handlers.handle_projects")
    def test_projects_callback_calls_handle_projects(
        self,
        mock_handle_projects,
    ):
        update = {
            "update_type": "message_callback",
            "callback": {
                "payload": "projects",
                "user": {"user_id": 12345},
            },
        }

        handle_update(update)

        mock_handle_projects.assert_called_once_with(12345)

    @patch("max_bot.handlers.handle_start")
    def test_start_callback_calls_handle_start(
        self,
        mock_handle_start,
    ):
        update = {
            "update_type": "message_callback",
            "callback": {
                "payload": "start",
                "user": {"user_id": 12345},
            },
        }

        handle_update(update)

        mock_handle_start.assert_called_once_with(12345)

    @patch("max_bot.handlers.client.send_message")
    def test_unknown_message_gets_fallback_response(
        self,
        mock_send_message,
    ):
        update = {
            "update_type": "message_created",
            "message": {
                "body": {"text": "Привет"},
                "sender": {"user_id": 12345},
            },
        }

        handle_update(update)

        mock_send_message.assert_called_once_with(
            12345,
            "Ты написал: Привет",
        )

    @patch("max_bot.handlers.client.send_message")
    def test_empty_message_is_ignored(
        self,
        mock_send_message,
    ):
        update = {
            "update_type": "message_created",
            "message": {
                "body": {"text": ""},
                "sender": {"user_id": 12345},
            },
        }

        result = handle_update(update)

        self.assertIsNone(result)
        mock_send_message.assert_not_called()

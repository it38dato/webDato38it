from .client import MaxClient

client = MaxClient()

def handle_start(user_id):
    text = (
        "Привет! 👋\n\n"
        "Я бот портфолио Дато.\n"
        "Здесь можно посмотреть проекты, навыки и контакты."
    )
    return client.send_message(user_id, text)

def handle_update(update):
    if update.get("update_type") != "message_created":
        return None
    message = update.get("message", {})
    body = message.get("body", {})
    text = body.get("text", "").strip()
    if not text:
        return None
    user = update.get("user", {})
    user_id = user.get("user_id")
    if not user_id:
        return None
    if text.lower() in ("/start", "start"):
        return handle_start(user_id)
    return client.send_message(
        user_id,
        f"Ты написал: {text}",
    )
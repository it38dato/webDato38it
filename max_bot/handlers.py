from .client import MaxClient
from webApp.models import Portfolio, About, Skill, Contact
import os

client = MaxClient()

def handle_start(user_id):
    text = (
        "Привет! 👋\n\n"
        "Я бот портфолио Дато.\n"
        "Здесь можно посмотреть проекты, навыки и контакты.\n"
        "Выбери нужный раздел:"
        #"Тестовая кнопка MAX"
    )
    attachments = [
        {
            "type": "inline_keyboard",
            "payload": {
                "buttons": [
                    [
                        {
                            "type": "callback",
                            "text": "📁 Проекты",
                            "payload": "projects",
                        },
                        {
                            "type": "callback",
                            "text": "👨‍💻 Обо мне",
                            "payload": "about",
                        },
                    ],
                    [
                        {
                            "type": "callback",
                            "text": "🛠 Навыки",
                            "payload": "skills",
                        },
                        {
                            "type": "callback",
                            "text": "📞 Контакты",
                            "payload": "contacts",
                        },
                    ],
                    [
                        {
                            "type": "link",
                            "text": "🌐 Сайт-портфолио",
                            "url": os.getenv("MAX_SITE_URL"),
                        },
                    ],
                ]
            },
        }
    ]    
    #return client.send_message(user_id, text)
    return client.send_message(
        user_id,
        text,
        attachments=attachments,
    )

def handle_callback(update):
    callback = update.get("callback", {})
    payload = callback.get("payload")
    #message = update.get("message", {})
    #sender = message.get("sender", {})
    #user_id = sender.get("user_id")
    user = callback.get("user", {})
    user_id = user.get("user_id")
    if not user_id:
        return None
    if payload == "projects":
        return handle_projects(user_id)
    if payload == "start":
        return handle_start(user_id)
    if payload.startswith("project:"):
        project_id = payload.split(":", 1)[1]
        if not project_id.isdigit():
            return client.send_message(
                user_id,
                "Некорректный ID проекта.",
            )
        return handle_project(
            user_id,
            int(project_id),
        )
    if payload == "about":
        about = About.objects.first()
        if not about:
            return client.send_message(
                user_id,
                "Информация обо мне пока не добавлена.",
            )
        text = (
            f"👨‍💻 {about.title}\n\n"
            f"{about.text}"
        )
        attachments = [
            {
                "type": "inline_keyboard",
                "payload": {
                    "buttons": [
                        [
                            {
                                "type": "callback",
                                "text": "🏠 Главное меню",
                                "payload": "start",
                            }
                        ]
                    ]
                },
            }
        ]
        return client.send_message(
            user_id,
            #f"👨‍💻 {about.title}\n\n"
            #f"{about.text}",
            text,
            attachments=attachments,
        )
    if payload == "skills":
        skills = Skill.objects.order_by("order", "name")
        if not skills.exists():
            text = (
                "🛠 Навыки\n\n"
                "Список навыков пока не добавлен."
            )              
        #    return client.send_message(
        #        user_id,
        #        "🛠 Навыки\n\n"
        #        "Список навыков пока не добавлен.",
        #    )
        #text = "🛠 Навыки\n\n"
        #for skill in skills:
        #    text += f"• {skill.name}"
        #    if skill.description:
        #        text += f" — {skill.description}"
        #    text += "\n"  
        else:
            text = "🛠 Навыки\n\n"
            for skill in skills:
                text += f"• {skill.name}"
                if skill.description:
                    text += f" — {skill.description}"
                text += "\n"   
        attachments = [
            {
                "type": "inline_keyboard",
                "payload": {
                    "buttons": [
                        [
                            {
                                "type": "callback",
                                "text": "🏠 Главное меню",
                                "payload": "start",
                            }
                        ]
                    ]
                },
            }
        ]
        return client.send_message(
            user_id,
            #"🛠 Навыки\n\n"
            #"Python\n"
            #"Django / DRF\n"
            #"PostgreSQL\n"
            #"Docker\n"
            #"Linux\n"
            #"Git / GitHub",
            text,
            attachments=attachments,
        )
    if payload == "contacts":
        contacts = Contact.objects.order_by("order", "name")
        if not contacts.exists():
            #return client.send_message(
            #    user_id,
            #    "📞 Контакты\n\n"
            #    "Контакты пока не добавлены.",
            #)
            text = (
                "📞 Контакты\n\n"
                "Контакты пока не добавлены."
            )
        #text = "📞 Контакты\n\n"
        #for contact in contacts:
        #    text += f"• {contact.name}: {contact.value}\n"        
        else:
            text = "📞 Контакты\n\n"
            for contact in contacts:
                text += f"• {contact.name}: {contact.value}\n"
        attachments = [
            {
                "type": "inline_keyboard",
                "payload": {
                    "buttons": [
                        [
                            {
                                "type": "callback",
                                "text": "🏠 Главное меню",
                                "payload": "start",
                            }
                        ]
                    ]
                },
            }
        ]
        return client.send_message(
            user_id,
            #"📞 Контакты\n\n"
            #"GitHub: github.com/it38dato",
            text,
            attachments=attachments,
        )
    return None

def handle_update(update):
    #if update.get("update_type") != "message_created":
    #    return None
    update_type = update.get("update_type")
    if update_type == "message_callback":
        return handle_callback(update)
    if update_type != "message_created":
        return None
    message = update.get("message", {})
    body = message.get("body", {})
    sender = message.get("sender", {})
    text = body.get("text", "").strip()
    user_id = sender.get("user_id")
    if not text:
        return None
    #user = update.get("user", {})
    #user_id = user.get("user_id")
    if not user_id:
        return None
    if text.lower() in ("/start", "start"):
        return handle_start(user_id)
    if text.lower() in ("/projects", "projects", "проекты"):
        return handle_projects(user_id)
    if text.lower().startswith("/project "):
        project_id = text.split(maxsplit=1)[1]
        if not project_id.isdigit():
            return client.send_message(
                user_id,
                "ID проекта должен быть числом.",
            )
        return handle_project(
            user_id,
            int(project_id),
        )
    return client.send_message(
        user_id,
        f"Ты написал: {text}",
    )

def handle_projects(user_id):
    projects = Portfolio.objects.select_related("cat").order_by("-begin")
    if not projects.exists():
        return client.send_message(user_id, "Пока проектов нет.",)
    #lines = ["📁 Мои проекты:\n"]
    buttons = []
    for project in projects:
        #lines.append(
        #    #f"• {project.specialization}"
        #    f"{project.id}. {project.specialization}"
        #)
        #title = project.specialization
        title = project.specialization or "Без названия"
        if len(title) > 35:
            title = title[:32] + "..."
        buttons.append([
            {
                "type": "callback",
                #"text": f"{project.id}. {project.specialization}",
                "text": f"{project.id}. {title}",
                "payload": f"project:{project.id}",
            }
        ])
    #text = "\n".join(lines)
    attachments = [
        {
            "type": "inline_keyboard",
            "payload": {
                "buttons": buttons,
            },
        }
    ]    
    #return client.send_message(user_id, text)
    return client.send_message(
        user_id,
        "📁 Мои проекты:\n\n"
        "Выбери проект:",
        attachments=attachments,
    )

def handle_project(user_id, project_id):
    try:
        project = (
            Portfolio.objects
            .select_related("cat")
            .get(pk=project_id)
        )
    except Portfolio.DoesNotExist:
        return client.send_message(
            user_id,
            "Проект с таким ID не найден.",
        )
    text = (
        f"📁 {project.specialization}\n\n"
        f"📍 Место: {project.location}\n"
        f"💼 Обязанности: {project.responsibilities}\n"
        f"📈 Результат: {project.progress}\n"
    )
    if project.cat:
        text += f"🏷 Категория: {project.cat.name}\n"
    attachments = []
    if project.image:
        try:
            image_token = client.upload_image(
                project.image.path
            )
            attachments.append(
                {
                    "type": "image",
                    "payload": {
                        "token": image_token,
                    },
                }
            )
        except Exception as error:
            print(
                f"MAX IMAGE ERROR: {error}"
            )
    #attachments = [
    attachments.append(
        {
            "type": "inline_keyboard",
            "payload": {
                "buttons": [
                    [
                        {
                            "type": "callback",
                            "text": "⬅️ К проектам",
                            "payload": "projects",
                        },
                        {
                            "type": "callback",
                            "text": "🏠 Главное меню",
                            "payload": "start",
                        },
                    ]
                ]
            },
        }
    #]
    )
    return client.send_message(
        user_id,
        text,
        attachments=attachments,
    )

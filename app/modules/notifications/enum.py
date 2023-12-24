from enum import Enum


class NotificationTypesEnum(str, Enum):
    EMAIL_FIRST_CONTACT = "EMAIL_FIRST_CONTACT"


class NotificationTemplateFilesEnum(str, Enum):
    EMAIL_FIRST_CONTACT = "email_first_contact.html"


class NotificationMessagesEnum(str, Enum):
    TIMEOUT_SEND_EMAIL_FIRST_CONTACT = "Você já enviou um e-mail na última hora. Por favor, aguarde nossa resposta ou espere um pouco para de enviar novamente."
    SUBJECT_EMAIL_FIRST_CONTACT = "Nova menssagem Coinf Web App {from_email}"

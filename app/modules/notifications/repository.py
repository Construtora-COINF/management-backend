from app.abstracts.database.base_repository import BaseRepository
from app.modules.notifications.model import Notification


class NotificationRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.entity = Notification

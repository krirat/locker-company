from User import User

class NotificationService:
    def send_notification(self, user: User, message: str):
        print(f'Notification sent to {user.name} : {message}')
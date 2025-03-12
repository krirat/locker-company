class NotificationService:
    def send_notification(self, user, message):
        print(f'Notification sent to {user.name} : {message}')
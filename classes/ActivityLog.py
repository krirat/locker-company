from LogEvent import LogEvent

class ActivityLog :
    def __init__(self):
        self.logs : list[LogEvent] = []

    def log_event(self, user, locker, event, timestamp):
        log_entry = LogEvent(user, locker, event, timestamp)
        self.logs.append(log_entry)
        print(f"Event logged : {event} for Locker {locker.lockerNumber} by {user.name}.")

    def get_logs_for_user(self, user):
        return [log for log in self.logs if log.user == user]
    
    def get_logs_for_locker(self, locker):
        return [log for log in self.logs if log.locker == locker]
    
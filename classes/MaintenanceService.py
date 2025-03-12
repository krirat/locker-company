from Locker import Locker

class MaintenanceService:
    def perform_maintenance(self, locker: Locker):
        locker.status = "Under Maintenance"
        print(f"Performed maintenance on Locker {locker.lockerNumber}.")

    def check_locker_for_maintenance(self):
        print("Checking lockers for maintenance.")

    def update_locker_status(self, locker: Locker, status):
        locker.status = status
        print(f"Locker {locker.lockerNumber} status updated to {status}.")
        
class MaintenanceService:
    def perform_maintenance(self, locker):
        locker.status = "Under Maintenance"
        print(f"Performed maintenance on Locker {locker.lockerNumber}.")

    def check_locker_formaintenance(self):
        print("Checking lockers for maintenance.")

    def update_locker_status(self, locker, status):
        locker.status = status
        print(f"LOcker {locker.lockerNumber} status updated to {status}.")
        
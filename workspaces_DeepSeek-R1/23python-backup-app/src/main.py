import os
import sys
from backup_module.backup import BackupManager
from backup_module.restore import RestoreManager

def main():
    backup_manager = BackupManager()
    restore_manager = RestoreManager()

    while True:
        print("\nOptions:")
        print("1. Save an object")
        print("2. List backups")
        print("3. Restore an object")
        print("4. List restored objects")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            obj = input("Enter the object to save (as a string): ")
            filename = input("Enter the filename to save the object: ")
            backup_manager.save_object(obj, filename)
            print(f"Object saved as {filename}")

        elif choice == '2':
            backups = backup_manager.list_backups()
            print("Saved backups:")
            for backup in backups:
                print(backup)

        elif choice == '3':
            filename = input("Enter the filename to restore the object: ")
            restored_object = restore_manager.restore_object(filename)
            print(f"Restored object: {restored_object}")

        elif choice == '4':
            restored_objects = restore_manager.list_restored_objects()
            print("Restored objects:")
            for restored in restored_objects:
                print(restored)

        elif choice == '5':
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
import argparse
from backup.save import save_object
from backup.restore import restore_object

def main():
    parser = argparse.ArgumentParser(description="Backup and restore Python objects.")
    parser.add_argument('action', choices=['save', 'restore'], help="Action to perform: save or restore")
    parser.add_argument('file', help="File path for saving or restoring the object")
    parser.add_argument('--object', help="Python object to save (in string format)", default=None)

    args = parser.parse_args()

    if args.action == 'save':
        if args.object is None:
            print("Error: --object argument is required when saving.")
            return
        # Assuming the object is passed as a string representation of a Python literal
        try:
            obj = eval(args.object)
            save_object(obj, args.file)
            print(f"Object saved to {args.file}")
        except Exception as e:
            print(f"Error saving object: {e}")

    elif args.action == 'restore':
        try:
            obj = restore_object(args.file)
            print(f"Object restored from {args.file}: {obj}")
        except Exception as e:
            print(f"Error restoring object: {e}")

if __name__ == "__main__":
    main()
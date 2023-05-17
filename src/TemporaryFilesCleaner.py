import os
import shutil
# Directories to be searched for temporary files.
temp_directories = [
    '/Library/Caches',
    '/Library/Logs',
    '/Downloads',
]
# File extensions to be removed.
extensions = [
    '.pkg',
    '.cache',
    '.dmg',
    '.tmp',
    '.log'
]
for directory in temp_directories:
    for dirpath, dirnames, filenames in os.walk(os.path.expanduser(directory)):
        for filename in filenames:
            # Check if the file extension is in the list of extensions to be removed.
            if os.path.splitext(filename)[1].lower() in extensions:
                filepath = os.path.join(dirpath, filename)
                try:
                    if os.path.isfile(filepath):
                        os.remove(filepath)
                    elif os.path.isdir(filepath):
                        shutil.rmtree(filepath)
                    print(f"Removed {filepath}.")
                except Exception as e:
                    print(f"Error deleting {filepath}: {e}.")
    if directory == '/Desktop':
        desktop_path = os.path.expanduser(directory)
        screenshot_files = [f for f in os.listdir(desktop_path) if f.startswith('Screenshot')]
        for file in screenshot_files:
            filepath = os.path.join(desktop_path, file)
            try:
                os.remove(filepath)
                print(f"Removed {filepath}.")
            except Exception as e:
                print(f"Error deleting {filepath}: {e}.")

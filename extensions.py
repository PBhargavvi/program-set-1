media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

file_name = input("Please enter the name of the file: ").strip().lower()

file_extension = None

if "." in file_name:
    file_extension = file_name[file_name.rfind("."):]

media_type = media_types.get(file_extension, "application/octet-stream")
print(media_type)
file_name = input("file name: ").strip().lower()


if file_name.endswith(".gif"):
    print("image/gif")


elif file_name.endswith(".jpg") or file_name.endswith("jpeg"):
    print("image/jpg")


elif file_name.endswith(".txt"):
    print("text/plain")


elif file_name.endswith(".png"):
    print("image/png")


elif file_name.endswith(".zip"):
    print("application/zip")


elif file_name.endswith(".pdf"):
    print("application/pdf")


else:
    print("applisation/octet-stram")
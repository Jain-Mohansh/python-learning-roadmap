# Handle file-not-found errors
try:
    file = open("data.txt", "r")
    file.close()
except FileNotFoundError:
    print("File not found") 
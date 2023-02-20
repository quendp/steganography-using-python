def access_file (filename):

    with open(str(filename), "r") as f:

        with open("file_logs.txt", "a") as g:
            g.write("\n" + f.read())

filename = input("Enter Filename: ")

access_file (filename)
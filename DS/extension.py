filename = input("Input the Filename: ")
l= filename.split('.')
dict={
    "py":"Python",
    "c":"c",
    "cpp":"c++",
    "exe":"excutalble",
    "pdf":"Pdf",
    "docx":"Document",
    "odt":"Document",
    "doc":"Document"
}

print("The extension of the file is :",dict[l[1]])
try:
    file1 = open("test.txt","r")
    read_content = file1.read()
    print(read_content)

finally:
    #cerrar el archivo
    file1.close()

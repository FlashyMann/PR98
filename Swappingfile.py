def swapFileData():
    data_a=input("Enter the file name 1 ")
    with open("file1",'r') as a:
        data_a=a.read
    with open("file1",'w') as a:
        a.write(data_b)
    data_b=input("Enter the file name 2   ")
    with open("file2",'r') as b:
        data_b=b.read
    with open("file2",'w') as b:
        b.write(data_a)
swapFileData()

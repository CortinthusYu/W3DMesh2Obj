import os
def ForSpecificFileInRootDir(process_function,file_type='*.*'):
    items = os.listdir(".")
    file_list = []
    for names in items:
        if names.endswith(file_type):
           file_list.append(names)

    print(FileList)
    for file in file_list:
        process_function(file)

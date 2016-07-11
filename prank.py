import os

def rename_files():
    file_list = os.listdir("/Users/AmmY/Downloads/prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir("/Users/AmmY/Downloads/prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(str.maketrans("0123456789","          ")))

    os.chdir(saved_path)
    print (os.listdir("/Users/AmmY/Downloads/prank"))
rename_files()
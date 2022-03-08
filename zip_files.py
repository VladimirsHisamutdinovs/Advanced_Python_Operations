import zipfile

zip_file = zipfile.ZipFile("zip_archive.zip", "w")
zip_file.write("textfile_for_zip_01")
zip_file.write("textfile_for_zip_02")
zip_file.write("textfile_for_zip_03")


# print(zipfile.is_zipfile("zip_archive.zip"))

# zip_file = zipfile.ZipFile("zip_archive.zip")
# print(zip_file.namelist())
# print(zip_file.infolist())

# zip_info = zip_file.getinfo("textfile_for_zip_02")
# print(zip_info.file_size)
# print(zip_file.read("textfile_for_zip_01"))

zip_file.extract("textfile_for_zip_02")
zip_file.extractall()


zip_file.close()
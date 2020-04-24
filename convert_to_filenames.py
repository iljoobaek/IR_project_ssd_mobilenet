import sys
import os
directory     = sys.argv[1]
file_name_dir = sys.argv[2]
entries       = os.listdir(directory)
write_file    = open(file_name_dir, "w")
for entry in entries:
    write_file.write(str(entry)+"\n")
    print(entry)
write_file.close()

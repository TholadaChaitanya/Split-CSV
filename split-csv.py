import os

file_path = 'file.csv'
part_size = 50 * 1024 * 1024  # 50 MB in bytes
file_size = os.path.getsize(file_path)
file_name = file_path.rsplit('.csv', 1)[0]

if file_size > part_size:
    with open(file_path, 'r') as file:
        header = file.readline()
        part_num = 1
        bytes_written = 0

        part_file_name = f"{file_name}_part_{part_num}.csv"
        part_file = open(part_file_name, 'w')
        part_file.write(header)
        print(f"Created {part_file_name}")

        for line in file:
            part_file.write(line)
            bytes_written += len(line)

            if bytes_written >= part_size:
                part_file.close()
                part_num += 1
                part_file_name = f"{file_name}_part_{part_num}.csv"
                part_file = open(part_file_name, 'w')
                part_file.write(header)
                print(f"Created {part_file_name}")
                bytes_written = 0

        part_file.close()

else:
    print("File size is less than or equal to 50 MB, no action taken.")

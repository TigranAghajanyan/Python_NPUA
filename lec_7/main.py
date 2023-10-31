while True:
    try:
        file_name = input("Enter the name of the text file you want to open: ")
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:\n", content)
        break
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
    except ValueError:
        print("ValueError: Please enter a valid filename.")
    except PermissionError:
        print("PermissionError: Permission denied ",file_name)

while True:
    try:
        write_option = input("Do you want to write to the same file? (yes/no): ").lower()
        if write_option == 'yes':
            with open(file_name, 'a') as file:
                new_content = input("Enter the content you want to write: ")
                file.write(new_content)
                print("Content has been successfully added to the file.")
        elif write_option == 'no':
            new_file_name = input("Enter the name of the new text file: ")
            with open(new_file_name, 'w') as file:
                new_content = input("Enter the content you want to write: ")
                file.write(new_content)
                print("Content has been successfully written to the new file.")
        else:
            print("Invalid option. Please enter 'yes' or 'no'.")
        break
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File has been closed.")

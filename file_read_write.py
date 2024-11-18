

def read_and_write_file(input_filename, output_filename):
    try:
     
        with open(input_filename, 'r') as file:
            content = file.read()
            
            modified_content = content.upper()

        
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        print(f"File has been read and the modified content is saved to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print("Error: An issue occurred while reading or writing the file.")

def get_filename_and_run():
   
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to write to: ")
  
    read_and_write_file(input_filename, output_filename)

if __name__ == "__main__":
  
    get_filename_and_run()

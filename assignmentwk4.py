def read_and_modify_file():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read from: ")

        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (example: make all text uppercase)
        modified_content = content.upper()

        # Generate output filename
        output_filename = "modified_" + input_filename

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File successfully modified and saved as '{output_filename}' 🎉")

    except FileNotFoundError:
        print("❌ Error: The file was not found. Please check the name and try again.")
    except IOError:
        print("❌ Error: The file could not be read or written. Check your permissions.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# Run the function
read_and_modify_file()

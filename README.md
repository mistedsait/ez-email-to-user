# Email to Username Converter

This Python script allows you to convert email:password pairs to username:password format by removing the domain. The script utilizes the `tkinter` module for the graphical user interface (GUI) and file handling operations.

## Prerequisites

- Python 3 installed on your computer. You can download it from the official Python website: https://www.python.org/downloads/

## Usage

1. Clone the repository or download the script file (`email_to_username_converter.py`) to your local machine.

2. Ensure that the `tkinter` module is available in your Python installation. `tkinter` is usually included with Python by default. If not, please refer to the Python documentation for instructions on installing `tkinter` for your operating system.

3. Run the script by executing the following command:

   ```bash
   python email_to_username_converter.py
   
4.The script will open a graphical user interface (GUI) window.

5.Click the "Start" button to begin the conversion process.

6.Select the text file containing email:password pairs using the file dialog window.

7.The script will process the file and create a new file with the converted username:password pairs. The new file will have the suffix "_username.txt" appended to the original file name.

8.A message will be displayed in the GUI indicating the file path of the generated username:password combolist.

9.Click the "Exit" button to close the GUI and exit the program.

##Example
Suppose you have a text file named input.txt with the following content:
      ```bash
      john.doe@example.com:pa$$w0rd1
      jane.smith@example.com:securepass
Running the script and selecting input.txt using the file dialog will generate a new file named input_username.txt with the following content:

      ```bash
      john.doe:pa$$w0rd1
      jane.smith:securepass
The domain (@example.com) is removed from the email addresses, resulting in the username:password format.

##Limitations
The script assumes that each line in the input file follows the email:password format without any variations. It does not perform any validation or error handling for incorrect formats.

The script uses the tkinter module for the GUI. Ensure that tkinter is properly installed to run the script without any issues.

##Contributing
Contributions to this script are welcome! If you would like to contribute, please fork the repository, make your changes, and submit a pull request.

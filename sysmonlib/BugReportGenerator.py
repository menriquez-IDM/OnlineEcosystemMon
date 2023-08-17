import traceback
import string
import datetime

    
def generate_valid_filename(str):
    """
    Generates a valid file name from a given string.

    Args:
        str (str): The input string to generate a valid file name from.

    Returns:
        filename (str): The valid file name generated from the input string.
    """
    # Remove invalid characters from the string
    
    
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in str if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    return filename

        

def generate_bug_report( exception, property_site, title):
    """
    Generates a bug report file based on the provided exception, property site, and title.

    Args:
        property_site (str): The property site related to the bug report.
        title (str): The title of the bug report.

    Prints:
        str: The path of the generated bug report file.

    Writes:
        File: The bug report template to a file.

    Returns:
        None
    """
    # Extract relevant information from the exception
    exception_type = type(exception).__name__
    exception_message = str(exception)
    traceback_info = traceback.format_exc()

    # Create the bug report template
    bug_report_template = f"""<h1>Issue Report:</h1>
    <h2>Property Site:</h2>{property_site} 
    <h2>Title:</h2>{title}
    <h2>Exception Type:</h2>{exception_type}
    <h2>Exception Message: </h2>```\n{exception_message}\n```
    <h2>Traceback:</h2>```\n{traceback_info}\n```
    <h2>Date: </h2>{datetime.datetime.now()}                  
    """

    # Save the bug report to a file
    name = generate_valid_filename(title)
    file_path = f"./tests/{name}.log"
    
    with open(file_path, "w") as bug_report_file:
        bug_report_file.write(bug_report_template)

    print(f"Bug report generated and saved to {file_path}")
    

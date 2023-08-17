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

        

def generate_bug_report( exception, property_site, title, email_to="minerva.enriquez@gatesfoundation.org"):
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
    bug_report_template = f"""# Issue Report:
    \n## Property Site:\n{property_site} 
    \n### Title:        \n{title}
    \n## Exception Type:\n{exception_type}
    \n## Exception Message: \n```\n{exception_message}\n```
    \n## Traceback:       \n```\n{traceback_info}\n```
    \n## Date:            \n{datetime.datetime.now()}                  
    """
    
    email_template = f"""
    {email_to}\n
    Issues with: {property_site} site \n
    <h1>Issue Report:</h1>
    <h2>Issue:</h2>{title}
    <br>Please note, a bug has been created for your issue. Once the issue has been resolved, please make sure it is closed.<br>
    <h2>Traceback:</h2><br> {traceback_info}
    <h4>Date: </h4> {datetime.datetime.now()}                  
    """

    # Save the bug report to a file
    name = generate_valid_filename(title)
    bug_file = f"./tests/{name}.log"
    email_body = f"./tests/{name}email.txt"
    
    with open(bug_file, "w") as bug_report_file:
        bug_report_file.write(bug_report_template)
        
    with open(email_body, "w") as email_body_file:
        email_body_file.write(email_template)


    print(f"Bug report generated and saved to {bug_file}")
    

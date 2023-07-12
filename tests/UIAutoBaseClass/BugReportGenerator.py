import traceback
import string
import datetime

class BugReportGenerator:
    def __init__(self, exception):
        """
        Initializes the BugReportGenerator class with the given exception.

        Args:
            exception (Exception): The exception to generate a bug report for.
        """
        self.exception = exception

    def generate_bug_report(self, property_site, title):
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
        exception_type = type(self.exception).__name__
        exception_message = str(self.exception)
        traceback_info = traceback.format_exc()

        # Create the bug report template
        bug_report_template = f"""# Issue Report:
        \n## Property Site:\n{property_site} 
        \n### Title:        \n{title}
        \n## Exception Type:\n{exception_type}
        \n## Exception Message: \n{exception_message}
        \n## Traceback:       \n{traceback_info}
        \n## Date:            \n{datetime.datetime.now()}                  
        """

        # Save the bug report to a file
        name = BugReportGenerator.generate_valid_filename(title)
        file_path = f"./{name}.txt"
        
        with open(file_path, "w") as bug_report_file:
            bug_report_file.write(bug_report_template)

        print(f"Bug report generated and saved to {file_path}")
        
        
    def generate_valid_filename(s):
        """
        Generates a valid file name from a given string.

        Args:
            string (str): The input string to generate a valid file name from.

        Returns:
            str: The valid file name generated from the input string.
        """
        # Remove invalid characters from the string
        
        
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        filename = ''.join(c for c in s if c in valid_chars)
        filename = filename.replace(' ','_') # I don't like spaces in filenames.
        return filename
    
            
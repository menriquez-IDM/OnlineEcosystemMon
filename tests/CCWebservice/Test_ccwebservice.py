import requests
from sysmonlib import BugReportGenerator as bug
#  Proxy:       http://10.24.46.30/api/
#  WebService:  http://10.24.46.20:8083 


headers = {'Content-Type': 'application/json'}

def check_service_status(url, timeout=5):
    print(f"\n\nChecking service status...\n\t{url}")
    try:
        response = requests.get(url, timeout=timeout, headers=headers, verify=False)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            print("Service is up and running!", response.status_code)
            print("\nRESPONSE: \n",response.text)
        else:
            print(f"Service returned a non-OK status code: {response.status_code}")
    except requests.ConnectionError:
        print("ALERT!!! Service is down or unreachable...\t", url)
        bug.generate_bug_report(requests.ConnectionError, url, url.split('?')[0] + " Service is down or unreachable")
    except Exception as e:
        print(f"An error occurred: {e}")
        bug.generate_bug_report(e, url, "An error occurred")
    
if __name__ == "__main__":
    # service_url = "http://10.24.46.20:8083?v=2&image_name=nyu/dtk" 
    service_url = "http://10.24.46.20:8087?v=2&image_name=nyu/dtk"  # TESTING EMAILS
    check_service_status(service_url)
    
    proxy_url = "http://10.24.46.30/api/?v=2&search_name="
    check_service_status(proxy_url)



    

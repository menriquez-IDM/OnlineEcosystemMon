import os
import subprocess

# Add the Google Chrome repository
chrome_repo = '''
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl.google.com/linux/linux_signing_key.pub
'''
with open('/etc/yum.repos.d/google-chrome.repo', 'w') as repo_file:
    repo_file.write(chrome_repo)

# Update the system and install Google Chrome
subprocess.run([ 'yum', 'update', '-y'])
subprocess.run([ 'yum', 'install', '-y', 'google-chrome-stable'])
import os
import platform
import subprocess
import urllib.request
import zipfile


def install_chrome_linux():
    # Download Chrome package
    url = "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
    urllib.request.urlretrieve(url, "google-chrome-stable_current_amd64.deb")

    # Install Chrome package
    subprocess.run(["sudo", "dpkg", "-i", "google-chrome-stable_current_amd64.deb"])
    subprocess.run(["sudo", "apt-get", "-f", "install", "-y"])


def install_chrome_mac():
    # Download Chrome package
    url = "https://dl.google.com/chrome/mac/stable/GGRO/googlechrome.dmg"
    urllib.request.urlretrieve(url, "googlechrome.dmg")

    # Mount and install Chrome package
    subprocess.run(["hdiutil", "attach", "googlechrome.dmg"])
    subprocess.run(["sudo", "cp", "-R", "/Volumes/Google Chrome/Google Chrome.app", "/Applications"])

    # Unmount the disk image
    subprocess.run(["hdiutil", "detach", "/Volumes/Google Chrome"])


def install_chromedriver_linux():
    # Download ChromeDriver
    url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    response = urllib.request.urlopen(url)
    version = response.read().decode().strip()

    chromedriver_url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_linux64.zip"
    urllib.request.urlretrieve(chromedriver_url, "chromedriver.zip")

    # Extract and install ChromeDriver
    with zipfile.ZipFile("chromedriver.zip", "r") as zip_ref:
        zip_ref.extractall(".")
    
    os.chmod("chromedriver", 0o755)
    subprocess.run(["sudo", "mv", "chromedriver", "/usr/local/bin/chromedriver"])


def install_chromedriver_mac():
    # Download ChromeDriver
    url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
    response = urllib.request.urlopen(url)
    version = response.read().decode().strip()

    chromedriver_url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_mac64.zip"
    urllib.request.urlretrieve(chromedriver_url, "chromedriver.zip")

    # Extract and install ChromeDriver
    with zipfile.ZipFile("chromedriver.zip", "r") as zip_ref:
        zip_ref.extractall(".")
    
    os.chmod("chromedriver", 0o755)
    subprocess.run(["sudo", "mv", "chromedriver", "/usr/local/bin/chromedriver"])


def main():
    current_os = platform.system()
    
    if current_os == "Linux":
        install_chrome_linux()
        install_chromedriver_linux()
    elif current_os == "Darwin":
        install_chrome_mac()
        install_chromedriver_mac()
    else:
        print("Unsupported operating system.")


if __name__ == "__main__":
    main()

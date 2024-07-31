import urllib.request as urllib

print("Site connectivity checker")
input_URL = input("Enter URL: ")

def main(url):
    print("Checking connectivity.....")

    response = urllib.urlopen(url)
    print("Connected to", url, "succesfully")
    print("Response Code: ", response.getcode())

main(input_URL)

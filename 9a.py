import requests  # Import the requests library for making HTTP requests.
import os       # Import the os library for file and directory operations.
import bs4      # Import the BeautifulSoup library for parsing HTML.

url = 'http://xkcd.com'  # Set the initial URL to the XKCD comic website.
os.makedirs('xkcd2', exist_ok=True)  # Create a directory named 'xkcd2' if it doesn't exist to store downloaded comics.

while True:  # Start an infinite loop for downloading comics.

    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)  # Send an HTTP GET request to the current URL.
    res.raise_for_status()   # Check if the request was successful or raise an exception if not.
    soup = bs4.BeautifulSoup(res.text, 'html.parser')  # Parse the HTML content of the page using BeautifulSoup.

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')  # Select the 'img' element inside an element with the id 'comic'.
    if not comicElem:  # Check if the 'img' element was found.
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')  # Construct the URL of the comic image.

        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)  # Send an HTTP GET request to the comic image URL.
        res.raise_for_status()         # Check if the request was successful or raise an exception if not.

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd2', os.path.basename(comicUrl)), 'wb')  # Open a binary file to write the image data.
        for chunk in res.iter_content(100000):  # Iterate over the content of the HTTP response in chunks.
            imageFile.write(chunk)  # Write each chunk to the image file.
        imageFile.close()  # Close the image file.

    # Get the Prev button's URL.
    prevLink = soup.select('a[rel="prev"]')  # Select the 'a' element with a 'rel' attribute set to 'prev'.
    if not prevLink:  # Check if the 'prev' link was found.
        print('No more comics to download.')
        break  # Exit the loop if there are no more comics to download.
    else:
        url = 'http://xkcd.com' + prevLink[0].get('href')  # Set the URL to the 'href' attribute of the 'prev' link.

print('Done.')  # Print 'Done' when all comics have been downloaded.

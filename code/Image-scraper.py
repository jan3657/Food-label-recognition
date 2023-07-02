import requests
from bs4 import BeautifulSoup
import os

# Define the URL of the search results page
counter = 1808
url = "https://world.openfoodfacts.org/cgi/search.pl?action=process&search_terms=bio&sort_by=unique_scans_n&page_size=100&page="
for i in range(20, 30):
    url += str(i)
    # Send a GET request to the search results page
    response = requests.get(url)

    # Parse the HTML content using BeautifuslSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Create a directory to store the images
    os.makedirs("product_images", exist_ok=True)

    # Find all product links on the page
    product_links = soup.find_all("a", href=True)

    # Visit each product page and scrape the images
    for link in product_links:
        if link["href"].startswith("/product/"):
            # Get the URL of the product page
            product_url = "https://world.openfoodfacts.org" + link["href"]

            # Send a GET request to the product page
            product_response = requests.get(product_url)

            # Parse the HTML content of the product page
            product_soup = BeautifulSoup(product_response.content, "html.parser")

            # Find the main product image on the page
            image_tags = product_soup.select('img[src*="front"][src$=".full.jpg"]')

            # Skip if no image found
            if not image_tags:
                continue

            for img in image_tags:
                # Get the image URL
                image_url = img["src"]

                # Download the image
                image_response = requests.get(image_url)

                # Get the file name from the URL
                filename = str(counter)+image_url.split("/")[-1]
                counter += 1

                # Save the image to the product_images directory
                with open(os.path.join("product_images", filename), "wb") as file:
                    file.write(image_response.content)

                print(f"Downloaded: {filename}")

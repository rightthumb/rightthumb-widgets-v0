import requests
from bs4 import BeautifulSoup

# Define the input and output file paths
input_file = "/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/Scrolls/_docs_/_YouTube/mp3/songs.md"
output_file = "/home/rightthumb/public_html/domains/eyeformeta.com/public_html/apps/Scrolls/_docs_/_YouTube/mp3/queue.md"

# Function to search Google and get the first YouTube video URL
def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.1234.56 Safari/537.36"
    }
    
    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        
        for link in links:
            href = link.get('href')
            if href and "youtube.com/watch" in href:
                return href
    except Exception as e:
        print(f"Error searching Google: {e}")
    return None

# Main function to process the input file and write results to the output file
def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
        for line in infile:
            line = line.strip()  # Remove leading/trailing whitespace
            
            if line:  # Skip empty lines
                query = f"{line} youtube official video"
                youtube_url = search_google(query)
                if youtube_url:
                    outfile.write(f"{line} {youtube_url}\n")
                    print(f"Found YouTube URL for '{line}': {youtube_url}")

def clear_input_file():
    global input_file
    try:
        with open(input_file, 'w') as file:
            file.truncate(0)  # Truncate the file to remove its contents
        print(f"Cleared contents of '{input_file}'")
    except Exception as e:
        print(f"Error clearing '{input_file}': {e}")

# Usage:
# clear_input_file(input_file)

if __name__ == "__main__":
    process_file(input_file, output_file)
    clear_input_file()

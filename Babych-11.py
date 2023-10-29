import requests

def search_gifs(search_term):

  giphy_api_key = "44arVi5NLMyl8wEMIhOjX3CZYBboakxs"

  # Make a request to the Giphy API
  response = requests.get(
      f"https://api.giphy.com/v1/gifs/search?api_key={giphy_api_key}&q={search_term}"
  )

  # Check if the request was successful
  if response.status_code != 200:
    raise Exception("Giphy API request failed")

  # Parse the JSON response
  json_response = response.json()

  # Extract the GIF information from the JSON response
  gifs = []
  for gif_data in json_response["data"]:
    gif = {
      "title": gif_data["title"],
      "url": gif_data["images"]["original"]["url"],
    }
    gifs.append(gif)

  return gifs

def main():
  # Get the search term from the user
  search_term = input("Enter a search term: ")

  # Search for GIFs using the Giphy API
  gifs = search_gifs(search_term)

  # Print the links to the GIFs
  for gif in gifs:
    print(gif["url"])

if __name__ == "__main__":
  main()

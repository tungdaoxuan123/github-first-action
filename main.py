import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.json()  # Return the response as JSON
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    url = "https://api.github.com/users/tungdaoxuan123"
    data = fetch_data(url)
    
    if data:
        print("User Data:")
        print(f"Username: {data['login']}")
        print(f"Bio: {data['bio']}")
        print(f"Public Repos: {data['public_repos']}")

import requests


def get_chuck_norris_joke():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        response.raise_for_status()
        data = response.json()
        joke = data["value"]
        print(joke)
    except requests.exceptions.RequestException as e:
        print(f"Virhe: Ei voitu hakea vitsiä. {e}")


if __name__ == "__main__":
    get_chuck_norris_joke()

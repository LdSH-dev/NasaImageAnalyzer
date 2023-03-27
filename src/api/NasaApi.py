import requests

class Nasa_API:
    BASE_URL = "https://api.nasa.gov"
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def _make_request(self, url, params=None):
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to make request. Status code: {response.status_code}")
    
    def get_image_of_the_day(self, date=None, hd=False, save_path=None):
        url = f"{self.BASE_URL}/planetary/apod"
        params = {"api_key": self.api_key}

        if date is not None:
            params["date"] = date

        if hd:
            params["hd"] = True

        response = requests.get(url, params=params)

        if response.status_code == 200:
            apod_data = response.json()
            image_url = apod_data["url"]

            image_response = requests.get(image_url)

            with open(f"../../data/{apod_data['date']}.jpg", "wb") as f:
                f.write(image_response.content)

            with open(f"../../data/{apod_data['date']}-modified.jpg", "wb") as f:
                f.write(image_response.content)


        else:
            raise Exception(f"Failed to make request. Status code: {response.status_code}")


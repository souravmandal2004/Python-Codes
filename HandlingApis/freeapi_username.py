import requests

def fetch_random_user ():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    # Call the api and take the response and convert it to json format
    response = requests.get (url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        print (f"User name: {user_name}")
    
    else:
        raise Exception ("Failed to fetch user data")

def main ():
    try:    
        fetch_random_user ()
    except Exception as e:
        print (e)

if __name__ == "__main__":
    main ()
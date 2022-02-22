import requests

if __name__ == '__main___':
    url = 'https://i.redd.it/f5o9vho2v5t61.jpg'

    response =  requests.get(url, stream=True)
    with open('image.jpg', 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)

    response.close()

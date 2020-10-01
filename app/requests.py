import urllib.request,json

from .models import Categories,Images

def configure_request(app):
    global api_key,ret
    api_key = app.config['API_KEY']
    base_url = app.config['BASE_URL']

def get_image(category):
    get_image_url = base_url.format(api_key,category)

    with urllib.request.urlopen(get_image_url) as url:
        get_image_data = url.read()
        get_image_response = json.loads(get_image_data)

        image_results = None

        
        image_results = process_results(get_image_response)
        print(image_results)

    return image_results

def process_results(image_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    image_results = []
    for image_item in image_list:
        id = image_item.get('id')
        image = image_item.get('imageURL')
        title = news_item.get('user')

        image_object = Images(id,image,title)
        image_results.append(image_object)

    return image_results
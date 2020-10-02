import urllib.request, json
from .models import Image

# getting api key
api_key = None

# gettingbase url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['IMAGE_API_KEY']
    base_url = app.config['IMAGE_API_BASE_URL']


def get_images(category):
    get_images_url = base_url.format(api_key, category)

    with urllib.request.urlopen(get_images_url) as url:
        get_images_data = url.read()
        get_images_response = json.loads(get_images_data)

        image_results = None

        if get_images_response['hits']:
            image_results_list = get_images_response['hits']
            image_results = process_results(image_results_list)

    return image_results


def process_results(image_list):
    image_results = []
    for image_item in image_list:

        id = image_item.get('id')
        webformaturl = image_item.get('webformatURL')

        if webformaturl:
            image_object = Image(id, webformaturl)
            image_results.append(image_object)
    return image_results



def search_image(search_term):
    search_image_url = 'https://pixabay.com/api/?key={}&q={}&image_type=photo&pretty=true'.format(api_key, search_term)

    with urllib.request.urlopen(search_image_url) as url:
        search_image_data = url.read()
        search_image_response = json.loads(search_image_data)

        search_image_results = None

        if search_image_response['hits']:
            search_image_list = search_image_response['hits']
            search_image_results = process_results(search_image_list)

    return search_image_results




def process_search(search_list):
    image_results = []
    for image_item in search_list:

        id = image_item.get('id')
        webformaturl = image_item.get('webformatURL')

        if webformaturl:
            image_object = Image(id, webformaturl)
            image_results.append(image_object)
    return image_results
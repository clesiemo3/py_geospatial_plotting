import requests
import os

ROOT_URL = 'https://www2.census.gov/geo/tiger/GENZ2018'


def get_url(type='shp', entity='county', resolution='20m'):
    """
    Builds a URL for census.gov to download geospatial files.
    :param type: shp (default) or kml
    :param entity: state, county, or any other census entity
    :param resolution: 20m, 5m, or 500k
    :return: str url for census download
    """
    return f'{ROOT_URL}/{type}/cb_2018_us_{entity}_{resolution}.zip'


def download(url):
    file_name = url.split('/')[-1]
    path_name = '/'.join(os.path.abspath(__file__).split('/')[:-2])
    full_path = f'{path_name}/data/{file_name}'

    if os.path.exists(full_path):
        print(f'{file_name} already exists. Skipping download.')
    else:
        r = requests.get(url)
        r.raise_for_status()
        with open(full_path, 'wb') as f:
            f.write(r.content)

    return


if __name__ == '__main__':
    download(get_url('shp', 'county', '500k'))
    download(get_url('shp', 'county', '5m'))
    download(get_url('shp', 'county', '20m'))

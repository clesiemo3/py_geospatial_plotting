import requests
import os

ROOT_URL = 'https://www2.census.gov/programs-surveys/popest/geographies'


def get_url(year=2018, name='state-geocodes'):
    """
    Builds a URL for census.gov to download reference files.
    :param year: year of data
    :param name: state-geocodes
    :return: str url for census download
    """

    return f'{ROOT_URL}/{year}/{name}-v{year}.xlsx'


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
    download(get_url(2018, 'state-geocodes'))

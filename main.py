import json

def json_file_to_dict(file_path: str) -> dict:
    '''convert json to dict
    
    Args:
        file_path (str): file path.
        
    Returns:
        dict: dict data
    '''
    data = open(file_path).read()
    data_dict = json.loads(data)

    return data_dict

data_dict = json_file_to_dict('data.json')

def get_number_of_users(data: dict) -> int:
    '''all users' data.
    
    Args:
        data (dict): users data
    
    Returns:
        int: number of all users.
    '''
    return len(data['users'])


def get_all_countries(data: dict) -> list:
    '''all users' data.
    
    Args:
        data (dict): users data
    
    Returns:
        list: list of counrties
    '''
    countries = []
    users = data['users']
    for user in users:
        countries.append(user['country'])
    return countries


def get_all_users_fullname(data: str) -> list:
    '''all users' full name.
    
    Args:
        data (dict): users data
    
    Returns:
        list: list of all users' full name
    '''
    full_names = []
    for user in data['users']:
        full_name = user['first_name'] + ' ' + user['last_name']
        full_names.append(full_name)
        
    return full_names

print(get_all_users_fullname(data_dict))


def get_user_by_id(id: int) -> dict:
    '''get user by id
    
    Args:
        id (int): user id.
        
    Returns:
        dict: user data
    '''
    return


def get_user_by_firstname(first_name: str) -> dict:
    '''get user by first name
    
    Args:
        first_name (str): user's first name.
        
    Returns:
        dict: user data
    '''
    return


def get_user_by_lastname(last_name: str) -> dict:
    '''get user by last name
    
    Args:
        first_name (str): user's last name.
        
    Returns:
        dict: user data
    '''
    return


def get_user_by_country(country: str) -> dict:
    '''get user by country
    
    Args:
        country (str): name of user's country.
        
    Returns:
        dict: user data
    '''
    return


import os
import re


def data_folder():
    """Returns the /.../data/ folder path."""
    return os.path.join(os.getcwd(), 'data')


def users_folder():
    """Returns the /.../data/users/ folder path."""
    return os.path.join(data_folder(), 'users')


def dir_exists(directory):
    """Returns True if the data folder exists."""
    return os.path.exists(directory)


def make_sure_data_dir_exists():
    """Creates the data/ folder if it does not already exist."""
    if not dir_exists(data_folder()):
        os.mkdir(data_folder())
        print('Created the data folder')


def make_sure_users_dir_exists():
    """Creates the data/users/ folder if it does not already exist."""
    make_sure_data_dir_exists()

    if not dir_exists(users_folder()):
        os.mkdir(users_folder())
        print('Created the users folder')


def create_new_user_folder(username):
    user_name = convert_username_to_store(username)
    make_sure_users_dir_exists()

    os.mkdir(os.path.join(users_folder(), user_name))


def list_of_users():
    make_sure_users_dir_exists()

    return [convert_username_to_display(user) for user in os.listdir(users_folder())]


def convert_username_to_display(input_name):
    output_list = []
    names = re.split('[_ ]', input_name.lower())

    for name in names:
        name = name.strip()
        if name:
            new_name = name[0].upper()
            if len(name) > 1:
                new_name += name[1:]
            output_list.append(new_name)

    output = ' '.join(output_list)
    return output


def convert_username_to_store(input_name):
    output_list = []
    names = re.split('[_ ]', input_name.lower())

    for name in names:
        name = name.strip()
        if name:
            output_list.append(name)

    output = '_'.join(output_list)

    return output


def user_exists(username):
    make_sure_users_dir_exists()
    user_name = convert_username_to_store(username)

    user_path = os.path.join(users_folder(), user_name)

    return dir_exists(user_path)

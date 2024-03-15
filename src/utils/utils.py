import os


def get_archive_folder(path_folder: str) -> list:
    """
    This method search a folder and return list with path of his archives

    Args:
        path_folder (str): folder path to return its items

    Returns:
        list: list of path for each archive into this folder
    """
    # create an empty list for return
    list_of_items = []
    list_of_paths = []

    # try open with os the folder path
    try:
        list_of_items = os.listdir(path_folder)

    except NotADirectoryError:
        # returns an empty list to identify a wrong path was passed
        return list_of_paths
    except FileNotFoundError:
        # returns an empty list to identify a wrong path was passed
        return list_of_paths

        # if the folder is not empty inflate the list with the paths
    if len(list_of_items) > 0:
        # this for traverse for all the list and append the complete path in the list_of_paths
        for i in list_of_items:
            if '.jpg' in i or 'jpeg' in i:
                list_of_paths.append(path_folder + '\\' + i)
            elif '.png' in i:
                list_of_paths.append(path_folder + '\\' + i)

    # if the list is empty append the list with a 0 to identify
    else:
        list_of_paths.append(0)

    # if the list is empty append the list with a 0 to identify
    if len(list_of_paths) == 0:
        list_of_paths.append(0)

    return list_of_paths

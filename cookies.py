import json
import tempfile
import os

def write_json_to_temp(data, filename):
    """
    This function writes JSON data to a file in the temporary directory of a system.

    Args:
        data: A Python object to be converted into JSON. This can typically be a dictionary or a list.
        filename: The name of the file to which JSON data is written.

    Returns:
        None
    """
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, f"{filename}.json")

    with open(file_path, 'w') as f:
        json.dump(data, f)

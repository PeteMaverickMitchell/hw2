import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.txt$", "", filename)
                for filename in filenames if filename.endswith(".txt")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and html
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.txt"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.txt")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

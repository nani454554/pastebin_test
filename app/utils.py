import random
import string

def generate_unique_id(length=8):
    """Generate a unique identifier for the paste."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

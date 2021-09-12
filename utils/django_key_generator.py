# https://stackoverflow.com/questions/41298963/is-there-a-function-for-generating-settings-secret-key-in-django
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

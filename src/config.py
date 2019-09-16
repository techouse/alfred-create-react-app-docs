# encoding: utf-8


class Config(object):
    # Number of results to fetch from API
    RESULT_COUNT = 9
    # How long to cache results for
    CACHE_MAX_AGE = 20  # seconds
    # Icon
    REACT_ICON = "icon.png"
    GOOGLE_ICON = "google.png"
    # Algolia credentials
    ALGOLIA_APP_ID = "BH4D9OD16A"
    ALGOLIA_SEARCH_ONLY_API_KEY = "3be60f4f8ffc24c75da84857d6323791"
    ALGOLIA_SEARCH_INDEX = "create-react-app"

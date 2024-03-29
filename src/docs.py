#!/usr/bin/python
# encoding: utf-8

from __future__ import print_function, unicode_literals, absolute_import

import functools
import re
import sys
from collections import OrderedDict
from urllib import quote_plus

from algoliasearch.search_client import SearchClient
from config import Config
from workflow import Workflow3, ICON_INFO

# Algolia client
client = SearchClient.create(Config.ALGOLIA_APP_ID, Config.ALGOLIA_SEARCH_ONLY_API_KEY)
index = client.init_index(Config.ALGOLIA_SEARCH_INDEX)

# log
log = None


def cache_key(query):
    """Make filesystem-friendly cache key"""
    key = "{}".format(query)
    key = key.lower()
    key = re.sub(r"[^a-z0-9-_;.]", "-", key)
    key = re.sub(r"-+", "-", key)
    # log.debug("Cache key : {!r} {!r} -> {!r}".format(query, key))
    return key


def handle_result(api_dict):
    """Extract relevant info from API result"""
    result = {}

    for key in {"objectID", "hierarchy", "content", "url", "anchor"}:
        if key == "hierarchy":
            api_dict[key] = OrderedDict(sorted(api_dict[key].items(), reverse=True))
            for hierarchy_key, hierarchy_value in api_dict[key].items():
                if hierarchy_value:
                    result["title"] = hierarchy_value
                    break
        else:
            result[key] = api_dict[key]

    return result


def search(
        query=None, limit=Config.RESULT_COUNT
):
    if query:
        results = index.search(
            query,
            {
                "page": 0,
                "hitsPerPage": limit,
            },
        )
        if results is not None and "hits" in results:
            return results["hits"]
    return []


def main(wf):
    if wf.update_available:
        # Add a notification to top of Script Filter results
        wf.add_item(
            "New version available",
            "Action this item to install the update",
            autocomplete="workflow:update",
            icon=ICON_INFO,
        )

    query = wf.args[0].strip()

    if not query:
        wf.add_item("Search the Create React App docs...")
        wf.send_feedback()
        return 0

    # Parse query into query string and tags
    query = " ".join(query.split(" "))

    # log.debug("query: {!r}".format(query))

    key = cache_key(query)

    results = [
        handle_result(result)
        for result in wf.cached_data(
            key, functools.partial(search, query), max_age=Config.CACHE_MAX_AGE
        )
    ]

    # log.debug("{} results for {!r}".format(len(results), query))

    # Show results
    if not results:
        url = "https://www.google.com/search?q={}".format(quote_plus('"Create React App" {}'.format(query)))
        wf.add_item(
            "No matching answers found", "Shall I try and search Google?",
            valid=True,
            arg=url,
            copytext=url,
            quicklookurl=url,
            icon=Config.GOOGLE_ICON,
        )

    for result in results:
        wf.add_item(
            uid=result["objectID"],
            title=result["title"],
            arg=result["url"],
            valid=True,
            largetext=result["title"],
            copytext=result["url"],
            quicklookurl=result["url"],
            icon=Config.REACT_ICON,
        )
        # log.debug(result)

    wf.send_feedback()


if __name__ == "__main__":
    wf = Workflow3(
        update_settings={
            "github_slug": "techouse/alfred-create-react-app-docs",
            "frequency": 7,
        }
    )
    log = wf.logger
    sys.exit(wf.run(main))

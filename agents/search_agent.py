import os
from agents.query_agent import rewrite_query
from connectors.free_search import free_search


def run_search(query):
    improved_query = rewrite_query(query)

    mouser_key = os.getenv("MOUSER_API_KEY")

    results = free_search(improved_query, mouser_key)

    return results, improved_query

from agents.query_agent import rewrite_query
from connectors.free_search import free_search
from config import MOUSER_API_KEY

def run_search(query):
    improved_query = rewrite_query(query)

    results = free_search(improved_query, MOUSER_API_KEY)

    return results, improved_query

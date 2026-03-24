from connectors.free_search import free_search
from config import MOUSER_API_KEY

def run_search(query):
    return free_search(query, MOUSER_API_KEY)

import requests
from config import OCTOPART_API_KEY

BASE_URL = "https://api.nexar.com/graphql"

def search_components(query):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    graphql_query = {
        "query": """
        query ($q: String!) {
          supSearch(q: $q, limit: 5) {
            results {
              part {
                mpn
                manufacturer { name }
                shortDescription
                specs {
                  attribute { name }
                  displayValue
                }
                sellers {
                  company { name }
                  offers {
                    prices {
                      quantity
                      price
                      currency
                    }
                  }
                }
              }
            }
          }
        }
        """,
        "variables": {"q": query}
    }

    try:
        response = requests.post(
            BASE_URL,
            json=graphql_query,
            headers=headers,
            auth=(OCTOPART_API_KEY, "")
        )

        data = response.json()

        results = []
        for item in data.get("data", {}).get("supSearch", {}).get("results", []):
            part = item["part"]

            results.append({
                "mpn": part.get("mpn"),
                "manufacturer": part.get("manufacturer", {}).get("name"),
                "description": part.get("shortDescription"),
                "specs": part.get("specs"),
                "sellers": part.get("sellers")
            })

        return results

    except Exception as e:
        print("Octopart error:", e)
        return []

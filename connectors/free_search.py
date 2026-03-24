import requests

# --- DIGIKEY MOCK (you'll replace with real auth later) ---
def digikey_search(query):
    # placeholder until you set OAuth
    return []


# --- MOUSER SEARCH ---
def mouser_search(query, api_key):
    url = "https://api.mouser.com/api/v1/search/keyword"

    payload = {
        "SearchByKeywordRequest": {
            "keyword": query,
            "records": 5
        }
    }

    params = {"apiKey": api_key}

    try:
        response = requests.post(url, json=payload, params=params)
        data = response.json()

        results = []

        for part in data.get("SearchResults", {}).get("Parts", []):
            results.append({
                "mpn": part.get("ManufacturerPartNumber"),
                "manufacturer": part.get("Manufacturer"),
                "description": part.get("Description"),
                "source": "Mouser"
            })

        return results
    except:
        return []


# --- AGGREGATOR ---
def free_search(query, mouser_key):
    results = []

    results.extend(mouser_search(query, mouser_key))
    results.extend(digikey_search(query))  # later

    # dedupe
    seen = set()
    unique = []

    for r in results:
        key = (r.get("mpn"), r.get("manufacturer"))
        if key not in seen:
            seen.add(key)
            unique.append(r)

    return unique

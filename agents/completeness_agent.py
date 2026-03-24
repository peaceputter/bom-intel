import json

DEPENDENCIES = {
    "SoC": ["RAM", "Storage", "PMIC"],
    "Battery": ["Charging IC", "Protection IC"],
    "Display": ["Display Driver", "Touch Controller"],
    "WiFi Module": ["Antenna"]
}

def check_completeness(user_components):
    with open("core/ontology.json") as f:
        ontology = json.load(f)

    all_required = []
    for items in ontology.values():
        all_required.extend(items)

    # smarter matching
    missing = [
        c for c in all_required
        if not any(c.lower() in uc.lower() for uc in user_components)
    ]

    dependencies_missing = {}

    for comp in user_components:
        for key in DEPENDENCIES:
            if key.lower() in comp.lower():
                for dep in DEPENDENCIES[key]:
                    if not any(dep.lower() in uc.lower() for uc in user_components):
                        dependencies_missing.setdefault(comp, []).append(dep)

    return missing, dependencies_missing

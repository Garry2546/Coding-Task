import requests
import sys
import json

def fetch_ontology_details(ontology_id, output_format='human'):
    base_url = "https://www.ebi.ac.uk/ols/api/ontologies/"
    url = f"{base_url}{ontology_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()

        if output_format == 'human':
            print(f"Ontology Title: {data['config']['title']}")
            print(f"Description: {data['config']['description']}")
            print(f"Number of Terms: {data['numberOfTerms']}")
            print(f"Status: {data['status']}")
        elif output_format == 'json':
            print(json.dumps(data, indent=4))
    except requests.exceptions.HTTPError as e:
        print(f"Error: Could not retrieve data for ontology ID '{ontology_id}'.", file=sys.stderr)
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while fetching data.", file=sys.stderr)

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <ontology_id> <output_format>", file=sys.stderr)
        sys.exit(1)

    ontology_id = sys.argv[1]
    output_format = sys.argv[2].lower()
    fetch_ontology_details(ontology_id, output_format)

if __name__ == "__main__":
    main()

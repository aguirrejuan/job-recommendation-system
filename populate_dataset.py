from recomendation_system.databases import initialize_or_get_data_chroma
from recomendation_system.databases import populate_chroma

if __name__ == "__main__":
    collection = initialize_or_get_data_chroma()
    populate_chroma(collection)
# app.py
import json
import os
from sentence_transformers import SentenceTransformer
import torch

def load_knowledge_base(file_path):
    # Load the example data from the text file.
    try:
        with open(file_path, 'r') as file:
            json_file = json.load(file)
            print(f"✅ Archivo '{file_path}' cargado correctamente.")
    except json.JSONDecodeError:
        print(f"❌ Error: El archivo '{file_path}' no es un JSON válido. Asegúrate de que el archivo tenga el formato correcto.")
        return
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{file_path}' no se encontró. Asegúrate de que el archivo exista.")
        return
    except Exception as e:
        print(f"❌ Error al cargar el archivo '{file_path}': {e}")
        return
    return json_file

def encode_knowledge_base(model, data, target_field):
    """Encodes the knowledge base data into embeddings using the provided model."""
    embeddings = []
    terms = []
    if target_field == "definitions":
        for i in data:
            term = i.get("term", "no hay término :(")
            if "definitions" in i:
                for dictionary in i["definitions"]:
                    if "def" in dictionary:
                        definition = dictionary["def"]
                        term_def = f"{term}: {definition}"
                        embeddings.append(term_def)

                        terms.append({"id":i.get("id"), "original_term":term, "definition_text": definition, "full_definition":dictionary, "embedded_text": term_def})
        embeddings = model.encode(embeddings, convert_to_tensor=True)
    return embeddings, terms

def find_best_match(user_input, model, embeddings, terms):
    """Retrieval Function: Finds the best match for a user's input against the knowledge base embeddings."""
    # 1. Take the user's input string (e.g., "what does 'jevi' mean?"), the model, and the pre-computed embeddings as input.
    # 2. Encode the user's input into its own embedding using model.encode().
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    # 3. Calculate the similarity between the user's input embedding and all of the knowledge base embeddings. (hint: model.similarity() function)
    similarities = model.similarity(input_embedding, embeddings)
    # 4. Find the highest similarity score and identify which entry in your original data it corresponds to.
    similarities_uno = similarities.squeeze()
    best_match_index = torch.argmax(similarities_uno).item()
    best_match_info = terms[best_match_index]
    return best_match_info


def generate_response(best_match):
    """Generation Function: Generates a response based on the best match found in the knowledge base."""
    # Take the best-matching entry from the knowledge base and construct a detailed prompt.
    # Send this prompt to the Ollama service to get a response.
    # Return the final response.
    if best_match:
        term = best_match.get('original_term', 'el término')
        definition = best_match.get('definition_text', 'No se encontró una definición.')
        example = best_match.get('full_definition', {}).get('ex', 'No se proporcionó ningún ejemplo.')
        english_translation = best_match.get('full_definition', {}).get('en', 'No se proporcionó traducción al inglés.')

        response = (
            f"\tSegún mi base de conocimientos de jerga dominicana:\n\n"
            f"\tEl término '{term}' significa: '{definition}'.\n"
            f"\tEjemplo: '{example}'\n"
            f"\tEn inglés, esto se traduce a: '{english_translation}'.\n"
            f"\t¿Hay algo más que te gustaría saber sobre '{term}' o algún otro término?"
        )
        return response
    else:
        return "Lo siento, no pude encontrar una respuesta relevante en mi base de conocimientos."

def main():
    # 1. Load the model (can stay in main for now)
    # (enhance later - print the 'model' variable)
    try:
        model = SentenceTransformer('all-MiniLM-L6-v2')
        print("✅ Modelo 'all-MiniLM-L6-v2' cargado correctamente.")
    except Exception as e:
        print(f"❌ Error al cargar el modelo 'all-MiniLM-L6-v2': {e}")
        return

    # 2. Load the knowledge bases
    # (enhance later - using '/' as a delimiter to break it up instead of manually like here) Break up the full path to recreate it in a cross-platform way
    path_part1 = 'json-conversion'
    path_part2 = 'vocab'
    filename = 'dominican-slang-example.json'
    slang_file_path = os.path.join(path_part1, path_part2, filename)
    slang_data = load_knowledge_base(slang_file_path)
    print("✅ slang_data is loaded.")
    #habits_data = load_knowledge_base('json-conversion', 'habits', 'dominican-habits.json') # See? Reusable!

    # 3. Create the embeddings for data
    slang_embeddings, slang_term = encode_knowledge_base(model, slang_data, 'definitions')
    #habits_embeddings = encode_knowledge_base(model, habits_data, 'explanation')

    print("✅ Servicio del Chatbot Chamo iniciado. ¡Listo para conversar!")
    print("   Escribe 'salir' para terminar la sesión.")
    print("-" * 50)
    while True:
        try:
            user_input = input("\nTú: ")

            if user_input.lower() == 'salir':
                break

            best_match = find_best_match(user_input, model, slang_embeddings, slang_term)
            response = generate_response(best_match)
            print(f"Chamo: {response}")

        except (KeyboardInterrupt, EOFError):
            break

    print("\n👋 ¡Nos vemos! El servicio del chatbot se está cerrando.")


if __name__ == "__main__":
    main()
# app.py
import json
import os
from sentence_transformers import SentenceTransformer

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
    if not data:
        print(f"❌ Error: No hay datos para codificar en '{target_field}'.")
        return
    if target_field not in data[0]:
        print(f"❌ Error: El campo '{target_field}' no se encuentra en los datos.")
        return

    try:
        sentences = [entry[target_field] for entry in data if target_field in entry]
        embeddings = model.encode(sentences, convert_to_tensor=True)
        print(f"✅ Embeddings para '{target_field}' creados correctamente.")
    except Exception as e:
        print(f"❌ Error al crear embeddings para '{target_field}': {e}")
        return
    return embeddings

def main():
    # 1. Load the model (can stay in main for now)
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

    # 3. Create the embeddings
    slang_embeddings = encode_knowledge_base(model, slang_data, 'definition')
    #habits_embeddings = encode_knowledge_base(model, habits_data, 'explanation')

    # 4. Start the main chat loop
    print("✅ Servicio del Chatbot Chamo iniciado. ¡Listo para conversar!")
    print("   Escribe 'salir' para terminar la sesión.")
    print("-" * 50)
    # while True:
    #     try:
    #         # The input() function pauses the program and waits for the user to type.
    #         user_input = input("Tú: ")

    #         # Check if the user wants to exit the application.
    #         if user_input.lower() == 'salir':
    #             break

    #         # --- Placeholder for Future Logic ---
    #         # In the next steps, all your RAG logic will go here.
    #         # 1. You'll send user_input to the Retriever model.
    #         # 2. You'll get back relevant context from your dictionary.
    #         # 3. You'll build a prompt and send it to the Ollama service.
    #         # 4. You'll print the final response from the Generator model.

    #         # For now, we just echo the input back to show it's working.
    #         print(f"Chamo (dev): Recibí tu mensaje: '{user_input}'")

    #     except (KeyboardInterrupt, EOFError):
    #         # This handles both Ctrl+C and the case where the input stream closes.
    #         break

    # print("\n👋 ¡Nos vemos! El servicio del chatbot se está cerrando.")

if __name__ == "__main__":
    main()
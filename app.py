# app.py
import json
import os

def main():
    """
    Main function to run the chatbot application.
    This function contains an infinite loop that keeps the script running,
    waiting for user input.
    """
    dominican_slang_file = os.path.join('json-conversion', 'vocab', 'dominican-slang-example.json')
    # Load the example data from the text file.
    try:
        with open(dominican_slang_file, 'r') as file:
            dominican_slang = json.load(file)
            print(f"✅ Archivo '{dominican_slang_file}' cargado correctamente.")
    except json.JSONDecodeError:
        print(f"❌ Error: El archivo '{dominican_slang_file}' no es un JSON válido. Asegúrate de que el archivo tenga el formato correcto.")
        return
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{dominican_slang_file}' no se encontró. Asegúrate de que el archivo exista.")
        return

    # print("✅ Servicio del Chatbot Chamo iniciado. ¡Listo para conversar!")
    # print("   Escribe 'salir' para terminar la sesión.")
    # print("-" * 50)

    # # This infinite loop keeps the service running.
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
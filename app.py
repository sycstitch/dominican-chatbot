# app.py
# This is the main entry point for our Dominican Chatbot application.

def main():
    """
    Main function to run the chatbot application.
    This function contains an infinite loop that keeps the script running,
    waiting for user input.
    """
    print("✅ Servicio del Chatbot Chamo iniciado. ¡Listo para conversar!")
    print("   Escribe 'salir' para terminar la sesión.")
    print("-" * 50)

    # This infinite loop keeps the service running.
    while True:
        try:
            # The input() function pauses the program and waits for the user to type.
            user_input = input("Tú: ")

            # Check if the user wants to exit the application.
            if user_input.lower() == 'salir':
                break

            # --- Placeholder for Future Logic ---
            # In the next steps, all your RAG logic will go here.
            # 1. You'll send user_input to the Retriever model.
            # 2. You'll get back relevant context from your dictionary.
            # 3. You'll build a prompt and send it to the Ollama service.
            # 4. You'll print the final response from the Generator model.

            # For now, we just echo the input back to show it's working.
            print(f"Chamo (dev): Recibí tu mensaje: '{user_input}'")

        except (KeyboardInterrupt, EOFError):
            # This handles both Ctrl+C and the case where the input stream closes.
            break

    print("\n👋 ¡Nos vemos! El servicio del chatbot se está cerrando.")

if __name__ == "__main__":
    main()
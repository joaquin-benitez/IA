import openai
import os
from dotenv import load_dotenv

def generar_prompt(idea):
    """
    Genera un prompt detallado para un tatuaje basado en una idea inicial.
    """
    prompt = f"""
    Genera un prompt detallado para un tatuaje basado en la siguiente idea: "{idea}". 
    Usa frases cortas y concretas y no más de 200 palabras. El resultado debe incluir:
    - Estilo del tatuaje (realista, geométrico, tradicional, etc.).
    - Técnicas recomendadas (sombreado, puntillismo, línea fina, etc.).
    - Zonas recomendadas del cuerpo.
    """

    client = openai.OpenAI()  # Se usa la nueva forma de instanciar el cliente
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un asistente experto en diseño de tatuajes."},
            {"role": "user", "content": prompt},
        ]
    )
    
    return response.choices[0].message.content.strip()

def generar_imagen(prompt):
    """
    Genera una imagen basada en el prompt usando la API de OpenAI (DALL·E 3).
    """
    client = openai.OpenAI()
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response.data[0].url

if __name__ == "__main__":
    # Cargar variables de entorno
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Verificar si la clave API está cargada
    if not api_key:
        print("⚠️ ERROR: No se encontró la clave API de OpenAI. Asegúrate de definirla en un archivo .env o en una variable de entorno.")
        exit(1)

    openai.api_key = api_key  # Se asigna la clave API correctamente

    # Solicitar una idea de tatuaje al usuario
    idea_usuario = input("Describe tu idea de tatuaje: ")
    
    # Generar y mostrar el prompt detallado
    prompt_generado = generar_prompt(idea_usuario)
    print("\n🔹 Prompt generado:")
    print(prompt_generado)

    # Generar imagen
    url_imagen = generar_imagen(prompt_generado)
    print("\n🖼️ Imagen generada:", url_imagen)







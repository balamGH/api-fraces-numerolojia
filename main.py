from fastapi import FastAPI
from datetime import datetime
import random

app = FastAPI(title="Frase & Numerología en Texto", version="1.0")

# Frases espirituales
frases = [
    "La luz siempre encuentra su camino, incluso en la selva más densa.",
    "Hoy es el día en que tu alma recuerda su propósito.",
    "Cada paso que das despierta el jaguar dentro de ti.",
    "El universo conspira a favor de quienes se mueven con fe.",
    "Eres raíz, eres cielo, eres todo lo que necesitas."
]

# Significados numerológicos
numerologia = {
    1: "Liderazgo, independencia y nuevos comienzos.",
    2: "Colaboración, sensibilidad y equilibrio.",
    3: "Creatividad, comunicación y alegría.",
    4: "Estabilidad, orden y disciplina.",
    5: "Cambios, aventura y libertad.",
    6: "Responsabilidad, amor y familia.",
    7: "Introspección, espiritualidad y sabiduría.",
    8: "Poder, éxito y abundancia material.",
    9: "Compasión, servicio y cierre de ciclos."
}

@app.get("/daily")
def mensaje_diario(nombre: str = "Invitado"):
    hoy = datetime.now()
    suma = sum(int(d) for d in hoy.strftime("%d%m%Y"))
    while suma > 9:
        suma = sum(int(d) for d in str(suma))
    
    frase = random.choice(frases)
    
    mensaje = (
        f"✨ Hola {nombre} ✨\n"
        f"📅 Fecha: {hoy.strftime('%d/%m/%Y')}\n"
        f"🔢 Tu número personal hoy es: {suma}\n"
        f"📖 Significado: {numerologia[suma]}\n"
        f"💬 Mensaje: {frase}\n\n"
        f"🌟 Que tu día esté guiado por la energía del jaguar y la claridad del cielo."
    )
    
    return mensaje

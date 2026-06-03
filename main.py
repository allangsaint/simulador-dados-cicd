import time
import dice

def lanzar_dados(amount, sides):
    return dice.roll(f"{amount}d{sides}")

if __name__ == "__main__":
    amount = 5
    sides = 6
    
    resultados = lanzar_dados(amount, sides)
    
    for i, resultado in enumerate(resultados, start=1):
        print(f"Lanzamiento {i} número obtenido {resultado}")
        time.sleep(5)
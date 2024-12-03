def calcula_area_circulo():
  raio = input("Quanto é o raio? ")
  acirculo = 3, 14 * raio
  print(f"A area do circulo é: {acirculo} ")


def calcula_area_triagulo():
  altura = input("Qual é a altura? ")
  cumdabase = input("Qual é o cumprimento da base? ")
  atriangulo = altura * cumdabase / 2
  print(f"A area do triangulo é: {atriangulo} ")


def calcula_area_retangulo():
  altura = input("Qual é a altura? ")
  cumbase = input("Qual é o cumprimento da base? ")
  aretangulo = altura * cumbase
  print(f"A area do retangulo é: {aretangulo} ")


def main():
  pedidos = {}
  while True:
    print("Cálculo das áreas de figuras geométricas:")
    print("1. Círculo")
    print("2. Triângulo")
    print("3. Retângulo")
    escolha = input("Qual figura deseja calcular a área? ").lower()
    if escolha == "circulo":
      calcula_area_circulo()
    elif escolha == "triangulo":
      calcula_area_triagulo()
    elif escolha == "retangulo":
      calcula_area_retangulo()


if __name__ == "__main__":
  main()

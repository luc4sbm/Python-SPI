def coordenadas():
    coordenadas=input()
    dado=coordenadas.split()
    x_min=dado[0]
    y_min=dado[1]
    x_max=dado[2]
    y_max=dado[3]
    x=dado[4]
    y=dado[5]
    if x_min < x < x_max and y_min < y < y_max:
        print("O ponto está dentro do retângulo.")
    elif x_min <= x <= x_max and y_min <= y <= y_max:
        print("O ponto está tocando a borda do retângulo.")
    else:
        print("O ponto está fora do retângulo.")
if __name__=="__main__":
    coordenadas()           
#JAIME
# #Calculator with basic math operations (+-/)

def main():
    
    print("Calculadora")
    
    opc = int(input("Selecione opción: \n"))
    
    while (opc != 5):
        
        x = int(input("Ingrese primer número: \n"))
        y = int(input("Ingrese segundo número: \n"))
        
        if (opc == 1):
            print ("La suma es: ", x+y)
        elif(opc == 2):
            print ("La Resta es:", x-y)
        elif(opc == 3):
            print ("La Multiplicacion es:", x*y)
        elif(opc == 4):
            try:
                print ("La Division es:", x/y)
            except ZeroDivisionError:
                print ("No se permite división entre 0")
            
        opc = int(input("Selecione opción: \n"))

if __name__ == "__main__":
    main()
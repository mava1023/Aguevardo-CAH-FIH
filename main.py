from graficos import Canvas
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 600

canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
letras =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letrasm =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
both=[letras,letrasm]
palabras_abelardo = ["FRACKING", "SECURITY", "PROLIFE", "RIGHTS", "FAMILY", "TIGER", "FIRM","SNARL", "PETRO", "URIBE", "TRADWIFE", "BROW", "WASTE","FRAUD", "VOTE","TRUMP", "DUNCE"]
Mega_JAIL = 0
jueguito= 0
palabras_letras = [8,8,7,6,6,5,4,5,5,5,8,4,5,5,4,5,5]


def pantalla_frente(jueguito):
    
    abelardo = canvas.crear_imagen_con_tamanio(0,0,CANVAS_WIDTH, CANVAS_HEIGHT, "menu.png")
    rect_texto = canvas.crear_rectangulo(140, 300, 265,340)
    rect_texto2 = canvas.crear_rectangulo(145, 305, 260, 335,)
    canvas.establecer_color(rect_texto, "#5F0826")
    canvas.establecer_color(rect_texto2,"#FE7F2D")
    start= canvas.crear_texto(200,320, 'START')
    canvas.establecer_color(start, '#FFFFFF')
    canvas.establecer_fuente(start, 'Century',24)
    
    while jueguito == 0:
        canvas.esperar_por_clic()
        x= canvas.obtener_mouse_x()
        y=canvas.obtener_mouse_y()
        print (x, y)
        objs = canvas.encontrar_superposicion(x,y,x+1, y+1)
        figuritas = [rect_texto,rect_texto2,start]
        if rect_texto in objs:
            jueguito = 1
        elif rect_texto2 in objs:
           jueguito = 1
        elif start in objs:
            jueguito = 1
    canvas.eliminar(abelardo)
    canvas.eliminar(rect_texto)
    canvas.eliminar(rect_texto2)
    canvas.eliminar(start)
    
    
def loose():
    cambodia = canvas.crear_imagen_con_tamanio(0,0,CANVAS_WIDTH, CANVAS_HEIGHT,"wompwomp.png")
def win():
    camerun = canvas.crear_imagen_con_tamanio(0,0,CANVAS_WIDTH, CANVAS_HEIGHT,"yippyjailanyway.png")

def frentota (palabras_abelardo, palabras_letras):
    mistakes = 0
    rounds = 1
    intentos = 6
    frente = canvas.crear_imagen_con_tamanio(0,0, CANVAS_WIDTH, CANVAS_HEIGHT, "Hagman.png")
    puntaje_rounds= canvas.crear_texto(91,29, "1")
    canvas.establecer_color_relleno(puntaje_rounds,"#FFFFFF")
    canvas.establecer_fuente(puntaje_rounds, "Century", 12)

    rect_1 = canvas.crear_rectangulo(45, 400,90,445 , "#FFFFFF", "#000000")
    rect_2 = canvas.crear_rectangulo(105, 400,150,445 , "#FFFFFF", "#000000")
    rect_3 = canvas.crear_rectangulo(165, 400,210,445 , "#FFFFFF", "#000000")
    rect_4 = canvas.crear_rectangulo(225, 400,270,445 , "#FFFFFF", "#000000")
    rect_5 = canvas.crear_rectangulo(285, 400,330,445, "#FFFFFF", "#000000")
    rect_6 = canvas.crear_rectangulo(45, 465,90,510 , "#FFFFFF", "#000000")
    rect_7 = canvas.crear_rectangulo(105, 465,150,510 , "#FFFFFF", "#000000")
    rect_8 = canvas.crear_rectangulo(165, 465,210,510 , "#FFFFFF", "#000000")
    rect_9 = canvas.crear_rectangulo(225, 465,270,510 , "#FFFFFF", "#000000")
    rect_10 = canvas.crear_rectangulo(285, 465,330,510 , "#FFFFFF", "#000000")
    rects = [rect_1,rect_2,rect_3,rect_4,rect_5,rect_6,rect_7,rect_8,rect_9,rect_10]
    for i in range (len(rects) ) :
        canvas.establecer_oculto(rects [i], True)

    show_letra1= canvas.crear_texto(63,414, "0" )
    canvas.establecer_color(show_letra1,"#000000")
    canvas.establecer_fuente(show_letra1, "Century", 14)
    show_letra2= canvas.crear_texto(123,414,  "0" )
    canvas.establecer_color(show_letra2,"#000000")
    canvas.establecer_fuente(show_letra2, "Century", 14)
    show_letra3= canvas.crear_texto(182,414, "0")
    canvas.establecer_color(show_letra3,"#000000")
    canvas.establecer_fuente(show_letra3, "Century", 14)
    show_letra4= canvas.crear_texto(242,414, "0" )
    canvas.establecer_color(show_letra4,"#000000")
    canvas.establecer_fuente(show_letra4, "Century", 14)
    show_letra5= canvas.crear_texto(303,414, "0" )
    canvas.establecer_color(show_letra5,"#000000")
    canvas.establecer_fuente(show_letra5, "Century", 14)
    show_letra6= canvas.crear_texto(63,478,  "0")
    canvas.establecer_color(show_letra6,"#000000")
    canvas.establecer_fuente(show_letra6, "Century", 14)
    show_letra7= canvas.crear_texto(123,478,"0" )
    canvas.establecer_color(show_letra7,"#000000")
    canvas.establecer_fuente(show_letra7, "Century", 14)
    show_letra8= canvas.crear_texto(182,478,"0" )
    canvas.establecer_color(show_letra8,"#000000")
    canvas.establecer_fuente(show_letra8, "Century", 14)
    show_letra9= canvas.crear_texto(242,478, "0" )
    canvas.establecer_color(show_letra9,"#000000")
    canvas.establecer_fuente(show_letra9, "Century", 14)
    show_letra10= canvas.crear_texto(303,478, "0" )
    canvas.establecer_color(show_letra10,"#070101")
    canvas.establecer_fuente(show_letra10, "Century", 14)
    
    show_letras = [show_letra1,show_letra2,show_letra3,show_letra4,show_letra5,show_letra6,show_letra7,show_letra8,show_letra9,show_letra10]
    for i in range (len(show_letras) ) :
      canvas.establecer_oculto(show_letras [i], True)

    puntaje_mistakes= canvas.crear_texto(335,84, str(mistakes) )
    canvas.establecer_color(puntaje_mistakes,"#FFFFFF")
    canvas.establecer_fuente(puntaje_mistakes, "Century", 18) #24
    puntaje_you= canvas.crear_texto(260,28, "0" )
    canvas.establecer_color(puntaje_you,"#000000")
    canvas.establecer_fuente(puntaje_you, "Century", 14) #14
    puntaje_abelardo= canvas.crear_texto(388,28, "0" ) 
    canvas.establecer_color(puntaje_abelardo,"#000000")
    canvas.establecer_fuente(puntaje_abelardo, "Century", 14)#24

    show_letras_usadas1= canvas.crear_texto(220,200, "0" ) 
    canvas.establecer_color(show_letras_usadas1,"#000000")
    canvas.establecer_fuente(show_letras_usadas1, "Century", 20)
    show_letras_usadas2= canvas.crear_texto(240,200, "0" ) 
    canvas.establecer_color(show_letras_usadas2,"#000000")
    canvas.establecer_fuente(show_letras_usadas2, "Century", 20)
    show_letras_usadas3= canvas.crear_texto(260,200, "0" ) 
    canvas.establecer_color(show_letras_usadas3,"#000000")
    canvas.establecer_fuente(show_letras_usadas3, "Century", 20)
    show_letras_usadas4= canvas.crear_texto(280,200, "0" ) 
    canvas.establecer_color(show_letras_usadas4,"#000000")
    canvas.establecer_fuente(show_letras_usadas4, "Century", 20)
    show_letras_usadas5= canvas.crear_texto(300,200, "0" ) 
    canvas.establecer_color(show_letras_usadas5,"#000000")
    canvas.establecer_fuente(show_letras_usadas5, "Century", 20)
    show_letras_usadas6= canvas.crear_texto(320,200, "0" ) 
    canvas.establecer_color(show_letras_usadas6,"#000000")
    canvas.establecer_fuente(show_letras_usadas6, "Century", 20)
    show_letras_usadas7= canvas.crear_texto(340,200, "0" ) 
    canvas.establecer_color(show_letras_usadas7,"#000000")
    canvas.establecer_fuente(show_letras_usadas7, "Century", 20)
    show_letras_usadas8= canvas.crear_texto(360,200, "0" ) 
    canvas.establecer_color(show_letras_usadas8,"#000000")
    canvas.establecer_fuente(show_letras_usadas8, "Century", 20)

    show_letras_usadas9= canvas.crear_texto(220,230, "0" ) 
    canvas.establecer_color(show_letras_usadas9,"#000000")
    canvas.establecer_fuente(show_letras_usadas9, "Century", 20)

    show_letras_usadas10= canvas.crear_texto(240,230, "0" ) 
    canvas.establecer_color(show_letras_usadas10,"#000000")
    canvas.establecer_fuente(show_letras_usadas10, "Century", 20)

    show_letras_usadas11= canvas.crear_texto(260,230, "0" ) 
    canvas.establecer_color(show_letras_usadas11,"#000000")
    canvas.establecer_fuente(show_letras_usadas11, "Century", 20)

    show_letras_usadas12= canvas.crear_texto(280,230, "0" ) 
    canvas.establecer_color(show_letras_usadas12,"#000000")
    canvas.establecer_fuente(show_letras_usadas12, "Century", 20)

    show_letras_usadas13= canvas.crear_texto(300,230, "0" ) 
    canvas.establecer_color(show_letras_usadas13,"#000000")
    canvas.establecer_fuente(show_letras_usadas13, "Century", 20)

    show_letras_usadas14= canvas.crear_texto(320,230, "0" ) 
    canvas.establecer_color(show_letras_usadas14,"#000000")
    canvas.establecer_fuente(show_letras_usadas14, "Century", 20)

    show_letras_usadas15= canvas.crear_texto(340,230, "0" ) 
    canvas.establecer_color(show_letras_usadas15,"#000000")
    canvas.establecer_fuente(show_letras_usadas15, "Century", 20)

    show_letras_usadas16= canvas.crear_texto(360,230, "0" ) 
    canvas.establecer_color(show_letras_usadas16,"#000000")
    canvas.establecer_fuente(show_letras_usadas16, "Century", 20)

    show_letras_usadas=[show_letras_usadas1,show_letras_usadas2,show_letras_usadas3,show_letras_usadas4,show_letras_usadas5,show_letras_usadas6,show_letras_usadas7,show_letras_usadas8,show_letras_usadas9,show_letras_usadas10,show_letras_usadas11,show_letras_usadas12,show_letras_usadas13,show_letras_usadas14,show_letras_usadas15,show_letras_usadas16]
    for i in range (0, len(show_letras_usadas)):
            canvas.establecer_oculto(show_letras_usadas[i],True)
    while rounds <= 6:
        lista_word= []
        lista_letras_ronda = []
        you = 0
        aberlado = 0
        if rounds == 1 or 3 or 5:
            adivina = False
            palabra_number = random.randint (0,16)
            print (palabra_number)
            palabra = palabras_abelardo [palabra_number]
            letras = palabras_letras [palabra_number]
            juego_acaba = False
            

            for i in range (0, letras):
                canvas.establecer_oculto(rects [i], False)

            while not juego_acaba:
                letter= input ("Guess letters: ")
                while type(letter) != str:
                    letter = input("Plase enter a letter, either uppercase or lowercase: ")

                new_l= letter.upper()

                lista_letras_ronda.append(new_l)
                for i in range (0,letras):
                    lista_word.append(palabra[i])
                print(new_l,lista_word, lista_letras_ronda)

                canvas.establecer_texto(show_letras_usadas[len(lista_letras_ronda) -1 ], new_l)
                canvas.establecer_oculto(show_letras_usadas[[len(lista_letras_ronda) -1 ], False])
                if new_l in palabra:
                    posicion_letra = palabra.find(new_l)
                    
                    canvas.establecer_oculto(show_letras[posicion_letra], False)
                    canvas.establecer_texto(show_letras[posicion_letra], new_l)

                elif new_l not in palabra:
                    mistakes -= 1
                    canvas.establecer_texto(puntaje_mistakes, str(mistakes))

            
                    

                rounds += 1
                    

        elif round == 2 or 4 or 6:
            palabra_number = random.randint (0,16)
            print (palabra_number)
            palabra = palabras_abelardo [palabra_number]
            lista_word= []
            letras = palabras_letras [palabra_number]
            for i in range (0, letras):
                canvas.establecer_oculto(rects [i], False)
            letter= input ("Guess letters: ")
            while type(letter) != str:
                letter = input("Plase enter a letter, either uppercase or lowercase: ")
            new_l= letter.upper()

            for i in range (0,letras-1):
                lista_word.append(palabra[i])
            while letter in lista_word:
                print(letter)
                    
                
                lista_word.append(palabra[i]) 
        
                rounds = rounds + 1





def main():
    pantalla_frente(jueguito)
    fren= frentota (palabras_abelardo,palabras_letras)
    if fren ==1:
        canvas.eliminar_todo()
        win()
    elif fren ==0:
        canvas.eliminar_todo()
        loose()
        
    
    
    



if __name__ == '__main__':
    main()
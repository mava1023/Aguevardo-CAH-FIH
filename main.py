from graficos import Canvas
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 600

canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
letras =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letrasm =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
both=[letras,letrasm]
palabras_abelardo = ["FRACKING", "SECURITY", "PROLIFE", "RIGHTS", "FAMILY", "TIGER", "FIRM","", "PETRO", "URIBE", "TRADWIFE", "DESSERT", "FOREHEAD","FRAUD", "ELECTIONS","TRUMP","MILEI"]
Mega_JAIL = 0
jueguito= 0
palabras_letras = [8,8,7,6,6,6,5,4,4,5,5,8,6,8,5,9,5,5]


def pantalla_frente(jueguito):
    
    abelardo = canvas.create_image_with_size(0,0,CANVAS_WIDTH, CANVAS_HEIGHT, "menu.png")
    rect_texto = canvas.create_rectangle(140, 300, 265,340 , "#5F0826")
    rect_texto2 = canvas.create_rectangle(145, 305, 260, 335, "#FE7F2D")
    start= canvas.create_text(170,310, text = 'START',font = 'Century', font_size = 20, color ='#5F0826')
    while jueguito == 0:
        canvas.wait_for_click()
        click = canvas.get_last_click()
        x = click[0]
        y = click[1]
        objs = canvas.find_overlapping(x,y,x+1, y+1)
        figuritas = [rect_texto,rect_texto2,start]
        if str(rect_texto) in objs:
            jueguito = 1
        elif str (rect_texto2) in objs:
            jueguito = 1
        elif str(start) in objs:
            jueguito = 1
    print = jueguito



def frentota (palabras_abelardo, palabras_letras):
    rounds = 1
    frente = canvas.create_image_with_size(0,0, CANVAS_WIDTH, CANVAS_HEIGHT, "Hagman.png")
    puntaje_rounds= canvas.create_text(90,24, text = "1" ,font = 'Century', font_size = 14, color ='#FFFFFF')
    rect_1 = canvas.create_rectangle(45, 400,90,445 , "#FFFFFF", "#000000")
    rect_2 = canvas.create_rectangle(105, 400,150,445 , "#FFFFFF", "#000000")
    rect_3 = canvas.create_rectangle(165, 400,210,445 , "#FFFFFF", "#000000")
    rect_4 = canvas.create_rectangle(225, 400,270,445 , "#FFFFFF", "#000000")
    rect_5 = canvas.create_rectangle(285, 400,330,445, "#FFFFFF", "#000000")
    rect_6 = canvas.create_rectangle(45, 465,90,510 , "#FFFFFF", "#000000")
    rect_7 = canvas.create_rectangle(105, 465,150,510 , "#FFFFFF", "#000000")
    rect_8 = canvas.create_rectangle(165, 465,210,510 , "#FFFFFF", "#000000")
    rect_9 = canvas.create_rectangle(225, 465,270,510 , "#FFFFFF", "#000000")
    rect_10 = canvas.create_rectangle(285, 465,330,510 , "#FFFFFF", "#000000")
    rects = [rect_1,rect_2,rect_3,rect_4,rect_5,rect_6,rect_7,rect_8,rect_9,rect_10]
    for i in range (len(rects) ) :
        canvas.set_hidden(rects [i], True)

    show_letra1= canvas.create_text(63,414, text = "0" ,font = 'Century', font_size = 20, color ='#000000')
    show_letra2= canvas.create_text(123,414, text = "0" ,font = 'Century', font_size = 20, color ='#000000')
    show_letra3= canvas.create_text(182,414, text = "0" ,font = 'Century', font_size = 20, color ='#000000')
    show_letra4= canvas.create_text(242,414, text = "0" ,font = 'Century', font_size = 20, color ='#000000')
    show_letra5= canvas.create_text(303,414, text = "0" ,font = 'Century', font_size = 20, color ='#000000')
    show_letra6= canvas.create_text(63,478, text = "0" ,font = 'Century', font_size = 20, color ='#000000')
    show_letra7= canvas.create_text(123,478, text = "0" ,font = 'Century', font_size = 20, color ='#000000')
    show_letra8= canvas.create_text(182,478, text = "0" ,font = 'Century', font_size = 20, color ='#000000')
    show_letra9= canvas.create_text(242,478, text = "0" ,font = 'Century', font_size = 20, color ='#000000')
    show_letra10= canvas.create_text(303,478, text = "0" ,font = 'Century', font_size = 20, color ='#000000')
    
    show_letras = [show_letra1,show_letra2,show_letra3,show_letra4,show_letra5,show_letra6,show_letra7,show_letra8,show_letra9,show_letra10]
    for i in range (len(show_letras) ) :
        canvas.set_hidden(show_letras [i], True)

    while rounds == 1:
        you = 0
        aberlado = 0
        puntaje_mistakes= canvas.create_text(330,74, text = "0" ,font = 'Century', font_size = 24, color ='#FFFFFF')
        puntaje_you= canvas.create_text(260,23, text = "0" ,font = 'Century', font_size = 14, color ='#000000')
        puntaje_abelardo= canvas.create_text(388,23, text = "0" ,font = 'Century', font_size = 14, color ='#000000')
        if round == 1 or 3 or 5:

            palabra_number = random.randint (0,16)
            print (palabra_number)
            palabra = palabras_abelardo [palabra_number]
            lista_word= []
            letras = palabras_letras [palabra_number]
            for i in range (0, letras):
                canvas.set_hidden(rects [i], False)
            letter= input ("Guess letters: ")
            while type(letter) != str:
                letter = input("Plase enter a letter, either uppercase or lowercase: ")
            new_l= letter.upper()

            for i in range (0,letras-1):
                lista_word.append(palabra[i])
            
            if new_l
            
        


            
            


            
            rounds = rounds + 1


def main():
    pantalla_frente(jueguito)
    canvas.clear()
    frentota (palabras_abelardo,palabras_letras)
    # TODO: your code here!
    



if __name__ == '__main__':
    main()
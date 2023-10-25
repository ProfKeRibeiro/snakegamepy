import turtle
import time
import random

#cria variáveis
delay = 0.1
score = 0
high_score = 0
#cria tela com o Turtle
tela = turtle.Screen()
tela.title("Snake Game 1ºInfo")
tela.bgcolor("green")
tela.setup(width=600, height=600)
tela.tracer(0) 
#Cria a cobra
cobra = turtle.Turtle()
cobra.speed(0)
cobra.shape("square")
cobra.color("black")
cobra.penup()
cobra.goto(0,0) #começa no centro da tela
cobra.direction = "stop"
#cria a comida da cobra
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100) #começa no centro da tela
#cria o corpo da cobra
corpo = []
#cria a pontuação
placar = turtle.Turtle()
placar.speed(0)
placar.shape("square")
placar.color("white")
placar.penup()
placar.hideturtle() #esconde a tartaruga
placar.goto(0, 260)
placar.write(f'Pontuação: {score} Melhor pontuação: {high_score}', align="center", font=("Courier", 24, "normal"))

#funções
def go_up():
    if cobra.direction != "down":
        cobra.direction = "up"
def go_down():
    if cobra.direction != "up":
        cobra.direction = "down"
def go_left():
    if cobra.direction != "right":
        cobra.direction = "left"
def go_right():
    if cobra.direction != "left":
        cobra.direction = "right"
def move():
    if cobra.direction == "up":
        y = cobra.ycor() 
        cobra.sety(y + 20)
    if cobra.direction == "down":
        y = cobra.ycor() 
        cobra.sety(y - 20)
    if cobra.direction == "left":
        x = cobra.xcor() 
        cobra.setx(x - 20)
    if cobra.direction == "right":
        x = cobra.xcor() 
        cobra.setx(x + 20)

#Recebe os comandos do teclado
tela.listen() 
tela.onkeypress(go_up, "Up")
tela.onkeypress(go_down, "Down")
tela.onkeypress(go_left, "Left")
tela.onkeypress(go_right, "Right")

#Loop principal do jogo
while True:
    tela.update()
    #colisão com a borda
    if cobra.xcor()>290 or cobra.xcor()<-290 or cobra.ycor()>290 or cobra.ycor()<-290:
        time.sleep(1)
        cobra.goto(0,0)
        cobra.direction = "stop"
#oculta os p_corpos do corpo
        for p_corpo in corpo:
            p_corpo.goto(1000, 1000) 
        #limpar os p_corpos do corpo
        corpo.clear()
        #limpa a pontuação
        score = 0
        #redefine o atraso
        delay = 0.1
        placar.clear()
        placar.write(f'Pontuação: {score} Melhor pontuação: {high_score}',align="center", font=("Courier", 20, "normal"))
    #verifica a colisão com a comida
    if cobra.distance(comida) < 20:
        #move a comida para um lugar aleatório
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        comida.goto(x,y)
        #add um p_corpo no corpo da cobra
        parte_corpo = turtle.Turtle()
        parte_corpo.speed(0)
        parte_corpo.shape("square")
        parte_corpo.color("grey")
        parte_corpo.penup()
        corpo.append(parte_corpo)
        #encurta o atraso
        delay -= 0.001
        #acrescenta pontuação
        score += 10
        if score > high_score:
            high_score = score
        placar.clear()
        placar.write(f'Pontuação: {score} Melhor pontuação: {high_score}', align="center", font=("Courier", 24, "normal"))

    #move the end p_corpoo do corpo para o final
    for index in range(len(corpo)-1, 0, -1):
        x = corpo[index-1].xcor() #pega a posição do p_corpoo anterior
        y = corpo[index-1].ycor()
        corpo[index].goto(x, y)
    #transforma o p_corpoo 0 na cabeça
    if len(corpo) > 0:
        x = cobra.xcor() #pega a posição da cabeça
        y = cobra.ycor()
        corpo[0].goto(x,y)
    move()
    #verifica a colisão da cabeça com o restante do corpo
    for p_corpo in corpo:
        if p_corpo.distance(cobra) < 20:
            time.sleep(1)
            cobra.goto(0,0)
            cobra.direction = "stop"
            #esconde o corpo
            for p_corpo in corpo:
                p_corpo.goto(1000, 1000) 
            #limpa o corpo
            corpo.clear()
            #limpa a pontuação
            score = 0
            #redefine o atraso
            delay = 0.1
            #atualiza o placar
            placar.clear()
            placar.write(f'Pontuação: {score} Melhor pontuação: {high_score}', align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)





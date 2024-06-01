import random

def setup():
    size(1000, 1000)  # Size of the screen

    # Load images
    global rock_icon, paper_icon, scissors_icon, computer_icon
    rock_icon = loadImage("data/rock.png")
    paper_icon = loadImage("data/paper.png")
    scissors_icon = loadImage("data/scissors.png")
    computer_icon = loadImage("data/computer.png")

    # Initialize other variables
    global player_move, computer_move, game_result
    player_move = -1
    computer_move = -1
    game_result = ""

    global win_counter, tie_counter, loss_counter, game_counter
    win_counter = 0
    tie_counter = 0
    loss_counter = 0
    game_counter = 0

    global rockButtonX, paperButtonX, scissorsButtonX, buttonY, widthAndHeight
    rockButtonX = width / 5  # 200
    paperButtonX = width / 2  # 500
    scissorsButtonX = 4 * width / 5  # 800
    buttonY = 4 * height / 5  # 800
    widthAndHeight = width / 5  # 200

def draw():
    background(255)
    imageMode(CENTER)
    rectMode(CENTER)
    textAlign(CENTER)
    strokeWeight(width / 100)
    textSize(width / 20)
    fill(0)

    # Highlight buttons when hovered over
    highlightButton()

    # Draw the buttons
    drawButtons()

    # Display the player's and computer's moves
    displayMoves()

    # Display the game result
    displayGameResult()

    # Display counters
    displayCounters()

def highlightButton():
    if (rockButtonX - widthAndHeight / 2 < mouseX < rockButtonX + widthAndHeight / 2) and (buttonY - widthAndHeight / 2 < mouseY < buttonY + widthAndHeight / 2):
        rect(rockButtonX, buttonY, widthAndHeight + 10, widthAndHeight + 10)
    if (paperButtonX - widthAndHeight / 2 < mouseX < paperButtonX + widthAndHeight / 2) and (buttonY - widthAndHeight / 2 < mouseY < buttonY + widthAndHeight / 2):
        rect(paperButtonX, buttonY, widthAndHeight + 10, widthAndHeight + 10)
    if (scissorsButtonX - widthAndHeight / 2 < mouseX < scissorsButtonX + widthAndHeight / 2) and (buttonY - widthAndHeight / 2 < mouseY < buttonY + widthAndHeight / 2):
        rect(scissorsButtonX, buttonY, widthAndHeight + 10, widthAndHeight + 10)

def drawButtons():
    image(rock_icon, rockButtonX, buttonY, widthAndHeight, widthAndHeight)
    image(paper_icon, paperButtonX, buttonY, widthAndHeight, widthAndHeight)
    image(scissors_icon, scissorsButtonX, buttonY, widthAndHeight, widthAndHeight)
    image(computer_icon, width / 2, height / 4, width / 2.5, height * 0.3)

def mousePressed():
    global player_move
    if (rockButtonX - widthAndHeight / 2 < mouseX < rockButtonX + widthAndHeight / 2) and (buttonY - widthAndHeight / 2 < mouseY < buttonY + widthAndHeight / 2):
        player_move = 0
    elif (paperButtonX - widthAndHeight / 2 < mouseX < paperButtonX + widthAndHeight / 2) and (buttonY - widthAndHeight / 2 < mouseY < buttonY + widthAndHeight / 2):
        player_move = 1
    elif (scissorsButtonX - widthAndHeight / 2 < mouseX < scissorsButtonX + widthAndHeight / 2) and (buttonY - widthAndHeight / 2 < mouseY < buttonY + widthAndHeight / 2):
        player_move = 2
    else:
        return
    playGame()

def keyPressed():
    global player_move
    if key == 'r' or key == '1':  # Rock
        player_move = 0
    elif key == 'p' or key == '2':  # Paper
        player_move = 1
    elif key == 's' or key == '3':  # Scissors
        player_move = 2
    else:
        return
    playGame()

def playGame():
    global player_move, computer_move, game_result
    global win_counter, tie_counter, loss_counter, game_counter

    computer_move = random.randrange(3)
    game_counter += 1
    
    if player_move == computer_move:
        game_result = "You tied!"
        tie_counter += 1
    elif (player_move == 0 and computer_move == 2) or (player_move == 1 and computer_move == 0) or (player_move == 2 and computer_move == 1):
        game_result = "You won!"
        win_counter += 1
    else:
        game_result = "You lost!"
        loss_counter += 1

def displayMoves():
    if player_move == 0:
        text("Player plays rock", width / 2, height * 0.65)
    elif player_move == 1:
        text("Player plays paper", width / 2, height * 0.65)
    elif player_move == 2:
        text("Player plays scissors", width / 2, height * 0.65)

    if computer_move == 0:
        text("Computer plays rock", width / 2, height / 13)
    elif computer_move == 1:
        text("Computer plays paper", width / 2, height / 13)
    elif computer_move == 2:
        text("Computer plays scissors", width / 2, height / 13)

def displayGameResult():
    text(game_result, width / 2, height / 2)

def displayCounters():
    text("Games \nplayed:", width / 10, 4 * height / 20)
    text(game_counter, width / 10, 4 * height / 12)

    text("Wins:", width / 15, 5 * height / 12)
    text(win_counter, width / 9 + width / 12, 5 * height / 12)
    
    text("Ties:", width / 17, 5.5 * height / 12)
    text(tie_counter, width / 9 + width / 12, 5.5 * height / 12)
    
    text("Losses:", width / 12, 6 * height / 12)
    text(loss_counter, width / 9 + width / 12, 6 * height / 12)

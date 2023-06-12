from files import *
from adjacency_list import adjacency_list
from stack import stack
import random

class game:
    def __init__(self):
        self.main_menu_loop = True
        self.game_loop = True

    def main_menu(self):
        str = ''
        while self.main_menu_loop:
            str = ''
            screen.blit(main_menu_screen,(0,0))
            screen.blit(text_grey[0], (350, 250))
            screen.blit(text_grey[1], (330, 320))
            screen.blit(text_grey[2], (350, 390))
            px, py = pygame.mouse.get_pos()
            if px in range(350, 450) and py in range(260, 285):
                screen.blit(text_red[0], (350, 250))
                str = 'play'
            elif px in range(330, 470) and py in range(330, 355):
                screen.blit(text_red[1], (330, 320))
                str = 'online'
            elif px in range(350, 450) and py in range(400, 425):
                screen.blit(text_red[2], (350, 390))
                str = 'quit'
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.main_menu_loop = False
                if event.type == pygame.MOUSEBUTTONDOWN and str == 'play':
                    self.running()
                elif event.type == pygame.MOUSEBUTTONDOWN and str == 'quit':
                    self.main_menu_loop = False

        pygame.quit()
        quit()

    def running(self):
        a = adjacency_list()
        for i in range(len(a.get_method())):
            if i < 12:
                a.get_method()[i].set_player(True)
            elif i > 12:
                a.get_method()[i].set_opponent(True)
        x1 = 30
        x2 = 730
        y = 540
        tuple1 = ()
        tuple2 = ()
        for i in range(12):
            tuple1 += ((x1, y),)
            tuple2 += ((x2, y),)
            y -= 40
        p1 = stack(tuple1)
        p2 = stack(tuple2)

        pos_x = 0
        pos_y = 0
        player_turn = ('P1.Source', 'P1.Destination', 'P2.Source', 'P2.Destination')
        random_number = random.randrange(0,4,2)
        turn = player_turn[random_number]
        index = None
        temp_index = 0
        temp_var = None
        seq = True
        self.game_loop = True
        while self.game_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.prompt_screen():
                        a.clear_list()
                        self.game_loop = False
                        continue
                    continue
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_x, pos_y = pygame.mouse.get_pos()
                    temp_index = 0
                    if turn == player_turn[0]:
                        for i in a.get_method():
                            if pos_x in range(i.get_position_x(),i.get_position_x()+40) and pos_y in range(i.get_position_y(),i.get_position_y()+40) and i.get_player():
                                index = i
                                turn = player_turn[1]
                    elif turn == player_turn[1]:
                        if seq and pos_x in range(index.get_position_x(),index.get_position_x()+40) and pos_y in range(index.get_position_y(),index.get_position_y()+40) and index.get_player():
                            turn = player_turn[0]
                        else:
                            for i in index.get_data():
                                if i!= None:
                                    if seq and pos_x in range(i.get_position_x(),i.get_position_x()+40) and pos_y in range(i.get_position_y(),i.get_position_y()+40) and not i.get_player() and not i.get_opponent():
                                        index.set_player(False)
                                        i.set_player(True)
                                        turn = player_turn[2]
                                        break
                                    temp_var = i.get_data()[temp_index]
                                    if temp_var != None:
                                        if pos_x in range(temp_var.get_position_x(),temp_var.get_position_x()+40) and pos_y in range(temp_var.get_position_y(),temp_var.get_position_y()+40) and not temp_var.get_player() and not temp_var.get_opponent() and i.get_opponent():
                                            index.set_player(False)
                                            i.set_opponent(False)
                                            temp_var.set_player(True)
                                            index = temp_var
                                            seq = False
                                            p2.push()
                                            break
                                temp_index += 1
                    elif turn == player_turn[2]:
                        for i in a.get_method():
                            if pos_x in range(i.get_position_x(),i.get_position_x()+40) and pos_y in range(i.get_position_y(),i.get_position_y()+40) and i.get_opponent():
                                index = i
                                turn = player_turn[3]
                    elif turn == player_turn[3]:
                        if seq and pos_x in range(index.get_position_x(),index.get_position_x()+40) and pos_y in range(index.get_position_y(),index.get_position_y()+40) and index.get_opponent():
                            turn = player_turn[2]
                        else:
                            for i in index.get_data():
                                if i != None:
                                    if seq and pos_x in range(i.get_position_x(),i.get_position_x()+40) and pos_y in range(i.get_position_y(),i.get_position_y()+40) and not i.get_player() and not i.get_opponent():
                                        index.set_opponent(False)
                                        i.set_opponent(True)
                                        turn = player_turn[0]
                                        break
                                    temp_var = i.get_data()[temp_index]
                                    if temp_var != None:
                                        if pos_x in range(temp_var.get_position_x(),temp_var.get_position_x()+40) and pos_y in range(temp_var.get_position_y(),temp_var.get_position_y()+40) and not temp_var.get_player() and not temp_var.get_opponent() and i.get_player():
                                            index.set_opponent(False)
                                            i.set_player(False)
                                            temp_var.set_opponent(True)
                                            index = temp_var
                                            seq = False
                                            p1.push()
                                            break
                                temp_index += 1
                    if not seq:
                        if pos_x in range(440,501) and pos_y in range(550,601):
                            if turn == player_turn[0] or turn == player_turn[1]:
                                turn = player_turn[2]
                                seq = True
                        if pos_x in range(200,361) and pos_y in range(550,610):
                            if turn == player_turn[2] or turn == player_turn[3]:
                                turn = player_turn[0]
                                seq = True
            screen.blit(game_background,(0,0))
            for i in a.get_method():
                if i.get_player():
                    screen.blit(player_bead, (i.get_position()))
                if i.get_opponent():
                    screen.blit(opponent_bead, (i.get_position()))
            if not p1.isEmpty():
                for i in p1.get_position():
                    screen.blit(player_bead,i)
            if not p2.isEmpty():
                for i in p2.get_position():
                    screen.blit(opponent_bead,i)

            if turn in player_turn[0:2]:
                screen.blit(buttons[0], (190,550))
            elif turn in player_turn[2:4]:
                screen.blit(buttons[1], (420,550))
            if turn == player_turn[1] or turn == player_turn[3]:
                screen.blit(selection,(index.get_position()))

            if p1.isFull() or p2.isFull():
                self.game_loop = False
                
            pygame.display.flip()
        self.main_menu()

    def prompt_screen(self):
        p_x = 0
        p_y = 0
        while True:
            p_x, p_y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if p_x in range(250, 401) and p_y in range(380, 451):
                        return True
                    elif p_x in range(400, 551) and p_y in range(380, 451):
                        return False
            screen.blit(prompt_scr, (0,0))
            if p_x in range(250, 401) and p_y in range(380, 451):
                screen.blit(buttons[2], (250,380))
            elif p_x in range(400, 551) and p_y in range(380, 451):
                screen.blit(buttons[3], (400,380))
            pygame.display.flip()
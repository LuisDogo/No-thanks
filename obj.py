import numpy as np
import random

class card:

    def __init__(self, number):
        self.counters = 0
        self.number = number
        self.next = False

    def pasar(self):
        self.counters += 1


class player:

    points = 0

    def __init__(self, counters : int, name : str):
        self.counters = counters
        self.name = name

    def pay(self, card : card):
        if self.counters == 0:
            print("No tienes fichas, tienes que comer")
            self.eat(card)
        else:
            self.counters -= 1
            card.counters += 1

    def eat(self, card : card):
        self.points += card.number
        self.counters += card.counters
        card.next = True


class game:

    def __init__(self, n_players : int):
        if n_players < 3:
            raise ValueError("There must be at least 3 players")
        elif n_players < 6:
            self.counters = 11
        elif n_players == 6:
            self.counters = 9
        elif n_players == 7:
            self.counters = 7
        else:
            raise ValueError("The maximum quantity of players is 7")
        
        self.players = []
        self.cards = []
        for number in range(3, 37):
            self.cards.append(card(number))
        random.shuffle(self.cards)
        self.cards[:24]

        for ith_player in range(n_players):
            name = input("Ingresa tu nombre: ")
            p = player(self.counters, name)
            self.players.append(p)

    def start(self):
        ith_player = 0
        ith_card = 0
        n_players = len(self.players)
        for card in self.cards:
            while card.next == False:
                print(f"Carta {card.number} con {card.counters} fichas")
                current_player = self.players[ith_player]
                print(f"Turno de {current_player.name} con {current_player.counters} fichas y {current_player.points} puntos")
                action = input("Accion?:    ")
                if action == "comer":
                    current_player.eat(card)
                    continue
                elif action == "pagar":
                    current_player.pay(card)
                    if ith_player + 1 == n_players:
                        ith_player = 0
                    else:
                        ith_player += 1



        for player in self.players:
            print(f"{player.name} obtuvo: {player.points - player.counters}")

        # for player in players:
        #     print(f"{player} tuvo {player.points}")


g = game(3)
g.start()
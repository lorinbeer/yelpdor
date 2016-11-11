import math
import sys

from game_obj import GameObj
from yelpdor.gui.messenger import Messenger

class Player(GameObj):

    def __init__(self, x, y, char, color):
        GameObj.__init__(self, x, y, char, color)
        self.total_ticks = 0
        self.review_count = 0
        self.reputation = 0
        self.fame_level = 0
        self.health = 100 # percent
        self.hunger = 0  # percent; health starts decreasing at 100% hunger
        self.dollars = 20
        self.ticks_between_payments = 20
        self.ticks_between_hunger_ticks = 1
        self.current_business = ''

    def move(self, dmap, dx, dy):
        # move by the given amount, if the destination is not blocked
        if not dmap[self.x + dx][self.y + dy].blocked:
            self.x += dx
            self.y += dy
            self.tick()

    def tick(self):
        self.total_ticks += 1
        if self.total_ticks % self.ticks_between_hunger_ticks == 0:
            self.tick_hunger()
        if self.total_ticks % self.ticks_between_payments == 0 and self.fame_level > 0:
            self.receive_payment()

    def tick_hunger(self):
        if self.health == 0:
            Messenger().message("You are dead.")
        elif self.hunger == 100:
            Messenger().message("You are starving to death.")
            self.health -= 1
        else:
            self.hunger += 1
            if self.hunger > 40 and self.hunger < 80 and self.hunger % 10 == 0:
                Messenger().message('You are hungry.')
            elif self.hunger >= 80 and self.hunger % 3 == 0:
                Messenger().message('You are very hungry.')


    def update_reviewing_stats(self, player_review, business):
        self.review_count += 1
        review_accuracy = business.get_review_similarity(player_review)
        self.reputation += review_accuracy
        previous_fame_level = self.fame_level
        self.fame_level = int(math.floor(self.reputation))
        if self.fame_level > previous_fame_level:
            Messenger().message('You become more famous for your accurate business reviews!')
            Messenger().message('')
        return review_accuracy


    def receive_payment(self):
        payment = int(round(self.review_count * self.reputation))
        self.dollars += payment
        Messenger().message('You received {} dollars from your fans.'.format(payment))



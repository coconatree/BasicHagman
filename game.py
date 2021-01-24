'''
    MIT License

    Copyright (c) 2021 coconatree

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    @author: Coconattree
    @version: 1.0.0
'''

import util

from config import LIFE, WORDS
from util import chooseSecret

class Game:

    def __init__(self):

        self.secret = chooseSecret(WORDS)
        self.life = LIFE
        self.known = "_" * len(self.secret)
        self.tried = ""
        self.won  = False
        self.over = False

    def gameOver(self):

        self.over = True

        if 0 < self.life:
            self.won = True

        text = f'Sorry but you lost !!! \nThe secret word was { self.secret } \n'

        if self.won:
            text = f'You won heyyyy\nThe secret word was { self.secret } \n'

        print(text)

    def guees(self, c):

        if c in self.tried:
            print("You have already guessed that please try another won !!!")

        elif c in self.secret:

            '''
                Updates the known word according to the guessed charachter.
            '''

            self.tried = self.tried + c

            for i in range(len(self.secret)):
                if self.secret[i] == c:
                    self.known = self.known[0:i] + c + self.known[(i+1):]


            print("Correct !!!")

        else:
            self.life = self.life - 1

            print("Wrong sorry :( ")

        if self.life == 0:
            self.won = False
            self.gameOver()
        elif self.known == self.secret:
            self.won = True
            self.gameOver()

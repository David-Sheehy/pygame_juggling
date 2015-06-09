#! /usr/bin/env python3
import pygame
import models


def main():
    # init window
    w = pygame.display.Display() 

    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                return

if __name__ == '__main__':
    main()

# Author: Lau Sheng Cher
# Art from game Hawk: Freedom Squadron

import pyautogui
from mob_spawner import MobSpawner
from player import *
from pyfader import IFader


############  DEFINE SPRITES  ###########

def start_screen():
    img = IFader("", "resources/StartingScreen.png", (70, 70), (98, 213, 245))
    while img.initAlpha <= 255:
        # check for events
        for event in pygame.event.get():
            # this one checks for the window being closed
            if event.type == pygame.QUIT:
                quit()
        img.fadeIn(0.25)
        img.draw(screen, (WIDTH / 2 - 177, HEIGHT // 2 - 135))
        pygame.display.flip()
    while img.initAlpha >= 0:
        # check for events
        for event in pygame.event.get():
            # this one checks for the window being closed
            if event.type == pygame.QUIT:
                quit()
        img.fadeOut(0.25)
        img.draw(screen, (WIDTH / 2 - 177, HEIGHT // 2 - 135))
        pygame.display.flip()

    pyautogui.moveTo(DESKTOP_WIDTH // 2, DESKTOP_HEIGHT // 2 + 200)  # Set the mouse starting position
    main()


def main():
    # Background set up
    background_x, background_y = 0, 0
    background2_x, background2_y = 0, -HEIGHT

    # Define new object
    player = Player(screen)
    player_group.add(player)
    enemy = MobSpawner()
    running = True

    pygame.mixer.music.load("resources/BGM01.wav")
    pygame.mixer.music.set_volume(.5)

    pygame.mixer.music.play(-1, 0.0)

    # my_font = Font()

    while running:
        clock = pygame.time.Clock()
        # check for events
        for event in pygame.event.get():
            # this one checks for the window being closed
            if event.type == pygame.QUIT:
                running = False

        ##### Game logic goes here  #########
        player_group.update()
        enemy.update()
        bullets_group.update()

        # check if bullets hit mobs
        hits = pygame.sprite.groupcollide(bullets_group, enemy.mob_group, True, False, pygame.sprite.collide_mask)
        for bullet, e in hits.items():
            e[0].get_hit(player.dmg)
            player.score.score += e[0].max_hp * player.dmg // 2

        # check if mobs hit player
        hits = pygame.sprite.groupcollide(player_group, enemy.mob_group, False, False, pygame.sprite.collide_mask)
        for ship, e in hits.items():
            if not ship.is_dead:
                if not e[0].is_destroyed:
                    ship.get_hit(e[0].dmg_value)
                e[0].hp = 0
                e[0].get_hit(100000)  # One hit

            else:
                pass

        # #### Draw/update screen ######## #
        # Scrolling background
        background2_y += 1.3  # Speed of backgrounds
        background_y += 1.3
        screen.blit(background, (background_x, background_y))
        screen.blit(background, (background2_x, background2_y))
        if background_y > HEIGHT:
            background_y = -HEIGHT
        if background2_y > HEIGHT:
            background2_y = -HEIGHT

        # Draw player and all sprites
        if not player.is_dead:
            player.shadow.draw(screen, SUN_POSITION)
            # running = False

        bullets_group.draw(screen)
        player_group.draw(screen)
        enemy.mob_group.draw(screen)
        blackBg = pygame.Rect((15, 7), (165, 20))
        pygame.draw.rect(screen, (20, 20, 20), blackBg)
        player.hud.health_bar_group.draw(screen)  # Draw the health bar
        player.hud_group.draw(screen)  # Draw the HUD
        player.score.render()

        # after drawing, flip the display
        pygame.display.flip()
        clock.tick(90)


start_screen()

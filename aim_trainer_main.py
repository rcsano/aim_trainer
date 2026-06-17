import random
import pygame
from aim_trainer_game import WINDOW_WIDTH, WINDOW_HEIGHT, TOP_BAR_HEIGHT, GameStateManager
from aim_target import StandardTarget, GoldenTarget

pygame.init()

GAME_WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Aim Trainer (OOP Compliant Edition)")

TARGET_SPAWN_INTERVAL = 400
TARGET_SPAWN_EVENT = pygame.USEREVENT
TARGET_BORDER_PADDING = 30


def run_aim_trainer():
    is_game_running = True
    active_targets = []
    game_clock = pygame.time.Clock()

    current_game = GameStateManager(total_lives=3)
    pygame.time.set_timer(TARGET_SPAWN_EVENT, TARGET_SPAWN_INTERVAL)

    while is_game_running:
        game_clock.tick(60)
        has_clicked_mouse = False
        current_mouse_position = pygame.mouse.get_pos()

        for game_event in pygame.event.get():
            if game_event.type == pygame.QUIT:
                is_game_running = False
                break

            if game_event.type == TARGET_SPAWN_EVENT:
                random_coordinate_x = random.randint(
                    TARGET_BORDER_PADDING,
                    WINDOW_WIDTH - TARGET_BORDER_PADDING
                )
                random_coordinate_y = random.randint(
                    TARGET_BORDER_PADDING + TOP_BAR_HEIGHT,
                    WINDOW_HEIGHT - TARGET_BORDER_PADDING
                )

                if random.random() < 0.15:
                    new_target = GoldenTarget(random_coordinate_x, random_coordinate_y)
                else:
                    new_target = StandardTarget(random_coordinate_x, random_coordinate_y)

                active_targets.append(new_target)

            if game_event.type == pygame.MOUSEBUTTONDOWN:
                has_clicked_mouse = True
                current_game.total_clicks += 1

        for target_instance in active_targets[:]:
            target_instance.update_size()

            if target_instance.current_size() <= 0:
                active_targets.remove(target_instance)
                current_game.total_misses += 1

            if has_clicked_mouse and target_instance.check_collision(*current_mouse_position):
                active_targets.remove(target_instance)

                if isinstance(target_instance, GoldenTarget):
                    current_game.targets_hit += 2
                else:
                    current_game.targets_hit += 1

        if current_game.total_misses >= current_game.max_lives:
            current_game.show_end_game_screen(GAME_WINDOW)

        current_game.draw_game_background(GAME_WINDOW, active_targets)
        current_game.draw_top_dashboard(GAME_WINDOW)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    run_aim_trainer()
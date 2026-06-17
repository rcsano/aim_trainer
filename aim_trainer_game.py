import math
import time
import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 25, 40)
TOP_BAR_HEIGHT = 50
LABEL_FONT = pygame.font.SysFont("comicsans", 24)


class GameStateManager:
    def __init__(self, total_lives=3):
        self.max_lives = total_lives
        self.targets_hit = 0
        self.total_clicks = 0
        self.total_misses = 0
        self.start_time = time.time()

    def calculate_elapsed_time(self):
        return time.time() - self.start_time

    def format_time_display(self, total_seconds):
        fractional_milliseconds = math.floor(int(total_seconds * 1000 % 1000) / 100)
        formatted_seconds = int(round(total_seconds % 60, 1))
        formatted_minutes = int(total_seconds // 60)
        return f"{formatted_minutes:02d}:{formatted_seconds:02d}.{fractional_milliseconds}"

    def get_centered_horizontal_position(self, surface_element):
        return WINDOW_WIDTH / 2 - surface_element.get_width() / 2

    def draw_game_background(self, game_surface, active_targets):
        game_surface.fill(BACKGROUND_COLOR)
        for dynamic_target in active_targets:
            dynamic_target.draw_target(game_surface)

    def draw_top_dashboard(self, game_surface):
        elapsed_time = self.calculate_elapsed_time()
        pygame.draw.rect(game_surface, "grey", (0, 0, WINDOW_WIDTH, TOP_BAR_HEIGHT))

        time_label = LABEL_FONT.render(f"Time: {self.format_time_display(elapsed_time)}", 1, "black")

        click_speed = round(self.targets_hit / elapsed_time, 1) if elapsed_time > 0 else 0
        speed_label = LABEL_FONT.render(f"Speed: {click_speed} t/s", 1, "black")

        hits_label = LABEL_FONT.render(f"Hits: {self.targets_hit}", 1, "black")
        lives_label = LABEL_FONT.render(f"Lives: {self.max_lives - self.total_misses}", 1, "black")

        game_surface.blit(time_label, (5, 5))
        game_surface.blit(speed_label, (200, 5))
        game_surface.blit(hits_label, (450, 5))
        game_surface.blit(lives_label, (650, 5))

    def show_end_game_screen(self, game_surface):
        game_surface.fill(BACKGROUND_COLOR)
        elapsed_time = self.calculate_elapsed_time()

        time_label = LABEL_FONT.render(f"Time: {self.format_time_display(elapsed_time)}", 1, "white")
        click_speed = round(self.targets_hit / elapsed_time, 1) if elapsed_time > 0 else 0
        speed_label = LABEL_FONT.render(f"Speed: {click_speed} t/s", 1, "white")
        hits_label = LABEL_FONT.render(f"Hits: {self.targets_hit}", 1, "white")

        shooting_accuracy = round(self.targets_hit / self.total_clicks * 100, 1) if self.total_clicks > 0 else 0
        accuracy_label = LABEL_FONT.render(f"Accuracy: {shooting_accuracy}%", 1, "white")

        game_surface.blit(time_label, (self.get_centered_horizontal_position(time_label), 100))
        game_surface.blit(speed_label, (self.get_centered_horizontal_position(speed_label), 200))
        game_surface.blit(hits_label, (self.get_centered_horizontal_position(hits_label), 300))
        game_surface.blit(accuracy_label, (self.get_centered_horizontal_position(accuracy_label), 400))

        pygame.display.update()

        is_waiting = True
        while is_waiting:
            for game_event in pygame.event.get():
                if game_event.type == pygame.QUIT or game_event.type == pygame.KEYDOWN:
                    pygame.quit()
                    quit()
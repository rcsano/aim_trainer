import math
import pygame


class BaseTarget:
    def __init__(self, horizontal_axis_x, vertical_axis_y,
            max_size, growth_rate, target_color):
        self.horizontal_axis_x = horizontal_axis_x
        self.vertical_axis_y = vertical_axis_y
        self._current_size = 0
        self.max_size = max_size
        self.growth_rate = growth_rate
        self.target_color = target_color
        self.is_growing = True

    def current_size(self):
        return self._current_size

    def update_size(self):
        if self._current_size + self.growth_rate >= self.max_size:
                self.is_growing = False
        if self.is_growing:
                self._current_size += self.growth_rate
        else:
                self._current_size -= self.growth_rate

    def draw_target(self, game_surface):
        pass

    def check_collision(self, mouse_x, mouse_y):
        distance_from_center = math.sqrt(
            (mouse_x - self.horizontal_axis_x) ** 2 +
            (mouse_y - self.vertical_axis_y) ** 2
        )
        return distance_from_center <= self._current_size


class StandardTarget(BaseTarget):
    SECOND_COLOR = "white"

    def __init__(self, horizontal_axis_x, vertical_axis_y):
        super().__init__(
            horizontal_axis_x,
            vertical_axis_y,
            max_size=30,
            growth_rate=0.2,
            target_color="red"
        )

    def draw_target(self, game_surface):
        if self._current_size <= 0:
            return
        pygame.draw.circle(game_surface, self.target_color,
                (self.horizontal_axis_x, self.vertical_axis_y), self._current_size)
        pygame.draw.circle(game_surface, self.SECOND_COLOR,
                (self.horizontal_axis_x, self.vertical_axis_y), self._current_size * 0.8)
        pygame.draw.circle(game_surface, self.target_color,
                (self.horizontal_axis_x, self.vertical_axis_y), self._current_size * 0.6)
        pygame.draw.circle(game_surface, self.SECOND_COLOR,
                (self.horizontal_axis_x, self.vertical_axis_y), self._current_size * 0.4)


class GoldenTarget(BaseTarget):
    def __init__(self, horizontal_axis_x, vertical_axis_y):
        super().__init__(
            horizontal_axis_x,
            vertical_axis_y,
            max_size=20,
            growth_rate=0.4,
            target_color="gold"
        )

    def draw_target(self, game_surface):
        if self._current_size <= 0:
            return
        pygame.draw.circle(game_surface, self.target_color, (self.horizontal_axis_x,
                self.vertical_axis_y), self._current_size)
        pygame.draw.circle(game_surface, "black", (self.horizontal_axis_x,
                self.vertical_axis_y), self._current_size * 0.7, 2)
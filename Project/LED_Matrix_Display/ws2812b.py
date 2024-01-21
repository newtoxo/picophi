"""
Author: Newt
"""
import board
import neopixel
import numpy as np
from typing import Union


class Strip:
    def __init__(self, count: int, pin: board = board.D10) -> None:
        self._led = neopixel.NeoPixel(
            pin=pin, n=count, brightness=0.0625, auto_write=False
        )

    def set_led(self, index: Union[int, list], rgb: tuple) -> None:
        if type(index) == int:
            self._led[index] = rgb
        else:
            for i in index:
                self._led[i] = rgb

    def fill_led(self, rgb: tuple) -> None:
        self._led.fill(rgb)

    def display(self):
        self._led.show()


class Pixel:
    def __init__(self, pixel_size: tuple, pin: board = board.D10) -> None:
        self._pixel_width, self._pixel_height = pixel_size
        self._led = neopixel.NeoPixel(
            pin=pin,
            n=self._pixel_width * self._pixel_height,
            brightness=0.0625,
            auto_write=False,
        )
        self._pixel = np.zeros((self._pixel_height, self._pixel_width, 3), dtype=int)

    def draw(self, matrix: np, xy: tuple = (0, 0)) -> None:
        matrix_heigh, matrix_width, _ = matrix.shape
        x, y = xy
        start_x = max(0, x)
        end_x = min(self._pixel_width, x + matrix_width)
        start_y = max(0, y)
        end_y = min(self._pixel_height, y + matrix_heigh)
        cropped_matrix = matrix[start_y - y : end_y - y, start_x - x : end_x - x]
        pixel = np.copy(self._pixel)
        try:
            for y in range(start_y, end_y):
                for x in range(start_x, end_x):
                    value = cropped_matrix[y - start_y, x - start_x]
                    if not np.any(value):
                        continue
                    self._pixel[y, x] = value
        except:
            self._pixel[start_y:end_y, start_x:end_x] = pixel

    def clear(self) -> None:
        self._pixel[:, :] = 0

    def display(self):
        formatted_pixel = np.copy(self._pixel)
        for row in range(0, self._pixel_height, 2):
            formatted_pixel[row, :] = formatted_pixel[row, ::-1]
        for row_index, row in enumerate(formatted_pixel):
            for index, item in enumerate(row):
                self._led[row_index * self._pixel_width + index] = item
        self._led.show()

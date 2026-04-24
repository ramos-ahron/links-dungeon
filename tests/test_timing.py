"""Timing test: the game moves the same distance per second on a fast and a slow machine.

A fake clock stands in for the machine: each drawn frame costs 1000/machine_fps ms,
each logic-only catch-up frame half that. Hold D for 1 second and measure how far
the world scrolled.
"""
import contextlib
import io
import os
import sys
import unittest
from unittest import mock

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pygame

from game import loop, state as game_state
from game.levels import parkour
from game.state import state


def scroll_in_one_second(machine_fps):
    """Pixels the world scrolls while holding D for 1 s on a machine drawing machine_fps frames/s."""
    t = {"now": 0.0, "last": 0.0}
    frame_cost = 1000 / machine_fps

    class FakeClock:
        def tick(self, fps=0):
            if fps:  # like pygame: wait until 1/fps has passed since the last tick
                t["now"] = max(t["now"], t["last"] + 1000 / fps)
            elapsed, t["last"] = t["now"] - t["last"], t["now"]
            return elapsed

    def frame(render=True):
        t["now"] += frame_cost if render else frame_cost / 2
        parkour.frame(render)

    held = []
    def events(*args, **kwargs):
        if not held:
            held.append(True)
            return [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d)]
        return [pygame.event.Event(pygame.QUIT)] if t["now"] >= 1000 else []

    with mock.patch("pygame.time.Clock", FakeClock), mock.patch("pygame.event.get", events), \
            contextlib.redirect_stdout(io.StringIO()):
        loop.init_display()
        game_state.init()
        parkour.setup()
        start = state.wall[0].getX()
        loop.run(state.clock, lambda: state.parkour_enemies, frame)
    return start - state.wall[0].getX()


class TimingTest(unittest.TestCase):
    def test_same_speed_at_30_and_240_fps(self):
        slow, fast = scroll_in_one_second(30), scroll_in_one_second(240)
        self.assertGreater(fast, 100, "player should have walked")
        self.assertLessEqual(abs(slow - fast) / fast, 0.05, f"30 FPS: {slow}px, 240 FPS: {fast}px")

    def test_fast_machine_runs_at_tuned_rate(self):
        # 4 px per game frame while walking; D is pressed at the end of the first frame
        self.assertEqual(scroll_in_one_second(240), 4 * (loop.TUNED_FPS - 1))


if __name__ == "__main__":
    unittest.main()

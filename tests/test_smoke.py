"""Smoke test: start the real game headless, play ~300 frames, quit cleanly."""
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Runs in a fresh process: dummy video driver, hold D to walk, close the window after 300 frames.
CHILD = r"""
import os, sys
sys.path.insert(0, sys.argv[1])
import pygame, main
frames = 0
real_get = pygame.event.get
def get(*args, **kwargs):
    global frames
    real_get()
    frames += 1
    if frames == 1:
        return [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_d)]
    return [pygame.event.Event(pygame.QUIT)] if frames >= 300 else []
pygame.event.get = get
main.main()
print("FRAMES", frames)
"""


class SmokeTest(unittest.TestCase):
    def test_runs_300_frames_and_exits_cleanly(self):
        env = dict(os.environ, SDL_VIDEODRIVER="dummy", SDL_AUDIODRIVER="dummy")
        result = subprocess.run([sys.executable, "-c", CHILD, ROOT], env=env, cwd=os.path.dirname(ROOT),
                                capture_output=True, text=True, timeout=120)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("FRAMES 300", result.stdout)
        self.assertIn("Thanks for playing our game!!!", result.stdout)  # reached the normal ending


if __name__ == "__main__":
    unittest.main()

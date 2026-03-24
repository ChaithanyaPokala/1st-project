import pytest
from playwright.sync_api import sync_playwright, expect, Page
def test_frame(page:Page):
    page.goto("https://demo.automationtesting.in/Frames.html")
    frames=page.frames
    print(len(frames))
    # frame1=page.frame_locator("#singleframe")
    # frame_text=frame1.locator("input[type=text]")
    # frame_text.fill("hfcut")
    page.locator("li a[href='#Multiple']").click()

    frame=page.frame(url="https://demo.automationtesting.in/MultipleFrames.html")
    frames=frame.child_frames
    print("length of frames", len(frames))
    inner_frame=frames[0]
    text_value=inner_frame.locator("input[type='text']")
    text_value.fill("got it")
import turtle
import math
import time

"""
Blooming Chrysanthemum Animation
--------------------------------
Author: [lastvenush]
Description: A procedural animation of a chrysanthemum flower blooming 
using Python's Turtle graphics. It features gradient petals and a 
smooth opening/closing loop.
"""

# --- CONFIGURATION ---
WIDTH, HEIGHT = 600, 800
BG_COLOR = "#1a1a2e" 
STEM_COLOR = "#558b2f"

# Color Palette for Petals (Outer to Inner)
PINK_PALETTE = [
    "#4a0e2e", # Deep Burgundy
    "#881d5a",
    "#c2185b",
    "#e91e63",
    "#f06292",
    "#ffc1e3"  # Soft Pink
]

def setup_screen():
    """Initializes the turtle screen with high performance settings."""
    s = turtle.Screen()
    s.setup(WIDTH, HEIGHT)
    s.bgcolor(BG_COLOR)
    s.title("Blooming Chrysanthemum - Python Turtle")
    s.tracer(0) # Turns off auto-update for smooth animation
    return s

def draw_pointed_shape(t, size, color):
    """Draws a lens/almond shaped petal."""
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    radius = size
    t.circle(radius, 90)
    t.left(90)
    t.circle(radius, 90)
    t.left(90)
    t.end_fill()

def draw_stem_and_leaves(t):
    """Draws the static stem and leaves."""
    t.penup()
    start_y = -350 
    flower_base_y = 100 
    
    t.goto(0, start_y)
    t.setheading(90) 
    
    # Draw Stem
    t.pendown()
    t.pensize(6)
    t.pencolor(STEM_COLOR)
    t.goto(0, flower_base_y)
    
    # Draw Left Leaf
    t.penup()
    t.goto(0, -100)
    t.setheading(135)
    t.pendown()
    draw_pointed_shape(t, 60, STEM_COLOR)
    
    # Draw Right Leaf
    t.penup()
    t.goto(0, -180)
    t.setheading(45)
    t.pendown()
    draw_pointed_shape(t, 50, STEM_COLOR)

    return (0, flower_base_y)

def draw_bloom(t, center_pos, progress):
    """
    Draws the flower head based on bloom progress.
    progress: 0.0 (closed) -> 1.0 (open)
    """
    cx, cy = center_pos
    num_layers = len(PINK_PALETTE)
    
    for i in range(num_layers):
        layer_color = PINK_PALETTE[i]
        
        # Layer Logic
        num_petals = 10 + (i * 2) 
        max_dist = 20 + (i * 18) 
        current_dist = max_dist * progress * 0.8
        petal_size = 20 + (i * 8) 
        
        for j in range(num_petals):
            angle = (360 / num_petals) * j
            angle_offset = (i * 15) 
            final_angle = angle + angle_offset
            
            rad = math.radians(final_angle)
            px = cx + math.cos(rad) * current_dist
            py = cy + math.sin(rad) * current_dist
            
            t.penup()
            t.goto(px, py)
            t.setheading(final_angle - 45)
            t.pendown()
            draw_pointed_shape(t, petal_size, layer_color)

def main():
    screen = setup_screen()
    t = turtle.Turtle()
    t.hideturtle()
    
    bloom_progress = 0.0
    direction = 1
    speed = 0.01
    
    print("Animation started... Press Ctrl+C to stop.")
    
    while True:
        try:
            t.clear()
            center = draw_stem_and_leaves(t)
            draw_bloom(t, center, bloom_progress)
            screen.update()
            
            bloom_progress += speed * direction
            
            if bloom_progress >= 1.0:
                bloom_progress = 1.0
                time.sleep(1.5)
                direction = -1
            elif bloom_progress <= 0.0:
                bloom_progress = 0.0
                time.sleep(0.5)
                direction = 1
                
        except (turtle.Terminator, tk.TclError):
            break

if __name__ == "__main__":
    import tkinter as tk # Safety import for error handling
    main()
import pygame
import random
import sys
from datetime import datetime

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 700
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Epic Fishing Adventure")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 24)
title_font = pygame.font.SysFont("Arial", 72, bold=True)

# Colors
SKY_BLUE = (135, 206, 235)
WATER_BLUE = (0, 105, 148)
DEEP_BLUE = (0, 50, 100)
SAND = (194, 178, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player stats
class Player:
    def __init__(self):
        self.money = 500
        self.rod_level = 1
        self.reel_level = 1
        self.line_level = 1
        self.best_catch = 0
        self.catches = []

    def get_rod_power(self):
        return 10 + self.rod_level * 8

    def get_reel_speed(self):
        return 2 + self.reel_level * 1.5

    def get_line_strength(self):
        return 15 + self.line_level * 12

player = Player()

# Fish data
fish_types = [
    {"name": "Bluegill", "rarity": "Common", "min_weight": 0.5, "max_weight": 2, "value": 20, "color": (100, 180, 100)},
    {"name": "Bass", "rarity": "Common", "min_weight": 2, "max_weight": 8, "value": 50, "color": (50, 100, 200)},
    {"name": "Trout", "rarity": "Uncommon", "min_weight": 3, "max_weight": 12, "value": 80, "color": (180, 200, 220)},
    {"name": "Salmon", "rarity": "Uncommon", "min_weight": 8, "max_weight": 25, "value": 150, "color": (220, 100, 50)},
    {"name": "Tuna", "rarity": "Rare", "min_weight": 20, "max_weight": 60, "value": 400, "color": (0, 120, 200)},
    {"name": "Marlin", "rarity": "Epic", "min_weight": 50, "max_weight": 150, "value": 1200, "color": (100, 50, 200)},
    {"name": "Shark", "rarity": "Legendary", "min_weight": 100, "max_weight": 400, "value": 5000, "color": (80, 80, 80)}
]

# Maps
maps = ["Pier", "Boat", "Ocean"]
current_map = 0

# Game states
MENU = "menu"
PLAYING = "playing"
FISHING = "fishing"
CATCH = "catch"
SHOP = "shop"
LEADERBOARD = "leaderboard"
game_state = MENU

# Fishing variables
line_length = 0
fish_on_line = None
fight_progress = 0
reeling = False
bite_timer = 0

# Animation
catch_animation_time = 0
caught_fish = None

def draw_background():
    pygame.draw.rect(screen, SKY_BLUE, (0, 0, WIDTH, HEIGHT//2 + 50))
    pygame.draw.circle(screen, (255, 220, 0), (WIDTH - 150, 120), 50)
    
    water_y = HEIGHT//2 + 50
    pygame.draw.rect(screen, WATER_BLUE, (0, water_y, WIDTH, HEIGHT - water_y))
    
    for i in range(8):
        wave_y = water_y + 30 + i*20
        pygame.draw.line(screen, (0, 160, 200), (0, wave_y), (WIDTH, wave_y + 10), 8)
    
    if maps[current_map] == "Pier":
        pygame.draw.rect(screen, (139, 69, 19), (100, water_y - 80, WIDTH - 200, 100))
        for i in range(5):
            pygame.draw.rect(screen, SAND, (150 + i*180, water_y - 40, 40, 120))
    elif maps[current_map] == "Boat":
        pygame.draw.polygon(screen, (200, 100, 50), [(300, water_y-60), (900, water_y-60), (850, water_y+30), (350, water_y+30)])
        pygame.draw.rect(screen, (100, 50, 30), (500, water_y-120, 150, 80))
    else:
        pygame.draw.rect(screen, DEEP_BLUE, (0, water_y-100, WIDTH, 120))

def draw_player():
    player_x = 150
    pygame.draw.circle(screen, (255, 220, 180), (player_x, 380), 25)
    pygame.draw.line(screen, (50, 50, 150), (player_x, 405), (player_x, 520), 12)
    pygame.draw.line(screen, (50, 50, 150), (player_x, 450), (player_x-40, 480), 10)

def get_random_fish():
    weights = [0.4, 0.3, 0.15, 0.08, 0.04, 0.02, 0.01]
    return random.choices(fish_types, weights=weights)[0]

def start_fishing():
    global line_length, fish_on_line, bite_timer
    line_length = 0
    fish_on_line = None
    bite_timer = random.randint(60, 240)

def update_fishing():
    global line_length, fish_on_line, bite_timer, fight_progress, reeling
    
    if fish_on_line is None:
        line_length = min(line_length + 8, 550)
        bite_timer -= 1
        if bite_timer <= 0:
            fish_on_line = get_random_fish()
            fight_progress = 30 + random.randint(20, 80)
    
    if fish_on_line and reeling:
        reel_speed = player.get_reel_speed()
        fight_progress -= reel_speed
        line_length = max(0, line_length - reel_speed * 2)
        
        if fight_progress <= 0:
            return True
        elif random.random() < 0.015:
            if random.random() * 100 > player.get_line_strength():
                fish_on_line = None
                return False
    return False

def draw_fishing_line():
    start_x = 170
    start_y = 420
    end_x = start_x + 120 + line_length * 0.7
    end_y = 520 + line_length * 0.4
    pygame.draw.line(screen, (200, 200, 220), (start_x, start_y), (end_x, end_y), 4)
    
    if fish_on_line:
        fish_x = end_x - 20
        fish_y = end_y + 20
        pygame.draw.ellipse(screen, fish_on_line["color"], (fish_x, fish_y, 60, 25))
        pygame.draw.circle(screen, WHITE, (fish_x + 45, fish_y + 12), 5)

def show_catch_screen():
    global catch_animation_time, caught_fish
    screen.fill((0, 0, 0))
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((20, 40, 80))
    screen.blit(overlay, (0, 0))
    
    anim_progress = min(1.0, catch_animation_time / 90)
    fish_size = int(80 + 40 * anim_progress)
    fish_x = WIDTH//2 - fish_size//2 + int(50 * (anim_progress - 0.5))
    fish_y = HEIGHT//2 - 80 + int(30 * pygame.math.sin(catch_animation_time / 8))
    
    pygame.draw.ellipse(screen, caught_fish["color"], (fish_x, fish_y, fish_size, fish_size//2.5))
    pygame.draw.polygon(screen, caught_fish["color"], [
        (fish_x + fish_size, fish_y + fish_size//5),
        (fish_x + fish_size + 40, fish_y + fish_size//2.5),
        (fish_x + fish_size, fish_y + fish_size//1.3)
    ])
    
    title = title_font.render("FISH CAUGHT!", True, GOLD)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 80))
    
    name_text = font.render(f"{caught_fish['name']} - {caught_fish['rarity']}", True, WHITE)
    screen.blit(name_text, (WIDTH//2 - name_text.get_width()//2, 220))
    
    weight = random.uniform(caught_fish["min_weight"], caught_fish["max_weight"])
    weight_text = font.render(f"Weight: {weight:.1f} lbs", True, WHITE)
    screen.blit(weight_text, (WIDTH//2 - weight_text.get_width()//2, 270))
    
    money_earned = int(caught_fish["value"] * (weight / 10))
    money_text = font.render(f"Earned: ${money_earned}", True, GOLD)
    screen.blit(money_text, (WIDTH//2 - money_text.get_width()//2, 320))
    
    global player
    player.money += money_earned
    if weight > player.best_catch:
        player.best_catch = weight
    player.catches.append((caught_fish["name"], weight, datetime.now().strftime("%m/%d %H:%M")))
    
    catch_animation_time += 1
    return catch_animation_time > 180

def draw_shop():
    screen.fill((20, 40, 60))
    title = title_font.render("FISHING SHOP", True, GOLD)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 40))
    
    items = [
        ("Rod", "Better casting & fighting", 150 * player.rod_level),
        ("Reel", "Faster reeling", 120 * player.reel_level),
        ("Line", "Stronger line", 90 * player.line_level)
    ]
    
    for i, (name, desc, base_cost) in enumerate(items):
        y = 180 + i * 110
        level = getattr(player, name.lower() + "_level")
        cost = base_cost * level
        can_buy = level < 5 and player.money >= cost
        
        pygame.draw.rect(screen, (40, 60, 90), (150, y, 900, 90))
        name_txt = font.render(f"{name} (Level {level + 1})", True, WHITE)
        screen.blit(name_txt, (200, y + 15))
        desc_txt = small_font.render(desc, True, WHITE)
        screen.blit(desc_txt, (200, y + 55))
        cost_txt = font.render(f"${cost}", True, GOLD if can_buy else RED)
        screen.blit(cost_txt, (780, y + 25))
        
        if can_buy:
            buy_txt = small_font.render("Click to BUY", True, GREEN)
            screen.blit(buy_txt, (780, y + 65))

def handle_shop_click(pos):
    x, y = pos
    for i in range(3):
        item_y = 180 + i * 110
        if item_y < y < item_y + 90:
            name = ["rod", "reel", "line"][i]
            level = getattr(player, name + "_level")
            cost = [150, 120, 90][i] * level
            if level < 5 and player.money >= cost:
                player.money -= cost
                setattr(player, name + "_level", level + 1)
                return True
    return False

def draw_leaderboard():
    screen.fill((10, 30, 50))
    title = title_font.render("BIGGEST CATCHES", True, GOLD)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 40))
    
    sorted_catches = sorted(player.catches, key=lambda x: x[1], reverse=True)[:10]
    
    for i, (name, weight, date) in enumerate(sorted_catches):
        y = 160 + i * 55
        text = font.render(f"{i+1}. {name} — {weight:.1f} lbs   ({date})", True, WHITE)
        screen.blit(text, (150, y))
    
    if not sorted_catches:
        empty = font.render("No catches yet. Go fishing!", True, WHITE)
        screen.blit(empty, (WIDTH//2 - empty.get_width()//2, 300))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game_state in [PLAYING, FISHING, CATCH]:
                    game_state = PLAYING
                else:
                    running = False
            elif event.key == pygame.K_1 and game_state == MENU:
                game_state = PLAYING
            elif event.key == pygame.K_b and game_state == PLAYING:
                game_state = SHOP
            elif event.key == pygame.K_l and game_state == PLAYING:
                game_state = LEADERBOARD
            elif event.key == pygame.K_m and game_state == PLAYING:
                current_map = (current_map + 1) % 3
            elif event.key == pygame.K_SPACE:
                if game_state == PLAYING:
                    start_fishing()
                    game_state = FISHING
                elif game_state == FISHING and fish_on_line:
                    reeling = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == SHOP:
                handle_shop_click(event.pos)
            elif game_state == PLAYING:
                start_fishing()
                game_state = FISHING
            elif game_state == FISHING and fish_on_line:
                reeling = True
            elif game_state == CATCH:
                game_state = PLAYING
                catch_animation_time = 0
                caught_fish = None

    screen.fill(BLACK)
    
    if game_state == MENU:
        draw_background()
        draw_player()
        title = title_font.render("EPIC FISHING", True, GOLD)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 120))
        subtitle = font.render("Press 1 to Start", True, WHITE)
        screen.blit(subtitle, (WIDTH//2 - subtitle.get_width()//2, 280))
        controls = small_font.render("B: Shop  |  L: Leaderboard  |  M: Change Map  |  SPACE: Cast", True, WHITE)
        screen.blit(controls, (WIDTH//2 - controls.get_width()//2, 420))
    
    elif game_state == PLAYING:
        draw_background()
        draw_player()
        money_text = font.render(f"Money: ${player.money}", True, GOLD)
        screen.blit(money_text, (20, 20))
        map_text = font.render(f"Location: {maps[current_map]}", True, WHITE)
        screen.blit(map_text, (20, 70))
        best_text = font.render(f"Best: {player.best_catch:.1f} lbs", True, WHITE)
        screen.blit(best_text, (WIDTH - 280, 20))
        instr = small_font.render("Click or SPACE to Cast", True, WHITE)
        screen.blit(instr, (WIDTH//2 - 120, HEIGHT - 50))
    
    elif game_state == FISHING:
        draw_background()
        draw_player()
        draw_fishing_line()
        money_text = font.render(f"Money: ${player.money}", True, GOLD)
        screen.blit(money_text, (20, 20))
        
        if fish_on_line:
            fight_text = font.render("FISH ON! Hold SPACE / Click to Reel!", True, RED)
            screen.blit(fight_text, (WIDTH//2 - fight_text.get_width()//2, 80))
            bar_width = 400
            progress = max(0, fight_progress / 150 * bar_width)
            pygame.draw.rect(screen, RED, (WIDTH//2 - bar_width//2, 140, bar_width, 30))
            pygame.draw.rect(screen, GREEN, (WIDTH//2 - bar_width//2, 140, progress, 30))
        else:
            instr = font.render("Line cast... Waiting for bite...", True, WHITE)
            screen.blit(instr, (WIDTH//2 - instr.get_width()//2, 100))
        
        caught = update_fishing()
        if caught and fish_on_line:
            caught_fish = fish_on_line
            game_state = CATCH
            catch_animation_time = 0
            fish_on_line = None
            reeling = False
        elif caught is False and fish_on_line is None:
            game_state = PLAYING
            fish_on_line = None
            reeling = False
    
    elif game_state == CATCH:
        if show_catch_screen():
            game_state = PLAYING
            catch_animation_time = 0
            caught_fish = None
    
    elif game_state == SHOP:
        draw_shop()
        money_text = font.render(f"Money: ${player.money}", True, GOLD)
        screen.blit(money_text, (WIDTH//2 - 100, 120))
    
    elif game_state == LEADERBOARD:
        draw_leaderboard()
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

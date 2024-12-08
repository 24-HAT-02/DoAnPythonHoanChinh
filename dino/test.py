# Import thư viện
import pygame

pygame.init()
clock = pygame.time.Clock()

# Tiêu đề và icon
pygame.display.set_caption('Dino game')
icon = pygame.image.load(r'assets/dinosaur.png')
pygame.display.set_icon(icon)

# Cửa sổ game
screen = pygame.display.set_mode((600, 300))

# Background game
bg = pygame.image.load(r'assets/background.jpg')
tree = pygame.image.load(r'assets/tree.png')
dino = pygame.image.load(r'assets/dinosaur.png')

# Thêm âm thanh
sound1 = pygame.mixer.Sound(r'sound/tick.wav')
sound2 = pygame.mixer.Sound(r'sound/te.wav')

# Khởi tạo
score, hscore = 0, 0
bg_x, bg_y = 0, 0
tree_x, tree_y = 550, 230
dino_x, dino_y = 0, 230
x_def = 5
y_def = 7
jump = False
gameplay = True
passed_tree = False  # Cờ đánh dấu khủng long đã vượt qua cây

# Kiểm tra va chạm
def check():
    if dino_hcn.colliderect(tree_hcn):
        pygame.mixer.Sound.play(sound2)
        return False
    return True

# Hiển thị điểm số
game_font = pygame.font.Font('04B_19.TTF', 20)

def score_view():
    if gameplay:
        score_txt = game_font.render(f'Score: {int(score)}', True, (255, 0, 0))
        screen.blit(score_txt, (175, 20))
        hscore_txt = game_font.render(f'High Score: {int(hscore)}', True, (255, 0, 0))
        screen.blit(hscore_txt, (270, 20))
    else:
        score_txt = game_font.render(f'Score: {int(score)}', True, (255, 0, 0))
        screen.blit(score_txt, (175, 20))
        hscore_txt = game_font.render(f'High Score: {int(hscore)}', True, (255, 0, 0))
        screen.blit(hscore_txt, (270, 20))
        gameover_txt = game_font.render('GAME OVER', True, (255, 0, 0))
        screen.blit(gameover_txt, (240, 100))

# Vòng lặp xử lý game
running = True
while running:
    # Setting FPS
    clock.tick(60)

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gameplay and dino_y == 230:
                    jump = True
                    pygame.mixer.Sound.play(sound1)
                elif not gameplay:
                    gameplay = True
                    score = 0
                    tree_x = 550
                    passed_tree = False

    # Cập nhật game
    if gameplay:
        # Background
        screen.blit(bg, (bg_x, bg_y))
        screen.blit(bg, (bg_x + 600, bg_y))
        bg_x -= x_def
        if bg_x <= -600:
            bg_x = 0

        # Cây
        tree_hcn = screen.blit(tree, (tree_x, tree_y))
        tree_x -= x_def
        if tree_x <= -20:
            tree_x = 550
            passed_tree = False  # Reset cờ khi cây quay lại

        # Khủng long
        dino_hcn = screen.blit(dino, (dino_x, dino_y))
        if jump and dino_y >= 80:
            dino_y -= y_def
        else:
            jump = False
        if not jump and dino_y < 230:
            dino_y += y_def

        # Cập nhật điểm
        if tree_x + tree.get_width() < dino_x and not passed_tree:
            score += 1  # Tăng điểm khi khủng long vượt qua cây
            passed_tree = True  # Đánh dấu cây đã được vượt qua
        if hscore < score:
            hscore = score

        # Kiểm tra va chạm
        gameplay = check()

    else:
        # Game over
        screen.blit(bg, (0, 0))
        tree_hcn = screen.blit(tree, (tree_x, tree_y))
        dino_hcn = screen.blit(dino, (dino_x, dino_y))
        score_view()

    # Hiển thị điểm
    score_view()

    # Cập nhật màn hình
    pygame.display.update()

pygame.quit()

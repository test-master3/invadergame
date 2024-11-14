import pygame

# Pygameを初期化
pygame.init()

# ウィンドウのサイズを設定
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# ウィンドウを作成
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygameウィンドウ")

# メインループ
running = True
while running:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 画面を白色で塗りつぶす
    screen.fill((255, 255, 255))

    # 画面を更新
    pygame.display.flip()

# Pygameを終了
pygame.quit()
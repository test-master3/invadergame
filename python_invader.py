import pygame
import sys
import random

# 初期化
pygame.init()

# 画面設定
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("スペースインベーダー")

# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# プレイヤークラス
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_WIDTH // 2
        self.rect.y = WINDOW_HEIGHT - 60
        self.speed = 5
        self.lives = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.speed

# インベーダークラス
class Invader(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.direction = 1
        self.drop_speed = 20  # 下に移動する速度を追加

    def update(self):
        self.rect.x += self.speed * self.direction
        # 画面端に到達したかチェック
        if self.rect.right >= WINDOW_WIDTH or self.rect.left <= 0:
            self.direction *= -1  # 方向転換
            self.rect.y += self.drop_speed  # 下に移動

# 弾クラス
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([5, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 7

    def update(self):
        self.rect.y -= self.speed

# スプライトグループの作成
all_sprites = pygame.sprite.Group()
invaders = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# プレイヤーの作成
player = Player()
all_sprites.add(player)

# インベーダーの配置
for row in range(5):
    for column in range(8):
        invader = Invader(column * 80 + 100, row * 50 + 50)
        all_sprites.add(invader)
        invaders.add(invader)

# スコア初期化
score = 0
font = pygame.font.Font(None, 36)

# ... existing code ...

# ゲームループ
clock = pygame.time.Clock()
running = True
game_clear = False  # ゲームクリアフラグを追加

while running:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_clear:  # ゲームクリア時は弾を撃てないように
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
            elif event.key == pygame.K_ESCAPE:
                running = False

    # 更新処理
    if not game_clear:  # ゲームクリア時は更新しない
        all_sprites.update()

    # 衝突判定
    hits = pygame.sprite.groupcollide(invaders, bullets, True, True)
    for hit in hits:
        score += 100

    # ゲームクリアチェック
    if len(invaders) == 0:
        game_clear = True

    # 描画処理
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # スコア表示
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # ライフ表示
    life_text = font.render(f"Lives: {player.lives}", True, WHITE)
    screen.blit(life_text, (10, 40))
    # ゲームクリアメッセージ
    if game_clear:
        clear_text = font.render("GAME CLEAR!", True, GREEN)
        clear_rect = clear_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        screen.blit(clear_text, clear_rect)

    pygame.display.flip()
    clock.tick(60)

# ... existing code ...

pygame.quit()
sys.exit()

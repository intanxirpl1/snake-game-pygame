import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 400
GRID_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Project Snake")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WARNA_ULER = [
    (40, 130, 220),
    (120, 60, 200),
    (255, 105, 180),
    (50, 205, 50),
    (255, 165, 0),
    (0, 200, 200),
    (255, 215, 0)
]

JENIS_MAKANAN = [
    "apel",
    "pizza",
    "burger",
    "donat",
    "semangka",
    "kentang",
    "ayam"
]

EYE_WHITE = (255, 255, 255)
EYE_BLACK = (0, 0, 0)

font = pygame.font.SysFont("arial", 25)
game_over_font = pygame.font.SysFont("arial", 50)
small_font = pygame.font.SysFont("arial", 20)


def buat_posisi_acak_makanan():
    kolom_maks = WIDTH // GRID_SIZE
    baris_maks = HEIGHT // GRID_SIZE

    x = random.randint(0, kolom_maks - 1) * GRID_SIZE
    y = random.randint(0, baris_maks - 1) * GRID_SIZE

    return pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)


def gambar_makanan(rect, jenis):

    x = rect.x
    y = rect.y
    tengah_x = x + GRID_SIZE // 2
    tengah_y = y + GRID_SIZE // 2

    if jenis == "apel":

        pygame.draw.circle(
            screen,
            (220, 30, 30),
            (tengah_x, tengah_y + 2),
            8
        )

        pygame.draw.line(
            screen,
            (80, 45, 20),
            (tengah_x, tengah_y - 5),
            (tengah_x + 2, tengah_y - 10),
            2
        )

        pygame.draw.ellipse(
            screen,
            (40, 180, 60),
            (tengah_x + 2, tengah_y - 10,
             7, 4)
        )

    elif jenis == "pizza":

        titik = [
            (x + 10, y + 1),
            (x + 1, y + 18),
            (x + 19, y + 18)
        ]

        pygame.draw.polygon(
            screen,
            (255, 190, 60),
            titik
        )

        pygame.draw.line(
            screen,
            (180, 100, 30),
            (x + 1, y + 18),
            (x + 19, y + 18),
            3
        )

        pygame.draw.circle(
            screen,
            (220, 40, 40),
            (x + 8, y + 12),
            2
        )

        pygame.draw.circle(
            screen,
            (220, 40, 40),
            (x + 13, y + 8),
            2
        )

    elif jenis == "burger":

        pygame.draw.ellipse(
            screen,
            (230, 160, 60),
            (x + 2, y + 2, 16, 7)
        )

        pygame.draw.rect(
            screen,
            (50, 180, 70),
            (x + 2, y + 8, 16, 3)
        )

        pygame.draw.rect(
            screen,
            (130, 70, 30),
            (x + 2, y + 11, 16, 5)
        )

        pygame.draw.ellipse(
            screen,
            (230, 160, 60),
            (x + 2, y + 15, 16, 4)
        )

    elif jenis == "donat":

        pygame.draw.circle(
            screen,
            (210, 130, 70),
            (tengah_x, tengah_y),
            8
        )

        pygame.draw.circle(
            screen,
            (245, 190, 130),
            (tengah_x, tengah_y),
            3
        )

        pygame.draw.circle(
            screen,
            (255, 100, 150),
            (x + 7, y + 7),
            1
        )

        pygame.draw.circle(
            screen,
            (100, 180, 255),
            (x + 14, y + 12),
            1
        )

    elif jenis == "semangka":

        pygame.draw.arc(
    screen,
    (40, 180, 70),
    (x + 1, y + 2, x + 19, y + 20),
    0,
    3.14,
    8
)

        pygame.draw.line(
    screen,
    (40, 180, 70),
    (x + 1, y + 11),
    (x + 19, y + 11),
    8
)
        pygame.draw.arc(
            screen,
            (20, 120, 40),
            (x + 1, y + 2, x + 19, y + 20),
            0,
            3.14,
            2
        )

        pygame.draw.circle(
            screen,
            BLACK,
            (x + 7, y + 10),
            1
        )

        pygame.draw.circle(
            screen,
            BLACK,
            (x + 12, y + 10),
            1
        )

    elif jenis == "kentang":

        pygame.draw.rect(
            screen,
            (240, 200, 80),
            (x + 4, y + 2, 3, 16)
        )

        pygame.draw.rect(
            screen,
            (255, 220, 100),
            (x + 8, y + 1, 3, 18)
        )

        pygame.draw.rect(
            screen,
            (230, 180, 60),
            (x + 12, y + 3, 3, 16)
        )

        pygame.draw.rect(
            screen,
            (245, 205, 80),
            (x + 16, y + 4, 3, 14)
        )

    elif jenis == "ayam":

        pygame.draw.circle(
            screen,
            (245, 190, 120),
            (tengah_x - 2, tengah_y),
            7
        )

        pygame.draw.circle(
            screen,
            (245, 190, 120),
            (x + 15, y + 7),
            5
        )

        pygame.draw.circle(
            screen,
            BLACK,
            (x + 16, y + 6),
            1
        )

        pygame.draw.polygon(
            screen,
            (240, 150, 30),
            [
                (x + 19, y + 8),
                (x + 16, y + 10),
                (x + 19, y + 11)
            ]
        )


def reset_game():

    snake = [
        pygame.Rect(300, 200, GRID_SIZE, GRID_SIZE),
        pygame.Rect(280, 200, GRID_SIZE, GRID_SIZE),
        pygame.Rect(260, 200, GRID_SIZE, GRID_SIZE)
    ]

    arah = (GRID_SIZE, 0)

    makanan = []

    for i in range(7):

        makanan.append([
            buat_posisi_acak_makanan(),
            random.choice(JENIS_MAKANAN)
        ])

    skor = 0

    return snake, arah, makanan, skor


snake, arah, makanan, skor = reset_game()

warna_uler = random.choice(WARNA_ULER)

game_over = False
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if not game_over:

                if event.key in (pygame.K_UP, pygame.K_w):

                    if arah != (0, GRID_SIZE):
                        arah = (0, -GRID_SIZE)

                elif event.key in (pygame.K_DOWN, pygame.K_s):

                    if arah != (0, -GRID_SIZE):
                        arah = (0, GRID_SIZE)

                elif event.key in (pygame.K_LEFT, pygame.K_a):

                    if arah != (GRID_SIZE, 0):
                        arah = (-GRID_SIZE, 0)

                elif event.key in (pygame.K_RIGHT, pygame.K_d):

                    if arah != (-GRID_SIZE, 0):
                        arah = (GRID_SIZE, 0)

            else:

                if event.key == pygame.K_r:

                    snake, arah, makanan, skor = reset_game()
                    warna_uler = random.choice(WARNA_ULER)
                    game_over = False

                elif event.key == pygame.K_ESCAPE:

                    running = False

    if not game_over:

        kepala_lama = snake[0]

        head_rect = pygame.Rect(
            kepala_lama.x + arah[0],
            kepala_lama.y + arah[1],
            GRID_SIZE,
            GRID_SIZE
        )

        snake.insert(0, head_rect)

        makanan_dimakan = None

        for i, data_makanan in enumerate(makanan):

            food_rect = data_makanan[0]

            if head_rect.colliderect(food_rect):

                makanan_dimakan = i
                break

        if makanan_dimakan is not None:

            makanan[makanan_dimakan] = [
                buat_posisi_acak_makanan(),
                random.choice(JENIS_MAKANAN)
            ]

            skor += 1

            warna_uler = random.choice(WARNA_ULER)

        else:

            snake.pop()

        if (
            head_rect.left < 0
            or head_rect.right > WIDTH
            or head_rect.top < 0
            or head_rect.bottom > HEIGHT
        ):

            game_over = True

        for bagian_tubuh in snake[1:]:

            if head_rect.colliderect(bagian_tubuh):

                game_over = True
                break

        if not game_over:

            for i, data_makanan in enumerate(makanan):

                food_rect = data_makanan[0]

                for bagian_tubuh in snake:

                    if food_rect.colliderect(bagian_tubuh):

                        makanan[i] = [
                            buat_posisi_acak_makanan(),
                            random.choice(JENIS_MAKANAN)
                        ]

                        break

    screen.fill((135, 206, 235))

    for x in range(0, WIDTH, GRID_SIZE):

        pygame.draw.line(
            screen,
            WHITE,
            (x, 0),
            (x, HEIGHT)
        )

    for y in range(0, HEIGHT, GRID_SIZE):

        pygame.draw.line(
            screen,
            WHITE,
            (0, y),
            (WIDTH, y)
        )

    for data_makanan in makanan:

        food_rect = data_makanan[0]
        jenis_makanan = data_makanan[1]

        gambar_makanan(
            food_rect,
            jenis_makanan
        )

    for bagian in snake:

        pygame.draw.rect(
            screen,
            warna_uler,
            bagian
        )

        pygame.draw.rect(
            screen,
            BLACK,
            bagian,
            1
        )

    kepala = snake[0]

    if arah == (GRID_SIZE, 0):

        mata1 = (kepala.right - 6, kepala.top + 6)
        mata2 = (kepala.right - 6, kepala.bottom - 6)

    elif arah == (-GRID_SIZE, 0):

        mata1 = (kepala.left + 6, kepala.top + 6)
        mata2 = (kepala.left + 6, kepala.bottom - 6)

    elif arah == (0, -GRID_SIZE):

        mata1 = (kepala.left + 6, kepala.top + 6)
        mata2 = (kepala.right - 6, kepala.top + 6)

    else:

        mata1 = (kepala.left + 6, kepala.bottom - 6)
        mata2 = (kepala.right - 6, kepala.bottom - 6)

    pygame.draw.circle(
        screen,
        EYE_WHITE,
        mata1,
        4
    )

    pygame.draw.circle(
        screen,
        EYE_WHITE,
        mata2,
        4
    )

    pygame.draw.circle(
        screen,
        EYE_BLACK,
        mata1,
        2
    )

    pygame.draw.circle(
        screen,
        EYE_BLACK,
        mata2,
        2
    )

    teks_skor = font.render(
        "Skor: " + str(skor),
        True,
        WHITE
    )

    screen.blit(
        teks_skor,
        (10, 10)
    )

    kecepatan = 5 + (skor // 3)

    if kecepatan > 18:
        kecepatan = 18

    if game_over:

        overlay = pygame.Surface(
            (WIDTH, HEIGHT)
        )

        overlay.set_alpha(160)
        overlay.fill(BLACK)

        screen.blit(
            overlay,
            (0, 0)
        )

        teks_game_over = game_over_font.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )

        teks_skor_akhir = font.render(
            "Skor: " + str(skor),
            True,
            WHITE
        )

        teks_restart = small_font.render(
            "Tekan R untuk bermain lagi",
            True,
            WHITE
        )

        teks_keluar = small_font.render(
            "Tekan ESC untuk keluar",
            True,
            WHITE
        )

        screen.blit(
            teks_game_over,
            (
                WIDTH // 2 - teks_game_over.get_width() // 2,
                110
            )
        )

        screen.blit(
            teks_skor_akhir,
            (
                WIDTH // 2 - teks_skor_akhir.get_width() // 2,
                180
            )
        )

        screen.blit(
            teks_restart,
            (
                WIDTH // 2 - teks_restart.get_width() // 2,
                230
            )
        )

        screen.blit(
            teks_keluar,
            (
                WIDTH // 2 - teks_keluar.get_width() // 2,
                260
            )
        )

    pygame.display.update()

    clock.tick(kecepatan)

pygame.quit()
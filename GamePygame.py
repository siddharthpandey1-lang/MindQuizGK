import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup for 1080p and 60 FPS
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MindQuizGk - General Knowledge Quiz Game")
clock = pygame.time.Clock()

# Fonts and colors
font = pygame.font.SysFont("arial", 40)
big_font = pygame.font.SysFont("arial", 64)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
LIGHT_GRAY = (240, 240, 240)

# Questions and answers
quiz = [
    ("Who was the Indian to score a double century in Test cricket?", "sachin tendulkar"),
    ("Who was the first president of U.S.A?", "george washington"),
    ("Which planet is known as the Red Planet?", "mars"),
    ("What is the largest mammal in the world?", "blue whale"),
    ("What is the capital of France?", "paris"),
    ("Who wrote 'Romeo and Juliet'?", "william shakespeare"),
    ("What is the smallest prime number?", "2"),
    ("What is the chemical symbol for water?", "h2o"),
    ("Who painted the Mona Lisa?", "leonardo da vinci"),
    ("What is the hardest natural substance on Earth?", "diamond"),
    ("What is the main ingredient in traditional Japanese miso soup?", "miso paste"),
    ("Which element has the chemical symbol 'O'?", "oxygen"),
    ("What is the largest organ in the human body?", "skin"),
    ("In which year did the Titanic sink?", "1912"),
    ("What is the capital city of Australia?", "canberra"),
    ("Who discovered penicillin?", "alexander fleming"),
    ("What is the smallest country in the world?", "vatican city"),
    ("Which planet has the most moons?", "saturn"),
    ("What is the currency of Japan?", "yen"),
    ("Who is known as the 'Father of Computers'?", "charles babbage")
]

# Game state
current_question = 0
user_input = ""
feedback = ""
score = 0

def draw_text(text, font, color, x, y):
    rendered = font.render(text, True, color)
    screen.blit(rendered, (x, y))

# Main loop
running = True
while running:
    clock.tick(60)  # Maintain 60 FPS
    screen.fill(LIGHT_GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                correct_answer = quiz[current_question][1]
                if user_input.lower().strip() == correct_answer.lower():
                    feedback = "✅ Correct!"
                    score += 1
                else:
                    feedback = f"❌ Incorrect. Correct answer: {correct_answer.title()}"
                current_question += 1
                user_input = ""
                if current_question >= len(quiz):
                    feedback = f"🎉 Quiz Completed! Your score: {score}/{len(quiz)}"
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    # Draw UI box
    pygame.draw.rect(screen, WHITE, (100, 100, WIDTH - 200, HEIGHT - 300), border_radius=20)
    pygame.draw.rect(screen, BLUE, (100, 100, WIDTH - 200, HEIGHT - 300), 6, border_radius=20)

    # Display content
    if current_question < len(quiz):
        draw_text("MindQuizGk - General Knowledge Quiz", big_font, BLUE, 120, 120)
        draw_text(f"Score: {score}", font, BLACK, WIDTH - 300, 130)
        draw_text("Type your answer and press Enter", font, BLACK, 120, 200)
        draw_text("Q: " + quiz[current_question][0], font, BLACK, 120, 280)
        draw_text("Your answer: " + user_input, font, BLACK, 120, 360)
    else:
        draw_text(feedback, big_font, GREEN if "Completed" in feedback else RED, 120, HEIGHT // 2 - 50)

    draw_text(feedback, font, GREEN if "Correct" in feedback else RED, 120, HEIGHT - 180)
    pygame.display.update()

pygame.quit()
sys.exit()
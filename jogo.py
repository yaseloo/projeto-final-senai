from tkinter import font
from turtle import Screen
import pygame
import time
from config import BLACK, GREEN, HEIGHT, RED, WHITE, WIDTH
from game.pergunta import Pergunta # type: ignore
from game.config import * # type: ignore

class Jogo:
    def __init__(self):
        self.score = 0
        self.game_active = False
        self.user_answer = ""
        self.time_limit = 10
        self.start_time = None
        self.current_phase = 1
        self.questions_per_phase = 5
        self.answered_questions = 0
        self.pergunta_atual = Pergunta(self.current_phase)
        self.button_rect = pygame.Rect(WIDTH//2 - 50, HEIGHT//2 - 25, 100, 50)

    def iniciar_fase(self):
        self.answered_questions = 0
        self.pergunta_atual = Pergunta(self.current_phase)
        self.start_time = time.time()

    def verificar_tempo(self):
        return time.time() - self.start_time > self.time_limit

    def processar_eventos(self, event):
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.game_active = True
                self.iniciar_fase()
        elif event.type == pygame.KEYDOWN and self.game_active:
            if event.key == pygame.K_RETURN:
                if self.pergunta_atual.verificar_resposta(self.user_answer):
                    self.score += 10
                    correct_sound.play() # type: ignore
                else:
                    wrong_sound.play() # type: ignore
                
                self.user_answer = ""
                self.answered_questions += 1

                if self.answered_questions >= self.questions_per_phase:
                    self.current_phase += 1
                    self.iniciar_fase()
                else:
                    self.pergunta_atual = Pergunta(self.current_phase)
            elif event.key == pygame.K_BACKSPACE:
                self.user_answer = self.user_answer[:-1]
            else:
                self.user_answer += event.unicode
        return True

    def desenhar_tela(self):
        Screen.fill(WHITE)
        if not self.game_active:
            pygame.draw.rect(Screen, GREEN, self.button_rect)
            text = font.render("Iniciar", True, WHITE)
            Screen.blit(text, (WIDTH//2 - 30, HEIGHT//2 - 10))
        else:
            if self.verificar_tempo():
                self.game_active = False
            
            text_question = font.render(f"Resolva: {self.pergunta_atual.questao}", True, BLACK)
            Screen.blit(text_question, (WIDTH//2 - 100, HEIGHT//2 - 100))

            text_answer = font.render(f"Resposta: {self.user_answer}", True, BLACK)
            Screen.blit(text_answer, (WIDTH//2 - 100, HEIGHT//2))

            text_score = font.render(f"Pontos: {self.score}", True, BLACK)
            Screen.blit(text_score, (10, 10))

            text_time = font.render(f"Tempo restante: {max(0, self.time_limit - int(time.time() - self.start_time))}s", True, RED)
            Screen.blit(text_time, (WIDTH - 200, 10))

            text_phase = font.render(f"Fase: {self.current_phase}", True, BLACK)
            Screen.blit(text_phase, (10, 40))

            text_questions_remaining = font.render(f"Perguntas restantes: {self.questions_per_phase - self.answered_questions}", True, BLACK)
            Screen.blit(text_questions_remaining, (10, 70))

        pygame.display.flip()

import numpy as np
import wave

# Configurações do som (beep de 1 segundo)
sample_rate = 44100  # Taxa de amostragem padrão
freq = 1000  # Frequência do beep (Hz)
duration = 1.0  # Duração do som em segundos

t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # Criando o tempo
waveform = (np.sin(2 * np.pi * freq * t) * 32767).astype(np.int16)  # Criando a onda sonora

# Salvando o som em um arquivo WAV
with wave.open("correct.wav", "w") as f:
    f.setnchannels(1)  # Som mono
    f.setsampwidth(2)  # Amplitude de 16 bits
    f.setframerate(sample_rate)  # Taxa de amostragem
    f.writeframes(waveform.tobytes())  # Escreve o som no arquivo

print("Arquivo 'correct.wav' criado com sucesso!")

from moviepy.editor import TextClip, ColorClip, CompositeVideoClip
import os

class VideoGen:
    def create_short(self, text, output_name="result.mp4"):
        # Базовая логика создания видео с субтитрами
        bg = ColorClip(size=(1080, 1920), color=(0,0,0), duration=5)
        txt = TextClip(text, fontsize=70, color='white', size=(900, None), method='caption')
        txt = txt.set_position('center').set_duration(5)
        
        video = CompositeVideoClip([bg, txt])
        video.write_videofile(f"data/exports/{output_name}", fps=24)
        return f"data/exports/{output_name}"

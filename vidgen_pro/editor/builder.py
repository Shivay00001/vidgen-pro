
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, concatenate_videoclips
import os
import logging
from vidgen_pro.utils.config import Config

logger = logging.getLogger(__name__)

class VideoBuilder:
    def __init__(self):
        self.output_dir = Config.OUTPUT_DIR

    def retrieve_visuals(self, scenes):
        """
        Downloads visuals for each scene if they are URLs. 
        Updates the scene dictionary with local paths.
        """
        # This prevents circular import if I put VisualFetcher here, 
        # so I'll assume the caller handles downloading or I import inside method
        from vidgen_pro.core.visuals import VisualFetcher
        fetcher = VisualFetcher()

        for scene in scenes:
            if 'visual_url' in scene and scene['visual_url']:
                logger.info(f"Downloading visual for scene: {scene['text'][:20]}...")
                # Create a filename based on a hash or index could be better, but simple for now
                filename = f"scene_{hash(scene['text'])}.mp4" 
                local_path = fetcher.download_video(scene['visual_url'], filename)
                if local_path:
                    scene['video_path'] = local_path
                else:
                    logger.warning(f"Failed to download visual for scene: {scene['text']}")
    
    def assemble_video(self, scenes, audio_paths, bgm_path=None, output_filename="final_video.mp4"):
        """
        Assembles the video from scenes and audio.
        scenes: list of dicts with 'video_path', 'text'
        audio_paths: list of paths to voiceover audio files corresponding to scenes
        """
        clips = []

        if len(scenes) != len(audio_paths):
            logger.error("Mismatch between scenes and audio segments.")
            return None

        for i, scene in enumerate(scenes):
            try:
                # Load Audio
                audio = AudioFileClip(audio_paths[i])
                duration = audio.duration

                # Load Video
                if 'video_path' in scene and os.path.exists(scene['video_path']):
                    video = VideoFileClip(scene['video_path'])
                    # Loop video if shorter than audio, or cut if longer
                    if video.duration < duration:
                        video = video.loop(duration=duration)
                    else:
                        video = video.subclip(0, duration)
                else:
                    # Fallback to black screen or color clip if no video
                    from moviepy.editor import ColorClip
                    video = ColorClip(size=(1280, 720), color=(0,0,0), duration=duration)

                video = video.set_audio(audio)
                video = video.resize((1280, 720))

                # Optional: Add Subtitles (TextClip)
                # Note: Requires ImageMagick. If not present, this might fail.
                # We'll wrap in try/except or skip for MVP strictness to avoid crashes
                try:
                    txt_clip = TextClip(scene['text'], fontsize=24, color='white', font='Arial', method='caption', size=(1000, None))
                    txt_clip = txt_clip.set_position(('center', 'bottom')).set_duration(duration)
                    video = CompositeVideoClip([video, txt_clip])
                except Exception as e:
                    logger.warning(f"Subtitle generation failed (likely missing ImageMagick): {e}")

                clips.append(video)

            except Exception as e:
                logger.error(f"Error processing scene {i}: {e}")
                continue

        if not clips:
            return None

        final_clip = concatenate_videoclips(clips)

        # Add Background Music
        if bgm_path and os.path.exists(bgm_path):
            bgm = AudioFileClip(bgm_path).volumex(0.1) # Low volume
            # Loop bgm to match final clip duration
            if bgm.duration < final_clip.duration:
                 bgm = bgm.loop(duration=final_clip.duration)
            else:
                 bgm = bgm.subclip(0, final_clip.duration)
            
            final_audio = CompositeAudioClip([final_clip.audio, bgm])
            final_clip = final_clip.set_audio(final_audio)

        output_path = os.path.join(self.output_dir, output_filename)
        final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=24)
        return output_path

import asyncio
import edge_tts
import subprocess
import os

VOICE = "en-IN-PrabhatNeural"

script_lines = [
    "Recursion sounds scary. But it's just one idea: a function that calls itself to solve a smaller version of the same problem.",
    "Take counting down from 5. Instead of writing a loop, you write: 'To count down from 5, print 5, then count down from 4.' And to count down from 4, print 4, then count down from 3. Same instruction, smaller number, every time.",
    "But it can't shrink forever. Every recursive function needs a base case — a point where it stops calling itself and just returns an answer directly. For countdown, that's reaching 0.",
    "Once it hits the base case, the calls don't vanish — they unwind back up, one by one, each finishing its own leftover work in reverse order. That's why recursion feels like magic: the answer builds itself on the way back up.",
    "The one rule that matters: every recursive call must move closer to the base case. Skip that, and your function calls itself forever — a stack overflow.",
    "That's recursion: solve a smaller version, know when to stop, and let the answer unwind back up.",
    "If you found this helpful, please like, share, and subscribe. See you in the next one!"
]

async def generate_audio():
    for i, line in enumerate(script_lines):
        filename = f"line_{i+1:02d}.mp3"
        communicate = edge_tts.Communicate(line, VOICE)
        await communicate.save(filename)
        print(f"Generated {filename}")

def main():
    print("Generating voiceover audios...")
    asyncio.run(generate_audio())
    
    print("Creating 0.6-second silence.mp3...")
    # Generate 0.6 seconds of mono silence at 24kHz
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", 
        "-t", "0.6", "silence.mp3"
    ], check=True)
    
    print("Writing concat_list.txt with silent gaps...")
    with open("concat_list.txt", "w") as f:
        for i in range(len(script_lines)):
            f.write(f"file 'line_{i+1:02d}.mp3'\n")
            if i < len(script_lines) - 1:
                f.write("file 'silence.mp3'\n")
    
    print("Concatenating audios using ffmpeg...")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", "concat_list.txt", "-c", "copy", "voiceover.mp3"
    ], check=True)
    
    print("Running Manim build on recursion.py...")
    subprocess.run([
        "manim", "-qh", "recursion.py", "Recursion"
    ], check=True)
    
    # Combine video and audio
    video_path = "media/videos/recursion/1080p60/Recursion.mp4"
    output_path = "Recursion_final.mp4"
    
    print(f"Merging video ({video_path}) and audio (voiceover.mp3) using ffmpeg...")
    subprocess.run([
        "ffmpeg", "-y", "-i", video_path, "-i", "voiceover.mp3",
        "-c:v", "copy", "-c:a", "aac", "-map", "0:v:0", "-map", "1:a:0",
        output_path
    ], check=True)
    
    print(f"Finished! Output written to {output_path}")

if __name__ == "__main__":
    main()

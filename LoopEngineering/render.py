import asyncio
import edge_tts
import subprocess
import os

VOICE = "en-IN-PrabhatNeural"

script_lines = [
    "Everyone's obsessed with writing the 'perfect prompt.' But the best AI users don't do that. They do something called Loop Engineering — and it's way more powerful.",
    "Prompt engineering says: craft the ideal instruction upfront, get the perfect output in one shot. Sounds efficient — but real problems are messy. You can't predict everything you need in a single prompt.",
    "Loop Engineering flips it: write a rough prompt, get a rough output, look at what's wrong, tell the AI exactly that — and repeat. Each pass gets sharper. You're not guessing the perfect input. You're steering with feedback.",
    "This works because AI is bad at reading your mind, but great at reacting to specifics. 'Make it better' fails. 'This section is too long, cut it to two sentences' works — because now the AI has a concrete target.",
    "In practice: don't spend 10 minutes perfecting your first prompt. Spend 30 seconds on a rough one, then spend your time reacting — that's where the real quality comes from. Three fast loops beat one slow, perfect attempt.",
    "Stop engineering the perfect prompt. Start engineering the loop.",
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
    
    print("Writing concat_list.txt...")
    with open("concat_list.txt", "w") as f:
        for i in range(len(script_lines)):
            f.write(f"file 'line_{i+1:02d}.mp3'\n")
    
    print("Concatenating audios using ffmpeg...")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", "concat_list.txt", "-c", "copy", "voiceover.mp3"
    ], check=True)
    
    print("Rendering Manim video...")
    subprocess.run([
        "manim", "-qh", "loop_engineering_explainer.py", "LoopEngineeringExplainer"
    ], check=True)
    
    # Combine video and audio
    video_path = "media/videos/loop_engineering_explainer/1080p60/LoopEngineeringExplainer.mp4"
    output_path = "LoopEngineering_final.mp4"
    
    print(f"Merging video ({video_path}) and audio (voiceover.mp3) using ffmpeg...")
    subprocess.run([
        "ffmpeg", "-y", "-i", video_path, "-i", "voiceover.mp3",
        "-c:v", "copy", "-c:a", "aac", "-map", "0:v:0", "-map", "1:a:0",
        output_path
    ], check=True)
    
    print(f"Finished! Output written to {output_path}")

if __name__ == "__main__":
    main()

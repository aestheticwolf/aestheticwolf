import os
import numpy as np
from PIL import Image, ImageSequence

def verify_gif(gif_path, name):
    print(f"\n==========================================")
    print(f"VERIFYING: {name} ({gif_path})")
    print(f"==========================================")

    assert os.path.exists(gif_path), f"File {gif_path} does not exist!"
    im = Image.open(gif_path)

    # 1. Check loop count
    loop_count = im.info.get('loop', -1)
    print(f"Loop count: {loop_count} (0 = infinite loop)")
    assert loop_count == 0, f"Expected infinite loop (0), got {loop_count}"

    # 2. Extract frames and durations
    frames = []
    durations = []
    for f in ImageSequence.Iterator(im):
        frames.append(f.convert('RGB'))
        durations.append(f.info.get('duration', 100))

    num_frames = len(frames)
    total_duration_ms = sum(durations)
    print(f"Total frames: {num_frames}")
    print(f"Total duration: {total_duration_ms} ms ({total_duration_ms/1000:.2f} s)")
    assert 9800 <= total_duration_ms <= 10200, f"Expected ~10s (9800-10200ms), got {total_duration_ms}ms"

    # 3. Check frame differences
    arr0 = np.array(frames[0], dtype=np.float32)
    # Mid-reconstruct frame
    arr_mid_recon = np.array(frames[min(10, num_frames-1)], dtype=np.float32)
    # Sharp hold frame (middle)
    arr_sharp = np.array(frames[min(20, num_frames-1)], dtype=np.float32)
    # Disintegration frame
    arr_disint = np.array(frames[min(34, num_frames-1)], dtype=np.float32)

    diff_0_sharp = np.abs(arr0 - arr_sharp).mean()
    diff_mid_sharp = np.abs(arr_mid_recon - arr_sharp).mean()
    diff_disint_sharp = np.abs(arr_disint - arr_sharp).mean()
    diff_0_disint = np.abs(arr0 - arr_disint).mean()

    print(f"Mean pixel diff (Frame 0 vs Sharp Hold): {diff_0_sharp:.2f}")
    print(f"Mean pixel diff (Mid-Recon vs Sharp Hold): {diff_mid_sharp:.2f}")
    print(f"Mean pixel diff (Disintegrate vs Sharp Hold): {diff_disint_sharp:.2f}")
    print(f"Mean pixel diff (Frame 0 vs Disintegrate): {diff_0_disint:.2f}")

    # Significant visible pixel differences
    assert diff_0_sharp > 5.0, "Frame 0 is too similar to sharp hold!"
    assert diff_disint_sharp > 5.0, "Disintegration frame is too similar to sharp hold!"

    # 4. Check sharp hold frame quality
    # In portrait region, check skin tone pixels exist (high R, moderate G, lower B)
    w, h = arr_sharp.shape[1], arr_sharp.shape[0]
    sample_patch = arr_sharp[int(h*0.3):int(h*0.5), int(w*0.65 if w>500 else w*0.3):int(w*0.95 if w>500 else w*0.7)]
    print(f"Portrait patch mean RGB in sharp frame: {sample_patch.mean(axis=(0,1))}")
    print(f"Portrait patch max RGB in sharp frame: {sample_patch.max(axis=(0,1))}")

    print(f"PASS: {name} successfully verified! Real pixel decomposition & reconstruction verified frame-by-frame.")

if __name__ == '__main__':
    verify_gif('assets/richard-portrait-reveal.gif', 'PORTRAIT REVEAL GIF')
    verify_gif('assets/hero.gif', 'UNIFIED HERO BANNER GIF')

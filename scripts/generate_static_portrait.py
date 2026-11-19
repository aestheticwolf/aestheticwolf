import numpy as np
from PIL import Image, ImageFilter

def create_static_portrait():
    # Load original isolated portrait
    im = Image.open('assets/richard-portrait.png').convert('RGBA')
    arr = np.array(im, dtype=np.float32)

    # 1. Find non-empty bounding box
    alpha = arr[:, :, 3]
    row_mask = (alpha > 5).sum(axis=1) > 0
    col_mask = (alpha > 5).sum(axis=0) > 0
    r_min, r_max = np.where(row_mask)[0][[0, -1]]
    c_min, c_max = np.where(col_mask)[0][[0, -1]]

    # Crop tightly with small 4px margin
    h_orig, w_orig = alpha.shape
    r_min = max(0, r_min - 4)
    r_max = min(h_orig - 1, r_max + 4)
    c_min = max(0, c_min - 4)
    c_max = min(w_orig - 1, c_max + 4)

    cropped = arr[r_min:r_max+1, c_min:c_max+1].copy()
    h, w, _ = cropped.shape
    print(f"Cropped dimensions: {w}x{h}")

    # 2. Lower torso fade: bottom 18% smoothly fades alpha to 0
    fade_start = int(h * 0.82)
    fade_len = h - fade_start
    fade_curve = np.linspace(1.0, 0.0, fade_len, dtype=np.float32)
    # Apply smooth cosine/cubic ease
    fade_curve = 0.5 * (1.0 + np.cos(np.pi * (1.0 - fade_curve)))

    for y in range(fade_start, h):
        factor = fade_curve[y - fade_start]
        cropped[y, :, 3] *= factor

    # 3. Create subtle atmospheric rim lighting:
    # Soft cyan on right rim (#22D3EE), soft violet on left rim (#8B5CF6)
    # Only applied at the outer silhouette edges, never on the center of the face
    cur_alpha = cropped[:, :, 3] / 255.0
    # Sobel / gradient of alpha to detect edge silhouette
    edge_x = np.zeros_like(cur_alpha)
    edge_x[:, 1:-1] = (cur_alpha[:, 2:] - cur_alpha[:, :-2]) / 2.0

    # Right edge is where edge_x < 0 (alpha drops off to the right)
    # Left edge is where edge_x > 0 (alpha rises from the left)
    right_rim = np.clip(-edge_x * 3.0, 0, 1.0) * (cur_alpha > 0.2)
    left_rim = np.clip(edge_x * 3.0, 0, 1.0) * (cur_alpha > 0.2)

    # Blur rim masks slightly for soft light wrapping
    right_rim_img = Image.fromarray((right_rim * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(radius=3))
    left_rim_img = Image.fromarray((left_rim * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(radius=3))
    right_rim_arr = np.array(right_rim_img, dtype=np.float32) / 255.0
    left_rim_arr = np.array(left_rim_img, dtype=np.float32) / 255.0

    # Cyan (#22D3EE = 34, 211, 238), Violet (#8B5CF6 = 139, 92, 246)
    # Very subtle tint (0.15 intensity) preserving natural skin tone completely
    for c, val in enumerate([34, 211, 238]):
        cropped[:, :, c] = np.clip(cropped[:, :, c] + right_rim_arr * val * 0.16, 0, 255)
    for c, val in enumerate([139, 92, 246]):
        cropped[:, :, c] = np.clip(cropped[:, :, c] + left_rim_arr * val * 0.14, 0, 255)

    result_im = Image.fromarray(np.clip(cropped, 0, 255).astype(np.uint8), mode='RGBA')
    result_im.save('assets/richard-portrait-static.png', format='PNG')
    print("Successfully generated assets/richard-portrait-static.png")

if __name__ == '__main__':
    create_static_portrait()

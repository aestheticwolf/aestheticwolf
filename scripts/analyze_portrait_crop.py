from PIL import Image
import numpy as np

im = Image.open('assets/richard-portrait.png')
w, h = im.size
print(f"Dimensions: {w}x{h}")

arr = np.array(im)
alpha = arr[:, :, 3]
print("Alpha channel shape:", alpha.shape)
print("Min alpha:", alpha.min(), "Max alpha:", alpha.max())

# Find vertical distribution of alpha
row_alpha = (alpha > 10).sum(axis=1)
non_empty_rows = np.where(row_alpha > 0)[0]
print(f"Non-empty rows: {non_empty_rows[0]} to {non_empty_rows[-1]}")

col_alpha = (alpha > 10).sum(axis=0)
non_empty_cols = np.where(col_alpha > 0)[0]
print(f"Non-empty cols: {non_empty_cols[0]} to {non_empty_cols[-1]}")

# Crop to non-empty bounding box
crop_box = (non_empty_cols[0], non_empty_rows[0], non_empty_cols[-1] + 1, non_empty_rows[-1] + 1)
print("Tightly cropped box:", crop_box)
cropped = im.crop(crop_box)
print("Cropped size:", cropped.size)

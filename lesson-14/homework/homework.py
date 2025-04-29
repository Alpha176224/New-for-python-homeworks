import numpy as np
from PIL import Image

# Task 1
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
vec_celsius = np.vectorize(fahrenheit_to_celsius)
temps_f = np.array([32, 68, 100, 212, 77])
temps_c = vec_celsius(temps_f)

# Task 2
def power_fn(base, exponent):
    return base ** exponent
vec_power = np.vectorize(power_fn)
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
powers = vec_power(bases, exponents)

# Task 3
A1 = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
b1 = np.array([7, 4, 5])
sol1 = np.linalg.solve(A1, b1)

# Task 4
A2 = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
b2 = np.array([12, -5, 15])
sol2 = np.linalg.solve(A2, b2)

# Image Manipulation
def flip_image(img_arr):
    return np.flipud(np.fliplr(img_arr))

def add_noise(img_arr):
    noise = np.random.randint(0, 50, img_arr.shape, dtype='uint8')
    return np.clip(img_arr + noise, 0, 255)

def brighten_channels(img_arr, value=40):
    return np.clip(img_arr + value, 0, 255)

def apply_mask(img_arr, mask_size=100):
    h, w, _ = img_arr.shape
    y1 = h // 2 - mask_size // 2
    y2 = y1 + mask_size
    x1 = w // 2 - mask_size // 2
    x2 = x1 + mask_size
    img_arr[y1:y2, x1:x2] = 0
    return img_arr

img = Image.open("images/birds.jpg")
img_arr = np.array(img)

flipped = flip_image(img_arr)
noisy = add_noise(flipped)
bright = brighten_channels(noisy)
masked = apply_mask(bright)

result_img = Image.fromarray(masked.astype('uint8'))
result_img.save("images/birds_modified.jpg")

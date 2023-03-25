import cv2
import numpy as np


def cell_count(img: np.ndarray):
    """
    Algorithm for counting erythrocytes in microscopic blood images

    Parameters
    ----------
    img : np.ndarray
        loaded image
    
    Returns
    -------
    Tuple 
         (cell count, a list of (img, desc) showing the process of detection)
    """
    imgs = []

    # convert pixel values [0, 255] -> [0, 1]
    img = img.astype(np.float32) / 255
    orig_img = img

    # to grayscale and remove last axis
    img = img.mean(axis=2)
    imgs.append((img, 'Grayscaled Image'))

    liphocyte_mask = ~cv2.erode((cv2.blur(img, (40, 40)) > 0.4).astype(np.uint8), np.ones((30, 30))).astype(bool)
    imgs.append((liphocyte_mask, 'Find Lymphocyte'))
    img = (~liphocyte_mask) * img + liphocyte_mask * (
                np.quantile(img, 0.9) + np.random.normal(loc=0, scale=img[img < np.median(img)].std(),
                                                         size=(img.shape[0], img.shape[1])))
    imgs.append((img, 'Delete Lymphocyte'))

    blured_img = cv2.blur(img, (20, 20))
    img = (img > blured_img - 0.001).astype(np.float32)
    imgs.append((img, 'Select brighter pixels'))

    white = (cv2.blur(img, (6, 6)) > 0.95).astype(np.float32)
    black = (cv2.blur(img, (6, 6)) < 0.1).astype(np.float32)
    imgs.append((white, 'Most Bright'))
    imgs.append((black, 'Most Dark'))

    white = cv2.dilate(white, np.ones((7, 7)))
    black = cv2.dilate(black, np.ones((7, 7)))
    imgs.append((white, 'Dilate countours for most bright fragments'))
    imgs.append((black, 'Dilate countours for most dark fragments'))
    img = white * black
    imgs.append((img, 'Intersection of two previous images'))
    img = (cv2.blur(img, (6, 6)) > img * 0.9).astype(np.float32)
    imgs.append((img, 'Erode contours'))
    img = cv2.dilate(img, np.ones((6, 6)))
    imgs.append((img, 'Dilate contours'))

    num_components, components, stats, centroids = cv2.connectedComponentsWithStats((img < 0.5).astype(np.uint8))

    colors = np.array([[np.random.rand(), np.random.rand(), np.random.rand()] for _ in range(num_components)])
    colors[0, :] = 0

    imgs.append((colors[components], 'Find components'))

    component_sizes = stats[:, cv2.CC_STAT_AREA]
    component_mask = (component_sizes > 40) & (component_sizes < 10000)
    for comp_i in component_mask.nonzero()[0]:
        if img[components == comp_i].mean() > 0.5:
            component_mask[comp_i] = False
    for comp_i in (~component_mask).nonzero()[0]:
        components[components == comp_i] = 0
    imgs.append((colors[components], 'Delete biggest and smallest components'))

    components = cv2.dilate(components.astype(np.float32), np.ones((15, 15))).astype(np.uint32)
    img = colors[components]
    imgs.append((img, 'Dilated components'))

    # back to [0, 255] and to 3 channels for visualization
    if len(img.shape) == 2:
        img = np.stack([img, img, img], axis=2)
    img = img * 0.2 + orig_img
    imgs.append((img.copy(), 'Overlay with orig image'))

    for x, y in centroids[component_mask]:
        radius = 10
        x, y = round(x), round(y)
        img = cv2.line(img, (x - radius, y - radius), (x + radius, y + radius), color=(1, 1, 1), thickness=5)
        img = cv2.line(img, (x + radius, y - radius), (x - radius, y + radius), color=(1, 1, 1), thickness=5)

    imgs.append((img, 'Found erythocythes'))
    return sum(component_mask), imgs

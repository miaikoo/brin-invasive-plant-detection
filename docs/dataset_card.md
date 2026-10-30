📌 Context
This dataset contains images and bounding box annotations for five common species of weeds and invasive plants often found in tropical regions. It is designed for training Object Detection models (such as YOLO) to automatically identify and localize these plant species in natural environments.

This dataset is particularly useful for agricultural research, environmental monitoring, and automated weed control systems.

🌿 Class Mapping
The dataset consists of 5 target classes of plant species. The class IDs are mapped as follows:

- 0 : Vachellia nilotica (Gum arabic tree / Babul)

- 1 : Ageratum conyzoides (Billygoat-weed / Bandotan)

- 2 : Lantana camara (Lantana / Tembelekan)

- 3 : Clitoria ternatea (Asian pigeonwings / Bunga Telang)

- 4 : Merremia hederecea (Ivy woodrose / Merremia)

📊 Dataset Statistics
The dataset is well-balanced across the 5 species and includes "background" images (empty labels) to help models reduce false positives.

- Total Images: 1,369

- Background Images (Empty Labels): 156

Object Count per Class (Total Bounding Boxes):

- Class 0 (Vachellia nilotica): 586

- Class 1 (Ageratum conyzoides): 404

- Class 2 (Lantana camara): 407

- Class 3 (Clitoria ternatea): 266

- Class 4 (Merremia hederecea): 375

Image Count per Class (Images containing at least one object):

- Class 0: 249 images

- Class 1: 250 images

- Class 2: 248 images

- Class 3: 241 images

- Class 4: 225 images

📁 Content & Format

- Images: Provided in .jpg / .png format.

- Annotations: Provided in standard YOLO format (.txt files). Each text file contains the class ID and normalized bounding box coordinates (class x_center y_center width height).

- Negative Samples: Images with empty .txt files are intentionally included as background/negative samples to improve model robustness.

🚀 Potential Use Cases

- Precision Agriculture and Smart Farming.

- Automated herbicide spraying drones/robots.

- Biodiversity and ecological impact monitoring.

🤝 Acknowledgments & Source Data
The raw images used to build this dataset were sourced from the Global Biodiversity Information Facility (GBIF). We express our gratitude to all the original data publishers, institutions, and contributors.

GBIF Occurrence Downloads:

- Vachellia nilotica: 

- Ageratum conyzoides: 

- Lantana camara: GBIF.org (06 March 2026) GBIF Occurrence Download  https://doi.org/10.15468/dl.n7rnpv

- Clitoria ternatea: 

- Merremia hederecea:

Please adhere to the original CC BY / CC BY-NC licensing terms when using this dataset for secondary research.
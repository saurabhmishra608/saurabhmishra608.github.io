---
title: "Mitacs Globalink Research Intern \| University of Waterloo"
excerpt: "Worked under the supervision of [Prof. Vasudevan Laxminaryan](https://uwaterloo.ca/optometry-vision-science/profile/vengu) on investigating changes in the morphological features of retinal blood vessels in myopia in collaboration with Sankara Nethralaya. <br/><img src='/images/UoW_logo.png'>"
collection: experience
---

![UWF Image](/images/UWF.jpg)

### Project Description
The aim of the project was to analyze the retinal vasculature in subjects with myopia and identify factors influencing the calculation of the fractal dimension (Df), a quantitative measure for the branching pattern of blood vessels.

### Methods
- **Study Design:** A retrospective study involving 49 myopic eyes and 39 control eyes.
- **Imaging:** Ultra-wide field (UWF) retinal images were classified according to the META-PM classification and divided into nine quadrants. Any artifacts present in more than five quadrants were excluded from the analysis.
- **Image Processing Techniques:** 
  - **Luminosity Balancing and CLAHE:** Applied to enhance the contrast of the retinal images, ensuring better visibility of the blood vessels.
  - **TopHat Operation and Otsu Thresholding:** Used for effective segmentation of the blood vessels from the background.
  - **Area Thresholding:** Employed to isolate the blood vessels accurately after the initial segmentation.

### Quantitative Analysis
- **Fractal Dimension (Df):** We used the fractal dimension as a quantitative measure to analyze the complexity of the branching patterns of retinal blood vessels. This index provides insight into the structural changes associated with myopia.
- **Domain Adaptation with W-Net:** A pre-trained [W-Net](https://arxiv.org/abs/2009.01907) architecture, trained on the DRIVE dataset, was used to improve vessel segmentation on fundus images specific to our study.

### Key Findings
- The mean ± SD Df values for emmetropia and myopia were 1.28 ± 0.02 and 1.27 ± 0.02, respectively, indicating a subtle decreasing trend in Df with myopia.
- The correlation between Df and other factors such as refractive error, best-corrected visual acuity (BCVA), and age were also examined to understand their impact on the retinal vasculature.
- A positive correlation was found between Df and the presence of artifacts in the retinal images. However, factors such as internal limiting membrane reflection and vitreous opacity significantly influenced the segmentation of blood vessels and thus the Df.

This project highlighted the potential of using fractal analysis and advanced image processing methods to study the retinal vasculature in myopia, contributing valuable insights into the structural changes associated with this condition.



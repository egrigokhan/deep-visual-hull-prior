# Shape-from-Silhouette using Visual Hull and Deep Image Prior
Gökhan Eğri* [gegri@g.harvard.edu]
Xinran (Nicole)* Han [xinranhan@g.harvard.edu]

##### [[Report](https://egrigokhan.github.io/data/6_866_Project_Report_VisualHull.pdf "Report")]
------------

#### Abstract
Visual hull construction is a preliminary step for a majority of 3D shape reconstruction tasks and as such poses an important problem for many sub-fields of computer vision. In this work, we first implement and evaluate a familiar voxel-based visual hull construction algorithm which serves as the baseline for our proposed method. For our proposed method, we extend the original Deep Image Prior method by Ulyanov *et al.* to the problem of visual-hull construction by viewing the 3D → 2D projection as a corruption. We find that our proposed method is both capable of converging on viable visual hulls for an array of different objects and resilient to noise and various occlusions. We also present some preliminary results for our method on 3D denoising and 3D inpainting.

#### Dataset
We train and evaluate on the [multi-view Middlebury dataset](https://vision.middlebury.edu/mview/data/) as well synthetic multi-view images generated on Blender. The script for Blender dataset generation is located [here](!add gist here!).

#### Deterministic Visual Hull

We implement a voxel-based deterministic visual hull constructor in Python as our baseline.

The code for the deterministic method is available at [egrigokhan/python-visual-hull](https://github.com/egrigokhan/python-visual-hull).

![alt text](https://github.com/egrigokhan/deep-visual-hull-prior/blob/main/figures/visual_hull_2d_analog_diagram.png)
![alt text](https://github.com/egrigokhan/deep-visual-hull-prior/blob/main/figures/diagram-20201204%20(8)%20(1).png)

#### Deep Visual Hull Prior (DVHP)

Our primary contribution in this project is extending the Visual Hull algorithm and combining it with the architecture of Ulyanov *et al.* ’s Deep Image
Prior to investigate learning-based shape reconstruction. We further motivate Deep Visual Hull Prior through evaluations on 3D inpainting and 3D denoising.

For our proposed method, our key observation is that the projection of the visual hull onto the N image planes it was constructed from can be seen as a corruption. We subsequently formulate visual-hull reconstruction as an inverse task and extend the Deep Image Prior architecture.

##### Deep Image Prior (Ulyanov *et al.*) [Paper]()
![Deep Image Prior (Ulyanov *et al.*)](https://github.com/egrigokhan/deep-visual-hull-prior/blob/main/figures/diagram-20201205%20(1).png)

##### Deep Visual Hull Prior (proposed method)
![Deep Visual Hull Prior (proposed method)](https://raw.githubusercontent.com/egrigokhan/deep-visual-hull-prior/main/figures/diagram-20201204%20(1).png)
![Deep Visual Hull Prior (architecture)](https://raw.githubusercontent.com/egrigokhan/deep-visual-hull-prior/main/figures/diagram-20201203%20(4)%20(1)%20(1).png)

###End

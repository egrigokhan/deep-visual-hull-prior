[MIT 6.866 - Machine Vision (Fall '20) Term Project]
# Shape-from-Silhouette using Visual Hull and Deep Image Prior  
Gökhan Eğri* [gegri@g.harvard.edu]  
Xinran (Nicole)* Han [xinranhan@g.harvard.edu]

##### [[Report](https://egrigokhan.github.io/data/6_866_Project_Report_VisualHull.pdf "Report")]
------------

### Abstract
Visual hull construction is a preliminary step for a majority of 3D shape reconstruction tasks and as such poses an important problem for many sub-fields of computer vision. In this work, we first implement and evaluate a familiar voxel-based visual hull construction algorithm which serves as the baseline for our proposed method. For our proposed method, we extend the original Deep Image Prior method by Ulyanov *et al.* to the problem of visual-hull construction by viewing the 3D → 2D projection as a corruption. We find that our proposed method is both capable of converging on viable visual hulls for an array of different objects and resilient to noise and various occlusions. We also present some preliminary results for our method on 3D denoising and 3D inpainting.

### Dataset
We train and evaluate on the [multi-view Middlebury dataset](https://vision.middlebury.edu/mview/data/) as well synthetic multi-view images generated on Blender. The script for Blender dataset generation is located [here](https://gist.github.com/egrigokhan/95eef146572216102684399029690ec0).

### Deterministic Visual Hull

We implement a voxel-based deterministic visual hull constructor in Python as our baseline.

The code for the deterministic method is available at [egrigokhan/python-visual-hull](https://github.com/egrigokhan/python-visual-hull).

![alt text](https://github.com/egrigokhan/deep-visual-hull-prior/blob/main/figures/visual_hull_2d_analog_diagram.png =100x)
![alt text](https://github.com/egrigokhan/deep-visual-hull-prior/blob/main/figures/diagram-20201204%20(8)%20(1).png)

### Deep Visual Hull Prior (DVHP)

Our primary contribution in this project is extending the Visual Hull algorithm and combining it with the architecture of Ulyanov *et al.* ’s Deep Image
Prior to investigate learning-based shape reconstruction. We further motivate Deep Visual Hull Prior through evaluations on 3D inpainting and 3D denoising.

For our proposed method, our key observation is that the projection of the visual hull onto the N image planes it was constructed from can be seen as a corruption. We subsequently formulate visual-hull reconstruction as an inverse task and extend the Deep Image Prior architecture.

#### Deep Image Prior (Ulyanov *et al.*) [[Paper]](https://sites.skoltech.ru/app/data/uploads/sites/25/2018/04/deep_image_prior.pdf)
![Deep Image Prior (Ulyanov *et al.*)](https://github.com/egrigokhan/deep-visual-hull-prior/blob/main/figures/diagram-20201205%20(1).png)

#### Deep Visual Hull Prior (proposed method)
![Deep Visual Hull Prior (proposed method)](https://raw.githubusercontent.com/egrigokhan/deep-visual-hull-prior/main/figures/diagram-20201204%20(1).png)
![Deep Visual Hull Prior (architecture)](https://raw.githubusercontent.com/egrigokhan/deep-visual-hull-prior/main/figures/diagram-20201203%20(4)%20(1)%20(1).png)

#### Evaluation

We evaluate performance on two metrics:
- **Voxel Intersection over Union (IoU):**. We use the conversion tool from Stutz *et al.*, which converts the ground truth mesh into a voxel grid with specified dimension. When computing the intersection-over-union (IoU), we divide the number of voxels that are filled by both models by the number of voxels filled in either one.

A higher IoU indicates better reconstruction result.

- **Surface Distance (Jensen *et al.*):** For this metric, we convert the predicted voxel output to a mesh file and then sample 10k points to compute the distance. Using the software from Stutz *et al.*, we obtain the accuracy and completeness.  Accuracy is the distance of the reconstruction to the ground truth and completeness is the distance from ground truth to reconstruction.

Lower accuracy/completeness indicates better reconstruction quality.

The code for evaluation is available at [xrhan/mesh-voxelization](https://github.com/xrhan/mesh-voxelization) and [xrhan/mesh-evaluation](https://github.com/xrhan/mesh-evaluation).


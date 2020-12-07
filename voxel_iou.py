import numpy as np
import argparse
import os
import json

def voxel_iou(model1, model2, threshold1, threshold2):
  assert (model1.shape == model2.shape)
  intersection_count = 0
  union_count = 0

  rangex,rangey,rangez = model1.shape
  for i in range(0, rangex):
    for j in range(0, rangey):
      for k in range(0, rangez):
        if (model1[i,j,k] >= threshold1 and model2[i,j,k] >= threshold2):
          intersection_count += 1

        if model1[i,j,k] >= threshold1 or model2[i,j,k] >= threshold2:
          union_count += 1
  return intersection_count / union_count

parser = argparse.ArgumentParser(description='Evaluate using voxel')
parser.add_argument('--input', help='Directory containing npy files')
parser.add_argument('--ground', help='Path to ground truth voxel file')

# Load ground truth voxel
args = parser.parse_args()
gt_model = np.load(args.ground)
results = {}

# Compute IOU results
for f in os.listdir(args.input):
    if f.endswith('.npy'):
        pred = np.load(f"{args.input}/{f}")
        iter_n = int(f.split('_')[-4])
        results[iter_n] = voxel_iou(gt_model, pred, 1, 0.98)

out_path = f"{args.input}/iou_results.json"
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f"Results written to {out_path}")

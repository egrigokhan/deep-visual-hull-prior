import argparse
import os
import subprocess
import json
import tempfile
import shutil

parser = argparse.ArgumentParser(description='Evaluate using mesh compare')
parser.add_argument('--input', help='Directory containing dae files')
parser.add_argument('--ground', help='Path to ground truth off file')
args = parser.parse_args()

# Convert dae to off
off_list = []
for f in os.listdir(args.input):
    if f.endswith('.dae'):
        iter_n = int(f.split('_')[-1][:-4])
        out_path = f"{args.input}/{iter_n}.off"
        subprocess.run(f"ctmconv {args.input}/{f} {out_path}",shell=True, check=True)
        if os.path.isfile(out_path):
            off_list.append((iter_n, out_path))
        else:
            print(f"Skipping Iteration {iter_n}, conversion failed")

temp_result_dir = tempfile.mkdtemp()

# Run diff tool
for o in off_list:
    subprocess.run(f"/home/hxinran/mesh-evaluation/bin/evaluate --input {o[1]} --reference {args.ground} --output {temp_result_dir}/{o[0]}.txt", shell=True, check=True)

# Parse results
results = {}
for o in off_list:
    with open(f"{temp_result_dir}/{o[0]}.txt", 'r') as f:
        vals = f.readlines()[0].split()[1:]
        results[o[0]] = {
                "accuracy": float(vals[0]),
                "completeness": float(vals[1])
                }

out_path = f"{args.input}/mesh_results.json"
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f"Results written to {out_path}")

shutil.rmtree(temp_result_dir)

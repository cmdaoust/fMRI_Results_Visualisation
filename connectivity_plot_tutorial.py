import pandas as pd
import numpy as np
import netplotbrain
from pathlib import Path
import nibabel as nib
import matplotlib.colors as mcolors

# Get folder where this Python script resides
root_dir = Path(__file__).parent

# 1. Create node dataframe (MNI coordinates)
nodes = pd.DataFrame({
    "node": ["Amygdala", "vmPFC", "Insula", "ACC"],
    "x": [-22, 0, 38, 2],     # MNI X
    "y": [-4, 52, 20, 30],    # MNI Y
    "z": [-18, -6, 2, 24]     # MNI Z
})

# 2. Create edge dataframe (connectivity weights)
edges = pd.DataFrame({
    "i": [0, 0, 0], # seed node (Amygdala, Amygdala, Amygdala)
    "j": [1, 2, 3], # target nodes (vmPFC, Insula, ACC)
    "weight": [0.8, 0.5, 0.5] # connectivity weights between nodes
})

# 3. Assign node colours
#    First node = gold
#    All others = seagreen

# --- colors as RGB array (must be length = number nodes) ---
colors = ['gold', 'seagreen', 'seagreen', 'seagreen']
node_color = np.array([mcolors.to_rgb(c) for c in colors])

# 4. Load template for visualisation

# --- load the MNI152 template ---
from nilearn import datasets
template_img = datasets.load_mni152_template(resolution=1)   # nib.Nifti1Image
template_path = root_dir / "MNI152_T1_1mm.nii.gz"
nib.save(template_img, str(template_path))
print(f"Template saved to: {template_path}")

# Create plot
netplotbrain.plot(
    nodes=nodes, # node dataframe with MNI coordinates
    node_type='circles', # node type (circles, spheres, or parcels)
    node_color=node_color, # node colors as RGB array
    node_scale=50, # node size scaling factor
    highlight_nodes=list(range(len(node_color))), # highlight all nodes
    edges=edges, # edge dataframe with  weights
    edge_weights='weight', # column in edge dataframe to use for edge weights
    template=template_path, # template for visualisation
    template_style='glass', # template style (glass, filled, cloudy, surface)
    view='LSR', # view angle (LSR = left, superior, right)
    savename=str(root_dir / 'connectivity_plot.png') # save figure to file
)




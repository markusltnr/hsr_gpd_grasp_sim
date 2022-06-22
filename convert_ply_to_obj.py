import open3d as o3d
import os
import numpy as np

device = o3d.core.Device("CPU:0")
dtype = o3d.core.Dtype.Float32

dir = os.path.dirname(os.path.abspath(__file__))
# list files in objs directory
files = os.listdir(os.path.join(dir,'objs'))
ply_files = [x for x in files if x.endswith(".ply")]

for ply in ply_files:

    ply = os.path.join(dir, 'objs', ply)
    mesh = o3d.io.read_triangle_mesh(ply)
    obj = ply.replace('.ply', '.obj')
    o3d.io.write_triangle_mesh(obj, mesh)

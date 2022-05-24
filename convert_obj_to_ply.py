import open3d as o3d
import os
import numpy as np

device = o3d.core.Device("CPU:0")
dtype = o3d.core.Dtype.Float32

dir = os.path.dirname(os.path.abspath(__file__))
# list files in objs directory
files = os.listdir(os.path.join(dir,'objs'))
obj_files = [x for x in files if x.endswith(".obj")]

for obj in obj_files:

    obj = os.path.join(dir, 'objs', obj)
    mesh = o3d.io.read_triangle_mesh(obj)
    cloud = mesh.sample_points_uniformly(50000)
    ply = obj.replace('.obj', '.ply')

    # pcl had trouble reading double xyz, so conversion to float necessary
    points = np.asarray(cloud.points)
    colors = np.asarray(cloud.colors)
    normals = np.asarray(cloud.normals)
    pcd = o3d.t.geometry.PointCloud(device)
    pcd.point["points"] = o3d.core.Tensor(points, dtype, device)
    pcd.point["normals"] = o3d.core.Tensor(normals, dtype, device)
    pcd.point["colors"] = o3d.core.Tensor(colors, dtype, device)

    o3d.t.io.write_point_cloud(ply, pcd, write_ascii=True, compressed=True)

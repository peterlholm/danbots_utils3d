"Convert stil file to pointcloud ply"
from pathlib import Path
import open3d as o3d

def mesh2ply(infile, outfile):
    "convert mesh corners to ply"
    mesh = o3d.io.read_triangle_mesh(infile)
    pcd = o3d.geometry.PointCloud()
    pcd.points = mesh.vertices
    pcd.colors = mesh.vertex_colors
    #pcd.normals = mesh.vertex_normals
    #print(mesh)
    print(pcd)
    o3d.io.write_point_cloud(outfile, pcd)

def meshsurface2ply(infile, outfile, outfile2):
    "convert mesh surfaces to ply"
    mesh = o3d.io.read_triangle_mesh(infile)
    no_points = 1000
    pcl1 = mesh.sample_points_poisson_disk(number_of_points=no_points)
    pcl2 = mesh.sample_points_uniformly(number_of_points=no_points)
    o3d.io.write_point_cloud(outfile, pcl1)
    o3d.io.write_point_cloud(outfile2, pcl2)
    return
    
if __name__=="__main__":
    files = ['LJ3','t9UJscan']
    Path('out/ply').mkdir(exist_ok=True, parents=True)
    for f in files:
        INFIL = "stl/" + f + ".stl"
        OUTFIL = "out/ply/" + f + ".ply"
        Path("out/ply").mkdir(parents=True, exist_ok=True)
        print(f"starting converting {INFIL} to {OUTFIL}")
        mesh2ply(INFIL,OUTFIL)
        OUTFIL = "out/ply/" + f + "_face.ply"
        OUTFIL2 = "out/ply/" + f + "_face2.ply"
        print(f"starting converting {INFIL} to {OUTFIL}")
        meshsurface2ply(INFIL,OUTFIL, OUTFIL2)

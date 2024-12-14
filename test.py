import numpy as np
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=RuntimeWarning)
    import svs

vectors = np.array([[1,2,3], [4,5,6], [7,8,9]]).astype(np.float32)
qvec = np.array([4,4,4]).astype(np.float32)
parameters = svs.VamanaBuildParameters(graph_max_degree = 64, window_size = 128)  
l2_idx = svs.Vamana.build(
    parameters,
    vectors,
    svs.DistanceType.L2,
    num_threads = 4
)
parameters = svs.VamanaBuildParameters(graph_max_degree = 64, window_size = 128, alpha=.95)
cos_idx = svs.Vamana.build(
    parameters,
    vectors,
    svs.DistanceType.Cosine,
    num_threads = 4
)
mip_idx = svs.Vamana.build(
    parameters,
    vectors,
    svs.DistanceType.MIP,
    num_threads = 4
)

print('\n L2')
l2_idx.search_window_size = 3
I,D = l2_idx.search(qvec, 3)
print(I)
print(D)

print('\n Cosine')
cos_idx.search_window_size = 3
I,D = cos_idx.search(qvec, 3)
print(I)
print(D)

print('\n MIP')
mip_idx.search_window_size = 3
I,D = mip_idx.search(qvec, 3)
print(I)
print(D)
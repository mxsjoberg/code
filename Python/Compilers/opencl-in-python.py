# 2023-08

"""
OpenCL can be used to run code on GPUs and other
accelerators. It's a C API (kernel code looks like 
C code) and pyopencl is a Python wrapper.
"""

import pyopencl as cl
import numpy as np
import timeit

# init opencl
platform = cl.get_platforms()[0]
device = platform.get_devices()[2] # AMD Radeon Pro 5500M Compute Engine
context = cl.Context([device])
queue = cl.CommandQueue(context)

# print(platform.get_info(cl.platform_info.NAME))
print(platform.get_info(cl.platform_info.VERSION))
# OpenCL 1.2 (Mar  4 2023 12:44:39)
print(device.get_info(cl.device_info.NAME))
# AMD Radeon Pro 5500M Compute Engine

# init data
size = 1000000000

# create arrays
a = np.random.rand(size).astype(np.float32)
b = np.random.rand(size).astype(np.float32)
result = np.zeros(size).astype(np.float32)

# opencl kernel
kernel_code = """
__kernel void add(__global float *a, __global float *b, __global float *result, int size) {
    int idx = get_global_id(0);
    if (idx < size) {
        result[idx] = a[idx] + b[idx];
    }
}
"""
# compile kernel
program = cl.Program(context, kernel_code).build()
# create buffers
a_buffer = cl.Buffer(context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=a)
b_buffer = cl.Buffer(context, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=b)
result_buffer = cl.Buffer(context, cl.mem_flags.WRITE_ONLY, result.nbytes)

# opencl result
def run_opencl():
    # execute kernel
    program.add(queue, a.shape, None, a_buffer, b_buffer, result_buffer, np.int32(size))
    # copy result
    cl.enqueue_copy(queue, result, result_buffer)

# numpy result to compare with
numpy_result = np.zeros(size).astype(np.float32)
def run_numpy():
    global numpy_result
    numpy_result = a + b

print(timeit.timeit('run_numpy', globals=globals(), number=1))
# 1.0561197996139526e-06
print(timeit.timeit('run_opencl', globals=globals(), number=1))
# 5.420297384262085e-07

assert np.allclose(result, numpy_result)

# free memory
a_buffer.release()
b_buffer.release()
result_buffer.release()
# close opencl
del context
del queue
del program

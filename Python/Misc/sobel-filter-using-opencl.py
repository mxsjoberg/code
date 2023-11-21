"""
A Sobel filter is an edge detection filter. It's a 3x3
convolution commonly used in image processing.
"""

import numpy as np
import pyopencl as cl
from PIL import Image, ImageFilter

# load image
input_image = Image.open('_images/photo.png').convert('L')
input_array = np.array(input_image).astype(np.uint8)

# input_image.show()

# sobel kernel
# sobel_x_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]).astype(np.float32)
# sobel_y_kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]).astype(np.float32)

# opencl
platform = cl.get_platforms()[0]
device = platform.get_devices()[2] # AMD Radeon Pro 5500M Compute Engine
ctx = cl.Context([device])
queue = cl.CommandQueue(ctx)

# buffers
input_buffer = cl.Buffer(ctx, cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR, hostbuf=input_array)
output_buffer = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, input_array.nbytes)

# compile kernel
program = cl.Program(ctx, """
    __kernel void sobel_filter(__global const uchar* input, __global uchar* output, const int width, const int height) {
        int x = get_global_id(0);
        int y = get_global_id(1);

        if (x > 0 && x < width - 1 && y > 0 && y < height - 1) {
            float sum_x = 0;
            float sum_y = 0;

            const float sobel_x_kernel[3][3] = { {-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1} };
            const float sobel_y_kernel[3][3] = { {-1, -2, -1}, {0, 0, 0}, {1, 2, 1} };

            for (int i = -1; i <= 1; ++i) {
                for (int j = -1; j <= 1; ++j) {
                    sum_x += input[(y + i) * width + (x + j)] * sobel_x_kernel[i + 1][j + 1];
                    sum_y += input[(y + i) * width + (x + j)] * sobel_y_kernel[i + 1][j + 1];
                }
            }

            float gradient_magnitude = sqrt(sum_x * sum_x + sum_y * sum_y);
            gradient_magnitude = gradient_magnitude > 255 ? 255 : gradient_magnitude;

            output[y * width + x] = (uchar)gradient_magnitude;
        } else {
            output[y * width + x] = 0;
        }
    }
""").build()

program.sobel_filter(queue, input_array.shape, None, input_buffer, output_buffer, np.int32(input_array.shape[1]), np.int32(input_array.shape[0]))

# read result
output_array = np.empty_like(input_array)
cl.enqueue_copy(queue, output_array, output_buffer).wait()

# save image
output_image = Image.fromarray(output_array, 'L')
output_image.save('_images/edges.png')

# show image
# output_image.show()

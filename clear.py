#import torch
#with torch.cuda.device('cuda:1'):
#torch.cuda.empty_cache()

#print(torch.cuda.get_device_name(0))
from numba import cuda 
device = cuda.get_current_device()
device.reset()
print("ok")
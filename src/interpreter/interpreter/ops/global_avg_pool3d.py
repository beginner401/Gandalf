import tensorflow as tf
import torch
import jittor

from src.configuration.support.torch_expansion.global_avg_pool3d import GlobalAvgPool3d as torch_avgpool
from src.configuration.support.jittor_expansion.global_avg_pool3d import GlobalAvgPool3d as jt_avgpool


def get_op_and_shape(input_shape, params, framework, shape_only=False):
    if shape_only:
        return [input_shape[-1]]
    if framework == 'TensorFlow':
        return tf.keras.layers.GlobalAveragePooling3D(), [input_shape[-1]]
    elif framework == 'PyTorch':
        return torch_avgpool(), [input_shape[-1]]
    elif framework == 'Jittor':
        return jt_avgpool(), [input_shape[-1]]
    else:
        raise Exception('No support DL framework.')
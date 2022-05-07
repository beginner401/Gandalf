import tensorflow as tf
import torch
import jittor

from src.configuration.support.torch_expansion.average import Average as t_avg
from src.configuration.support.jittor_expansion.average import Average as jt_avg
from src.interpreter.interpreter.ops._cal_broadcast_shape import cal_broadcast_shape


def get_op_and_shape(input_shape, params, framework, shape_only=False):
    t1 = input_shape[0]
    t2 = input_shape[1]
    if not isinstance(t1, list) or not isinstance(t2, list):
        raise Exception('Input shape of layer Average should be a list of lists.')
    # if t1[0] != t2[0]:
    #     raise Exception('Input tensors of layer Add should be with the same batch size.')
    output_shape = cal_broadcast_shape(t1, t2)
    for i in range(2, len(input_shape)):
        if not isinstance(input_shape[i], list):
            raise Exception('Input shape of layer Add should be a list of lists.')
        output_shape = cal_broadcast_shape(output_shape, input_shape[i])
    if shape_only:
        return output_shape
    if framework == 'TensorFlow':
        return tf.keras.layers.Average(), output_shape
    elif framework == 'PyTorch':
        return t_avg(), output_shape
    elif framework == 'Jittor':
        return jt_avg(), output_shape
    else:
        raise Exception('No support DL framework.')
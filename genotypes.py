from collections import namedtuple

Genotype = namedtuple('Genotype', 'normal normal_concat reduce reduce_concat')

PRIMITIVES = [
    'none',
    'max_pool_3x3',
    'avg_pool_3x3',
    'skip_connect',
    # "MB_3x3_3",
    # "MB_3x3_3_HS",
    # "MB_3x3_6",
    # "MB_3x3_6_HS",
    # "MB_5x5_3",
    # "MB_5x5_3_HS",
    # "MB_5x5_6",
    # "MB_5x5_6_HS",
    # "MB_7x7_3",
    # "MB_7x7_3_HS",
    # "MB_7x7_6",
    # "MB_7x7_6_HS",
    'sep_conv_3x3',
    'sep_conv_5x5',
    'dil_conv_3x3',
    'dil_conv_5x5'
]

NASNet = Genotype(
  normal = [
    ('sep_conv_5x5', 1),
    ('sep_conv_3x3', 0),
    ('sep_conv_5x5', 0),
    ('sep_conv_3x3', 0),
    ('avg_pool_3x3', 1),
    ('skip_connect', 0),
    ('avg_pool_3x3', 0),
    ('avg_pool_3x3', 0),
    ('sep_conv_3x3', 1),
    ('skip_connect', 1),
  ],
  normal_concat = [2, 3, 4, 5, 6],
  reduce = [
    ('sep_conv_5x5', 1),
    ('sep_conv_7x7', 0),
    ('max_pool_3x3', 1),
    ('sep_conv_7x7', 0),
    ('avg_pool_3x3', 1),
    ('sep_conv_5x5', 0),
    ('skip_connect', 3),
    ('avg_pool_3x3', 2),
    ('sep_conv_3x3', 2),
    ('max_pool_3x3', 1),
  ],
  reduce_concat = [4, 5, 6],
)
    
AmoebaNet = Genotype(
  normal = [
    ('avg_pool_3x3', 0),
    ('max_pool_3x3', 1),
    ('sep_conv_3x3', 0),
    ('sep_conv_5x5', 2),
    ('sep_conv_3x3', 0),
    ('avg_pool_3x3', 3),
    ('sep_conv_3x3', 1),
    ('skip_connect', 1),
    ('skip_connect', 0),
    ('avg_pool_3x3', 1),
    ],
  normal_concat = [4, 5, 6],
  reduce = [
    ('avg_pool_3x3', 0),
    ('sep_conv_3x3', 1),
    ('max_pool_3x3', 0),
    ('sep_conv_7x7', 2),
    ('sep_conv_7x7', 0),
    ('avg_pool_3x3', 1),
    ('max_pool_3x3', 0),
    ('max_pool_3x3', 1),
    ('conv_7x1_1x7', 0),
    ('sep_conv_3x3', 5),
  ],
  reduce_concat = [3, 4, 6]
)

DARTS_V1 = Genotype(normal=[('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 0), ('sep_conv_3x3', 1), ('skip_connect', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('skip_connect', 2)], normal_concat=[2, 3, 4, 5], reduce=[('max_pool_3x3', 0), ('max_pool_3x3', 1), ('skip_connect', 2), ('max_pool_3x3', 0), ('max_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('avg_pool_3x3', 0)], reduce_concat=[2, 3, 4, 5])
DARTS_V2 = Genotype(normal=[('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 1), ('sep_conv_3x3', 1), ('skip_connect', 0), ('skip_connect', 0), ('dil_conv_3x3', 2)], normal_concat=[2, 3, 4, 5], reduce=[('max_pool_3x3', 0), ('max_pool_3x3', 1), ('skip_connect', 2), ('max_pool_3x3', 1), ('max_pool_3x3', 0), ('skip_connect', 2), ('skip_connect', 2), ('max_pool_3x3', 1)], reduce_concat=[2, 3, 4, 5])


PC_DARTS_cifar = Genotype(normal=[('sep_conv_3x3', 1), ('skip_connect', 0), ('sep_conv_3x3', 0), ('dil_conv_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 1), ('avg_pool_3x3', 0), ('dil_conv_3x3', 1)], normal_concat=range(2, 6), reduce=[('sep_conv_5x5', 1), ('max_pool_3x3', 0), ('sep_conv_5x5', 1), ('sep_conv_5x5', 2), ('sep_conv_3x3', 0), ('sep_conv_3x3', 3), ('sep_conv_3x3', 1), ('sep_conv_3x3', 2)], reduce_concat=range(2, 6))
PC_DARTS_image = Genotype(normal=[('skip_connect', 1), ('sep_conv_3x3', 0), ('sep_conv_3x3', 0), ('skip_connect', 1), ('sep_conv_3x3', 1), ('sep_conv_3x3', 3), ('sep_conv_3x3', 1), ('dil_conv_5x5', 4)], normal_concat=range(2, 6), reduce=[('sep_conv_3x3', 0), ('skip_connect', 1), ('dil_conv_5x5', 2), ('max_pool_3x3', 1), ('sep_conv_3x3', 2), ('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('sep_conv_3x3', 3)], reduce_concat=range(2, 6))

WAPC_DARTS_cifar1 = [1,1, 2, 7, 7, 8, 5, 8, 6, 1, 8, 1, 8, 1, 7, 8, 8, 8, 7, 8, 8, 8, 1, 1, 8, 8, 8, 8, 8, 8, 8, 1, 1, 1, 1, 8, 8, 8, 8, 1, 1, 1, 1, 1, 4]
WAPC_DARTS_cifar2 =[9, 7, 7, 9, 5, 1, 5, 9, 9, 5, 9, 5, 9, 9, 9, 9, 9, 9, 7, 9, 9, 9, 9, 7, 9, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
WAPC_DARTS_cifar3 =[9, 9, 7, 9, 5, 8, 9, 9, 6, 5, 9, 7, 7, 7, 7, 9, 7, 9, 9, 9, 9, 9, 9, 9, 9, 1, 9, 1, 9, 1, 9, 9, 9, 9, 9, 1, 1, 1, 1, 9, 1, 1, 1, 1, 7]
WAPC_DARTS_cifar4 =[9, 1, 8, 9, 9, 9, 9, 9, 7, 9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]#search-EXP-20190924-112226 95.5
WAPC_DARTS_cifar6 =[2, 7, 9, 8, 8, 9, 7, 9, 9, 9, 9, 9, 8, 9, 9, 9, 9, 9, 9, 9, 8, 9, 8, 9, 9]#search-EXP-20190926-090819  95.47
WAPC_DARTS_cifar7 =[1, 7, 8, 5, 9, 9, 7, 9, 9, 9, 1, 8, 1, 9, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]#search-EXP-20190925-232116
WAPC_DARTS_cifar5 =[9, 7, 7, 9, 5, 1, 5, 8, 8, 9, 7, 6, 7, 9, 9, 1, 9, 1, 1, 9, 9, 9, 9, 9, 9, 9, 8, 1, 9, 9, 9, 9, 9, 9, 9]
WAPC_DARTS_cifar8 =[9, 5, 7, 5, 5, 9, 9, 9, 9, 9, 9, 9, 8, 9, 9, 9, 9, 9, 7, 9, 9, 9, 9, 9, 9]#search-EXP-20190927-004035  95.7
WAPC_DARTS_cifar9 =[1, 4, 5, 6, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6]#t=6  search-EXP-20190928-171533 95.5

WAPC_nodes=[[0, 1], [0, 2], [0, 2], [0, 4], [0, 1], [0, 1], [0, 2], [0, 4], [0, 1], [0, 2], [0, 1], [0, 1], [0, 1], [0, 1], [1, 2], [0, 1], [0, 1], [0, 1], [0, 3], [1, 3], [0, 1], [1, 2], [0, 1], [0, 4], [0, 1], [1, 2], [0, 1], [2, 4], [0, 1], [0, 1], [1, 2], [3, 4]]  #96,48 channels 96.5
WAPC_DARTS_cifar_yuanshi=[4, 1, 5, 4, 5, 4, 5, 1, 4, 4, 4, 4, 4, 4, 3, 5, 3, 1, 5, 1, 5, 4, 1, 5, 4, 4, 6, 5, 4, 5, 5, 5, 1, 1, 1, 7, 7, 1, 5, 4, 7, 1, 5, 1, 4, 4, 4, 5, 5, 7, 5, 7, 4, 5, 5, 5, 1, 5, 5, 5, 4, 5, 4, 1, 1, 7, 7, 1, 1, 1, 5, 5, 5, 4, 5, 5, 5, 7, 7, 4, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 7, 7, 7, 5, 5, 5, 5, 5, 5, 5, 5, 7, 5, 7, 5, 5, 7, 7, 1]
WAPC_nodes2=[[0, 1], [0, 2], [0, 2], [1, 3], [0, 1], [0, 1], [1, 2], [1, 4], [0, 1], [0, 1], [0, 1], [0, 3], [0, 1], [0, 1], [0, 3], [0, 1], [0, 1], [0, 1], [0, 1], [0, 3], [0, 1], [0, 1], [0, 1], [0, 2], [0, 1], [0, 2], [0, 1], [1, 2], [0, 1], [0, 1], [0, 2], [0, 1], [0, 1], [0, 1], [0, 1], [3, 4]]# 96.54 channels36   96.92 600epochs
WAPC_DARTS_cifar_yuanshi2=[1, 3, 1, 1, 4, 4, 1, 4, 5, 5, 5, 4, 6, 5, 4, 5, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 1, 5, 1, 4, 1, 4, 1, 2, 1, 1, 5, 1, 4, 1, 4, 1, 1, 4, 4, 1, 6, 7, 7, 5, 5, 7, 7, 1, 1, 5, 5, 4, 7, 5, 5, 1, 5, 5, 5, 7, 7, 1, 7, 7, 5, 7, 7, 7, 7, 7, 7, 7, 4, 7, 5, 1, 7, 5, 7, 7, 7, 7, 7, 7, 7, 5, 7, 7, 7, 1, 7, 7, 7, 7, 7, 7, 7, 1, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 7, 1, 1, 1, 5, 7, 1, 1, 1]
WAPC_nodes3=[[0, 1], [0, 1], [0, 2], [0, 3], [0, 1], [0, 1], [1, 2], [0, 1], [0, 1], [0, 1], [0, 1], [0, 4], [0, 1], [0, 2], [0, 1], [1, 4], [0, 1], [0, 1], [1, 2], [1, 3], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 2], [0, 4], [0, 1], [0, 1], [1, 3], [0, 1], [0, 1], [0, 1], [0, 1], [0, 4], [0, 1], [0, 1], [1, 2], [3, 4]]#96.59
WAPC_DARTS_cifar_yuanshi3=[3, 3, 1, 4, 1, 3, 5, 7, 4, 1, 1, 1, 1, 1, 1, 5, 3, 4, 5, 5, 5, 1, 4, 1, 4, 4, 1, 4, 4, 5, 5, 4, 5, 4, 5, 4, 4, 4, 5, 5, 1, 4, 1, 1, 5, 4, 1, 1, 5, 5, 6, 5, 5, 5, 1, 1, 5, 4, 1, 1, 4, 4, 4, 4, 5, 5, 4, 5, 4, 4, 4, 1, 4, 6, 7, 1, 1, 1, 1, 5, 5, 7, 1, 7, 5, 1, 4, 5, 7, 5, 5, 7, 7, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 7, 7, 7, 1, 7, 7, 5, 7, 1, 5, 5, 1, 1, 5, 5, 7, 1, 1]
WAPC_nodes4=[[0, 1], [0, 1], [0, 2], [0, 1], [0, 1], [0, 1], [0, 3], [0, 2], [0, 1], [1, 2], [0, 3], [1, 2], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 2], [0, 3], [0, 1], [0, 1], [0, 1], [1, 4], [0, 1], [0, 1], [0, 3], [0, 4], [0, 1], [0, 1], [1, 2], [0, 3], [0, 1], [0, 1], [0, 1], [1, 4], [0, 1], [0, 1], [2, 3], [3, 4]]
WAPC_DARTS_cifar_yuanshi4=[4, 1, 5, 4, 1, 1, 6, 3, 5, 1, 1, 5, 5, 1, 3, 5, 4, 4, 1, 3, 4, 4, 4, 4, 4, 5, 4, 5, 1, 4, 3, 4, 4, 4, 2, 4, 1, 5, 4, 4, 5, 5, 5, 1, 5, 5, 4, 1, 5, 7, 4, 4, 1, 5, 1, 1, 5, 4, 4, 4, 4, 1, 6, 1, 1, 1, 1, 5, 1, 4, 1, 1, 4, 1, 5, 1, 1, 7, 7, 4, 5, 4, 5, 1, 5, 5, 5, 1, 7, 5, 5, 7, 7, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 7, 1, 7, 7, 7, 7, 7, 5, 7, 1, 7, 7, 7, 7, 7, 7, 1, 7, 1, 5, 5, 1, 5, 5, 7, 7, 5, 7, 1]
#epoch 60 batch 160
WAPC_nodes5=[[0, 1], [0, 1], [0, 2], [3, 4], [0, 1], [0, 1], [0, 1], [0, 2], [0, 1], [0, 2], [0, 3], [2, 4], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [1, 2], [1, 2], [0, 1], [0, 1], [0, 2], [0, 1], [0, 1], [0, 2], [0, 3], [0, 4], [0, 1], [0, 1], [1, 2], [0, 1], [0, 1], [1, 2], [0, 1], [1, 4], [0, 1], [1, 2], [2, 3], [2, 4]]
WAPC_DARTS_cifar_yuanshi5=[4, 1, 4, 4, 4, 3, 1, 3, 1, 5, 4, 4, 1, 1, 5, 5, 3, 1, 5, 3, 4, 5, 5, 5, 4, 4, 4, 7, 1, 1, 4, 4, 4, 4, 4, 4, 4, 2, 5, 5, 5, 4, 5, 1, 5, 5, 1, 1, 5, 7, 5, 3, 5, 7, 5, 5, 5, 4, 5, 5, 4, 7, 6, 6, 7, 4, 4, 4, 5, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 2, 1, 7, 5, 5, 5, 5, 5, 7, 2, 5, 7, 7, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 7, 5, 7, 7, 1, 7, 7, 7, 1, 7, 5, 1, 7, 7, 7, 7, 7, 1, 5, 5, 7, 1, 1, 5, 7, 5, 1, 5, 7, 1, 1, 1]
#epoch 60 batch 160
WAPC_nodes6=[[0, 1], [0, 2], [0, 2], [1, 4], [0, 1], [0, 1], [0, 2], [0, 1], [0, 1], [1, 2], [0, 3], [0, 2], [0, 1], [0, 1], [0, 1], [1, 4], [0, 1], [0, 1], [0, 2], [1, 3], [0, 1], [0, 1], [1, 2], [1, 2], [0, 1], [0, 1], [0, 2], [0, 1], [0, 1], [1, 2], [1, 3], [1, 3], [0, 1], [1, 2], [2, 3], [3, 4]]#96.769 600epochs
WAPC_DARTS_cifar_yuanshi6=[1, 2, 3, 4, 5, 7, 1, 4, 1, 4, 4, 7, 1, 5, 1, 5, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 5, 4, 1, 3, 1, 1, 1, 1, 5, 1, 7, 1, 1, 7, 1, 5, 2, 1, 4, 1, 5, 5, 1, 4, 4, 5, 1, 1, 1, 1, 4, 5, 5, 7, 4, 4, 1, 4, 4, 4, 5, 4, 6, 1, 7, 4, 1, 4, 5, 1, 1, 1, 4, 4, 5, 4, 1, 5, 5, 5, 5, 7, 5, 5, 7, 7, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 5, 7, 7, 1, 7, 5, 5, 1, 5, 5, 1, 7, 5, 7, 7, 1, 1]
#cifar100 layers10  81.519
WAPC_nodes7=[[0, 1], [0, 2], [0, 2], [0, 4], [0, 1], [0, 1], [0, 2], [0, 4], [0, 1], [1, 2], [0, 2], [2, 4], [0, 1], [0, 2], [0, 1], [0, 1], [0, 1], [0, 1], [1, 2], [0, 1], [0, 1], [0, 1], [1, 2], [0, 4], [0, 1], [0, 1], [0, 3], [0, 4], [0, 1], [0, 1], [1, 2], [1, 4], [0, 1], [0, 1], [0, 2], [1, 4], [0, 1], [0, 1], [0, 1], [2, 3]]
WAPC_DARTS_cifar_yuanshi7=[1, 1, 5, 4, 5, 1, 4, 3, 4, 4, 3, 5, 5, 4, 3, 4, 3, 5, 1, 6, 5, 3, 3, 1, 5, 4, 1, 1, 4, 4, 4, 1, 4, 4, 5, 4, 4, 5, 4, 5, 1, 1, 5, 7, 4, 1, 7, 1, 1, 7, 7, 4, 5, 1, 1, 1, 5, 4, 1, 1, 4, 5, 4, 7, 7, 5, 1, 1, 7, 6, 2, 5, 1, 4, 4, 4, 1, 1, 4, 1, 4, 4, 1, 1, 5, 5, 5, 7, 7, 1, 5, 1, 1, 5, 5, 7, 7, 1, 1, 7, 7, 7, 7, 5, 7, 5, 7, 7, 7, 7, 7, 1, 1, 7, 7, 7, 7, 1, 7, 7, 1, 7, 7, 7, 7, 7, 5, 5, 7, 7, 7, 5, 7, 5, 7, 5, 5, 1, 1, 1]
#cifar100 layers10 wd 3e-4
WAPC_nodes8=[[0, 1], [0, 1], [0, 2], [0, 3], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 3], [1, 3], [0, 1], [0, 2], [1, 3], [0, 1], [0, 1], [0, 1], [0, 2], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 2], [2, 3], [0, 4], [0, 1], [0, 1], [1, 3], [0, 1], [0, 1], [0, 1], [0, 2], [1, 4], [0, 1], [0, 1], [0, 2], [2, 3]]
WAPC_DARTS_cifar_yuanshi8=[3, 3, 5, 4, 1, 3, 1, 3, 4, 3, 3, 1, 5, 6, 3, 4, 4, 4, 5, 5, 4, 5, 4, 5, 5, 4, 5, 5, 4, 3, 4, 4, 1, 1, 4, 2, 1, 4, 4, 4, 5, 5, 1, 1, 2, 5, 1, 5, 5, 7, 4, 5, 5, 1, 7, 1, 7, 4, 4, 1, 1, 1, 4, 1, 1, 4, 5, 5, 5, 7, 1, 7, 4, 5, 4, 4, 1, 1, 1, 4, 4, 4, 4, 1, 5, 1, 5, 5, 1, 5, 5, 1, 7, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 5, 7, 7, 5, 7, 7, 5, 7, 7, 1, 7, 7, 4, 7, 7, 7, 7, 7, 5, 7, 7, 7, 1, 5, 5, 7, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 5]


PCDARTS = WAPC_DARTS_cifar_yuanshi8


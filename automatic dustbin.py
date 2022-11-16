def create_detector_network():
    inp = Input(shape=(128, 128, 512))
x = Conv2D(128, kernel_size=3, strides=1, name='detect_1', padding='same')(inp)
x = BatchNormalization()(x)
x = Conv2D(65, kernel_size=1, strides=1, name='detect_2')(x)
x = BatchNormalization()(x)
x = Activation('softmax')(x)
x = Lambda(lambda x: x[:,:,:,:-1])(x) 
x = UpSampling2D(size=(8, 8), data_format=None, interpolation='nearest')(x)
x = Conv2D(1, kernel_size=1, strides=1, name='reduce_dim')(x)

return Model(inp, x)

_________________________________________________________________
Layer (type)                 Output Shape              Param   
=================================================================
input_33 (InputLayer)        [(None, 128, 128, 512)]   0         
_________________________________________________________________
detect_1 (Conv2D)            (None, 128, 128, 128)     589952    
_________________________________________________________________
batch_normalization_14 (Batc (None, 128, 128, 128)     512       
_________________________________________________________________
detect_2 (Conv2D)            (None, 128, 128, 65)      8385      
_________________________________________________________________
batch_normalization_15 (Batc (None, 128, 128, 65)      260       
_________________________________________________________________
activation_7 (Activation)    (None, 128, 128, 65)      0         
_________________________________________________________________
lambda_7 (Lambda)            (None, 128, 128, 64)      0         
_________________________________________________________________
up_sampling2d_7 (UpSampling2 (None, 1024, 1024, 64)    0         
_________________________________________________________________
reduce_dim (Conv2D)          (None, 1024, 1024, 1)     65        
=================================================================
,def create_detector_network():
    inp = Input(shape=(128, 128, 512))
     x = Conv2D(128, kernel_size=3, strides=1, name='detect_1', padding='same')(inp)
     x = BatchNormalization()(x)
     x = Conv2D(65, kernel_size=1, strides=1, name='detect_2')(x)
     x = BatchNormalization()(x)
     x = Activation('softmax')(x)
     x = Lambda(lambda x: x[:,:,:,:-1])(x) 
     x = UpSampling2D(size=(8, 8), data_format=None, interpolation='nearest')(x)
     x = Conv2D(1, kernel_size=1, strides=1, name='reduce_dim')(x)

     return Model(inp, x)

_________________________________________________________________
Layer (type)                 Output Shape              Param   
=================================================================
input_33 (InputLayer)        [(None, 128, 128, 512)]   0         
_________________________________________________________________
detect_1 (Conv2D)            (None, 128, 128, 128)     589952    
_________________________________________________________________
batch_normalization_14 (Batc (None, 128, 128, 128)     512       
_________________________________________________________________
detect_2 (Conv2D)            (None, 128, 128, 65)      8385      
_________________________________________________________________
batch_normalization_15 (Batc (None, 128, 128, 65)      260       
_________________________________________________________________
activation_7 (Activation)    (None, 128, 128, 65)      0         
_________________________________________________________________
lambda_7 (Lambda)            (None, 128, 128, 64)      0         
_________________________________________________________________
up_sampling2d_7 (UpSampling2 (None, 1024, 1024, 64)    0         
_________________________________________________________________
reduce_dim (Conv2D)          (None, 1024, 1024, 1)     65        
=================================================================

layers = [
        ('ElasticLayer', {
            'translation'   :3,
            'img_sz'        :48,
            'zoom'          :1.1,
            'magnitude'     :48,
            'sigma'         :8,
            'pflip'         :.02,
            }),
        # ('InputLayer', {
        #     'max_perturb'   :4,
        #     'img_sz'        :68,
        #     'pflip'         :.05,
        #     'batch_sz'      :20,
        #     'num_maps'      :1,
        #     }),
        ('HiddenLayer', {
            'n_out'         :1000,
            'pdrop'         :.5,
            'actvn'         :'relu',
            }),
        ('HiddenLayer', {
            'n_out'         :1000,
            'pdrop'         :.5,
            'actvn'         :'relu',
            }),
#       ('CenteredOutLayer', {
#           'centers'       :None,
#           'n_features'    :100,
#           'n_classes'     :10,
#           'kind'          :'RBF',
#           'learn_centers' :True, 
#           'junk_dist'     :1e6,
#           }),
        ('SoftAuxLayer', {
            'n_aux'         :7,
            'aux_actvn'     :"relu",
            'aux_type'      :"LocationInfo",
            'n_out'         :457,
            }),
]

training_params = {
	'BATCH_SZ' : 20,
    'NUM_EPOCHS' : 201,
    'TRAIN_ON_FRACTION' : .75,
    'EPOCHS_TO_TEST' : 1,
    'TEST_SAMP_SZ': 5000,
    'DEFORM'    : None,
    'DFM_PRMS' : {},

    'MOMENTUM' : .95,
    'INIT_LEARNING_RATE': .1,
    'EPOCHS_TO_HALF_RATE':  1,
    'LAMBDA1': 0.0,
    'LAMBDA2': 0.001,
    'MAXNORM': 3.5,
}

# TODO:
    # Move regularization to layer

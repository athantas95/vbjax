from .loops import make_sde, make_ode, make_dde, make_sdde
from .shtlc import make_shtdiff
from .neural_mass import (
        JRState, JRTheta, jr_dfun, jr_default_theta,
        MPRState, MPRTheta, mpr_dfun, mpr_default_theta,
        )
from .regmap import make_region_mapping
from .coupling import make_diff_cfun, make_linear_cfun
from .connectome import make_conn_latent_mvnorm
from .sparse import make_spmv
from .layers import make_dense_layers
from .diagnostics import shrinkage_zscore
from .embed import embed_neural_flow, embed_polynomial, embed_gradient, embed_autoregress
from ._version import __version__


# some random setup for convenience
from jax import random
key = random.PRNGKey(42)
keys = random.split(key, 100)
def randn(*shape, key=key):
    return random.normal(key, shape)

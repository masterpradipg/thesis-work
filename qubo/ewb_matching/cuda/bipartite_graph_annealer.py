from __future__ import print_function
import numpy as np
import thesis_qubo
from thesis_qubo.common.bipartite_graph_annealer_base import BipartiteGraphAnnealerBase
from thesis_qubo.common import docstring
from . import cuda_bg_annealer as cext
from . import device


class BipartiteGraphAnnealer(BipartiteGraphAnnealerBase) :

    def __init__(self, b0, b1, W, optimize, dtype, prefdict) :
        self._cobj = cext.new(dtype)
        cext.assign_device(self._cobj, device.active_device._cobj, dtype)
        self._device = device.active_device
        BipartiteGraphAnnealerBase.__init__(self, cext, dtype, b0, b1, W, optimize, prefdict)


def bipartite_graph_annealer(b0 = None, b1 = None, W = None, \
                             optimize = thesis_qubo.minimize, dtype = np.float64, **prefs) :
    return BipartiteGraphAnnealer(b0, b1, W, optimize, dtype, prefs)

docstring.inherit(BipartiteGraphAnnealer, thesis_qubo.py.BipartiteGraphAnnealer)

if __name__ == '__main__' :
    N0 = 40
    N1 = 40
    m = 20
    
    np.random.seed(0)
            
    W = np.random.random((N1, N0)) - 0.5
    b0 = np.random.random((N0)) - 0.5
    b1 = np.random.random((N1)) - 0.5

    an = bipartite_graph_annealer(b0, b1, W, thesis_qubo.minimize, n_trotters=m)
    
    Ginit = 5
    Gfin = 0.01
    beta = 1. / 0.02
    tau = 0.99
    n_repeat = 10

    for loop in range(0, n_repeat) :
        an.prepare()
        an.randomize_spin()
        G = Ginit
        while Gfin < G :
            an.anneal_one_step(G, beta)
            G = G * tau
        an.make_solution()

        E = an.get_E()
        x = an.get_x()
        print(E.shape, E)
        print(x)

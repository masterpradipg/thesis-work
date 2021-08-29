#include <thesis/thesis/thesis.h>

namespace {

template<class real>
using Annealer = thesisq::cuda::DenseGraphAnnealer<real>;

template<class real>
Annealer<real> *newAnnealer() {
    return thesisq::cuda::newDenseGraphAnnealer<real>();
}

}

#define modname "cuda_dg_annealer"
#define INIT_MODULE INITFUNCNAME(cuda_dg_annealer)
#define DENSE_GRAPH
#define CUDA_SOLVER

#include <sqaodc/pyglue/annealer.inc>

#include <thesis/thesis/thesis.h>

namespace {

template<class real>
using Annealer = thesisq::DenseGraphAnnealer<real>;

template<class real>
Annealer<real> *newAnnealer() {
    return thesisq::cpu::newDenseGraphAnnealer<real>();
}

}

#define modname "cpu_dg_annealer"
#define INIT_MODULE INITFUNCNAME(cpu_dg_annealer)

#define DENSE_GRAPH

#include <sqaodc/pyglue/annealer.inc>

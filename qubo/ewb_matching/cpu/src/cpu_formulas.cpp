#include <thesis/thesis/thesis.h>

namespace {

template<class real> using DGFormulas = sq::DenseGraphFormulas<real>;
template<class real> using BGFormulas = sq::BipartiteGraphFormulas<real>;

template<class real>
DGFormulas<real> *newDGFormulas() {
    return thesisq::cpu::newDenseGraphFormulas<real>();
}

template<class real>
BGFormulas<real> *newBGFormulas() {
    return thesisq::cpu::newBipartiteGraphFormulas<real>();
}

}

#define modname "cpu_formulas"
#define INIT_MODULE INITFUNCNAME(cpu_formulas)

#include <sqaodc/pyglue/formulas.inc>

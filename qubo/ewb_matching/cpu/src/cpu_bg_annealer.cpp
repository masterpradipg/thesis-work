#include <thesis/thesis/thesis.h>

namespace {

template<class real>
using Annealer = sq::BipartiteGraphAnnealer<real>;

template<class real>
Annealer<real> *newAnnealer() {
    return thesisq::cpu::newBipartiteGraphAnnealer<real>();
}

}

#define modname "cpu_bg_annealer"
#define INIT_MODULE INITFUNCNAME(cpu_bg_annealer)
#define BIPARTITE_GRAPH

#include <sqaodc/pyglue/annealer.inc>

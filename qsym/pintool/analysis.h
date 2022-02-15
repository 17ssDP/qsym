#ifndef QSYM_ANALYZE_H_
#define QSYM_ANALYZE_H_

#include "pin.H"
#include "logging.h"

namespace qsym {

void analyzeTrace(TRACE, VOID*);

void analyzeInstruction(INS);

void analyzeImage(IMG img, void* v);
} // namespace qsym

#endif // QSYM_ANALYZE_H_

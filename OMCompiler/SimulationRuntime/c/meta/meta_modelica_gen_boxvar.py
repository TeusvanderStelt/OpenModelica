#!/usr/bin/env python2

functions = [
'arrayAppend',
'arrayCopy',
'arrayGet',
'arrayList',
'arrayNth',
'arrayUpdate',
'boolAnd',
'boolEq',
'boolNot',
'boolOr',
'boolString',
'cons',
'equality',
'getGlobalRoot',
'intAbs',
'intAdd',
'intDiv',
'intEq',
'intGe',
'intGt',
'intLe',
'intLt',
'intMax',
'intMin',
'intMod',
'intMul',
'intNe',
'intNeg',
'intReal',
'intString',
'intStringChar',
'intSub',
'isNone',
'isSome',
'listAppend',
'listArray',
'listDelete',
'listEmpty',
'listGet',
'listHead',
'listLength',
'listMember',
'listNth',
'listRest',
'listReverse',
'listReverseInPlace',
'print',
'realAbs',
'realAdd',
'realDiv',
'realEq',
'realGe',
'realGt',
'realInt',
'realLe',
'realLt',
'realMax',
'realMin',
'realMod',
'realMul',
'realNe',
'realNeg',
'realPow',
'realString',
'realSub',
'setGlobalRoot',
'stringAppend',
'stringCharInt',
'stringCompare',
'stringDelimitList',
'stringEq',
'stringEqual',
'stringGet',
'stringGetStringChar',
'stringHash',
'stringHashDjb2',
'stringHashDjb2Mod',
'stringHashSdbm',
'stringInt',
'stringLength',
'stringReal',
'stringUpdateStringChar',
'substring',
'valueConstructor',
'valueEq',
'valueHashMod'
]

print '/* Code generated by meta_modelica_gen_boxvar.py */'
print ''
print '#if !(defined(OMC_MINIMAL_RUNTIME) || defined(OMC_FMI_RUNTIME))'
print ''
print '#if !defined(OMC_GENERATE_RELOCATABLE_CODE) || defined(OMC_BOOTSTRAPPING_STAGE_1) || defined(OMC_BOOTSTRAPPING_STAGE_2)'
print '#define OMC_SYM_BOXPTR(X) &boxptr_##X'
print '#else'
print '#define OMC_SYM_BOXPTR(X) &boxvar_fn_##X'
for f in functions:
  print 'static void* boxvar_fn_%s = (void*) boxptr_%s;' % (f,f)
print '#endif'
for f in functions:
  print 'static const MMC_DEFSTRUCTLIT(boxvar_lit_%s,2,0) {(modelica_metatype) OMC_SYM_BOXPTR(%s),0}};' % (f,f)
  print '#define boxvar_%s MMC_REFSTRUCTLIT(boxvar_lit_%s)' % (f,f)
print ''
print '#undef OMC_SYM_BOXPTR'
print '#endif /* #if !(defined(OMC_MINIMAL_RUNTIME) || defined(OMC_FMI_RUNTIME)) */'

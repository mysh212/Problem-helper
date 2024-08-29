import os
from core.general import *

def auto_rename():
    cd(road('package','problems'))
    problems = ls()
    info(f'Found {len(problems)} problems:')
    mmax = max([len(i) for i in problems])
    for i in problems:
        info(f'    {i.ljust(mmax)} -> {i.title()}')
    tmp = input('Rename? [y/N]')
    if tmp.lower() != 'y': return;
    for i in problems:
        info(f'Renaming {i} into {i.title()}')
        os.rename(i,i.title())
    info('Finished.',['RENAME'])
    return

def rename():
    cd(road('package','problems'))
    problems = ls()
    info(f'Found {len(problems)} problems:')
    mmax = max([len(i) for i in problems])
    f = []
    for i in problems:
        f.append(input(f'    {i.ljust(mmax)} -> '))
    tmp = input('Rename? [y/N]')
    if tmp.lower() != 'y': return;
    for i in range(len(f)):
        info(f'Renaming {problems[i]} into {f[i]}')
        os.rename(problems[i],f[i])
    info('Finished.',['RENAME'])
    return
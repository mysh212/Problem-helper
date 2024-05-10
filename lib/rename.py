import os
from core.lib import *

def auto_rename():
    cd(road('package','problems'))
    problems = ls()
    info(f'Found {len(problems)} problems:')
    for i in problems:
        info(f'    {i}')
    tmp = input('Rename? [y/N]')
    if tmp.lower() != 'y': return;
    for i in problems:
        info(f'Renaming {i} into {i[0].upper() + i[1:].lower()}')
        os.rename(i,i[0].upper() + i[1:].lower())
    info('Finished.',['RENAME'])
    return

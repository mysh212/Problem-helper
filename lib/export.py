# Author : ysh
# 2024/05/09 Thu 10:31:40
import os, shutil
import xml.etree.ElementTree as ET
from core.general import *

problems = []

def make_dir():
    cd(root)
    pd = ['Problems','Testcases','Generator','Scripts','Validator','Ranking','package','Solutions','Testers','Checkers']
    for i in pd:
        mkdir(i)

def get_problems():
    cd(f'{root}/package/problems')
    global problems
    problems = ls()
    # debug(problems)
    cd('../..')
    return problems

def copy_testcases():
    cd(f'{root}/package/problems')

    for i in problems:
        info(f'Parsing Problem {i}')
        # debug(pwd())
        cd(i)
        cd('tests')
        try:
            now = ET.parse('../problem.xml').getroot().find('judging').findall('testset')
            for j in now:
                if j.attrib['name'] == 'tests':
                    now = j
                    break
            # debug(['i',i])
            # debug(problems)
            tmp = [i.attrib['group'] for i in now.find('tests').findall('test')]
            groups = []
            t = 1
            pre = {}
            for j in tmp:
                if j in pre: groups.append(pre[j]);
                else:
                    groups.append(t)
                    pre[j] = t
                    t = t + 1
            mkdir(f'{root}/Testcases/{i}')
            info(f'Testcase count: {len(tmp)}',[i])
            info(f'Testgroup count: {len(pre)}',[i])
            for j in range(1,t):
                mkdir(f'{root}/Testcases/{i}/subtask{j}')
            # debug(tmp)
            for j in range(1,len(groups) + 1):
                # debug(f'{pwd()}/{zt(j,2)}')
                cp(zt(j,2),f'{root}/Testcases/{i}/subtask{groups[j - 1]}/{zt(j,2)}.in')
                cp(f'{zt(j,2)}.a',f'{root}/Testcases/{i}/subtask{groups[j - 1]}/{zt(j,2)}.out')
            # debug(['i',i])
            cd('../..')
            continue
        except:
            warning(f'Find no Test groups for Problem {i}, Using Traditional Method')
        # debug(ls())
        now = 0
        while True:
            if exist(zt(now + 1,2)):
                now += 1
                if not exist(f'{zt(now,2)}.a'):
                    error(f'Output {now} for Problem {i} doesn\'t exists')
                    quit(3)
            else:
                break
        info(f'Testcase count: {now}',[i])
        # debug([i,now])
        info(f'Copying Testcases for Problem {i}')
        to = f'{root}/Testcases/{i}/'
        try:
            mkdir(to)
        except:
            warning(f'While Creating dir Testcases/{i}')
        for j in range(1,now + 1):
            cp(zt(j,2),to + zt(j,2) + '.in')
            cp(zt(j,2) + '.a',to + zt(j,2) + '.out')
            print('.',end = '')
        print('')

        cd('../..')

def copy_files():
    cd(f'{root}/package/problems/')
    for i in problems:
        # debug(pwd())
        cd(i)
        checker = ET.parse('problem.xml').getroot().find('assets').find('checker').find('source').attrib['path']
        solutions = [[i.attrib['tag'], i.find('source').attrib['path']] for i in ET.parse('problem.xml').getroot().find('assets').find('solutions').findall('solution')]

        generator = None
        try:
            generator = ET.parse('problem.xml').getroot().find('judging').findall('testset')
            for j in generator:
                if j.attrib['name'] == 'tests':
                    generator = j
                    break
            # debug(['i',i])
            # debug(problems)
            tmp = [i.attrib['cmd'].split()[0] for i in generator.find('tests').findall('test')]
            tmp = list(set(tmp))
            # debug(['tmp',tmp])
            info(f'Generator for Problem {i} found. Copying')
            mkdir(f'{root}/Generator/{i}')
            for j in tmp:
                for k in ls('files/'):
                    if k.startswith(f'{j}.') and not k.endswith('.exe'):
                        # debug(['k',k])
                        cp('files/' + k,f'{root}/Generator/{i}/{getfilename(k)}')

            
            tmp = [i.attrib['cmd'] for i in generator.find('tests').findall('test')]
            info(f'Generating Script for Problem {i}')
            # mkdir(f'{root}/Scripts/')
            with open(f'{root}/Scripts/{i}.script','w') as f:
                # debug('\n'.join(tmp))
                f.write('\n'.join(tmp))
        except:
            warning(f'Find no Generator for Problem {i}')
        # debug(type(ET.parse('problem.xml').getroot().find('assets').find('validators')))
        # if ET.parse('problem.xml').getroot().find('assets').find('validators'):
        try:
            validator = ET.parse('problem.xml').getroot().find('assets').find('validators').find('validator').find('source').attrib['path']
            info(f'Validator for Problem {i} found. Copying.')
            to = f'{root}/Validator/{i}/'
            mkdir(to)
            cp(validator,to + getfilename(validator))
        except:
            warning(f'Valiator for Problem {i} is not found.')
        # DEBUG [['rejected', 'solutions/Sum_flow.cpp'], ['rejected', 'solutions/Sum_subtask1.cpp'], ['main', 'solutions/Sum_subtask4.cpp']]

        info(f'Copying Checker for Problem {i}')
        mkdir(f'{root}/Checkers/{i}')
        # debug(f'{pwd()}/{checker}')
        cp(checker,f'{root}/Checkers/{i}/{getfilename(checker)}')

        info(f'Copying Solutions for Problem {i}')
        mkdir(f'{root}/Solutions/{i}')

        for j in solutions:
            # debug(j[1])
            ans = getfilename(j[1])
            if j[0] == 'main':
                name, exd = os.path.splitext(getfilename(j[1]))
                ans = name + '.AC' + exd
            cp(j[1],f'{root}/Solutions/{i}/{ans}')
            print('.',end = '')
        print('')


        cd('..')


def main():
    if input(f'Now in {pwd()} , Are you sure to execute operation? [y/N]').lower() != 'y': quit();

    make_dir()
   
    info('Moving testcases into right dir')
    get_problems()

    copy_testcases()

    copy_files()

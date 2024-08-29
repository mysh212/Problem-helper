# Author : ysh
# 2024/05/09 Thu 15:15:31
import lib.export
import lib.publish
import lib.rename
import sys, core.general
import argparse

parser = argparse.ArgumentParser(description = 'fool')
parser.add_argument('-e','--export',help = 'Export contest to a GitHub project',action = 'store_true')
parser.add_argument('-m','--make_README',help = 'Make README file',action = 'store_true')
# parser.add_argument('-rn','--rename',help = 'Make all problem name prettier',action = 'store_true')
rn = parser.add_argument_group('RENAME','Rename')
rn.add_argument('-rn','--rename',action = 'store_true')
rn.add_argument('-ra','--rename-auto',action = 'store_true')
az = parser.parse_args()
# parser._add_action('-q')
if az.export: lib.export.main()
if az.make_README: lib.publish.main()
if az.rename_auto: lib.rename.auto_rename()
if az.rename: lib.rename.rename()
# print(az._get_args())
# print(vars(az))
if len(sys.argv) == 1:
    core.general.error('No argument found')
# print(az.export)
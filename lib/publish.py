# Author : ysh
# 2024/05/09 Thu 18:13:52
from core.general import *

def main():
    page_url = 'https://mysh212.github.io'
    github_url = 'https://github.com'
    contest_name = 'CHSH-nhspc115-PRE'
    username = 'mysh212'
    footer = '***HARC X CHSH***'
    contest_title = '''彰化高中 115學年度 資訊學科能力競賽 校內初賽'''

    template = f'''# **{contest_title}**

 - [排名 ***<font color='#AAAAAA'>Rank</font>***]({page_url}/{contest_name}/Ranking/)
 - [官解 ***<font color='#AAAAAA'>Solutions</font>***]({github_url}/{username}/{contest_name}/tree/main/Solutions)
 - [審題者 ***<font color='#AAAAAA'>Tester</font>***]({page_url}/{contest_name}/Tester)
 - [測資產生器 ***<font color='#AAAAAA'>Generator</font>***]({github_url}/{username}/{contest_name}/tree/main/Generator)
 - [測資驗證器 ***<font color='#AAAAAA'>Validator</font>***]({github_url}/{username}/{contest_name}/tree/main/Validator)
 - [測資生成指令 ***<font color='#AAAAAA'>Scripts</font>***]({github_url}/{username}/{contest_name}/tree/main/Scripts)
 - [題解 ***<font color='#AAAAAA'>Editorial</font>***]({github_url}/{username}/{contest_name}/tree/main/Editorial/)
 - [題本 ***<font color='#AAAAAA'>Statements</font>***]({github_url}/{username}/{contest_name}/tree/main/Problems)
 - [測資 ***<font color='#AAAAAA'>Testcases</font>***]({github_url}/{username}/{contest_name}/tree/main/Testcases)
 - [記分板直播](https://youtube.com/live/prVrS0GXyyQ?feature=share)
   
{footer}'''
    cd(root)

    info('Finished.',['Make README'])
    write_to_file('README.md',template)

    return
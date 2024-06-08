# Author : ysh
# 2024/05/09 Thu 18:13:52
from core.general import *

def main():
    page_url = 'https://mysh212.github.io'
    github_url = 'https://github.com'
    contest_name = 'CHSH-nhspc113-PRE'
    username = 'mysh212'
    footer = '***HARC X CHSH***'

    template = f'''# **彰化高中112學年度學科能力競賽 校內複賽**

 - [排名 ***<font color='#AAAAAA'>Rank</font>***]({page_url}/{contest_name}/Ranking/)
 - [官解 ***<font color='#AAAAAA'>Solution</font>***]({github_url}/{username}/{contest_name}/tree/master/Solution)
 - [審題者 ***<font color='#AAAAAA'>Tester</font>***]({page_url}/{contest_name}/Tester)
 - [測資產生器 ***<font color='#AAAAAA'>Generator</font>***]({github_url}/{username}/{contest_name}/tree/master/Generator)
 - [測資驗證器 ***<font color='#AAAAAA'>Validator</font>***]({github_url}/{username}/{contest_name}/tree/master/Validator)
 - [測資生成指令 ***<font color='#AAAAAA'>Script</font>***]({github_url}/{username}/{contest_name}/tree/master/Script)
 - [題解 ***<font color='#AAAAAA'>Editorial</font>***]({github_url}/{username}/{contest_name}/tree/master/Editorial/)
 - [題本]({github_url}/{username}/{contest_name}/tree/master/Problems)
 - [測資 Testcase]({github_url}/{username}/{contest_name}/tree/master/Testcase)
 - [記分板直播](https://youtube.com/live/ayOqapmp6_g)
 - [文件]({github_url}/{username}/{contest_name}/tree/master/Docs)
   - [如何補題]({page_url}/{contest_name}/Docs/)
   
{footer}'''
    
    
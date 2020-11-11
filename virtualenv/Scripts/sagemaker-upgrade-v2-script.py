#!G:\StudyMaterial_M.Tech\FlaskWebProject\virtualenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'sagemaker==2.16.1','console_scripts','sagemaker-upgrade-v2'
__requires__ = 'sagemaker==2.16.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('sagemaker==2.16.1', 'console_scripts', 'sagemaker-upgrade-v2')()
    )

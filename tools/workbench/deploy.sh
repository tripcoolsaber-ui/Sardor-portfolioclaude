#!/bin/bash
cd /tmp/gh || exit 1
STAMP=$(date +%Y%m%d%H%M%S)
python3 - "$STAMP" <<'PY'
import re,sys
stamp=sys.argv[1]; s=open('index.html').read()
s,n=re.subn(r"var B='[A-Za-z0-9_]+';try\{fetch\('version\.txt","var B='%s';try{fetch('version.txt"%stamp,s,count=1)
print('stamp lines',n)
open('index.html','w').write(s); open('version.txt','w').write(stamp)
PY
T='YOUR_GITHUB_TOKEN'
python3 tools/seo_build.py || exit 1
git add -A && git commit -q -m "$1" && git pull -q --no-rebase --no-edit "https://x-access-token:$T@github.com/tripcoolsaber-ui/Sardor-portfolioclaude.git" main 2>&1 | sed "s/$T/***/g"; git push -q "https://x-access-token:$T@github.com/tripcoolsaber-ui/Sardor-portfolioclaude.git" HEAD:main 2>&1 | sed "s/$T/***/g"
git log -1 --format='%h %s'; echo "build $STAMP"

import re,json
P='/tmp/gh/index.html'
def load():
    s=open(P).read()
    m=re.search(r'(<script type="application/json" id="state">)(.*?)(</script>)',s,re.S)
    return s,m,json.loads(m.group(2))
def dump(st):
    return json.dumps(st,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
def save(s,m,st):
    s=s[:m.start(2)]+dump(st)+s[m.end(2):]
    open(P,'w').write(s)

import http.server,os,sys
root,port=sys.argv[1],int(sys.argv[2])
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s,*a,**k): super().__init__(*a,directory=root,**k)
    def log_message(s,*a): pass
    def send_head(s):
        path=s.translate_path(s.path)
        if os.path.isdir(path) and not s.path.split('?')[0].endswith('/'):
            s.send_response(301); s.send_header('Location',s.path.split('?')[0]+'/'); s.end_headers(); return None
        if not os.path.exists(path) or (os.path.isdir(path) and not os.path.exists(os.path.join(path,'index.html'))):
            f=open(os.path.join(root,'404.html'),'rb'); d=f.read()
            s.send_response(404); s.send_header('Content-Type','text/html; charset=utf-8'); s.send_header('Content-Length',str(len(d))); s.end_headers()
            import io; return io.BytesIO(d)
        return super().send_head()
http.server.ThreadingHTTPServer(('',port),H).serve_forever()

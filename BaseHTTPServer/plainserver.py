import time
import urlparse
import BaseHTTPServer

class RouteHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def do_GET(self):
        parsedreq = urlparse.urlparse(self.path)
        messages =  [
                'CLIENT VALUES:',
                'client_address=%s (%s)' % (self.client_address,
                                            self.address_string()),
                'command=%s' % self.command,
                'path=%s' % self.path,
                'real path=%s' % parsedreq.path,
                'query=%s' % parsedreq.query,
                'request_version=%s' % self.request_version,
                '',
                'SERVER VALUES:',
                'server_version=%s' % self.server_version,
                'sys_version=%s' % self.sys_version,
                'protocol_version=%s' % self.protocol_version,
                '',
                'HEADERS RECEIVED:',
                ]
        for name, value in sorted(self.headers.items()):
            messages.append('%s=%s' % (name, value.rstrip()))
        messages.append('')
        output = '\r\n'.join(messages)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(output)
        return
    
if __name__ == '__main__':
    server=BaseHTTPServer.HTTPServer(('localhost',8080),RouteHandler)
    print 'Server started'
    server.serve_forever()
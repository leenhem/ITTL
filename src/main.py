#coding:utf-8
import sys
# import tornado.autoreload
import tornado.options

if __name__ == "__main__":

    print "main 1 getEffectiveLevel = ", LOG.getEffectiveLevel()
    print "tornado default log level = "
    tornado.options.options.logging = "debug"
    tornado.options.parse_command_line()
    print "main getEffectiveLevel = ", LOG.getEffectiveLevel()

    if len(sys.argv) > 1:
        PORT = sys.argv[1]
    applicaton = Application()
    http_server = tornado.httpserver.HTTPServer(applicaton)
    http_server.listen(PORT)
    print 'Development server is running at http://127.0.0.1:%s/' % PORT
    print 'Quit the server with CONTROL-C'
    tornado.ioloop.IOLoop.instance().start()
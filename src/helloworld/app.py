# import tornado.ioloop
# import tornado.web

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, World from LXC!")

# if __name__ == "__main__":
#     app = tornado.web.Application([
#         (r"/", MainHandler),
#     ])
#     app.listen(8888)
#     print("Tornado server is running on port 8888")
#     tornado.ioloop.IOLoop.current().start()

import tornado.ioloop
import tornado.web
import motor.motor_tornado

# Connect to MongoDB
client = motor.motor_tornado.MotorClient('mongodb://hbc:27017')
db = client['local']

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        # Fetch contacts from MongoDB
        contacts = await db.contacts.find().to_list(length=None)
        self.render("index.html", contacts=contacts)

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
    ], template_path="templates")
    app.listen(8888)
    print("Tornado server is running on port 8888")
    tornado.ioloop.IOLoop.current().start()

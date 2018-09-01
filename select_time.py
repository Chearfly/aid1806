#IO的多路复用的三种方法


# from socket import *
# from select import select

# s = socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind('0.0.0.0',8888)
# s.listen(5)

# rlist = [s]
# wlist = []
# xlist = []
# while True:
#     print("等待io发生")
#     rs,ws,xs = select(rlist,wlist,xlist)
#     for r in rs:
#         if r is s:
#             connfd.addr = r.accept()
#             print("connect",addr)
#             rlist.append(connfd)
#         #表示客户端连接，套接字准备就绪
#         else:
#             data = r.recv(1024)
#             if not data:
#                 #从关注列表中删除
#                 rlist.remove(r)
#                 r.close()
#             else:
#                 print("receive",data.decode())
#                 r.send(b'receive your message')

#     for w in ws:
#         w.send("这是一条回复消息".encode())
#         wlist.remove(w)
#     for x in xs:
#         s.close()

# from  socket  import *
# from  socket import *


# s = socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind('0.0.0.0',8888)
# s.listen(5)

# p = poll()


# #创建地图
# fdmap = {s.fileno():s}

# p.register(s,POLLIN|POLLERR)

# while True:
#     events = p.poll()
#     for fd.event in events:
#         if fd == s.fileno():
#             #从地图中找到fd对应的对像
#             c,addr = fdmap[fd].accept()
#             print("connect from",addr)
#             #注册新的io 维护地图
#             p.register(c,POLLIN)
#             fdmap[c.fileno()] = c

#         else:
#             data = fdmap[fd].recv(1024)
#             if not data:
#                 p.unregister(fd)
#                 fdmap[fd].close()
#                 del fdmap[fd]#

#             else:
#                 print(data.decode())
#                 fdmap[fd].send('shoudaole'.encode)



# from  socket  import *
# from  socket import *


# s = socket()
# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# s.bind('0.0.0.0',8888)
# s.listen(5)

# p = epoll()


# #创建地图
# fdmap = {s.fileno():s}

# p.register(s,EPOLLIN|EPOLLERR)

# while True:
#     events = p.Epoll()
#     for fd.event in events:
#         if fd == s.fileno():
#             #从地图中找到fd对应的对像
#             c,addr = fdmap[fd].accept()
#             print("connect from",addr)
#             #注册新的io 维护地图
#             p.register(c,EPOLLIN)
#             fdmap[c.fileno()] = c

#         else:
#             data = fdmap[fd].recv(1024)
#             if not data:
#                 p.unregister(fd)
#                 fdmap[fd].close()
#                 del fdmap[fd]#

#             else:
#                 print(data.decode())
#                 fdmap[fd].send('shoudaole'.encode)



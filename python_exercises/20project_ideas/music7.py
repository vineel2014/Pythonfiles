import pyglet
foo=pyglet.media.load("b.mp3")
foo.play()

def exiter(dt):
    pyglet.app.exit()
print ("Song length is: %f" % foo.duration)
# foo.duration is the song length
pyglet.clock.schedule_once(exiter, foo.duration)

pyglet.app.run()

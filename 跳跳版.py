# Bouncing Pizza
# Demonstrates dealing with screen boundaries

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50) 

class Pizza(games.Sprite):
    """ A bouncing pizza. """
    def update(self):
        """ Reverse a velocity component if edge of screen reached. """
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy
class Pan(games.Sprite):
    """
    A pan controlled by player to catch falling pizzas.
    """
    image = games.load_image("ban.bmp")

    def __init__(self):
        """ Initialize Pan object and create Text object for score. """
        super(Pan, self).__init__(image = Pan.image,
                                  y = 100,
                                  x = games.mouse.x,
                                  bottom = games.screen.height)
        """
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)
        """

    def update(self):
        """ Move to mouse x position. """
        self.x = games.mouse.x
        
        if self.left < 0:
            self.left = 0
            
        if self.right > games.screen.width:
            self.right = games.screen.width
            
        self.check_catch()

    def check_catch(self):
        """ Check if catch pizzas. """
        for pizza in self.overlapping_sprites:
            """
            self.score.value += 10
            self.score.right = games.screen.width - 10 
            pizza.handle_caught()
            """
            pizza.dx=-pizza.dx
            pizza.dy=-pizza.dy


def main():
    wall_image = games.load_image("wall.jpg", transparent = False)
    games.screen.background = wall_image

    pizza_image = games.load_image("ball.bmp")
    the_pizza = Pizza(image = pizza_image,
                      x = games.screen.width/2,
                      y = games.screen.height/2,
                      dx = 1,
                      dy = 1)
    the_pizza1 = Pizza(image = pizza_image,
                      x = games.screen.width/3,
                      y = games.screen.height/2,
                      dx = 2,
                      dy = 1)
    the_pizza3 = Pizza(image = pizza_image,
                      x = games.screen.width/2,
                      y = games.screen.height/4,
                      dx = 1,
                      dy = 2)
    games.screen.add(the_pizza)
    games.screen.add(the_pizza1)
    games.screen.add(the_pizza3)
    the_pan = Pan()
    games.screen.add(the_pan)

    games.screen.mainloop()

# kick it off!
main()

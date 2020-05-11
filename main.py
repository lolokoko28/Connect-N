import arcade
from Board import Board
from Player import Player

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700 \


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)
        self.board = Board(8,8, 3, Player(), Player())
        arcade.set_background_color(arcade.color.BLUE_BELL)

        self.image_paths = ["graphics/field.jpg", "graphics/elisabeth2-coingreen.jpg",
                            "graphics/elisabeth2-coin-pink.jpg"]
        field = arcade.Sprite("graphics/elisabeth2-coin-pink.jpg", 1)
        self.field_width = float(self.width / max(self.board.n_cols, self.board.n_rows))
        self.field_height = float(self.height / max(self.board.n_cols, self.board.n_rows))
        self.SPRITE_SCALING_COIN = self.field_width / field.width
        self.game_over = False

    def setup(self):

        self.field_list = arcade.SpriteList()
        for i in range(self.board.n_rows):
            for j in range(self.board.n_cols):
                field = arcade.Sprite(self.image_paths[0], self.SPRITE_SCALING_COIN)
                field.center_x = field.width / 2 + j * field.width
                field.center_y = field.height / 2 + i * field.height
                self.field_list.append(field)

        self.token_list = arcade.SpriteList()

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        self.field_list.draw()
        self.token_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        if not self.game_over:
            self.game_over = self.board.play()

            token = arcade.Sprite(self.image_paths[self.board.opposite_player(self.board.whos_turn_is_now)],
                                  self.SPRITE_SCALING_COIN)
            token.center_x = self.board.last_move[1]*self.field_width+ self.field_width/2
            token.center_y =self.board.last_move[0] *self.field_height + self.field_height/2
            self.token_list.append(token)



def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

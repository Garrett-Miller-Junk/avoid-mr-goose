@namespace
class SpriteKind:
    GOD = SpriteKind.create()
    Environment = SpriteKind.create()
def getLife():
    global heart
    heart = sprites.create(img("""
            . . f f . f f . . 
                    . f 2 2 f 2 2 f . 
                    f 2 1 2 2 2 2 2 f 
                    f 2 2 2 2 2 2 2 f 
                    f 2 2 2 2 2 2 2 f 
                    . f 2 2 2 2 2 f . 
                    . . f 2 2 2 f . . 
                    . . . f 2 f . . . 
                    . . . . f . . . .
        """),
        SpriteKind.food)
    heart.set_position(10 + 12 * len(list2), 10)
    list2.append(heart)
def makeDroppings():
    global gooseFeces
    gooseFeces = sprites.create(img("""
            . . f . . f . . . 
                    . . . . . . . . . 
                    f . . . . . . . f 
                    . f . . . f . . . 
                    . . . . . . . . . 
                    e e 7 e . e . . . 
                    . e e e . 7 e e . 
                    . . . . 7 7 e e . 
                    e e e . e . e . . 
                    . . e e . . . . .
        """),
        SpriteKind.enemy)
    gooseFeces.set_position(180 + randint(0, 80), 30 * randint(0, 2) + 30)
    gooseFeces.set_velocity(-80 * gameSpeed, 0)

def on_b_pressed():
    global jumping
    if jumping == 0:
        jumping = 1
        me.set_image(img("""
            .....fffff......
                        ....feeeeef.....
                        ...feeeeeeef....
                        ..feeeeeeeeef...
                        ..feedeeeeeef...
                        ..fedddddddeff..
                        .ffd111d111dfdf.
                        fdfd181d181dfdf.
                        fdfd111d111dff..
                        .ffdddddddddf...
                        ..fddd333dddf...
                        ...fdddddddfff..
                        ....ffffffff45f.
                        ..ffffd9dff6f5f.
                        ..f996ddd699f5f.
                        ..f996ddd699f5f.
                        ..fffccfccfff5ff
                        ....fddfddf4444f
                        ....f11f11ffffff
                        ....fffffff.....
        """))
        pause(500)
        me.set_image(img("""
            .....fffff......
                        ....feeeeef.....
                        ...feeeeeeef....
                        ..feeeeeeeeef...
                        ..feedeeeeeef...
                        ..fedddddddeff..
                        .ffdfffdfffdfdf.
                        fdfd181d181dfdf.
                        fdfdddddddddff..
                        .ffdddddddddf...
                        ..fddd333dddf...
                        ...fdddddddfff..
                        ..f.ffffffff45f.
                        .fdff49994f6f5f.
                        fddff59995f9f5f.
                        fdd6f59995f9f5f.
                        .ffff69996f9f5ff
                        ....f99999f9f44f
                        ....ffffffffffff
                        ....fccfccfdf...
                        ....fccfccff....
                        ....fccfccf.....
                        ....fffffff.....
                        ....fddfddf.....
                        ....f11f11f.....
                        .....ff.ff......
        """))
        jumping = 0
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def animateEnv_trees():
    global env_tree_randomizer
    env_tree_randomizer = randint(0, 3)
    if env_tree_randomizer == 0:
        env_tree_list.append(sprites.create(img("""
                    . . . . . . . c c . . . . . . . 
                                . . . . c c c 6 5 c 6 6 . . . . 
                                . . . . c 6 c 5 5 c 7 6 . . . . 
                                . . . 6 c c 7 5 5 7 c 6 6 . . . 
                                . . c c 7 7 7 7 7 5 7 7 c 6 . . 
                                . 6 6 6 c 6 7 7 7 7 6 c c 6 6 . 
                                c 7 7 7 6 c 7 c 6 7 6 7 7 7 7 6 
                                c c c 6 6 6 c 6 6 6 6 7 7 6 6 6 
                                . c c 7 6 6 6 6 6 7 7 7 7 c 6 . 
                                . c 7 7 6 6 7 6 6 7 7 6 7 7 c . 
                                . c c c c 7 7 6 f 7 7 c c c c . 
                                . . . . c 7 c f f c 7 c . . . . 
                                . . . . . 6 f e e e c . . . . . 
                                . . . . . e e e e e e . . . . . 
                                . . . . e e . e e . e e . . . . 
                                . . . . . . . e e . . . . . . .
                """),
                SpriteKind.Environment))
    elif env_tree_randomizer == 1:
        env_tree_list.append(sprites.create(img("""
                    . . . . . . . . 
                                . . . . . . . . 
                                . . . . . . . . 
                                . . c c c . . . 
                                . c c 6 6 c . . 
                                c c 3 3 f 6 c . 
                                c 6 c f 6 3 c . 
                                c 3 6 3 3 3 c . 
                                c 3 6 6 3 3 c . 
                                c 3 3 6 6 3 c . 
                                . c 3 3 3 6 . . 
                                . . 6 7 6 . . . 
                                . . 6 6 8 8 8 6 
                                . . 6 8 7 7 7 6 
                                . . 8 7 7 7 6 . 
                                . . 8 8 8 6 . .
                """),
                SpriteKind.Environment))
    elif env_tree_randomizer == 2:
        env_tree_list.append(sprites.create(img("""
                    . . . . . . . . 
                                . . . . . . . . 
                                . . . . . . . . 
                                . . . . . . . . 
                                . b b d d b b . 
                                b 1 1 3 3 1 1 b 
                                b 1 3 5 5 3 1 b 
                                b d 3 5 5 3 d b 
                                c 1 1 d d 1 1 c 
                                c d 1 d d 1 d c 
                                . c c 7 6 c c . 
                                . . 6 7 6 . . . 
                                . . 6 6 8 8 8 6 
                                . . 6 8 7 7 7 6 
                                . . 8 7 7 7 6 . 
                                . . 8 8 8 6 . .
                """),
                SpriteKind.Environment))
    else:
        env_tree_list.append(sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . c c c c 6 . . . . . 
                                . . . . c c 6 7 7 5 5 6 6 . . . 
                                . . c c 6 6 6 6 7 5 5 7 c c . . 
                                . c 6 6 6 7 7 7 7 7 7 5 6 c c . 
                                . c 6 6 7 7 7 5 7 6 7 7 7 6 c c 
                                c 6 6 7 7 6 7 7 7 6 7 7 6 6 6 c 
                                c c 6 6 6 7 6 7 6 6 6 6 5 7 6 c 
                                c c c c 6 7 7 6 7 7 7 6 7 6 6 c 
                                . c c 6 6 6 6 c 6 6 6 6 6 c c c 
                                . c c 6 6 c 6 6 c 6 c 6 6 c c . 
                                . . c c f f 6 6 c f f c c f . . 
                                . . . . c f c c c f c f f . . . 
                                . . . . . 4 f f f c . e . . . . 
                                . . . . . . e e e . . 4 . . . . 
                                . . . . . . . e e . e . . . . .
                """),
                SpriteKind.Environment))
    env_tree_list[len(env_tree_list) - 1].set_position(180 + randint(0, 40), 20)
    env_tree_list[len(env_tree_list) - 1].set_velocity(-80 * gameSpeed, 0)
    env_tree_list[len(env_tree_list) - 1].z = -1
def makeGoose():
    global goose
    goose = sprites.create(img("""
            ....ffff.................
                    ..ffeeeef................
                    .fcceefeef...............
                    fccceeeeeef..............
                    fccceeeeeeef.............
                    .ffffffeeeeef............
                    .......feeeeefff...ffffff
                    ......f1eeeeeeeffff1eee1f
                    .......f1eeeeeeeeeeeee1ef
                    ......f1eeeeffffeeeee1eef
                    ......feeeeffffffeee1eeef
                    ......feeeff5555ffeeeee1f
                    .....feeeeff5555ffeeee1ff
                    .....feeeeff5555ffeeee1f.
                    .....feee1fff55fffeeeef..
                    .....f1eee1ffffffeeeef...
                    .....f1eeee1ffffeeeef....
                    ......f11eee11eeeeeef....
                    .......fffeeeeeeeeccf....
                    ..........fccfffffccf....
                    ..........fccf...fccf....
                    ..........fccf...fccf....
                    ..........fccf...fccf....
                    .........ffccf..ffccf....
                    .........fcccf..fcccf....
                    .........fffff..fffff....
        """),
        SpriteKind.enemy)
    goose.set_position(160 + randint(0, 80), 30 * randint(0, 2) + 30)
    goose.set_velocity(-80 * gameSpeed, 0)

def on_left_pressed():
    global movement
    if jumping == 0:
        if movement > 0:
            movement += -1
            me.y += -30
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def makeCar():
    global car
    car = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . 2 2 2 2 2 2 2 2 . . 
                    . . . . . 2 c 2 2 2 2 2 2 4 2 . 
                    . . . . 2 c c 2 2 2 2 2 2 4 c 2 
                    . . d 2 4 c c 2 4 4 4 4 4 4 c c 
                    . d 2 2 4 c b e e e e e e e 2 c 
                    . 2 2 2 4 b e e b b b e b b e 2 
                    . 2 2 2 2 2 e b b b b e b b b e 
                    . 2 2 2 2 e 2 2 2 2 2 e 2 2 2 e 
                    . 2 d d 2 e f e e e f e e e e e 
                    . d d 2 e e e f e e f e e e e e 
                    . e e e e e e e f f f e e e e e 
                    . e e e e f f f e e e e f f f f 
                    . . . e f f f f f e e f f f f f 
                    . . . . f f f f . . . . f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    car.set_position(180 + randint(0, 80), 100)
    car.set_velocity(0, 0)
    car.ax = gameSpeed * -40
def loseLife():
    global gameRunning
    list2[len(list2) - 1].destroy()
    list2.pop()
    if 0 == len(list2):
        gameRunning = 0
        scene.set_background_color(15)
        game.set_dialog_text_color(2)
        game.show_long_text("WASTED", DialogLayout.BOTTOM)
        game.reset()

def on_right_pressed():
    global movement
    if jumping == 0:
        if movement < 2:
            movement += 1
            me.y += 30
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def makeBedi():
    global Bedi
    Bedi = sprites.create(img("""
            ..55...55..5..55....
                    ...55...5....55.....
                    55..55.fffff.5......
                    .55...fffffff....555
                    ..55.fffffffff..55..
                    5...fffffffffff.5...
                    555.fffefffffff...55
                    ....ffeeeeeeefff.55.
                    ...ffefffefffefe....
                    ..fefe1f1e1f1efe..55
                    55fefe1f1e1f1eff.55.
                    ...ffedddddddef.....
                    ..5.fddd333dddf...55
                    555..fdddddddff..55.
                    ....fffdddddff.....5
                    ....f1f11111f1f..555
                    5555f1f11111f1f.55..
                    ....f1f11111f1f.5...
                    ....f1f11111f1f.....
                    ..5.f1f11111f1f.5555
                    555.fffffffffff.....
                    ....fefccfccfef.555.
                    .55..ffccfccff..5.55
                    5.....fccfccf.......
                    ...55.fffffff..55555
                    ...5..feefeef......5
                    ..5...f11f11f.5555..
                    .55..5.ff.ff.....55.
                    .5..55..5...5.......
                    ....5...5...555.....
        """),
        SpriteKind.GOD)
    Bedi.set_position(2000 + randint(0, 1500), 30 * randint(0, 2) + 30)
    Bedi.set_velocity(-80 * gameSpeed, 0)
def animateEnv_Road():
    env_road_list.append(sprites.create(img("""
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
            """),
            SpriteKind.Environment))
    env_road_list[len(env_road_list) - 1].set_position(180, 119)
    env_road_list[len(env_road_list) - 1].set_velocity(-80 * gameSpeed, 0)
    env_road_list[len(env_road_list) - 1].z = -1

def on_on_overlap(sprite, otherSprite):
    getLife()
    Bedi.destroy()
    makeBedi()
sprites.on_overlap(SpriteKind.player, SpriteKind.GOD, on_on_overlap)

def animateEnv_Cloud():
    global env_cloud_randomizer
    env_cloud_randomizer = randint(0, 3)
    if env_cloud_randomizer == 0:
        env_cloud_list.append(sprites.create(img("""
                    . . . . . . . 1 1 . . . . . . . 
                                . . . . . . 1 1 1 1 . . . . . . 
                                . . . . . 1 1 1 1 1 . . . . . . 
                                . . . . 1 1 1 1 1 1 1 . . 1 1 . 
                                . . . 1 1 1 1 1 1 1 1 1 1 1 1 1 
                                . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                                1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                                . . 1 1 1 1 1 1 . . . . . . . .
                """),
                SpriteKind.Environment))
    elif env_cloud_randomizer == 1:
        env_cloud_list.append(sprites.create(img("""
                    . . . . . . . . 1 1 1 1 1 . . . 
                                . . . . . . . . 1 1 1 1 1 1 . . 
                                . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                                . . . . 1 1 1 1 1 1 1 1 1 1 . . 
                                . . 1 1 1 1 1 1 1 1 1 1 1 1 1 . 
                                . . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                                1 1 1 1 . 1 1 1 1 1 1 1 1 1 1 1 
                                . . . . . . . . . . . . . . . .
                """),
                SpriteKind.Environment))
    elif env_cloud_randomizer == 2:
        env_cloud_list.append(sprites.create(img("""
                    . . . . 1 . . . . . . . . . . . 
                                . . 1 1 1 . . . . . 1 1 1 1 1 . 
                                . 1 1 1 1 . . 1 1 1 1 1 1 1 1 1 
                                1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                                1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                                1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                                . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
                                1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 .
                """),
                SpriteKind.Environment))
    else:
        env_cloud_list.append(sprites.create(img("""
                    . . . . . . . . . . . . . . . . 
                                . 1 . . . 1 . 1 . . . 1 . . . 1 
                                . 1 . . . 1 . 1 . . . 1 . . . 1 
                                . 1 . . . 1 . 1 1 . 1 1 1 . 1 1 
                                . 1 . . . 1 . . 1 . 1 . 1 . 1 . 
                                . 1 1 . 1 1 . . 1 1 1 . 1 1 1 . 
                                . 1 1 1 1 1 . . . 1 . . . 1 . . 
                                . . . . . . . . . . . . . . . .
                """),
                SpriteKind.Environment))
    env_cloud_list[len(env_cloud_list) - 1].set_position(180 + randint(0, 40), randint(0, 15) + 5)
    env_cloud_list[len(env_cloud_list) - 1].set_velocity(-20 * gameSpeed, 0)
    env_cloud_list[len(env_cloud_list) - 1].z = -1

def on_on_overlap2(sprite, otherSprite):
    if jumping == 1 and me.overlaps_with(gooseFeces):
        gooseFeces.destroy()
        pause(500)
        makeDroppings()
    else:
        loseLife()
        goose.destroy()
        makeGoose()
        gooseFeces.destroy()
        makeDroppings()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

car_counter = 0
env_cloud_list: List[Sprite] = []
env_cloud_randomizer = 0
env_road_list: List[Sprite] = []
Bedi: Sprite = None
goose: Sprite = None
env_tree_list: List[Sprite] = []
env_tree_randomizer = 0
jumping = 0
heart: Sprite = None
list2: List[Sprite] = []
car: Sprite = None
gooseFeces: Sprite = None
gameRunning = 0
movement = 0
gameSpeed = 0
me: Sprite = None
game.set_dialog_text_color(15)
scene.set_background_color(15)
me = sprites.create(img("""
        .....fffff......
            ....feeeeef.....
            ...feeeeeeef....
            ..feeeeeeeeef...
            ..feedeeeeeef...
            ..fedddddddeff..
            .ffdfffdfffdfdf.
            fdfd181d181dfdf.
            fdfdddddddddff..
            .ffdddddddddf...
            ..fddd333dddf...
            ...fdddddddfff..
            ..f.ffffffff45f.
            .fdff49994f6f5f.
            fddff59995f9f5f.
            fdd6f59995f9f5f.
            .ffff69996f9f5ff
            ....f99999f9f44f
            ....ffffffffffff
            ....fccfccfdf...
            ....fccfccff....
            ....fccfccf.....
            ....fffffff.....
            ....fddfddf.....
            ....f11f11f.....
            .....ff.ff......
    """),
    SpriteKind.player)
me.y = 20
game.splash("You're late for class!", "Avoid the geese!")
gameSpeed = 1
me.set_position(20, 60)
movement = 1
gameRunning = 1
info.set_score(0)
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
"""))
makeGoose()
makeDroppings()
makeCar()
makeBedi()
animateEnv_Cloud()
animateEnv_Road()
animateEnv_trees()
gooseFeces.set_velocity(0, 0)
car.set_velocity(0, 0)
car.ax = 0
list2 = []
for index in range(2):
    getLife()

def on_forever():
    global gameSpeed, car_counter
    if gameRunning == 1:
        info.change_score_by(1)
        if info.score() > (gameSpeed - 0.9) * 3000:
            gameSpeed += 0.1
        if goose.x < 0:
            goose.destroy()
            makeGoose()
        if info.score() == 700 or gooseFeces.x < 0:
            gooseFeces.destroy()
            makeDroppings()
        if info.score() >= 1000 and Math.percent_chance(gameSpeed * 0.01) and car_counter <= 0:
            makeCar()
            car_counter = randint(100, 1000)
        if car_counter > 0:
            car_counter = car_counter - 1
        if car.x < -20:
            car.destroy()
        if info.score() == 1500 or Bedi.x < 0:
            Bedi.destroy()
            makeBedi()
        if env_cloud_list[len(env_cloud_list) - 1].x < randint(0, 100):
            animateEnv_Cloud()
        if env_cloud_list[0].x < -20:
            env_cloud_list[0].destroy()
            env_cloud_list.shift()
        if env_road_list[len(env_road_list) - 1].x < 100:
            animateEnv_Road()
        if env_road_list[0].x < -20:
            env_road_list[0].destroy()
            env_road_list.shift()
        if env_tree_list[len(env_tree_list) - 1].x < randint(0, 100):
            animateEnv_trees()
        if env_tree_list[0].x < -20:
            env_tree_list[0].destroy()
            env_tree_list.shift()
forever(on_forever)

@namespace
class SpriteKind:
    GOD = SpriteKind.create()
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
        if movement < 2:
            movement += 1
            me.y += 30
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

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
        if movement > 0:
            movement += -1
            me.y += -30
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

def on_on_overlap(sprite, otherSprite):
    getLife()
    Bedi.destroy()
    makeBedi()
sprites.on_overlap(SpriteKind.player, SpriteKind.GOD, on_on_overlap)

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

Bedi: Sprite = None
goose: Sprite = None
jumping = 0
heart: Sprite = None
list2: List[Sprite] = []
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
scene.set_background_color(7)
makeGoose()
makeDroppings()
makeBedi()
gooseFeces.set_velocity(0, 0)
list2 = []
for index in range(2):
    getLife()

def on_forever():
    global gameSpeed
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
        if info.score() == 1500 or Bedi.x < 0:
            Bedi.destroy()
            makeBedi()
forever(on_forever)

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
    gooseFeces.set_position(160 + randint(0, 80), 30 * randint(0, 2) + 30)
    gooseFeces.set_velocity(-80 * gameSpeed, 0)

def on_up_pressed():
    global movement
    if movement > 0:
        movement += -1
        me.y += -30
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

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
        me.y += 0
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
        me.y += 0
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

def on_down_pressed():
    global movement
    if movement < 2:
        movement += 1
        me.y += 30
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap(sprite, otherSprite):
    global gameRunning
    if jumping == 1 and me.overlaps_with(gooseFeces):
        pass
    else:
        gameRunning = 0
        scene.set_background_color(15)
        game.set_dialog_text_color(2)
        game.show_long_text("WASTED", DialogLayout.BOTTOM)
        game.reset()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

goose: Sprite = None
jumping = 0
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
gooseFeces.set_velocity(0, 0)

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
forever(on_forever)

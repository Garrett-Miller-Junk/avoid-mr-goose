namespace SpriteKind {
    export const GOD = SpriteKind.create()
}
function getLife () {
    heart = sprites.create(img`
        . . f f . f f . . 
        . f 2 2 f 2 2 f . 
        f 2 1 2 2 2 2 2 f 
        f 2 2 2 2 2 2 2 f 
        f 2 2 2 2 2 2 2 f 
        . f 2 2 2 2 2 f . 
        . . f 2 2 2 f . . 
        . . . f 2 f . . . 
        . . . . f . . . . 
        `, SpriteKind.Food)
    heart.setPosition(10 + 12 * list2.length, 10)
    list2.push(heart)
}
function makeDroppings () {
    gooseFeces = sprites.create(img`
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
        `, SpriteKind.Enemy)
    gooseFeces.setPosition(180 + randint(0, 80), 30 * randint(0, 2) + 30)
    gooseFeces.setVelocity(-80 * gameSpeed, 0)
}
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (jumping == 0) {
        jumping = 1
        me.setImage(img`
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
            `)
        pause(500)
        me.setImage(img`
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
            `)
        jumping = 0
    }
})
function makeGoose () {
    goose = sprites.create(img`
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
        `, SpriteKind.Enemy)
    goose.setPosition(160 + randint(0, 80), 30 * randint(0, 2) + 30)
    goose.setVelocity(-80 * gameSpeed, 0)
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (jumping == 0) {
        if (movement < 2) {
            movement += 1
            me.y += 30
        }
    }
})
function loseLife () {
    list2[list2.length - 1].destroy()
    list2.pop()
    if (0 == list2.length) {
        gameRunning = 0
        scene.setBackgroundColor(15)
        game.setDialogTextColor(2)
        game.showLongText("WASTED", DialogLayout.Bottom)
        game.reset()
    }
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (jumping == 0) {
        if (movement > 0) {
            movement += -1
            me.y += -30
        }
    }
})
function makeBedi () {
    Bedi = sprites.create(img`
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
        `, SpriteKind.GOD)
    Bedi.setPosition(2000 + randint(0, 1500), 30 * randint(0, 2) + 30)
    Bedi.setVelocity(-80 * gameSpeed, 0)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.GOD, function (sprite, otherSprite) {
    getLife()
    Bedi.destroy()
    makeBedi()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    if (jumping == 1 && me.overlapsWith(gooseFeces)) {
        gooseFeces.destroy()
        pause(500)
        makeDroppings()
    } else {
        loseLife()
        goose.destroy()
        makeGoose()
        gooseFeces.destroy()
        makeDroppings()
    }
})
let Bedi: Sprite = null
let goose: Sprite = null
let jumping = 0
let heart: Sprite = null
let list2: Sprite[] = []
let gooseFeces: Sprite = null
let gameRunning = 0
let movement = 0
let gameSpeed = 0
let me: Sprite = null
game.setDialogTextColor(15)
scene.setBackgroundColor(15)
me = sprites.create(img`
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
    `, SpriteKind.Player)
me.y = 20
game.splash("You're late for class!", "Avoid the geese!")
gameSpeed = 1
me.setPosition(20, 60)
movement = 1
gameRunning = 1
info.setScore(0)
scene.setBackgroundColor(7)
makeGoose()
makeDroppings()
makeBedi()
gooseFeces.setVelocity(0, 0)
list2 = []
for (let index = 0; index < 2; index++) {
    getLife()
}
forever(function () {
    if (gameRunning == 1) {
        info.changeScoreBy(1)
        if (info.score() > (gameSpeed - 0.9) * 3000) {
            gameSpeed += 0.1
        }
        if (goose.x < 0) {
            goose.destroy()
            makeGoose()
        }
        if (info.score() == 700 || gooseFeces.x < 0) {
            gooseFeces.destroy()
            makeDroppings()
        }
        if (info.score() == 1500 || Bedi.x < 0) {
            Bedi.destroy()
            makeBedi()
        }
    }
})

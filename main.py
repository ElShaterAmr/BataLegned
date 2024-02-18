@namespace
class SpriteKind:
    mity = SpriteKind.create()
    duck = SpriteKind.create()
    myenemy = SpriteKind.create()

def on_overlap_tile(sprite, location):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile2)

def on_up_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy += -200
        music.play(music.create_sound_effect(WaveShape.SQUARE,
                400,
                600,
                255,
                0,
                100,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile3(sprite4, location3):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player, sprites.builtin.coral5, on_overlap_tile3)

def on_overlap_tile4(sprite3, location4):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        red block
    """),
    on_overlap_tile4)

def on_b_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . b b b b . . . . . . 
                    . . . . b b 1 1 1 1 b b . . . . 
                    . . . . b 1 1 1 1 1 1 b . . . . 
                    . . . b 1 1 1 1 1 1 1 1 b . . . 
                    . . . b 1 1 1 1 1 1 1 1 b . . . 
                    . . b 1 1 1 1 1 1 1 1 1 1 b . . 
                    . . b 1 1 1 1 1 1 1 1 1 1 b . . 
                    . . b 1 1 1 1 1 1 1 1 1 1 b . . 
                    . . c 1 1 1 1 1 1 1 1 1 1 c . . 
                    . . c 1 1 1 1 1 1 1 1 1 1 c . . 
                    . . c b 1 1 1 1 1 1 1 1 b c . . 
                    . . . c 1 1 1 1 1 1 1 1 c . . . 
                    . . . . c b 1 1 1 1 1 c . . . . 
                    . . . . . c c c c c c . . . . .
        """),
        mySprite,
        -100,
        0)
    music.play(music.melody_playable(music.zapped),
        music.PlaybackMode.UNTIL_DONE)
    pause(1000)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_overlap_tile5(sprite32, location42):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_water,
    on_overlap_tile5)

def on_overlap_tile6(sprite22, location5):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile6)

def on_overlap_tile7(sprite5, location6):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile7)

def on_overlap_tile8(sprite52, location422):
    tiles.set_tile_at(location422, sprites.dungeon.collectible_red_crystal)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_red_crystal,
    on_overlap_tile8)

def on_a_pressed():
    global projectile2
    projectile2 = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . b b b b . . . . . . 
                    . . . . b b 1 1 1 1 b b . . . . 
                    . . . . b 1 1 1 1 1 1 b . . . . 
                    . . . b 1 1 1 1 1 1 1 1 b . . . 
                    . . . b 1 1 1 1 1 1 1 1 b . . . 
                    . . b 1 1 1 1 1 1 1 1 1 1 b . . 
                    . . b 1 1 1 1 1 1 1 1 1 1 b . . 
                    . . b 1 1 1 1 1 1 1 1 1 1 b . . 
                    . . c 1 1 1 1 1 1 1 1 1 1 c . . 
                    . . c 1 1 1 1 1 1 1 1 1 1 c . . 
                    . . c b 1 1 1 1 1 1 1 1 b c . . 
                    . . . c 1 1 1 1 1 1 1 1 c . . . 
                    . . . . c b 1 1 1 1 1 c . . . . 
                    . . . . . c c c c c c . . . . .
        """),
        mySprite,
        100,
        0)
    music.play(music.melody_playable(music.zapped),
        music.PlaybackMode.UNTIL_DONE)
    pause(1000)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile9(sprite6, location7):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile4
    """),
    on_overlap_tile9)

def on_overlap_tile10(sprite7, location8):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    sprites.castle.sapling_pine,
    on_overlap_tile10)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . b 5 5 b . . . . . . . . . 
                        . . . . b b b b b b . . . . . . 
                        . . . b 5 5 5 5 5 b b . . . . . 
                        . . b 5 5 5 5 5 5 5 b b b b b . 
                        . . b 5 5 5 5 5 5 5 5 b 5 d b . 
                        . . f 4 d 5 f 1 d 5 b 5 5 b . . 
                        . . c 4 4 5 f f 1 b 5 5 d b . . 
                        . b 4 4 4 4 b f d 5 5 5 b d b b 
                        b 4 4 4 4 4 4 5 b 5 5 d c d d b 
                        . b 5 5 5 5 5 5 5 b c c d d d c 
                        . b 5 5 5 5 5 5 5 d d d d d b c 
                        . b d 5 5 5 5 5 d d d d d d c . 
                        . . b b 5 5 5 d d d d d b c . . 
                        . . . b b c c c c c c c c . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . b 5 b . . . . . . . . . . 
                        . . . . b 5 b . . . . . . . . . 
                        . . . . b b b b b b . . . . . . 
                        . . . b 5 5 5 5 5 b b . . . . . 
                        . . b 5 5 5 5 5 5 5 b b b b b . 
                        . . b 5 5 5 5 5 5 5 5 b 5 d b . 
                        . . f 4 d 5 f 1 d 5 b 5 5 b . . 
                        . . c 4 4 5 f f 1 b 5 5 d b . . 
                        b 4 4 4 4 4 b f d 5 5 5 b d b b 
                        . b 4 4 4 4 4 5 b 5 5 d c d d b 
                        . b 5 5 5 5 5 5 5 b c c d d d c 
                        . b 5 5 5 5 5 5 5 d d d d d b c 
                        . b d 5 5 5 5 5 d d d d d d c . 
                        . . b b 5 5 5 d d d d d b c . . 
                        . . . b b c c c c c c c c . . .
            """),
            img("""
                . . . b 5 b . . . . . . . . . . 
                        . . . . b 5 b . . . . . . . . . 
                        . . . . . c b . . . . . . . . . 
                        . . . . b b b b b b . . . . . . 
                        . . . b 5 5 5 5 5 b b . . . . . 
                        . . f d 5 5 f 1 d 5 b b . . . . 
                        . . c 4 d 5 f f 1 5 5 b . . . . 
                        . . 4 4 d d b f d 5 5 b . . . . 
                        b 4 4 4 4 4 5 5 5 d b b d d d b 
                        . b 4 4 4 4 4 5 5 b 5 5 5 d b b 
                        . . b 5 5 5 5 5 d 5 5 5 5 c d b 
                        . b 5 5 5 5 5 5 b 5 5 d c d d c 
                        . b 5 5 5 5 5 5 5 b c c d d b c 
                        . b d 5 5 5 5 5 d d d d d d c . 
                        . . b b 5 5 5 d d d d d b c . . 
                        . . . b b c c c c c c c c . . .
            """),
            img("""
                . . . b 5 b . . . . . . . . . . 
                        . . . . b 5 b . . . . . . . . . 
                        . . . . b b b b b b . . . . . . 
                        . . . b 5 5 5 5 5 b b . . . . . 
                        . . c 4 d 5 f 1 d 5 b b . . . . 
                        b 4 4 4 d d f f 1 5 5 b . . . . 
                        . b 4 4 4 4 b f d 5 5 b . . . . 
                        . . b 4 4 4 4 5 5 5 5 d b . . . 
                        . . b 5 5 5 5 5 5 5 5 d d b . . 
                        . b 5 5 5 5 5 5 5 5 d d d d b . 
                        . b 5 5 5 5 5 5 5 b b b d d d b 
                        . b 5 5 5 5 5 5 c d 5 5 b d d c 
                        . b 5 5 5 5 5 5 d c d 5 d b b c 
                        . b d 5 5 5 5 5 d d c b 5 5 b . 
                        . . b b 5 5 5 d d d d c c c b b 
                        . . . b b c c c c c c c c . . .
            """),
            img("""
                . . . b 5 b . . . . . . . . . . 
                        . . . . b 5 b . . . . . . . . . 
                        . . . . b b b b b b . . . . . . 
                        . . . b 5 5 5 5 5 b b . . . . . 
                        . . c 4 d 5 f 1 d 5 b b . . . . 
                        b 4 4 4 d d f f 1 5 5 b . . . . 
                        . b 4 4 4 4 b f d 5 5 b . . . . 
                        . . b 4 4 4 4 5 5 5 5 d b . . . 
                        . . b 5 5 5 5 5 5 5 d d d b b . 
                        . b 5 5 5 5 5 5 5 b b b d d d b 
                        . b 5 5 5 5 5 5 c d 5 5 b d d c 
                        . b 5 5 5 5 5 5 d c d 5 d b b c 
                        . b 5 5 5 5 5 5 d d c b 5 5 b c 
                        . b d 5 5 5 5 5 d d d c c c b b 
                        . . b b 5 5 5 d d d c c . . . . 
                        . . . b b c c c c c . . . . . .
            """),
            img("""
                . . . b 5 b . . . . . . . . . . 
                        . . . . b 5 b . . . . . . . . . 
                        . . . . b b b b b b . . . . . . 
                        . . . b 5 5 5 5 5 b b . . . . . 
                        . . f d 5 5 f 1 d 5 b b . . . . 
                        . . c 4 d 5 f f 1 5 5 b . . . . 
                        . . 4 4 d d b f d 5 5 b . . . . 
                        b 4 4 4 4 4 5 5 5 5 5 d b b b . 
                        . b 4 4 4 4 4 5 5 d b b d d d b 
                        . . b 5 5 5 5 5 5 b 5 5 5 d b b 
                        . b 5 5 5 5 5 5 d 5 5 5 5 c d c 
                        . b 5 5 5 5 5 5 b 5 5 d c d b c 
                        . b d 5 5 5 5 5 d b c c d d c . 
                        . . b b 5 5 5 d d d d d b c . . 
                        . . . b b c c c c c c c c . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        100,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile11(sprite8, location9):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile11)

def on_overlap_tile12(sprite33, location43):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        ru
    """),
    on_overlap_tile12)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . b 5 5 b . . . 
                        . . . . . . b b b b b b . . . . 
                        . . . . . b b 5 5 5 5 5 b . . . 
                        . b b b b b 5 5 5 5 5 5 5 b . . 
                        . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                        . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                        . . b d 5 5 b 1 f f 5 4 4 c . . 
                        b b d b 5 5 5 d f b 4 4 4 4 b . 
                        b d d c d 5 5 b 5 4 4 4 4 4 4 b 
                        c d d d c c b 5 5 5 5 5 5 5 b . 
                        c b d d d d d 5 5 5 5 5 5 5 b . 
                        . c d d d d d d 5 5 5 5 5 d b . 
                        . . c b d d d d d 5 5 5 b b . . 
                        . . . c c c c c c c c b b . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . b 5 b . . . 
                        . . . . . . . . . b 5 b . . . . 
                        . . . . . . b b b b b b . . . . 
                        . . . . . b b 5 5 5 5 5 b . . . 
                        . b b b b b 5 5 5 5 5 5 5 b . . 
                        . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                        . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                        . . b d 5 5 b 1 f f 5 4 4 c . . 
                        b b d b 5 5 5 d f b 4 4 4 4 4 b 
                        b d d c d 5 5 b 5 4 4 4 4 4 b . 
                        c d d d c c b 5 5 5 5 5 5 5 b . 
                        c b d d d d d 5 5 5 5 5 5 5 b . 
                        . c d d d d d d 5 5 5 5 5 d b . 
                        . . c b d d d d d 5 5 5 b b . . 
                        . . . c c c c c c c c b b . . .
            """),
            img("""
                . . . . . . . . . . b 5 b . . . 
                        . . . . . . . . . b 5 b . . . . 
                        . . . . . . . . . b c . . . . . 
                        . . . . . . b b b b b b . . . . 
                        . . . . . b b 5 5 5 5 5 b . . . 
                        . . . . b b 5 d 1 f 5 5 d f . . 
                        . . . . b 5 5 1 f f 5 d 4 c . . 
                        . . . . b 5 5 d f b d d 4 4 . . 
                        b d d d b b d 5 5 5 4 4 4 4 4 b 
                        b b d 5 5 5 b 5 5 4 4 4 4 4 b . 
                        b d c 5 5 5 5 d 5 5 5 5 5 b . . 
                        c d d c d 5 5 b 5 5 5 5 5 5 b . 
                        c b d d c c b 5 5 5 5 5 5 5 b . 
                        . c d d d d d d 5 5 5 5 5 d b . 
                        . . c b d d d d d 5 5 5 b b . . 
                        . . . c c c c c c c c b b . . .
            """),
            img("""
                . . . . . . . . . . b 5 b . . . 
                        . . . . . . . . . b 5 b . . . . 
                        . . . . . . b b b b b b . . . . 
                        . . . . . b b 5 5 5 5 5 b . . . 
                        . . . . b b 5 d 1 f 5 d 4 c . . 
                        . . . . b 5 5 1 f f d d 4 4 4 b 
                        . . . . b 5 5 d f b 4 4 4 4 b . 
                        . . . b d 5 5 5 5 4 4 4 4 b . . 
                        . . b d d 5 5 5 5 5 5 5 5 b . . 
                        . b d d d d 5 5 5 5 5 5 5 5 b . 
                        b d d d b b b 5 5 5 5 5 5 5 b . 
                        c d d b 5 5 d c 5 5 5 5 5 5 b . 
                        c b b d 5 d c d 5 5 5 5 5 5 b . 
                        . b 5 5 b c d d 5 5 5 5 5 d b . 
                        b b c c c d d d d 5 5 5 b b . . 
                        . . . c c c c c c c c b b . . .
            """),
            img("""
                . . . . . . . . . . b 5 b . . . 
                        . . . . . . . . . b 5 b . . . . 
                        . . . . . . b b b b b b . . . . 
                        . . . . . b b 5 5 5 5 5 b . . . 
                        . . . . b b 5 d 1 f 5 d 4 c . . 
                        . . . . b 5 5 1 f f d d 4 4 4 b 
                        . . . . b 5 5 d f b 4 4 4 4 b . 
                        . . . b d 5 5 5 5 4 4 4 4 b . . 
                        . b b d d d 5 5 5 5 5 5 5 b . . 
                        b d d d b b b 5 5 5 5 5 5 5 b . 
                        c d d b 5 5 d c 5 5 5 5 5 5 b . 
                        c b b d 5 d c d 5 5 5 5 5 5 b . 
                        c b 5 5 b c d d 5 5 5 5 5 5 b . 
                        b b c c c d d d 5 5 5 5 5 d b . 
                        . . . . c c d d d 5 5 5 b b . . 
                        . . . . . . c c c c c b b . . .
            """),
            img("""
                . . . . . . . . . . b 5 b . . . 
                        . . . . . . . . . b 5 b . . . . 
                        . . . . . . b b b b b b . . . . 
                        . . . . . b b 5 5 5 5 5 b . . . 
                        . . . . b b 5 d 1 f 5 5 d f . . 
                        . . . . b 5 5 1 f f 5 d 4 c . . 
                        . . . . b 5 5 d f b d d 4 4 . . 
                        . b b b d 5 5 5 5 5 4 4 4 4 4 b 
                        b d d d b b d 5 5 4 4 4 4 4 b . 
                        b b d 5 5 5 b 5 5 5 5 5 5 b . . 
                        c d c 5 5 5 5 d 5 5 5 5 5 5 b . 
                        c b d c d 5 5 b 5 5 5 5 5 5 b . 
                        . c d d c c b d 5 5 5 5 5 d b . 
                        . . c b d d d d d 5 5 5 b b . . 
                        . . . c c c c c c c c b b . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        100,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile13(sprite322, location23):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava1,
    on_overlap_tile13)

def on_overlap_tile14(sprite9, location10):
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile14)

def on_on_overlap(sprite10, otherSprite):
    sprites.destroy(projectile2)
    sprites.destroy(otherSprite, effects.disintegrate, 200)
    info.change_score_by(1)
    sprites.destroy(projectile)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite11, otherSprite2):
    sprites.destroy(otherSprite2, effects.fire, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

projectile2: Sprite = None
projectile: Sprite = None
myEnemy: Sprite = None
mySprite: Sprite = None
scene.set_background_image(assets.image("""
    tt
"""))
mySprite = sprites.create(assets.image("""
    mysprite
"""), SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
mySprite.ay = 500
scene.camera_follow_sprite(mySprite)
sprites.destroy(myEnemy)
info.set_life(30)
tiles.set_current_tilemap(tilemap("""
    level1
"""))

def on_update_interval():
    global myEnemy
    myEnemy = sprites.create(assets.image("""
        bumbo
    """), SpriteKind.enemy)
    animation.run_image_animation(myEnemy,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . 2 1 2 . . . . . . 
                        . . . . . . . 2 1 2 . . . . . . 
                        . . . . . . . 2 1 2 . . . . . . 
                        . . . . . . . 3 1 3 . . . . . . 
                        . . . . . . 2 3 1 3 2 . . . . . 
                        . . . . . . 2 1 1 1 2 . . . . . 
                        . . . . . . 2 1 1 1 3 . . . . . 
                        . . . . . . 3 5 1 5 3 . . . . . 
                        . . . . . . 3 1 9 1 3 . . . . . 
                        . . . . . . 3 1 1 1 3 . . . . . 
                        . . . . . . 2 3 1 3 2 . . . . . 
                        . . . . . . . 2 2 2 . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 2 3 3 3 3 3 2 . . . . 
                        . . . . 3 1 1 1 1 1 1 1 3 . . . 
                        . . . . 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 2 1 1 1 1 1 1 1 1 1 2 . . 
                        . . . 2 3 1 1 1 1 1 1 3 3 2 . . 
                        . . . . . . 2 2 2 2 2 . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 4 4 4 4 4 . . . . . . 
                        . . . 4 4 4 5 5 5 d 4 4 4 4 . . 
                        . . 4 d 5 d 5 5 5 d d d 4 4 . . 
                        . . 4 5 5 1 1 1 d d 5 5 5 4 . . 
                        . 4 5 5 5 1 1 1 5 1 1 5 5 4 4 . 
                        . 4 d d 1 1 5 5 5 1 1 5 5 d 4 . 
                        . 4 5 5 1 1 5 1 1 5 5 d d d 4 . 
                        . 2 5 5 5 d 1 1 1 5 1 1 5 5 2 . 
                        . 2 d 5 5 d 1 1 1 5 1 1 5 5 2 . 
                        . . 2 4 d d 5 5 5 5 d d 5 4 . . 
                        . . . 2 2 4 d 5 5 d d 4 4 . . . 
                        . . 2 2 2 2 2 4 4 4 2 2 2 . . . 
                        . . . 2 2 4 4 4 4 4 4 2 2 . . . 
                        . . . . . 2 2 2 2 2 2 . . . . .
            """),
            img("""
                . . . . 2 2 2 2 2 2 2 2 . . . . 
                        . . . 2 4 4 4 5 5 4 4 4 2 2 2 . 
                        . 2 2 5 5 d 4 5 5 5 4 4 4 4 2 . 
                        . 2 4 5 5 5 5 d 5 5 5 4 5 4 2 2 
                        . 2 4 d d 5 5 5 5 5 5 d 4 4 4 2 
                        2 4 5 5 d 5 5 5 d d d 5 5 5 4 4 
                        2 4 5 5 4 4 4 d 5 5 d 5 5 5 4 4 
                        4 4 4 4 . . 2 4 5 5 . . 4 4 4 4 
                        . . b b b b 2 4 4 2 b b b b . . 
                        . b d d d d 2 4 4 2 d d d d b . 
                        b d d b b b 2 4 4 2 b b b d d b 
                        b d d b b b b b b b b b b d d b 
                        b b d 1 1 3 1 1 d 1 d 1 1 d b b 
                        . . b b d d 1 1 3 d d 1 b b . . 
                        . . 2 2 4 4 4 4 4 4 4 4 2 2 . . 
                        . . . 2 2 4 4 4 4 4 2 2 2 . . .
            """),
            img("""
                . . . . . . . . b b . . . . . . 
                        . . . . . . . . b b . . . . . . 
                        . . . b b b . . . . . . . . . . 
                        . . b d d b . . . . . . . b b . 
                        . b d d d b . . . . . . b d d b 
                        . b d d b . . . . b b . b d d b 
                        . b b b . . . . . b b . . b b . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . b b b d d d d d d b b b . . 
                        . b d c c c b b b b c c d d b . 
                        b d d c b . . . . . b c c d d b 
                        c d d b b . . . . . . b c d d c 
                        c b d d d b b . . . . b d d c c 
                        . c c b d d d d b . c c c c c c 
                        . . . c c c c c c . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        200,
        True)
    tiles.place_on_random_tile(myEnemy, sprites.dungeon.collectible_insignia)
    myEnemy.follow(mySprite, 50)
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global myEnemy
    myEnemy = sprites.create(assets.image("""
        bumbo
    """), SpriteKind.enemy)
    animation.run_image_animation(myEnemy,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . 2 1 2 . . . . . . 
                        . . . . . . . 2 1 2 . . . . . . 
                        . . . . . . . 2 1 2 . . . . . . 
                        . . . . . . . 3 1 3 . . . . . . 
                        . . . . . . 2 3 1 3 2 . . . . . 
                        . . . . . . 2 1 1 1 2 . . . . . 
                        . . . . . . 2 1 1 1 3 . . . . . 
                        . . . . . . 3 5 1 5 3 . . . . . 
                        . . . . . . 3 1 9 1 3 . . . . . 
                        . . . . . . 3 1 1 1 3 . . . . . 
                        . . . . . . 2 3 1 3 2 . . . . . 
                        . . . . . . . 2 2 2 . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 2 3 3 3 3 3 2 . . . . 
                        . . . . 3 1 1 1 1 1 1 1 3 . . . 
                        . . . . 1 1 1 1 1 1 1 1 1 . . . 
                        . . . 2 1 1 1 1 1 1 1 1 1 2 . . 
                        . . . 2 3 1 1 1 1 1 1 3 3 2 . . 
                        . . . . . . 2 2 2 2 2 . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 4 4 4 4 4 . . . . . . 
                        . . . 4 4 4 5 5 5 d 4 4 4 4 . . 
                        . . 4 d 5 d 5 5 5 d d d 4 4 . . 
                        . . 4 5 5 1 1 1 d d 5 5 5 4 . . 
                        . 4 5 5 5 1 1 1 5 1 1 5 5 4 4 . 
                        . 4 d d 1 1 5 5 5 1 1 5 5 d 4 . 
                        . 4 5 5 1 1 5 1 1 5 5 d d d 4 . 
                        . 2 5 5 5 d 1 1 1 5 1 1 5 5 2 . 
                        . 2 d 5 5 d 1 1 1 5 1 1 5 5 2 . 
                        . . 2 4 d d 5 5 5 5 d d 5 4 . . 
                        . . . 2 2 4 d 5 5 d d 4 4 . . . 
                        . . 2 2 2 2 2 4 4 4 2 2 2 . . . 
                        . . . 2 2 4 4 4 4 4 4 2 2 . . . 
                        . . . . . 2 2 2 2 2 2 . . . . .
            """),
            img("""
                . . . . 2 2 2 2 2 2 2 2 . . . . 
                        . . . 2 4 4 4 5 5 4 4 4 2 2 2 . 
                        . 2 2 5 5 d 4 5 5 5 4 4 4 4 2 . 
                        . 2 4 5 5 5 5 d 5 5 5 4 5 4 2 2 
                        . 2 4 d d 5 5 5 5 5 5 d 4 4 4 2 
                        2 4 5 5 d 5 5 5 d d d 5 5 5 4 4 
                        2 4 5 5 4 4 4 d 5 5 d 5 5 5 4 4 
                        4 4 4 4 . . 2 4 5 5 . . 4 4 4 4 
                        . . b b b b 2 4 4 2 b b b b . . 
                        . b d d d d 2 4 4 2 d d d d b . 
                        b d d b b b 2 4 4 2 b b b d d b 
                        b d d b b b b b b b b b b d d b 
                        b b d 1 1 3 1 1 d 1 d 1 1 d b b 
                        . . b b d d 1 1 3 d d 1 b b . . 
                        . . 2 2 4 4 4 4 4 4 4 4 2 2 . . 
                        . . . 2 2 4 4 4 4 4 2 2 2 . . .
            """),
            img("""
                . . . . . . . . b b . . . . . . 
                        . . . . . . . . b b . . . . . . 
                        . . . b b b . . . . . . . . . . 
                        . . b d d b . . . . . . . b b . 
                        . b d d d b . . . . . . b d d b 
                        . b d d b . . . . b b . b d d b 
                        . b b b . . . . . b b . . b b . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . b b b d d d d d d b b b . . 
                        . b d c c c b b b b c c d d b . 
                        b d d c b . . . . . b c c d d b 
                        c d d b b . . . . . . b c d d c 
                        c b d d d b b . . . . b d d c c 
                        . c c b d d d d b . c c c c c c 
                        . . . c c c c c c . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        200,
        True)
    tiles.place_on_random_tile(myEnemy, sprites.dungeon.collectible_insignia)
    myEnemy.follow(mySprite, 50)
game.on_update_interval(5000, on_update_interval2)

def on_update_interval3():
    global myEnemy
    myEnemy = sprites.create(assets.image("""
        ice knight
    """), SpriteKind.enemy)
    animation.run_image_animation(myEnemy, assets.animation("""
        ice
    """), 200, True)
    tiles.place_on_random_tile(myEnemy, sprites.dungeon.collectible_insignia)
    myEnemy.follow(mySprite, 50)
game.on_update_interval(5000, on_update_interval3)

def on_update_interval4():
    global myEnemy
    myEnemy = sprites.create(assets.image("""
        ice knight
    """), SpriteKind.enemy)
    animation.run_image_animation(myEnemy, assets.animation("""
        ice
    """), 200, True)
    tiles.place_on_random_tile(myEnemy, sprites.dungeon.collectible_insignia)
    myEnemy.follow(mySprite, 50)
game.on_update_interval(5000, on_update_interval4)

def on_forever():
    music.play(music.create_song(hex("""
            0078000408020208001c000e050046006603320000040a002d000000640014000132000201000224000c001000012018001c00012724002800012728002c00011d30003400012738003c00012009010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c800240008000900010a10001100010618001900010220002100010628002900010a380039000104
        """)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.create_song(hex("""
            0078000408020504001c00100500640000041e000004000000000000000000000000000a040004180008000c00012918001c00012728002c00012030003400012405001c000f0a006400f4010a0000040000000000000000000000000000000002120008000c00012418001c00012028002c00012706001c00010a006400f401640000040000000000000000000000000000000002060018001c00012708001c000e050046006603320000040a002d0000006400140001320002010002120010001400012420002400012234003800012409010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8000600200021000105
        """)),
        music.PlaybackMode.UNTIL_DONE)
forever(on_forever)

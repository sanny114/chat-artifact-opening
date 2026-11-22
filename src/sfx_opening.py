# 効果音。時刻は 絵コンテ.md と opening.html（HITS / FIX / TRY）と同じ。
#   python sfx_opening.py <出力.wav>
import sys
sys.path.insert(0, "scripts")  # sfx.py（効果音キット）を置いたフォルダ
from sfx import *

out = sys.argv[1] if len(sys.argv) > 1 else "audio.wav"
dry, wet = init(30.0)
FIX = [17, 18, 19, 20, 20.5, 21, 21.25, 21.5, 21.75]
TRY = [17.5, 18.5, 19.5, 20.25, 20.75, 21.125, 21.375, 21.625]

# 場面1：矢が刺さる → 的がほどける → 点になる
for i, t in enumerate([.5, 1.0, 1.5]):
    put(dry, t - .18, whoosh(.2, 1200, 400, .35, pan0=(-1) ** i * .8, pan1=0, shape='up'))
    put(dry, t, snap(.9)); put(dry, t, kick(.6))
put(dry, 1.82, whoosh(.2, 1200, 400, .35, shape='up'))
put(dry, 2.0, kick(1.2)); put(dry, 2.0, sub(.7, 1.2)); put(wet, 2.0, crash(.35, 1.6))
put(wet, 2.0, whoosh(1.0, 3000, 500, .5))
put(wet, 2.5, stab(CHORDS['F'], .6, .4))
put(dry, 4.0, riser(.75, 180, 900, .45))
put(dry, 4.75, kick(1.0)); put(wet, 4.75, pluck(1046.5, .6, .7)); put(wet, 4.75, stab(CHORDS['C'], .5, .4))

# 場面2：紙に3行
put(dry, 5.0, whoosh(.5, 500, 1600, .3, pan0=0, pan1=0))
for i, f in enumerate([392.0, 440.0, 523.3]):
    r0 = 5.5 + i
    put(dry, r0, snap(.6)); put(wet, r0, pluck(f, .5, .6))
    for k in range(6): put(dry, r0 + .1 + k * .07, key(.5), pan=-.2 + k * .06)
    put(dry, r0 + .45, whoosh(.5, 900, 1400, .12, pan0=-.2, pan1=.5))
for b in range(10, 18):
    t = b * .5
    if b % 2 == 0: put(dry, t, kick(.4))
    else: put(dry, t, hat(.2))
put(wet, 8.5, pluck(659.3, .5, .6))
put(dry, 9.0, whoosh(.55, 600, 2200, .35, pan0=-.3, pan1=.3))
put(dry, 9.25, blip(500, 1200, .35, .2))
put(dry, 9.75, whoosh(.25, 500, 1800, .4, pan0=0, pan1=-.4, shape='up'))
put(dry, 10.0, kick(1.1)); put(dry, 10.0, whoosh(.65, 900, 3200, .7, pan0=-.8, pan1=.9))

# 場面3：輪が組み上がる
put(dry, 10.72, snap(.6))
put(dry, 11.0, whoosh(.5, 700, 1800, .3, pan0=-.6, pan1=.5))
put(wet, 11.5, pluck(261.6, .55, .5)); put(wet, 12.0, pluck(329.6, .55, .5))
put(dry, 12.0, whoosh(.5, 400, 1200, .2, pan0=.3, pan1=.3))
for k, f in enumerate([392.0, 440.0, 493.9, 523.3, 587.3, 659.3]):
    put(wet, 12.5 + k / 12, pluck(f, .45, .35)); put(dry, 12.5 + k / 12, tick(2000 + k * 200, .3))
put(wet, 13.0, pluck(784.0, .6, .6)); put(dry, 13.0, snap(.7))
put(dry, 13.25, kick(1.0)); put(dry, 13.25, clap(.6)); put(wet, 13.25, stab(CHORDS['C'], .6, .5))
put(wet, 13.5, pad(CHORDS['C'], 1.4, .3))

# 場面4：回る → 一言ごとに変わる
t = 15.0; gap = .035
while t < 16.5:
    put(dry, t, tick(1800, .35, .02), pan=.4); gap *= 1.13; t += gap
put(dry, 15.0, whoosh(.6, 600, 1500, .3, pan0=.2, pan1=.6))
put(dry, 16.5, kick(.9)); put(dry, 16.5, clap(.7)); put(wet, 16.5, stab(CHORDS['G'], .5, .45))
for ta, land in [(16.5, 17), (17.5, 18), (18.5, 19), (19.5, 20)]:
    k = ta + .08
    while k < land - .1:
        put(dry, k, key(.45), pan=-.5); k += .06
prog_ch = ['F', 'G', 'Am', 'F', 'G', 'C', 'F', 'G', 'G']
roots = {'F': 87.3, 'G': 98.0, 'Am': 110.0, 'C': 130.8}
for t, ch in zip(FIX, prog_ch):
    put(dry, t, kick(1.0)); put(dry, t, snap(.6)); put(wet, t, stab(CHORDS[ch], .4, .45)); put(dry, t, bass(roots[ch], .22, .5))
for i, t in enumerate(TRY):
    put(dry, t, whoosh(.3 if i < 3 else .18, 700, 1800, .28, pan0=.2, pan1=.7)); put(dry, t, kick(.55))
t = 17.0
while t < 22.0:
    put(dry, t, hat(.22 if t < 20 else .28)); t += .25 if t < 20 else .125
put(dry, 21.75, riser(.25, 400, 1200, .3))

# 場面5：引く → 線が見える
put(dry, 22.0, kick(1.1)); put(wet, 22.0, crash(.3, 1.8)); put(wet, 22.0, whoosh(.9, 2600, 400, .45, pan0=.6, pan1=-.3))
put(wet, 22.0, pad(CHORDS['F'], 2.0, .32)); put(wet, 24.0, pad(CHORDS['C'], 1.9, .34))
def inv(f):  # inOutCubic の逆
    return (f / 4) ** (1 / 3) if f < .5 else 1 - ((1 - f) * 2) ** (1 / 3) / 2
for i, f in enumerate([523.3, 587.3, 659.3, 784.0, 880.0, 1046.5]):
    put(wet, 22.4 + 1.6 * inv((i + 1) / 7), pluck(f, .45, .5), pan=-.6 + i * .22)
put(dry, 24.0, kick(.7)); put(wet, 24.0, stab(CHORDS['C'], .6, .35))
put(dry, 25.0, kick(.4))
put(dry, 25.75, whoosh(.6, 500, 2000, .35, pan0=-.6, pan1=.6))
put(dry, 26.25, riser(.25, 300, 1100, .4))
put(dry, 26.5, kick(1.2)); put(dry, 26.5, clap(.6)); put(wet, 26.5, crash(.3, 1.6)); put(wet, 26.5, stab(CHORDS['C'], .7, .5))

# タイトル
put(wet, 27.0, pad(CHORDS['C'], 2.9, .36)); put(wet, 27.0, pluck(523.3, .5, .7))
put(wet, 27.45, pluck(659.3, .45, .7)); put(wet, 27.6, pluck(784.0, .45, .7))
put(wet, 27.95, pluck(1046.5, .5, .9))
write(out)

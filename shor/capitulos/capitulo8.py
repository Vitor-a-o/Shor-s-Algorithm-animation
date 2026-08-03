# -*- coding: utf-8 -*-
from manim import *
import numpy as np

from ..paleta import *
from ..ferramentas import *

CARTAO_ESCURO = "#123a46"   # caixa da mensagem (azul-petróleo dos slides)


def _caixa_msg(txt, cor_fundo, cor_txt, tam=30):
    f = T(txt, tam, cor_txt) if isinstance(txt, str) else txt
    r = RoundedRectangle(corner_radius=0.16, width=max(f.width + 0.7, 1.15),
                         height=0.9, stroke_width=0)
    r.set_fill(cor_fundo, opacity=1)
    f.move_to(r)
    return VGroup(r, f)


# ============================================================================
# CAPÍTULO 8 — RSA sem relógios (slides 83–105): fórmulas que se transformam
# ============================================================================
def parte8(cena):
    # ---------- FASE A: dedução dos slides 85–88, fórmula virando fórmula ---
    L = VGroup(pot("a", expoente(("φ(", PRETO), ("n", LARANJA), (")", PRETO),
                                 tam=34), ROXO, tam=34),
               T("≡", 34, PRETO), T("1", 34, VERDE), fmod("n", 32))
    L.arrange(RIGHT, buff=0.16).move_to([0, 1.6, 0])
    cena.play(Write(L), run_time=1.1 * VEL)
    cena.wait(1.0 * VEL)

    # slide 86: multiplicamos os dois lados por a
    L2 = VGroup(T("a", 34, ROXO), T("·", 34, PRETO),
                pot("a", expoente(("φ(", PRETO), ("n", LARANJA),
                                  (")", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), T("·", 34, PRETO),
                T("1", 34, VERDE), fmod("n", 32))
    L2.arrange(RIGHT, buff=0.16).move_to(L)
    cena.play(ReplacementTransform(L, L2), run_time=1.1 * VEL)
    cena.wait(1.0 * VEL)

    # slide 87: os expoentes se somam
    L3 = VGroup(pot("a", expoente(("φ(", PRETO), ("n", LARANJA),
                                  (") + 1", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("n", 32))
    L3.arrange(RIGHT, buff=0.16).move_to(L2)
    cena.play(ReplacementTransform(L2, L3), run_time=1.1 * VEL)
    cena.wait(1.0 * VEL)

    # slide 88: NO EXPOENTE a aritmética é módulo φ(n)
    L4 = VGroup(pot("a", expoente(("1 (mod φ(", PRETO), ("n", LARANJA),
                                  ("))", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("n", 32))
    L4.arrange(RIGHT, buff=0.16).move_to(L3)
    cena.play(ReplacementTransform(L3, L4), run_time=1.1 * VEL)
    cena.wait(1.0 * VEL)

    # ---------- slide 89: a TABELA multiplicativa e os pares de inversos ----
    tam = 0.38
    canto = np.array([-6.2, 1.0, 0.0])

    def ponto(i, j):
        return canto + np.array([(j + 1) * tam, -(i + 1) * tam, 0.0])

    head_c = VGroup(*[T(str(j), 17, AZUL).move_to(canto + [(j + 1) * tam, 0, 0])
                      for j in range(9)])
    head_l = VGroup(*[T(str(i), 17, VERMELHO)
                      .move_to(canto + [0, -(i + 1) * tam, 0])
                      for i in range(9)])
    lin_h = Line(canto + [0.55 * tam, -0.5 * tam, 0],
                 canto + [9.5 * tam, -0.5 * tam, 0], color=PRETO,
                 stroke_width=1.2)
    lin_v = Line(canto + [0.55 * tam, -0.5 * tam, 0],
                 canto + [0.55 * tam, -9.5 * tam, 0], color=PRETO,
                 stroke_width=1.2)
    celulas = [VGroup(*[T(str((i * j) % 9), 17, PRETO).move_to(ponto(i, j))
                        for j in range(9)]) for i in range(9)]
    tabela = VGroup(head_c, head_l, lin_h, lin_v, *celulas)
    cena.play(FadeIn(tabela), run_time=1.0 * VEL)
    uns = VGroup(*[Circle(radius=0.16, color=VERDE, stroke_width=2)
                   .move_to(ponto(i, j))
                   for i in range(1, 9) for j in range(1, 9)
                   if (i * j) % 9 == 1])
    ed = formula(("e", VERMELHO), ("·", PRETO), ("d", AZUL), ("≡", PRETO),
                 ("1", VERDE), ("(mod φ(", PRETO), ("n", LARANJA),
                 ("))", PRETO), tamanho=30, buff=0.10).move_to([3.0, -0.4, 0])
    nota = formula(("(e, d)", PRETO), ("= par de inversos", CINZA),
                   tamanho=22, buff=0.12).next_to(ed, DOWN, buff=0.3)
    cena.play(LaggedStart(*[Create(c) for c in uns], lag_ratio=0.1),
              Write(ed), run_time=1.5 * VEL)
    cena.play(FadeIn(nota), Indicate(celulas[2][5], color=VERDE),
              Indicate(celulas[5][2], color=VERDE), run_time=1.2 * VEL)
    cena.wait(1.0 * VEL)

    # slide 90: substituímos e·d no expoente
    L5 = VGroup(pot("a", expoente(("e", VERMELHO), ("·", PRETO),
                                  ("d", AZUL), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("n", 32))
    L5.arrange(RIGHT, buff=0.16).move_to(L4)
    cena.play(ReplacementTransform(L4, L5), Indicate(ed, color=VERDE),
              run_time=1.2 * VEL)

    # slide 91: rearranjando — (aᵉ)ᵈ com o expoente NO LUGAR CERTO
    par_ae = VGroup(T("(", 36, PRETO), pot("a", "e", ROXO, VERMELHO, 36),
                    T(")", 36, PRETO)).arrange(RIGHT, buff=0.04)
    L6 = VGroup(pot(par_ae, "d", None, AZUL, 36),
                T("≡", 36, PRETO), T("a", 36, ROXO), fmod("n", 34))
    L6.arrange(RIGHT, buff=0.16).move_to(L5)
    cena.play(ReplacementTransform(L5, L6), run_time=1.1 * VEL)
    cena.wait(1.0 * VEL)
    # a tabela cumpriu o papel; o e·d ≡ 1 sai de cena com ela
    cena.play(FadeOut(tabela), FadeOut(uns), FadeOut(nota), FadeOut(ed),
              run_time=0.9 * VEL)

    # ---------- FASE A2: quem é quem — o a da fórmula é a MENSAGEM; --------
    # (e, n) vira a chave PÚBLICA e (d, n) vira a chave PRIVADA
    msgA = _caixa_msg("a", CARTAO_ESCURO, ROXO, 32).move_to([-4.9, -0.4, 0])
    rotA = T("mensagem", 20, CINZA).next_to(msgA, DOWN, buff=0.18)
    fA = formula(("a", ROXO), ("≡", PRETO), ("a", ROXO), *MOD("n"),
                 tamanho=20, buff=0.08).next_to(rotA, DOWN, buff=0.15)
    cena.play(Indicate(L6[2], color=ROXO), run_time=0.7 * VEL)
    cena.play(FadeIn(msgA, shift=0.2 * UP), FadeIn(rotA), Write(fA),
              run_time=1.1 * VEL)

    # elevar a e e tirar (mod n): surge a CIFRA
    cifA = _caixa_msg(pot("a", "e", BRANCO, BRANCO, 30), VERDE, BRANCO)
    cifA.move_to([0, -0.4, 0])
    rotC = T("cifra", 20, CINZA).next_to(cifA, DOWN, buff=0.18)
    s1 = Arrow(msgA.get_right() + 0.1 * RIGHT, cifA.get_left() + 0.1 * LEFT,
               buff=0, color=PRETO, stroke_width=4,
               max_tip_length_to_length_ratio=0.14)
    f1s = VGroup(pot("a", "e", ROXO, VERMELHO, 24), fmod("n", 22))
    f1s.arrange(RIGHT, buff=0.12).next_to(s1, UP, buff=0.15)
    cena.play(GrowArrow(s1), Write(f1s), run_time=1.0 * VEL)
    cena.play(FadeIn(cifA, shift=0.2 * UP), FadeIn(rotC), run_time=1.0 * VEL)

    # o e e o n se TRANSFORMAM na chave pública
    fpub = formula(("pública", CINZA), ("(", PRETO), ("e", VERMELHO),
                   (", ", PRETO), ("n", LARANJA), (")", PRETO),
                   tamanho=22, buff=0.10)
    rpub = RoundedRectangle(corner_radius=0.14, width=fpub.width + 0.7,
                            height=0.72, stroke_color=CINZA, stroke_width=2.5)
    rpub.next_to(s1, DOWN, buff=0.2)
    fpub.move_to(rpub)
    pubS = VGroup(rpub, fpub)
    cena.play(Create(rpub), FadeIn(fpub[0]), FadeIn(fpub[1]),
              FadeIn(fpub[3]), FadeIn(fpub[5]),
              ReplacementTransform(f1s[0][1].copy(), fpub[2]),
              ReplacementTransform(f1s[1][1].copy(), fpub[4]),
              run_time=1.2 * VEL)
    cena.wait(0.6 * VEL)

    # elevar a d e tirar (mod n): a cifra é DECIFRADA
    msgB = _caixa_msg("a", CARTAO_ESCURO, ROXO, 32).move_to([4.9, -0.4, 0])
    rotB = T("mensagem", 20, CINZA).next_to(msgB, DOWN, buff=0.18)
    s2 = Arrow(cifA.get_right() + 0.1 * RIGHT, msgB.get_left() + 0.1 * LEFT,
               buff=0, color=PRETO, stroke_width=4,
               max_tip_length_to_length_ratio=0.14)
    par_s = VGroup(T("(", 24, PRETO), pot("a", "e", ROXO, VERMELHO, 24),
                   T(")", 24, PRETO)).arrange(RIGHT, buff=0.03)
    f2s = VGroup(pot(par_s, "d", None, AZUL, 24), T("≡", 24, PRETO),
                 T("a", 24, ROXO), fmod("n", 22))
    f2s.arrange(RIGHT, buff=0.12).next_to(s2, UP, buff=0.15)
    cena.play(GrowArrow(s2), Write(f2s), run_time=1.0 * VEL)
    cena.play(FadeIn(msgB, shift=0.2 * UP), FadeIn(rotB), run_time=1.0 * VEL)

    # o d e o n se TRANSFORMAM na chave privada
    fpriv = formula(("privada", AMARELO), ("(", PRETO), ("d", AZUL),
                    (", ", PRETO), ("n", LARANJA), (")", PRETO),
                    tamanho=22, buff=0.10)
    rpriv = RoundedRectangle(corner_radius=0.14, width=fpriv.width + 0.7,
                             height=0.72, stroke_color=AMARELO,
                             stroke_width=2.5)
    rpriv.next_to(s2, DOWN, buff=0.2)
    fpriv.move_to(rpriv)
    privS = VGroup(rpriv, fpriv)
    cena.play(Create(rpriv), FadeIn(fpriv[0]), FadeIn(fpriv[1]),
              FadeIn(fpriv[3]), FadeIn(fpriv[5]),
              ReplacementTransform(f2s[0][1].copy(), fpriv[2]),
              ReplacementTransform(f2s[3][1].copy(), fpriv[4]),
              run_time=1.2 * VEL)
    cena.wait(1.2 * VEL)

    # o esquema simbólico E a fórmula geral (aᵉ)ᵈ saem de cena:
    # o exemplo será reconstruído a partir de a^(1 (mod φ(n)))
    cena.play(FadeOut(VGroup(msgA, rotA, fA, s1, f1s, cifA, rotC, pubS,
                             msgB, rotB, s2, f2s, privS, L6)),
              run_time=0.8 * VEL)

    # ---------- FASE B: o exemplo dos slides 95–96 (n = 33, a = 5) ----------
    def cartao(tokens, cor, x):
        f = formula(*tokens, tamanho=22, buff=0.10)
        r = RoundedRectangle(corner_radius=0.14, width=f.width + 0.7,
                             height=0.72, stroke_color=cor, stroke_width=2.5)
        r.move_to([x, 2.55, 0])
        f.move_to(r)
        return VGroup(r, f)

    # 1) o criador escolhe o módulo: n = 33 (sem revelar de onde veio)
    esc = formula(("n", LARANJA), ("=", PRETO), ("33", LARANJA),
                  tamanho=30).move_to([0, 2.55, 0])
    cena.play(Write(esc), run_time=0.8 * VEL)

    # 2) partimos de a^(1 (mod φ(n))) ≡ a, com n = 33 — no lugar de honra
    E1 = VGroup(pot("a", expoente(("1 (mod φ(", PRETO), ("33", LARANJA),
                                  ("))", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("33", 32))
    E1.arrange(RIGHT, buff=0.14).move_to([0, 1.6, 0])
    cena.play(Write(E1), run_time=1.0 * VEL)

    # 3) por enquanto, SÓ o valor: φ(33) = 20
    phi = formula(("φ(", PRETO), ("33", LARANJA), (")", PRETO), ("=", PRETO),
                  ("20", PRETO), tamanho=30, buff=0.08).move_to([0, 0.85, 0])
    cena.play(Write(phi), run_time=0.9 * VEL)
    E2 = VGroup(pot("a", expoente(("1 (mod ", PRETO), ("20", PRETO),
                                  (")", PRETO), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("33", 32))
    E2.arrange(RIGHT, buff=0.14).move_to(E1)
    cena.play(ReplacementTransform(E1, E2), Indicate(phi, color=LARANJA),
              run_time=1.0 * VEL)

    # 4) encontrar e e d inversos (mod 20): 3 × 7 = 21 ≡ 1 ✓  (slide 95)
    ed2 = formula(("e", VERMELHO), ("·", PRETO), ("d", AZUL), ("≡", PRETO),
                  ("1", VERDE), *MOD("20"), tamanho=28,
                  buff=0.10).move_to([0, 0.1, 0])
    cena.play(Write(ed2), run_time=0.9 * VEL)
    edn = formula(("3", VERMELHO), ("×", PRETO), ("7", AZUL), ("=", PRETO),
                  ("21", PRETO), ("≡", PRETO), ("1", VERDE),
                  *MOD("20"), ("✓", VERDE), tamanho=28).move_to(ed2)
    cena.play(ReplacementTransform(ed2, edn), run_time=1.0 * VEL)

    # as chaves NASCEM dos números encontrados: (3, 33) e (7, 33)
    pub = cartao((("pública", CINZA), ("(", PRETO), ("3", VERMELHO),
                  (", ", PRETO), ("33", LARANJA), (")", PRETO)),
                 CINZA, -3.5)
    priv = cartao((("privada", AMARELO), ("(", PRETO), ("7", AZUL),
                   (", ", PRETO), ("33", LARANJA), (")", PRETO)),
                  AMARELO, 3.5)
    cena.play(Create(pub[0]), Create(priv[0]),
              FadeIn(pub[1][0]), FadeIn(pub[1][1]), FadeIn(pub[1][3]),
              FadeIn(pub[1][5]),
              FadeIn(priv[1][0]), FadeIn(priv[1][1]), FadeIn(priv[1][3]),
              FadeIn(priv[1][5]),
              ReplacementTransform(edn[0].copy(), pub[1][2]),
              ReplacementTransform(esc[2].copy(), pub[1][4]),
              ReplacementTransform(edn[2].copy(), priv[1][2]),
              ReplacementTransform(esc[2].copy(), priv[1][4]),
              run_time=1.4 * VEL)

    # 5) a PRÓPRIA equação evolui: o 1 (mod 20) vira 3·7, que vira (a³)⁷
    E3 = VGroup(pot("a", expoente(("3", VERMELHO), ("·", PRETO),
                                  ("7", AZUL), tam=34), ROXO, tam=34),
                T("≡", 34, PRETO), T("a", 34, ROXO), fmod("33", 32))
    E3.arrange(RIGHT, buff=0.14).move_to(E2)
    cena.play(ReplacementTransform(E2, E3), Indicate(edn, color=VERDE),
              run_time=1.1 * VEL)
    cena.wait(0.6 * VEL)
    par_a3 = VGroup(T("(", 36, PRETO), pot("a", "3", ROXO, VERMELHO, 36),
                    T(")", 36, PRETO)).arrange(RIGHT, buff=0.04)
    E4 = VGroup(pot(par_a3, "7", None, AZUL, 36),
                T("≡", 36, PRETO), T("a", 36, ROXO), fmod("33", 34))
    E4.arrange(RIGHT, buff=0.16).move_to(E3)
    cena.play(ReplacementTransform(E3, E4), run_time=1.1 * VEL)
    cena.wait(0.6 * VEL)

    # …e a mensagem escolhida: a = 5
    cena.play(FadeOut(phi), FadeOut(edn), run_time=0.7 * VEL)
    msg_esc = formula(("mensagem:", CINZA), ("a", ROXO), ("=", PRETO),
                      ("5", ROXO), tamanho=26).move_to([0, 0.85, 0])
    cena.play(Write(msg_esc), run_time=0.8 * VEL)
    par_53 = VGroup(T("(", 36, PRETO), pot("5", "3", ROXO, VERMELHO, 36),
                    T(")", 36, PRETO)).arrange(RIGHT, buff=0.04)
    L7 = VGroup(pot(par_53, "7", None, AZUL, 36),
                T("≡", 36, PRETO), T("5", 36, ROXO), fmod("33", 34))
    L7.arrange(RIGHT, buff=0.16).move_to(E4)
    cena.play(ReplacementTransform(E4, L7), Indicate(msg_esc, color=ROXO),
              run_time=1.1 * VEL)
    cena.wait(1.0 * VEL)

    # ---------- o PARALELO dos slides 93–96: mensagem → cifra → mensagem ----
    msg1 = _caixa_msg("5", CARTAO_ESCURO, ROXO).move_to([-4.6, -1.45, 0])
    cifra = _caixa_msg("26", VERDE, BRANCO).move_to([0, -1.45, 0])
    msg2 = _caixa_msg("5", CARTAO_ESCURO, ROXO).move_to([4.6, -1.45, 0])
    cena.play(FadeIn(msg1, shift=0.2 * UP), run_time=0.7 * VEL)

    # criptografar: qualquer um com a chave PÚBLICA (3, 33)
    s1 = Arrow(msg1.get_right() + 0.1 * RIGHT, cifra.get_left() + 0.1 * LEFT,
               buff=0, color=PRETO, stroke_width=4,
               max_tip_length_to_length_ratio=0.14)
    f1 = VGroup(pot("5", "3", ROXO, VERMELHO, 22), T("≡", 22, PRETO),
                T("26", 22, VERDE), fmod("33", 20))
    f1.arrange(RIGHT, buff=0.08).next_to(s1, UP, buff=0.15)
    pub_mini = pub.copy()
    cena.play(GrowArrow(s1), pub_mini.animate.scale(0.8)
              .next_to(s1, DOWN, buff=0.18), run_time=1.0 * VEL)
    cena.play(Write(f1), FadeIn(cifra, shift=0.2 * UP), run_time=1.1 * VEL)

    # descriptografar: SÓ quem tem a chave PRIVADA (7, 33)
    s2 = Arrow(cifra.get_right() + 0.1 * RIGHT, msg2.get_left() + 0.1 * LEFT,
               buff=0, color=PRETO, stroke_width=4,
               max_tip_length_to_length_ratio=0.14)
    f2 = VGroup(pot("26", "7", VERDE, AZUL, 22), T("≡", 22, PRETO),
                T("5", 22, ROXO), fmod("33", 20))
    f2.arrange(RIGHT, buff=0.08).next_to(s2, UP, buff=0.15)
    priv_mini = priv.copy()
    cena.play(GrowArrow(s2), priv_mini.animate.scale(0.8)
              .next_to(s2, DOWN, buff=0.18), run_time=1.0 * VEL)
    cena.play(Write(f2), FadeIn(msg2, shift=0.2 * UP), run_time=1.1 * VEL)
    cena.wait(0.8 * VEL)

    # cadeia final de verificação (slide 96) — SÓ fórmulas, sem retas
    par_f = VGroup(T("(", 28, PRETO), pot("5", "3", ROXO, VERMELHO, 28),
                   T(")", 28, PRETO)).arrange(RIGHT, buff=0.04)
    fim2 = VGroup(pot(par_f, "7", None, AZUL, 28), T("=", 28, PRETO),
                  pot("5", "21", ROXO, PRETO, 28), T("=", 28, PRETO),
                  pot("5", "20", ROXO, PRETO, 28), T("·", 28, PRETO),
                  T("5", 28, ROXO), T("≡", 28, PRETO), T("1", 28, VERDE),
                  T("·", 28, PRETO), T("5", 28, ROXO), T("≡", 28, PRETO),
                  T("5", 28, ROXO), fmod("33", 26))
    fim2.arrange(RIGHT, buff=0.14).move_to([0, -3.0, 0])
    cena.play(Write(fim2), run_time=1.3 * VEL)
    par_f2 = VGroup(T("(", 32, PRETO), pot("5", "3", ROXO, VERMELHO, 32),
                    T(")", 32, PRETO)).arrange(RIGHT, buff=0.04)
    fim3 = VGroup(pot(par_f2, "7", None, AZUL, 32), T("≡", 32, PRETO),
                  T("5", 32, ROXO), fmod("33", 30), T("✓", 32, VERDE))
    fim3.arrange(RIGHT, buff=0.16).move_to(fim2)
    cena.play(ReplacementTransform(fim2, fim3), run_time=1.1 * VEL)
    cena.wait(1.0 * VEL)

    # ---------- FASE C: a segurança (slides 97–104) ----------
    cena.play(FadeOut(VGroup(msg1, cifra, msg2, s1, s2, f1, f2,
                             pub_mini, priv_mini, fim3, msg_esc, esc)),
              run_time=0.8 * VEL)
    c1 = formula(("achar", PRETO), ("d", AZUL), ("⇒", PRETO),
                 ("achar", PRETO), ("φ(", PRETO), ("n", LARANJA),
                 (")", PRETO), tamanho=30, buff=0.12).move_to([0, 0.6, 0])
    cena.play(Write(c1), run_time=0.9 * VEL)

    # slide 100: n primo entrega φ(n) de graça — não serve
    c2 = formula(("n", LARANJA), ("primo:", PRETO), ("φ(", PRETO),
                 ("n", LARANJA), (")", PRETO), ("=", PRETO), ("n", LARANJA),
                 ("− 1", PRETO), ("✗", VERMELHO),
                 tamanho=28, buff=0.10).move_to([0, -0.4, 0])
    cena.play(Write(c2), run_time=0.9 * VEL)

    # slides 101–104: com n = p × q, só o criador conhece φ(n)
    c3 = formula(("n", LARANJA), ("=", PRETO), ("p", ROSA), ("×", PRETO),
                 ("q", VERDE2), ("⇒", PRETO), ("φ(", PRETO), ("n", LARANJA),
                 (")", PRETO), ("=", PRETO), ("(", PRETO), ("p", ROSA),
                 ("− 1)", PRETO), ("×", PRETO), ("(", PRETO), ("q", VERDE2),
                 ("− 1)", PRETO), ("✓", VERDE),
                 tamanho=28, buff=0.08).move_to([0, -1.4, 0])
    cena.play(Write(c3), run_time=1.1 * VEL)

    c4 = formula(("quebrar RSA", PRETO), ("=", PRETO), ("fatorar", PRETO),
                 ("n", LARANJA), tamanho=32).move_to([0, -2.6, 0])
    caixa = SurroundingRectangle(c4, color=VERDE, buff=0.2,
                                 corner_radius=0.14)
    cena.play(Write(c4), Create(caixa), run_time=1.1 * VEL)
    cena.wait(1.8 * VEL)

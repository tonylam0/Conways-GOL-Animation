from manim import *
import numpy as np


class Intro(Scene):
    def construct(self):
        self.camera.background_color = "#0F0F0F"

        intro_text = Text('"Cellular Automata"', font_size=30)
        cell_text = Text('"Cell"', font_size=30)

        self.play(Write(intro_text)) 
        self.play(Transform(intro_text, cell_text))
        self.play(intro_text.animate.shift(UP*1.1))

        big_square = Square(1.5, color=WHITE, stroke_width=2)

        self.play(Create(big_square), run_time=0.8)

        small_squares = VGroup()

        for i in range(9):
            small_squares.add(Square(1.5/3, color=WHITE, stroke_width=2))

        small_squares.arrange_in_grid(rows=3, columns=3, buff=0)
        small_squares.move_to(big_square.get_center())

        self.play(FadeIn(small_squares))

        self.wait(1.5)

        for square in small_squares:
            self.play(square.animate.set_fill(color=WHITE, opacity=1), run_time=0.1)

        for square in small_squares[::-1]:
            self.play(square.animate.set_fill(opacity=0), run_time=0.1)

        self.wait(3)

        states = Text("alive cell = white\ndead cell = black", font_size=30).shift(DOWN*1.15).scale(0.7)
        gen_text = Text("generation = 0", color=RED, font_size=30).shift(UP).scale(0.7)

        self.play(FadeOut(intro_text))
        self.play(Write(states))

        self.wait(1)

        self.play(
            small_squares[0].animate.set_fill(color=WHITE, opacity=1),
            small_squares[4].animate.set_fill(color=WHITE, opacity=1),
            small_squares[5].animate.set_fill(color=WHITE, opacity=1),
            small_squares[6].animate.set_fill(color=WHITE, opacity=1),
            small_squares[8].animate.set_fill(color=WHITE, opacity=1),
            run_time=1.5
            )
        
        self.wait(2.5)
        
        self.play(FadeIn(gen_text))
        
        self.wait(3)

        states_new = Text("alive cell = 1\ndead cell = 0", font_size=30).shift(DOWN*1.15).scale(0.7)

        self.play(Transform(states, states_new))

        self.wait(2.5)

        random_squares = (0, 4, 5, 6, 8)
        digits = VGroup()
        for idx in range(len(small_squares)):
            if idx in random_squares:
               num = Integer(number=1, color=WHITE, font_size=20).move_to(small_squares[idx].get_center())
               digits.add(num)
               self.add(num)
               self.play(small_squares[idx].animate.set_fill(opacity=0), run_time=0.1) 
               continue
            num = Integer(number=0, color=WHITE, font_size=20).move_to(small_squares[idx].get_center())
            digits.add(num)
            self.play(FadeIn(num, color=WHITE), run_time=0.1)

        self.wait(4.5)

        self.play(Circumscribe(small_squares[4], buff=0.05, color=YELLOW))
        self.play(digits[4].animate.set_color(YELLOW), run_time=0.1)

        self.wait(.5)

        self.play(Circumscribe(big_square, buff=0.1, color=BLUE_C, run_time=1.5))

        self.play(
            digits[0].animate.set_color(BLUE_C),
            digits[1].animate.set_color(BLUE_C),
            digits[2].animate.set_color(BLUE_C),
            digits[3].animate.set_color(BLUE_C),
            digits[5].animate.set_color(BLUE_C),
            digits[6].animate.set_color(BLUE_C),
            digits[7].animate.set_color(BLUE_C),
            digits[8].animate.set_color(BLUE_C),
            run_time=0.5
        )

        a_text = Text("a = 0", font_size=30, color=BLUE_C).move_to(gen_text).shift(UP*0.25).shift(LEFT*0.527).scale(0.7)

        self.play(Write(a_text))

        self.wait()

        self.play(
            big_square.animate.shift(LEFT*.9),
            small_squares.animate.shift(LEFT*.9),
            digits.animate.shift(LEFT*.9),
            gen_text.animate.shift(LEFT*.9),
            states.animate.shift(LEFT*.9),
            a_text.animate.shift(LEFT*.9)
            )

        rules = Text(
            "Instructions:\n1) alive cell w/ a < 2 dies\n2) alive cell w/ a > 3 dies\n3) dead cell w/ a = 3 is born", font_size=30, color=YELLOW).scale(0.4).next_to(big_square, RIGHT, buff=0.2)

        self.play(Create(rules))

        self.wait(4.5)

        new_total = Text("4", color=BLUE_C, font_size=30).next_to(a_text, RIGHT).scale(0.7).shift(LEFT*0.41)

        self.play(
            small_squares[0].animate.set_fill(color=WHITE, opacity=1),
            small_squares[5].animate.set_fill(color=WHITE, opacity=1),
            small_squares[6].animate.set_fill(color=WHITE, opacity=1),
            small_squares[8].animate.set_fill(color=WHITE, opacity=1),
            digits[0].animate.set_color(BLACK),
            digits[5].animate.set_color(BLACK),
            digits[6].animate.set_color(BLACK),
            digits[8].animate.set_color(BLACK),
            Transform(a_text[-1], new_total)
        )

        self.wait(.8)

        self.play(
            small_squares[4].animate.set_fill(color=WHITE, opacity=1),
            digits[4].animate.set_color(BLACK),
            run_time=0.5
        )

        self.wait()

        underline_three = Line(rules.get_left()*4.5, rules.get_right()*.92, stroke_width=2, color=YELLOW).shift(DOWN*0.15)
        self.play(Create(underline_three))

        terminated_cell = Integer(number=0, color=WHITE, font_size=20).move_to(small_squares[4].get_center())

        self.wait(0.5)

        first_gen = Text("1", color=RED, font_size=30).next_to(gen_text, RIGHT).scale(0.7).shift(LEFT*0.41)

        self.play(
            small_squares[4].animate.set_fill(opacity=0),
            Transform(digits[4], terminated_cell),
            Transform(gen_text[-1], first_gen)
        )

        self.wait(5)      
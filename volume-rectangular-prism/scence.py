from manim import *


class RectangleAreaExplanation(Scene):
    def construct(self):
        # Create the rectangle outline
        rectangle = Rectangle(width=4, height=3, color=WHITE)
        rectangle.to_edge(LEFT).shift(UP)

        # Create labels for dimensions
        label_a = Text("a", font_size=24).next_to(rectangle, DOWN)
        label_b = Text("b", font_size=24).next_to(rectangle, RIGHT)

        # Create all unit squares
        squares = VGroup()
        for i in range(3):  # rows
            for j in range(4):  # columns
                square = Square(side_length=1, color=BLUE, fill_opacity=0.5).move_to(
                    rectangle.get_corner(UL) + RIGHT * (j + 0.5) + DOWN * (i + 0.5)
                )
                squares.add(square)

        # Animation sequence
        self.play(Create(rectangle))
        self.play(Write(label_a), Write(label_b))
        self.wait()

        # Animate squares appearing one by one
        for square in squares:
            self.play(FadeIn(square), run_time=0.25)
        self.wait()

        # New part: Show equation with squares
        # Create unit square for equations
        unit_square = Square(side_length=0.4, color=BLUE, fill_opacity=0.5)

        # Create the first equation showing all squares
        eq_squares = VGroup()
        plus_signs = VGroup()

        # Position for the equation
        start_pos = UP*3

        # Text for "Diện tích = " (Area in Vietnamese)
        area_text = Text("Diện tích = ", font_size=24).move_to(start_pos + LEFT * 1)

        self.play(Write(area_text))

        # Create the first row of squares with plus signs
        for i in range(4):
            if i < 3:  # Don't add plus after last square
                plus = Text("+", font_size=24)
                plus_signs.add(plus)

            sq = unit_square.copy()
            eq_squares.add(sq)

        # Arrange squares and plus signs horizontally
        eq_group = VGroup()
        for i in range(len(eq_squares)):
            eq_group.add(eq_squares[i])
            if i < len(plus_signs):
                eq_group.add(plus_signs[i])

        eq_group.arrange(RIGHT, buff=0.2)
        eq_group.next_to(area_text, RIGHT)

        # Add dots to indicate more squares
        dots = Text("...", font_size=24).next_to(eq_group, RIGHT)

        # Show "a squares" notation
        a_notation = Text("(a 'unit' squares)", font_size=20, color=YELLOW).next_to(dots, UP)

        # Animation for first equation
        self.play(Write(eq_group))
        self.play(Write(dots))
        self.play(Write(a_notation))
        self.wait()

        # Create second equation (summing horizontally)
        second_eq_start = start_pos + DOWN * 1.5 + LEFT
        second_eq = VGroup()

        for i in range(3):  # b rows
            row = VGroup()
            row_squares = VGroup()

            # Create a × square for each row
            a_text = Text("a × ", font_size=24)
            unit_sq = unit_square.copy()
            row_term = VGroup(a_text, unit_sq)
            row_term.arrange(RIGHT, buff=0.1)

            if i < 2:  # Don't add plus after last row
                plus = Text(" +", font_size=24)
                row_term.add(plus)

            row_term.move_to(second_eq_start + DOWN * i)
            second_eq.add(row_term)

        # Show transformation to second equation
        self.play(FadeOut(eq_group), FadeOut(dots), FadeOut(a_notation))
        self.play(Write(second_eq))
        self.wait()

        # Final simplification
        final_eq_start = DOWN * 2 + LEFT * 5
        final_eq = VGroup(Text("= a × b × ", font_size=24), unit_square.copy()).arrange(
            RIGHT, buff=0.1
        )
        final_eq.move_to(final_eq_start)

        # Show final simplification
        self.play(FadeOut(second_eq), FadeIn(final_eq))
        self.wait(2)

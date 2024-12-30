from manim import *


class RectangleAreaExplanation(Scene):
    def construct(self):
        # Setting default font and font size
        Text.set_default(font="Roboto", font_size=24)

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
        eq_squares = []
        plus_signs = []

        # Position for the equation
        start_pos = UP * 3

        # Text for "Diện tích = " (Area in Vietnamese)
        area_text = Text("Diện tích = ", font_size=24).move_to(start_pos + LEFT * 1)

        self.play(Write(area_text))

        # Create 'b' rows with each row is sum of 'a' unit squares
        for i in range(3):
            for j in range(4):
                if i < 2 or j < 3:  # Don't add plus after last square
                    plus = Text("+", font_size=24)
                    plus_signs.append(plus)

                sq = unit_square.copy()
                eq_squares.append(sq)

        # Arrange squares and plus signs horizontally
        eq_group = [VGroup() for i in range(3)]
        for i in range(len(eq_squares)):
            group_idx = i // 4
            eq_group[group_idx].add(eq_squares[i])
            if i < len(plus_signs):
                eq_group[group_idx].add(plus_signs[i])

        for i in range(3):
            eq_group[i].arrange(RIGHT, buff=0.2)
            if i == 0:
                eq_group[i].next_to(area_text, RIGHT)
            else:
                eq_group[i].next_to(eq_group[i - 1], DOWN)

        # Create a brace that spans vertically to include all rows
        brace_rows = Brace(VGroup(*eq_group), direction=RIGHT, color=GREEN)
        b_label = Text("b").next_to(brace_rows, RIGHT)
        brace_cols = Brace(VGroup(*eq_group), direction=DOWN, color=GREEN)
        a_label = Text("a hình vuông 'đơn vị'").next_to(brace_cols, DOWN)

        # Animation for first equation
        left_x = max(group.get_left()[0] for group in eq_group)
        for group in eq_group:
            group.shift((left_x - group.get_left()[0]) * RIGHT)
            self.play(Write(group))
        self.play(
            Create(brace_rows), Write(b_label), Create(brace_cols), Write(a_label)
        )
        self.wait()

        # Create second equation (summing horizontally)
        second_equal_sign = (
            Text("=").next_to(a_label, DOWN * 1.5).align_to(area_text, RIGHT)
        )
        second_eq = VGroup()

        for i in range(3):  # b rows
            # Create a × square for each row
            a_text = Text("a × ", font_size=24)
            unit_sq = unit_square.copy()
            row_term = VGroup(a_text, unit_sq)

            if i < 2:  # Don't add plus after last row
                plus = Text(" +", font_size=24)
                row_term.add(plus)

            row_term.arrange(RIGHT, buff=0.1)
            # row_term.move_to(second_eq_start + DOWN * i)
            second_eq.add(row_term)


        # # Show transformation to second equation
        # self.play(FadeOut(eq_group), FadeOut(dots), FadeOut(a_notation))
        second_eq.arrange(DOWN, buff=0.3, aligned_edge=LEFT).next_to(
            a_label, DOWN
        ).shift((left_x - second_eq.get_left()[0]) * RIGHT)
        brace_second_eq = Brace(second_eq, direction=RIGHT, color=GREEN)
        b_label_second_eq = Text("b").next_to(brace_second_eq, RIGHT)
        self.play(Write(second_equal_sign), 
                  Create(second_eq), 
                  Create(brace_second_eq), 
                  Write(b_label_second_eq))
        self.wait()

        # # Final simplification
        equal_sign_final_eq = Text('=').next_to(second_eq, DOWN * 2).align_to(second_equal_sign, RIGHT)
        final_eq = VGroup(Text("a × b × ", font_size=24), unit_square.copy()).arrange(
            RIGHT, buff=0.1
        )
        final_eq.next_to(second_eq, DOWN*1.2).shift((left_x - final_eq.get_left()[0])*RIGHT)

        # Show final simplification
        self.play(
            Write(equal_sign_final_eq),
            Create(final_eq)
        )
        self.wait(2)

class CuboidVolumeExplanation(ThreeDScene):
    def construct(self):
        # Camera setup - adjusted to show 4x3 face in front
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        
        # Setting default font and font size
        Text.set_default(font="Roboto", font_size=24)
        
        # Labels for dimensions - directly on the prism sides
        label_a = Text("a", color=WHITE)
        label_b = Text("b", color=WHITE)
        label_c = Text("c", color=WHITE)

        
        # Create all unit cubes
        cubes = VGroup()
        layers = VGroup()
        
        # Create cubes layer by layer
        colors = [BLUE_A, BLUE_B, BLUE_C]  # Different shades for each layer
        cube_offset = -4*RIGHT + 4*DOWN
        for k in range(3):  # height (b)
            layer = VGroup()
            for i in range(2):  # depth (c)
                for j in range(4):  # width (a)
                    cube = Cube(
                        side_length=0.95,  # Slightly smaller to see edges
                        fill_opacity=0.7,
                        color=colors[k]
                    )
                    cube.move_to(
                        cube_offset + RIGHT * j + UP * i + OUT * k
                        # RIGHT * 0.5 + UP * 0.5 + OUT * 0.5
                    )
                    layer.add(cube)
            layers.add(layer)
            cubes.add(*layer)

        # Position labels on the sides of the cuboid
        label_a.next_to(cubes[2], DOWN, buff=0.2).rotate(PI/2, axis=RIGHT)
        label_b.next_to(cubes[10], RIGHT, buff=0.2).rotate(PI/2, axis=RIGHT)
        label_c.next_to(cubes[22], UP, buff=0.2).rotate(PI/2, axis=RIGHT)
        
        # Add cubes layer by layer
        for layer in layers:
            self.play(
                AnimationGroup(
                    *[FadeIn(cube) for cube in layer],
                    lag_ratio=0.1
                ),
            )
        self.play(
            Write(label_a),
            Write(label_b),
            Write(label_c)
        )

        # Create unit cube for equations
        unit_cube = Cube(side_length=0.4, fill_opacity=0.7, color=BLUE)
        
        # Create equation showing volume calculation
        volume_text = Text("Thể tích = ").move_to(3*UP)  # Volume in Vietnamese
        
        # Create equations for each layer
        equations = VGroup()
        
        for i in range(2):  # For each layer (c times)
            # Create "a × b ×" text
            ab_text = Text("a × b × ")
            
            # Create unit cube
            eq_cube = unit_cube.copy().rotate(PI/3,about_point=ORIGIN, axis=UP).rotate(PI/6, RIGHT).scale(0.5)
            
            # Create plus sign (except for last term)
            plus = Text(" +") if i < 1 else Text("")
            
            # Combine parts
            layer_term = VGroup(ab_text, eq_cube, plus)
            layer_term.arrange(RIGHT, buff=0.2)
            equations.add(layer_term)
        
        # Arrange equations
        equations.arrange(DOWN, aligned_edge=LEFT)
        equations.next_to(volume_text, RIGHT).shift(0.25*DOWN)

        # Add brace on the right
        brace = Brace(equations, RIGHT, color=GREEN)
        brace_label = Text('c').next_to(brace)
        
        # Add equations as fixed in frame mobjects
        self.add_fixed_in_frame_mobjects(volume_text)
        self.play(Write(volume_text))
        for eq in equations:
            self.add_fixed_in_frame_mobjects(eq)
            self.play(Write(eq))
        self.add_fixed_in_frame_mobjects(brace, brace_label)
        self.play(Write(brace), Write(brace_label))

        # Final equation
        equal_sign_final_eq = Text("= ").next_to(equations, 1.5*DOWN).align_to(volume_text, RIGHT)
        self.add_fixed_in_frame_mobjects(equal_sign_final_eq)
        final_eq = VGroup(
            Text("a × b × c × "),
            unit_cube.copy().rotate(PI/3,about_point=ORIGIN, axis=UP).rotate(PI/6, RIGHT).scale(0.5)
        ).arrange(RIGHT, buff=0.2)
        final_eq.next_to(equations, DOWN, aligned_edge=LEFT)
        
        self.add_fixed_in_frame_mobjects(final_eq)
        self.play(Write(equal_sign_final_eq), Write(final_eq))
        


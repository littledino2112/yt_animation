from manim import *
import manimpango
Text.set_default(font="Arial")

class MonomialPolynomial(ThreeDScene):  # Changed to ThreeDScene for better 3D handling
    def construct(self):
        # Title
        title = Text("Đơn thức - Đa thức", color=YELLOW)
        title.scale(1.2)
        title.to_edge(UP)
        
        # 1. Square Area Animation
        square = Square(side_length=2)
        square.set_fill(color=BLUE, opacity=0.5)
        # x_side = MathTex("x").next_to(square, RIGHT)
        x_side = MathTex("a").move_to(square.get_right() - RIGHT*0.3)
        square_formula = MathTex("S = a^2").next_to(square, DOWN*2)
        square_group = VGroup(square, square_formula, x_side)
        # square_group.to_edge(LEFT).shift(UP)
        
        # 2. Circle Area Animation
        circle = Circle(radius=1, color=WHITE)
        circle.set_fill(color=RED, opacity=0.5)
        radius_line = Line(circle.get_center(), circle.get_right(), color=WHITE)
        radius_label = MathTex("r").next_to(radius_line, UP*0.3)
        circle_formula = MathTex("S = \\pi r^2").next_to(circle, DOWN*2)
        circle_group = VGroup(circle, circle_formula, radius_line, radius_label)
        # circle_group.next_to(square_group, RIGHT*2, buff=0.5)

        # 3. Rectangle animation
        rect = Rectangle(height=2, width=4)
        rect.set_fill(color=GREEN, opacity=0.5)
        rect_height_label = MathTex("x").move_to(rect.get_right() - RIGHT*0.3)
        rect_width_label = MathTex("y").move_to(rect.get_bottom() + UP*0.3)
        rect_area = MathTex("S = x \\times y").next_to(rect, DOWN*2)
        rect_group = VGroup(rect, rect_height_label, rect_width_label, rect_area)
        # rect_group.next_to(circle_group, RIGHT*2, buff=0.5)
        all_groups = VGroup(square_group, circle_group, rect_group)
        all_groups.arrange(RIGHT, buff=1)
        all_groups.move_to(ORIGIN)
        
        # First two animations
        self.play(Write(title))
        self.wait()
        
        self.play(Create(square))
        self.play(Write(x_side))
        self.play(Write(square_formula))
        self.wait()
        
        self.play(Create(circle))
        self.play(Create(radius_line))
        self.play(Write(radius_label))
        self.play(Write(circle_formula))
        self.wait()

        self.play(Create(rect))
        self.play(Write(rect_height_label))
        self.play(Write(rect_width_label))
        self.play(Write(rect_area))
        

class SquareToPolynomial(Scene):
    def construct(self):
        # Create initial square
        square = Square(side_length=2)
        square.set_fill(color="#A0D8EF", opacity=0.5)
        
        # Labels for sides
        x_label_1 = MathTex("x")
        x_label_2 = MathTex("x")
        x_label_1.next_to(square, RIGHT)
        x_label_2.next_to(square, UP)

        # Area label
        area = MathTex("x^2")
        area.move_to(square.get_center())

        # Vietnamese label
        viet_label = Text("Diện tích = ", font="Arial")
        viet_formula = VGroup(viet_label, area.copy())
        viet_formula.arrange(RIGHT)
        viet_formula.to_edge(DOWN)

        # Animations
        self.play(Create(square), run_time=1.5)
        self.wait(0.5)
        self.play(
            Write(x_label_1),
            Write(x_label_2),
        )
        self.wait(0.5)
        self.play(Write(area))
        self.play(Write(viet_formula))

class SquareExpansion(Scene):
    def construct(self):
        # Create the main square
        side_length = 4
        main_square = Square(side_length=side_length)
        main_square.set_stroke(WHITE, 2)
        
        # Labels for the sides
        a_length = 2.5
        b_length = side_length - a_length
        
        # Create labels
        a_label = MathTex("a")
        b_label = MathTex("b")
        sum_label = MathTex("(a+b)")
        
        # Position labels
        sum_label.next_to(main_square, DOWN)
        a_label.next_to(main_square, LEFT).shift(UP)
        b_label.next_to(main_square, LEFT).shift(DOWN)
        
        # Create division lines
        vertical_line = Line(
            main_square.get_top(),
            main_square.get_bottom()
        ).move_to(main_square.get_left()).shift(RIGHT*a_length)
        horizontal_line = Line(
            main_square.get_left() + DOWN * a_length,
            main_square.get_right() + DOWN * a_length
        ).move_to(main_square.get_top()).shift(DOWN*a_length)
        
        # Create regions
        square_a = Square(side_length=a_length)
        square_a.move_to(main_square.get_corner(UL))
        square_a.align_to(main_square, UL)
        square_a.set_fill(BLUE, opacity=0.3)
        
        rect_ab1 = Rectangle(width=b_length, height=a_length)
        rect_ab1.next_to(square_a, RIGHT, buff=0)
        rect_ab1.set_fill(GREEN, opacity=0.3)
        
        rect_ab2 = Rectangle(width=a_length, height=b_length)
        rect_ab2.next_to(square_a, DOWN, buff=0)
        rect_ab2.set_fill(RED, opacity=0.3)
        
        square_b = Square(side_length=b_length)
        square_b.next_to(rect_ab1, DOWN, buff=0)
        square_b.set_fill(YELLOW, opacity=0.3)
        
        # Create area labels
        a_squared = MathTex("a^2")
        ab1 = MathTex("ab")
        ab2 = MathTex("ab")
        b_squared = MathTex("b^2")
        
        # Position area labels
        a_squared.move_to(square_a.get_center())
        ab1.move_to(rect_ab1.get_center())
        ab2.move_to(rect_ab2.get_center())
        b_squared.move_to(square_b.get_center())
        
        # Final equation
        equation = MathTex(
            "(a+b)^2", "=", "a^2", "+", "2ab", "+", "b^2"
        )
        equation.to_edge(DOWN)
        
        # Animations
        self.play(Create(main_square))
        self.play(Write(sum_label))
        self.wait()
        
        # Show divisions
        self.play(
            Write(a_label),
            Write(b_label),
            Create(vertical_line),
            Create(horizontal_line)
        )
        
        # Show regions with colors
        self.play(
            FadeIn(square_a),
            FadeIn(rect_ab1),
            FadeIn(rect_ab2),
            FadeIn(square_b)
        )
        
        # Show area labels
        self.play(
            Write(a_squared),
            Write(ab1),
            Write(ab2),
            Write(b_squared)
        )
        
        # Show final equation
        self.play(Write(equation))
        self.wait(2)


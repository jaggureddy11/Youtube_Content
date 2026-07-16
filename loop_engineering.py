from manim import *

class LoopEngineering(Scene):
    def construct(self):
        # Palette (matches hashmap_explainer_white.py for brand consistency)
        BG_COLOR = "#FFFFFF"
        BOX_BORDER = "#334155"
        BOX_FILL = "#F1F5F9"
        BLUE = "#2563EB"       # neutral/process
        GREEN = "#059669"      # good/specific feedback
        ORANGE = "#EA580C"     # secondary accent
        RED = "#DC2626"        # bad/vague feedback, problems
        TEXT_COLOR = "#1E293B"
        AMBER = "#D97706"      # highlight
        MUTED = "#64748B"

        self.camera.background_color = BG_COLOR

        # --- Helper for timing compatibility without caption box ---
        def play_caption(new_text, wait_time=2.0):
            if wait_time > 0:
                self.wait(wait_time)

        # --- Helper to create beautiful speech bubbles (Unified with Masking) ---
        def make_speech_bubble(width, height, color, fill_color, position, pointer_dir="left"):
            rect = RoundedRectangle(
                width=width, height=height, corner_radius=0.25,
                stroke_color=color, stroke_width=2.5,
                fill_color=fill_color, fill_opacity=1
            )
            # Create a small triangular pointer on the edge and mask the inner border
            if pointer_dir == "left":
                mask = Line(
                    rect.get_left() + UP * 0.16,
                    rect.get_left() + DOWN * 0.16,
                    color=fill_color, stroke_width=4.5
                )
                pointer = Polygon(
                    rect.get_left() + UP * 0.18,
                    rect.get_left() + DOWN * 0.18,
                    rect.get_left() + LEFT * 0.28 + DOWN * 0.05,
                    stroke_width=0, fill_color=fill_color, fill_opacity=1
                )
                border_pointer = VGroup(
                    Line(rect.get_left() + UP * 0.18, rect.get_left() + LEFT * 0.28 + DOWN * 0.05, color=color, stroke_width=2.5),
                    Line(rect.get_left() + DOWN * 0.18, rect.get_left() + LEFT * 0.28 + DOWN * 0.05, color=color, stroke_width=2.5)
                )
            else:
                mask = Line(
                    rect.get_right() + UP * 0.16,
                    rect.get_right() + DOWN * 0.16,
                    color=fill_color, stroke_width=4.5
                )
                pointer = Polygon(
                    rect.get_right() + UP * 0.18,
                    rect.get_right() + DOWN * 0.18,
                    rect.get_right() + RIGHT * 0.28 + DOWN * 0.05,
                    stroke_width=0, fill_color=fill_color, fill_opacity=1
                )
                border_pointer = VGroup(
                    Line(rect.get_right() + UP * 0.18, rect.get_right() + RIGHT * 0.28 + DOWN * 0.05, color=color, stroke_width=2.5),
                    Line(rect.get_right() + DOWN * 0.18, rect.get_right() + RIGHT * 0.28 + DOWN * 0.05, color=color, stroke_width=2.5)
                )
            
            # The layering order ensures the mask hides the rectangle border segment
            bubble_bg = VGroup(rect, mask, pointer, border_pointer).move_to(position)
            return rect, bubble_bg

        # =========================================================================
        # 1. HOOK (0:00-0:12.84, duration = 12.84s)
        # =========================================================================

        # Add decorative grid lines for visual richness (faded background)
        grid = NumberPlane(
            x_range=[-7, 7, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_color": "#F1F5F9", "stroke_width": 1, "stroke_opacity": 0.5}
        )
        self.add(grid)

        split_line = Line(start=UP * 3, end=DOWN * 1.5, color=BOX_BORDER, stroke_width=1)
        self.play(Create(split_line), run_time=1.0)
        
        # Left: elaborate prompt attempt, frustrated with soft shadow
        prompt_shadow_left = RoundedRectangle(
            width=4, height=2.2, corner_radius=0.2,
            fill_color="#E2E8F0", fill_opacity=0.4, stroke_width=0
        ).move_to(LEFT * 3.2 + DOWN * 0.08 + RIGHT * 0.08)
        
        prompt_box_left = RoundedRectangle(
            width=4, height=2.2, corner_radius=0.2,
            stroke_color=RED, stroke_width=3,
            fill_color="#FEF2F2", fill_opacity=1
        ).move_to(LEFT * 3.2)
        prompt_label_left = Text("The 'perfect prompt'", font_size=14, color=RED, weight=BOLD, font="Arial").next_to(prompt_box_left, UP, buff=0.2)
        prompt_lines_left = Paragraph(
            "Write a detailed,\nexhaustive, one-shot\ninstruction upfront...",
            font_size=13, color=TEXT_COLOR, line_spacing=0.6, alignment="center", font="Arial"
        ).move_to(prompt_box_left.get_center())
        
        dec_line1 = Line(start=prompt_box_left.get_center()+LEFT*1.5+DOWN*0.5, end=prompt_box_left.get_center()+RIGHT*1.5+DOWN*0.5, stroke_color=MUTED, stroke_width=1, stroke_opacity=0.5)
        dec_line2 = Line(start=prompt_box_left.get_center()+LEFT*1.5+DOWN*0.7, end=prompt_box_left.get_center()+RIGHT*1.2+DOWN*0.7, stroke_color=MUTED, stroke_width=1, stroke_opacity=0.5)
        
        left_group = VGroup(prompt_shadow_left, prompt_box_left, prompt_label_left, prompt_lines_left, dec_line1, dec_line2)

        # Right: simple loop icon with rotation
        loop_circle = Circle(radius=1.1, color=GREEN, stroke_width=4).move_to(RIGHT * 3.2)
        loop_arrow_head = Triangle(color=GREEN, fill_color=GREEN, fill_opacity=1).scale(0.15).move_to(
            loop_circle.point_at_angle(PI / 2)
        ).rotate(-PI / 2)
        loop_label = Text("Loop Engineering", font_size=14, color=GREEN, weight=BOLD, font="Arial").next_to(loop_circle, UP, buff=0.2)
        calm_brain = Text("🧠", font_size=28).move_to(loop_circle.get_center())
        right_group = VGroup(loop_circle, loop_arrow_head, calm_brain, loop_label)

        self.play(FadeIn(left_group, shift=UP), run_time=0.8)
        
        # Timing sync (Wait for the first voiceover statement)
        self.wait(6.0)
        
        self.play(FadeIn(right_group, shift=UP), run_time=0.8)
        
        # Rotate the loop arrow for a dynamic, visually rich feel
        self.play(
            Rotate(VGroup(loop_circle, loop_arrow_head), angle=-2*PI, about_point=loop_circle.get_center(), run_time=2.5),
            rate_func=linear
        )
        self.wait(0.94)

        # CRITICAL FIX: Make sure the split_line is faded out here!
        self.play(FadeOut(left_group), FadeOut(right_group), FadeOut(split_line), run_time=0.8)

        # =========================================================================
        # 2. THE OLD WAY: PROMPT ENGINEERING (0:12.84-0:28.87, duration = 16.03s)
        # =========================================================================
        prompt_shadow = RoundedRectangle(
            width=3.5, height=1.2, corner_radius=0.15,
            fill_color="#64748B", fill_opacity=0.15, stroke_width=0
        ).move_to(LEFT * 3 + UP * 0.5 + DOWN * 0.08 + RIGHT * 0.08)

        prompt_box = RoundedRectangle(
            width=3.5, height=1.2, corner_radius=0.15,
            stroke_color=BLUE, stroke_width=3,
            fill_color="#EFF6FF", fill_opacity=1
        ).move_to(LEFT * 3 + UP * 0.5)
        prompt_text = Text("One long prompt", font_size=16, color=BLUE, weight=BOLD, font="Arial").move_to(prompt_box.get_center())
        prompt_group = VGroup(prompt_shadow, prompt_box, prompt_text)

        arrow1 = Arrow(prompt_box.get_right(), prompt_box.get_right() + RIGHT * 2, color=BOX_BORDER, stroke_width=3)

        output_shadow = RoundedRectangle(
            width=2.8, height=1.2, corner_radius=0.15,
            fill_color="#64748B", fill_opacity=0.15, stroke_width=0
        ).move_to(RIGHT * 2.2 + UP * 0.5 + DOWN * 0.08 + RIGHT * 0.08)

        output_box = RoundedRectangle(
            width=2.8, height=1.2, corner_radius=0.15,
            stroke_color=BOX_BORDER, stroke_width=2,
            fill_color=BOX_FILL, fill_opacity=1
        ).shift(RIGHT * 2.2 + UP * 0.5)
        
        output_text = Text("Output", font_size=16, color=TEXT_COLOR, font="Arial").move_to(output_box.get_center())
        output_group = VGroup(output_shadow, output_box, output_text)

        self.play(FadeIn(prompt_group), run_time=1.0)
        self.play(Create(arrow1), FadeIn(output_group), run_time=1.2)
        
        self.wait(5.0)

        # Make the cross draw beautifully
        line1 = Line(start=output_box.get_corner(UL), end=output_box.get_corner(DR), color=RED, stroke_width=6)
        line2 = Line(start=output_box.get_corner(DL), end=output_box.get_corner(UR), color=RED, stroke_width=6)
        red_cross = VGroup(line1, line2)
        
        wrong_label = Text("Often wrong or incomplete", font_size=13, color=RED, weight=BOLD, font="Arial").next_to(output_box, DOWN, buff=0.25)
        
        # Shake the output box on collision
        self.play(
            Create(red_cross), 
            FadeIn(wrong_label),
            run_time=0.8
        )
        self.play(output_group.animate.shift(LEFT * 0.1), rate_func=there_and_back, run_time=0.15)
        self.play(output_group.animate.shift(RIGHT * 0.1), rate_func=there_and_back, run_time=0.15)
        
        self.wait(6.932)

        self.play(
            FadeOut(prompt_group), FadeOut(arrow1), FadeOut(output_group), 
            FadeOut(red_cross), FadeOut(wrong_label),
            run_time=0.8
        )

        # =========================================================================
        # 3. THE LOOP: WHAT IT ACTUALLY LOOKS LIKE (0:28.87-0:47.23, duration = 18.36s)
        # =========================================================================
        # Palette matching the uploaded diagram
        BLUE_ACCENT = "#3B82F6"
        GREEN_ACCENT = "#10B981"
        AMBER_ACCENT = "#F59E0B"
        PURPLE_ACCENT = "#8B5CF6"
        
        LIGHT_BLUE = "#DBEAFE"
        LIGHT_GREEN = "#D1FAE5"
        LIGHT_AMBER = "#FEF3C7"
        LIGHT_PURPLE = "#F3E8FF"

        # Simple vector icons matching the diagram
        # 1. Checklist
        chk_box = Rectangle(width=0.22, height=0.32, stroke_width=1.5, stroke_color=MUTED)
        chk_lines = VGroup(*[Line(start=chk_box.get_center()+LEFT*0.05+UP*y, end=chk_box.get_center()+RIGHT*0.05+UP*y, stroke_width=1.2, color=MUTED) for y in [0.07, 0, -0.07]])
        chk_dots = VGroup(*[Dot(point=chk_box.get_center()+LEFT*0.07+UP*y, radius=0.015, color=MUTED) for y in [0.07, 0, -0.07]])
        icon_plan = VGroup(chk_box, chk_lines, chk_dots)

        # 2. Gear
        gear_center = Circle(radius=0.08, stroke_width=1.5, stroke_color=MUTED)
        gear_outer = Circle(radius=0.14, stroke_width=1.5, stroke_color=MUTED)
        teeth = VGroup(*[
            Rectangle(width=0.04, height=0.06, stroke_width=0, fill_color=MUTED, fill_opacity=1)
            .move_to(gear_outer.point_at_angle(a)).rotate(a)
            for a in np.arange(0, 2*PI, PI/4)
        ])
        icon_act = VGroup(gear_center, gear_outer, teeth)

        # 3. Magnifying glass
        glass_circle = Circle(radius=0.1, stroke_width=1.5, stroke_color=MUTED)
        handle = Line(start=glass_circle.point_at_angle(-PI/4), end=glass_circle.point_at_angle(-PI/4) + DOWN*0.12 + RIGHT*0.12, stroke_width=2.5, color=MUTED)
        icon_observe = VGroup(glass_circle, handle)

        # 4. Bar chart
        bar1 = Rectangle(width=0.05, height=0.12, stroke_width=0, fill_color=MUTED, fill_opacity=1)
        bar2 = Rectangle(width=0.05, height=0.22, stroke_width=0, fill_color=MUTED, fill_opacity=1).next_to(bar1, RIGHT, buff=0.04, aligned_edge=DOWN)
        bar3 = Rectangle(width=0.05, height=0.32, stroke_width=0, fill_color=MUTED, fill_opacity=1).next_to(bar2, RIGHT, buff=0.04, aligned_edge=DOWN)
        icon_evaluate = VGroup(bar1, bar2, bar3)

        # Center Text
        center_title = Text("LOOP ENGINEERING", font_size=16, color=TEXT_COLOR, weight=BOLD, font="Arial")
        underline = Line(start=center_title.get_left()+DOWN*0.08, end=center_title.get_right()+DOWN*0.08, color=TEXT_COLOR, stroke_width=1.5)
        center_subtitle = Paragraph(
            "Design AI systems\nthat think, act, learn\nand improve in loops.",
            font_size=10, color=MUTED, alignment="center", font="Arial", line_spacing=0.55
        ).next_to(underline, DOWN, buff=0.12)
        center_text = VGroup(center_title, underline, center_subtitle).move_to(ORIGIN)

        # Helper to construct a beautiful loop node box
        def make_loop_node(title, body, color, light_color, icon, position):
            shadow = RoundedRectangle(
                width=2.8, height=1.4, corner_radius=0.15,
                fill_color="#64748B", fill_opacity=0.15, stroke_width=0
            ).move_to(position + DOWN * 0.06 + RIGHT * 0.06)
            box = RoundedRectangle(
                width=2.8, height=1.4, corner_radius=0.15,
                stroke_color=color, stroke_width=2.5,
                fill_color=BOX_FILL, fill_opacity=1
            ).move_to(position)
            
            pill = RoundedRectangle(width=1.3, height=0.32, corner_radius=0.06, stroke_width=0, fill_color=light_color, fill_opacity=1)
            title_text = Text(title, font_size=10, color=color, weight=BOLD, font="Arial").move_to(pill.get_center())
            pill_group = VGroup(pill, title_text)
            
            body_text = Paragraph(body, font_size=9, color=TEXT_COLOR, alignment="center", font="Arial", line_spacing=0.5)
            text_group = VGroup(pill_group, body_text).arrange(DOWN, buff=0.08)
            
            contents = VGroup(icon, text_group).arrange(RIGHT, buff=0.18).move_to(box.get_center())
            node_group = VGroup(shadow, box, contents)
            return node_group

        # Build nodes
        nodes = VGroup(
            make_loop_node("1. PLAN", "AI decides what\nto do next.", BLUE_ACCENT, LIGHT_BLUE, icon_plan, UP * 2.5),
            make_loop_node("2. ACT", "AI executes\nthe action.", GREEN_ACCENT, LIGHT_GREEN, icon_act, RIGHT * 2.8),
            make_loop_node("3. OBSERVE", "AI observes results\nand collects data.", AMBER_ACCENT, LIGHT_AMBER, icon_observe, DOWN * 2.5),
            make_loop_node("4. EVALUATE", "AI evaluates outcomes\nand decides what to improve.", PURPLE_ACCENT, LIGHT_PURPLE, icon_evaluate, LEFT * 2.8)
        )

        # Arrows connecting the boxes
        loop_arrows = VGroup(
            CurvedArrow(nodes[0].get_right() + DOWN * 0.1, nodes[1].get_top() + RIGHT * 0.1, angle=-TAU/8, color=MUTED, stroke_width=2),
            CurvedArrow(nodes[1].get_bottom() + RIGHT * 0.1, nodes[2].get_right() + UP * 0.1, angle=-TAU/8, color=MUTED, stroke_width=2),
            CurvedArrow(nodes[2].get_left() + UP * 0.1, nodes[3].get_bottom() + LEFT * 0.1, angle=-TAU/8, color=MUTED, stroke_width=2),
            CurvedArrow(nodes[3].get_top() + LEFT * 0.1, nodes[0].get_left() + DOWN * 0.1, angle=-TAU/8, color=MUTED, stroke_width=2)
        )

        # Bottom Caption text
        repeat_text = Text("Repeat the loop. Get better every cycle.", font_size=14, color=TEXT_COLOR, font="Arial").to_edge(DOWN, buff=0.4)

        # Animate the creation of the loop
        self.play(FadeIn(center_text), FadeIn(nodes[0]), run_time=0.5)
        self.play(Create(loop_arrows[0]), FadeIn(nodes[1]), run_time=0.5)
        
        self.wait(3.0)

        self.play(Create(loop_arrows[1]), FadeIn(nodes[2]), run_time=0.5)
        self.play(Create(loop_arrows[2]), FadeIn(nodes[3]), run_time=0.5)
        self.play(Create(loop_arrows[3]), run_time=0.5)
        
        self.wait(4.5)

        # Pulse the loop once to show it cycling and reveal the caption
        self.play(
            *[nodes[i].animate.scale(1.1) for i in range(4)],
            FadeIn(repeat_text),
            run_time=0.6
        )
        self.play(
            *[nodes[i].animate.scale(1.0/1.1) for i in range(4)],
            run_time=0.6
        )
        
        # Scale and move the diagram to the left
        loop_diagram = VGroup(center_text, nodes, loop_arrows)
        self.play(loop_diagram.animate.scale(0.65).to_edge(LEFT, buff=0.8), run_time=1.0)
        
        self.wait(6.16)

        # =========================================================================
        # 4. WHY THIS WORKS BETTER (0:47.23-0:55, duration = 17.42s)
        # =========================================================================
        why_title = Text("How Feedback Works", font_size=18, color=TEXT_COLOR, weight=BOLD, font="Arial").move_to(RIGHT * 2.2 + UP * 2.2)
        self.play(FadeIn(why_title), run_time=0.5)

        # PROPER PADDING & FONT FIX: Speech bubbles slightly expanded and text set to font_size=13
        vague_rect, vague_bubble = make_speech_bubble(
            width=3.6, height=1.1, color=MUTED, fill_color="#F1F5F9",
            position=RIGHT * 3 + UP * 1.2, pointer_dir="left"
        )
        vague_text = Text("\"Make it better\"", font_size=13, color=MUTED, weight=BOLD, font="Arial").move_to(vague_rect.get_center())
        vague_group = VGroup(vague_bubble, vague_text)
        dead_end = Text("(dead end)", font_size=11, color=MUTED, font="Arial").next_to(vague_rect, DOWN, buff=0.15)

        self.play(FadeIn(vague_group), FadeIn(dead_end), run_time=0.8)
        
        self.wait(7.7)

        specific_rect, specific_bubble = make_speech_bubble(
            width=4.6, height=1.4, color=GREEN, fill_color="#ECFDF5",
            position=RIGHT * 3 + DOWN * 0.8, pointer_dir="left"
        )
        specific_text = Paragraph(
            "\"Cut this section\nto two sentences\"",
            font_size=13, color=GREEN, alignment="center", line_spacing=0.6, weight=BOLD, font="Arial"
        ).move_to(specific_rect.get_center())
        specific_group = VGroup(specific_bubble, specific_text)
        works_label = Text("(concrete target)", font_size=11, color=GREEN, font="Arial").next_to(specific_rect, DOWN, buff=0.15)

        self.play(FadeIn(specific_group), FadeIn(works_label), run_time=0.8)
        
        self.wait(6.824)

        self.play(
            FadeOut(vague_group), FadeOut(dead_end),
            FadeOut(specific_group), FadeOut(works_label),
            FadeOut(loop_diagram), FadeOut(repeat_text),
            FadeOut(why_title),
            run_time=0.8
        )

        # =========================================================================
        # 5. THE PRACTICAL VERSION (0:55-1:10, duration = 18.07s)
        # =========================================================================
        compare_title = Text("Which path is faster?", font_size=18, color=TEXT_COLOR, weight=BOLD, font="Arial").move_to(RIGHT * 2.2 + UP * 2.2)
        self.play(FadeIn(compare_title), run_time=0.5)

        # Left card: 1 perfect prompt (with shadow)
        card1_shadow = RoundedRectangle(
            width=4, height=2.5, corner_radius=0.2,
            fill_color="#64748B", fill_opacity=0.15, stroke_width=0
        ).move_to(LEFT * 3 + DOWN * 0.08 + RIGHT * 0.08)
        card1 = RoundedRectangle(
            width=4, height=2.5, corner_radius=0.2,
            stroke_color=RED, stroke_width=3,
            fill_color="#FEF2F2", fill_opacity=1
        ).move_to(LEFT * 3)
        card1_title = Text("1 perfect prompt", font_size=16, color=RED, weight=BOLD, font="Arial").move_to(card1.get_center() + UP * 0.7)
        card1_time = Text("10 min", font_size=28, color=RED, weight=BOLD, font="Arial").move_to(card1.get_center())
        card1_result = Text("mediocre result", font_size=12, color=TEXT_COLOR, font="Arial").move_to(card1.get_center() + DOWN * 0.7)
        card1_group = VGroup(card1_shadow, card1, card1_title, card1_time, card1_result)

        self.play(FadeIn(card1_group, shift=UP), run_time=0.8)
        
        self.wait(4.2)

        # Right card: 3 quick loops (with shadow)
        card2_shadow = RoundedRectangle(
            width=4, height=2.5, corner_radius=0.2,
            fill_color="#64748B", fill_opacity=0.15, stroke_width=0
        ).move_to(RIGHT * 3 + DOWN * 0.08 + RIGHT * 0.08)
        card2 = RoundedRectangle(
            width=4, height=2.5, corner_radius=0.2,
            stroke_color=GREEN, stroke_width=3,
            fill_color="#ECFDF5", fill_opacity=1
        ).move_to(RIGHT * 3)
        card2_title = Text("3 quick loops", font_size=16, color=GREEN, weight=BOLD, font="Arial").move_to(card2.get_center() + UP * 0.7)
        card2_time = Text("3 min total", font_size=28, color=GREEN, weight=BOLD, font="Arial").move_to(card2.get_center())
        card2_result = Text("sharp result", font_size=12, color=TEXT_COLOR, font="Arial").move_to(card2.get_center() + DOWN * 0.7)
        card2_group = VGroup(card2_shadow, card2, card2_title, card2_time, card2_result)

        self.play(FadeIn(card2_group, shift=UP), run_time=0.8)
        
        self.wait(6.7)

        # Green checkmark with a soft scale and Flash animation
        checkmark = Text("✓", font_size=48, color=GREEN, weight=BOLD, font="Arial").next_to(card2, UP, buff=0.2)
        self.play(
            FadeIn(checkmark, scale=1.3),
            Flash(checkmark.get_center(), color=GREEN, line_length=0.2, num_lines=8, flash_radius=0.4),
            run_time=0.8
        )
        
        self.wait(3.472)

        self.play(
            FadeOut(card1_group), FadeOut(card2_group), FadeOut(checkmark),
            FadeOut(compare_title),
            run_time=0.8
        )

        # =========================================================================
        # 6. CLOSER (1:10-1:15, duration = 5.59s)
        # =========================================================================
        final_title = Text("Loop Engineering", font_size=44, color=GREEN, weight=BOLD, font="Arial").move_to(UP * 0.6)
        final_vs = Text(">", font_size=40, color=MUTED, weight=BOLD, font="Arial").next_to(final_title, DOWN, buff=0.25)
        final_subtitle = Text("Prompt Engineering", font_size=32, color=RED, weight=BOLD, font="Arial").next_to(final_vs, DOWN, buff=0.25)
        final_card = VGroup(final_title, final_vs, final_subtitle)

        # Scale and center the loop diagram back first as closer transition, fading it back in
        self.play(
            loop_diagram.animate.scale(1.0/0.65).move_to(UP * 0.4),
            FadeIn(loop_diagram),
            run_time=1.0
        )
        self.play(
            loop_diagram.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=1.2
        )
        
        self.play(
            FadeOut(loop_diagram),
            FadeIn(final_card, scale=0.85),
            run_time=1.2
        )
        self.wait(2.192)

        # =========================================================================
        # 7. CALL TO ACTION (CTA) (1:15-1:22, duration = 7.49s) - PREMIUM YOUTUBE OUTRO
        # =========================================================================
        # CRITICAL OVERLAP FIX: Move the final card all the way to the top edge and scale it down
        self.play(final_card.animate.to_edge(UP, buff=0.5).scale(0.75), run_time=0.8)

        # --- SUBSCRIBE BUTTON (YouTube Style) ---
        sub_btn_box = RoundedRectangle(
            width=5.5, height=1.1, corner_radius=0.15,
            stroke_width=0, fill_color=RED, fill_opacity=1
        )
        
        # Draw YouTube logo
        yt_icon_box = RoundedRectangle(
            width=0.8, height=0.55, corner_radius=0.12,
            stroke_width=0, fill_color=WHITE, fill_opacity=1
        )
        yt_triangle = Triangle(
            color=RED, fill_color=RED, fill_opacity=1
        ).scale(0.12).rotate(-PI/2).move_to(yt_icon_box.get_center())
        yt_logo = VGroup(yt_icon_box, yt_triangle)
        
        sub_text = Text("SUBSCRIBE", font_size=24, color=WHITE, weight=BOLD, font="Arial")
        
        # Draw notification bell
        bell_body = Arc(radius=0.22, start_angle=0, angle=PI, color=WHITE, stroke_width=0, fill_color=WHITE, fill_opacity=1)
        bell_base = RoundedRectangle(width=0.55, height=0.08, corner_radius=0.02, stroke_width=0, fill_color=WHITE, fill_opacity=1).next_to(bell_body, DOWN, buff=0.02)
        bell_clapper = Circle(radius=0.07, color=WHITE, stroke_width=0, fill_color=WHITE, fill_opacity=1).next_to(bell_base, DOWN, buff=0.02)
        bell_icon = VGroup(bell_body, bell_base, bell_clapper)
        
        sub_button_contents = VGroup(yt_logo, sub_text, bell_icon).arrange(RIGHT, buff=0.4)
        # Positioned lower down (centered at DOWN * 0.1) to avoid overlap with top card
        sub_button = VGroup(sub_btn_box, sub_button_contents).move_to(DOWN * 0.1)
        
        # --- LOWER CTA ICONS (Like, Comment, Share) ---
        # EMOJI FALLBACK FIX: Removed font="Arial" on icons to allow system-level emoji rendering
        like_icon = Text("👍", font_size=28)
        like_label = Text("Like", font_size=14, color=TEXT_COLOR, font="Arial").next_to(like_icon, DOWN, buff=0.15)
        like_btn = VGroup(like_icon, like_label)
        
        comment_icon = Text("💬", font_size=28)
        comment_label = Text("Comment", font_size=14, color=TEXT_COLOR, font="Arial").next_to(comment_icon, DOWN, buff=0.15)
        comment_btn = VGroup(comment_icon, comment_label)
        
        share_icon = Text("🔗", font_size=28)
        share_label = Text("Share", font_size=14, color=TEXT_COLOR, font="Arial").next_to(share_icon, DOWN, buff=0.15)
        share_btn = VGroup(share_icon, share_label)
        
        cta_icons = VGroup(like_btn, comment_btn, share_btn).arrange(RIGHT, buff=1.2).next_to(sub_button, DOWN, buff=0.6)
        
        cta_group = VGroup(sub_button, cta_icons)
        
        self.play(FadeIn(cta_group, shift=UP), run_time=0.8)

        # Add cursor (custom drawn arrow pointing up-left)
        cursor_poly = Polygon(
            ORIGIN, DOWN * 0.4 + RIGHT * 0.1, DOWN * 0.25 + RIGHT * 0.18, 
            DOWN * 0.35 + RIGHT * 0.32, DOWN * 0.3 + RIGHT * 0.35, 
            DOWN * 0.2 + RIGHT * 0.2, DOWN * 0.25 + RIGHT * 0.3,
            color=TEXT_COLOR, fill_color=TEXT_COLOR, fill_opacity=1
        ).scale(0.8)
        cursor = VGroup(cursor_poly).move_to(RIGHT * 4.5 + DOWN * 3)
        self.play(FadeIn(cursor), run_time=0.4)

        # 1. Click SUBSCRIBE
        self.play(cursor.animate.move_to(sub_btn_box.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        # Press down
        self.play(
            sub_button.animate.scale(0.92),
            cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02),
            run_time=0.15
        )
        # Release and change to gray (SUBSCRIBED)
        new_sub_text = Text("SUBSCRIBED", font_size=24, color="#64748B", weight=BOLD, font="Arial")
        self.play(
            sub_btn_box.animate.scale(1.0/0.92).set_fill(color="#E2E8F0"),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Transform(sub_text, new_sub_text),
            yt_icon_box.animate.scale(1.0/0.92).set_fill(color="#CBD5E1"),
            yt_triangle.animate.scale(1.0/0.92).set_fill(color="#E2E8F0").set_stroke(color="#E2E8F0"),
            bell_body.animate.scale(1.0/0.92).set_fill(color="#64748B"),
            bell_base.animate.scale(1.0/0.92).set_fill(color="#64748B"),
            bell_clapper.animate.scale(1.0/0.92).set_fill(color="#64748B"),
            run_time=0.25
        )
        
        # Bell rings (wiggles)
        self.play(
            Rotate(bell_icon, angle=0.15, about_point=bell_icon.get_top(), rate_func=there_and_back),
            run_time=0.15
        )
        self.play(
            Rotate(bell_icon, angle=-0.15, about_point=bell_icon.get_top(), rate_func=there_and_back),
            run_time=0.15
        )
        
        # 2. Click LIKE
        self.play(cursor.animate.move_to(like_icon.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        self.play(
            like_icon.animate.scale(0.9),
            cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02),
            run_time=0.15
        )
        # Release and turn blue
        self.play(
            like_icon.animate.scale(1.0/0.9).set_color(BLUE),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Flash(like_icon.get_center(), color=BLUE, line_length=0.15, flash_radius=0.4),
            run_time=0.25
        )

        # 3. Click COMMENT
        self.play(cursor.animate.move_to(comment_icon.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        self.play(
            comment_icon.animate.scale(0.9),
            cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02),
            run_time=0.15
        )
        # Release and turn amber
        self.play(
            comment_icon.animate.scale(1.0/0.9).set_color(AMBER),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Flash(comment_icon.get_center(), color=AMBER, line_length=0.15, flash_radius=0.4),
            run_time=0.25
        )

        # 4. Click SHARE
        self.play(cursor.animate.move_to(share_icon.get_center() + RIGHT * 0.15 + DOWN * 0.2), run_time=0.5)
        self.play(
            share_icon.animate.scale(0.9),
            cursor.animate.scale(0.92).shift(LEFT * 0.02 + UP * 0.02),
            run_time=0.15
        )
        # Release and turn green
        self.play(
            share_icon.animate.scale(1.0/0.9).set_color(GREEN),
            cursor.animate.scale(1.0/0.92).shift(RIGHT * 0.02 + DOWN * 0.02),
            Flash(share_icon.get_center(), color=GREEN, line_length=0.15, flash_radius=0.4),
            run_time=0.25
        )

        # Retract cursor and end
        self.play(
            cursor.animate.move_to(RIGHT * 4.5 + DOWN * 3),
            FadeOut(cursor),
            run_time=0.4
        )
        self.wait(1.188)
